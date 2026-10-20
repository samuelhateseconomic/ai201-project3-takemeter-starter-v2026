# Public Reddit collection: 50 text posts

Collected on October 20, 2026 from the connected Chrome browser.

- Community: r/ChatGPT, visibly marked Public in its community information.
- Discovery: its New feed, scrolled through posts without selecting by quality label.
- Unit: submission title plus body. Comments, usernames, scores, and community flairs are not classifier inputs.
- Files: `reddit_50_posts.csv` for reading/labeling and `reddit_50_posts.json` for the separately stored title/body and collection metadata.
- Count: 50 distinct submission IDs. These are collected posts, not synthetic examples or staff examples.
- Filters: text-type posts with nonempty bodies and no spoiler or NSFW flag in the rendered feed. A long bilingual support-email repost was excluded.
- 44 bodies were extracted from their full public submission pages; six were extracted from public feed text bodies already loaded in Chrome.
- Chrome began returning `ERR_BLOCKED_BY_CLIENT` during the remaining detail-page visits. The six feed records have `detail_verified=false`; their completeness must be checked before treating them as final training examples. No blocked page was bypassed.
- The browser was already signed in, but these were submissions in a public community; no private or invitation-only content was accessed.
- Whitespace reflects rendered text. Typos, opinions, quoted model responses, and author claims are preserved. Claims within the posts have not been fact-checked.
- No quality labels were assigned. The text includes AI-generated passages quoted by authors, satire, short questions, complaints, and longer arguments. This variation should be considered when designing labels.
- This is a chronological convenience sample, not a random or representative sample of Reddit. It is separate from the earlier search-indexed reading sample; do not add their row counts without deduplicating.

## Candidate distinctions from reading this collection

1. **Some posts give a specific example; others state a general impression.** One describes a pinned chat failing while other chats still work (`t3_1xaqy1n`). Another says ChatGPT has become worse without showing a failed task (`t3_1xaoh8e`).

2. **Some describe what they tried; others only describe the problem.** Authors mention switching models, restarting chats, or changing instructions, while others simply ask whether anyone has the same issue. For example, `t3_1xagknu` describes copying a chat to a second model for review, while `t3_1xarlnh` lists symptoms without a diagnostic procedure or comparison.

3. **Some include numbers; others use vague amounts.** Posts name five-hour limits (`t3_1xasfaq`), hours of lost work (`t3_1xabrg8`), or subscription prices (`t3_1xaqamq`). Others say “slow,” “often,” or “much better.” A number is an observable feature, not proof that a claim is reliable.

4. **Some acknowledge uncertainty; others make sweeping claims.** One author explicitly calls their probabilities guesses (`t3_1xaf7oa`). Others describe a model as useless based on their own experience; for example, `t3_1xao1t8` presents a sweeping capability verdict based on personal project problems.

These are overlapping features to explore, not final mutually exclusive labels.
For example, a strongly worded complaint can still contain specific observations.
The assistant read and collected these texts; this does not assert that the
student has personally read or labeled all 50.
