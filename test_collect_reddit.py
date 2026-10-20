"""Offline checks; synthetic fixtures are never written as collected posts."""

import csv
import unittest
from unittest.mock import patch

import collect_reddit as collector


def post(number):
    return dict(id=str(number), subreddit="ChatGPT", is_self=True,
                selftext=f"Body {number}", title=f"Title {number}",
                permalink=f"/r/ChatGPT/comments/{number}/")


def listing(start, stop, after):
    return {"data": {"children": [dict(kind="t3", data=post(i))
                                  for i in range(start, stop)], "after": after}}


class CollectionTests(unittest.TestCase):
    def test_reading_sample(self):
        with open("data/reddit_reading_sample.csv", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 35)
        self.assertEqual(len({row["source_url"] for row in rows}), 35)
        self.assertTrue(all(row["text"] and row["observation"] for row in rows))

    def test_eligibility(self):
        self.assertTrue(collector.eligible(post(1), "ChatGPT"))
        for change in [dict(spoiler=True), dict(selftext="[removed]"),
                       dict(selftext=""), dict(is_self=False),
                       dict(subreddit="OtherCommunity"), dict(over_18=True),
                       dict(stickied=True), dict(author="AutoModerator")]:
            with self.subTest(change=change):
                self.assertFalse(collector.eligible(dict(post(1), **change), "ChatGPT"))

    def test_pagination_and_deduplication(self):
        replies = [{"data": {"subreddit_type": "public"}},
                   listing(1, 101, "t3_100"), listing(100, 201, None)]
        with patch.object(collector, "fetch_json", side_effect=replies), \
                patch.object(collector.time, "sleep"):
            posts, pages = collector.collect("ChatGPT", 200)
        self.assertEqual(len(posts), 200)
        self.assertEqual(len({row["id"] for row in posts}), 200)
        self.assertEqual(pages, 2)

    def test_shortfall_is_not_filled(self):
        replies = [{"data": {"subreddit_type": "public"}}, listing(1, 4, None)]
        with patch.object(collector, "fetch_json", side_effect=replies), \
                patch.object(collector.time, "sleep"):
            posts, _ = collector.collect("ChatGPT", 200)
        self.assertEqual(len(posts), 3)

    def test_nonpublic_community_stops(self):
        with patch.object(collector, "fetch_json", return_value={"data": {"subreddit_type": "private"}}):
            with self.assertRaisesRegex(RuntimeError, "not confirmed public"):
                collector.collect("ChatGPT", 200)


if __name__ == "__main__":
    unittest.main()
