"""Collect public Reddit text submissions without a login (standard library only)."""

import argparse
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def fetch_json(url):
    request = Request(url, headers={"User-Agent": "TakeMeter-class-project/0.1"})
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as error:
        raise RuntimeError(
            f"Reddit returned HTTP {error.code}. Collection stopped; "
            "no login or access-control bypass was attempted."
        ) from error
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Could not read the public Reddit listing: {error}") from error


def eligible(post, subreddit):
    body = post.get("selftext", "").strip()
    return (
        post.get("subreddit", "").casefold() == subreddit.casefold()
        and post.get("is_self") is True
        and bool(body)
        and body.casefold() not in {"[removed]", "[deleted]"}
        and not any(post.get(flag) for flag in ("spoiler", "over_18", "stickied"))
        and not post.get("removed_by_category")
        and not post.get("author") in {"AutoModerator", "[deleted]"}
        and bool(re.fullmatch(r"[a-z0-9]+", post.get("id", "")))
        and post.get("permalink", "").startswith(f"/r/{post.get('subreddit')}/comments/")
    )


def collect(subreddit, target):
    base = f"https://www.reddit.com/r/{subreddit}"
    about = fetch_json(base + "/about.json?raw_json=1")
    if about.get("data", {}).get("subreddit_type") != "public":
        raise RuntimeError("Community is not confirmed public; collection stopped.")
    posts = []
    ids, texts, cursors = set(), set(), set()
    after = None
    pages = 0
    while len(posts) < target:
        time.sleep(2)
        params = {"limit": 100, "raw_json": 1}
        if after:
            params["after"] = after
        listing = fetch_json(base + "/new.json?" + urlencode(params)).get("data", {})
        pages += 1
        for child in listing.get("children", []):
            post = child.get("data", {})
            if child.get("kind") != "t3" or not eligible(post, subreddit):
                continue
            text = post.get("title", "").strip() + "\n\n" + post["selftext"].strip()
            normalized = " ".join(text.casefold().split())
            if post["id"] in ids or normalized in texts:
                continue
            ids.add(post["id"])
            texts.add(normalized)
            posts.append({
                "id": post["id"], "text": text,
                "source_url": "https://www.reddit.com" + post["permalink"],
                "created_utc": post.get("created_utc", ""),
            })
            if len(posts) == target:
                break
        after = listing.get("after")
        if not after or after in cursors:
            break
        cursors.add(after)
    return posts, pages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subreddit", default="ChatGPT")
    parser.add_argument("--count", type=int, default=200)
    parser.add_argument("--output", type=Path, default=Path("data/reddit_posts.csv"))
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_]{2,21}", args.subreddit) or args.count < 1:
        parser.error("Use a valid subreddit name and a positive count.")
    manifest = args.output.with_suffix(".manifest.json")
    if args.output.exists() or manifest.exists():
        parser.error("Output already exists; choose a new --output path to preserve it.")
    try:
        posts, pages = collect(args.subreddit, args.count)
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "text", "source_url", "created_utc"])
        writer.writeheader()
        writer.writerows(posts)
    complete = len(posts) == args.count
    manifest.write_text(json.dumps({
        "subreddit": args.subreddit, "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "target": args.count, "collected": len(posts), "complete": complete,
        "pages": pages, "method": "Public unauthenticated /new.json listing",
        "unit": "Submission title plus selftext; comments excluded",
        "filters": "No empty, removed, deleted, spoiler-tagged, NSFW, pinned, or duplicate posts",
        "sampling": "Newest eligible submissions; not a random sample; English not automatically verified",
    }, indent=2) + "\n", encoding="utf-8")
    print(f"Collected {len(posts)}/{args.count} posts into {args.output}")
    return 0 if complete else 2


if __name__ == "__main__":
    sys.exit(main())
