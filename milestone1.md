# Milestone 1: community choice and exploratory reading

**Collection update (October 20, 2026):** Chrome access became available.
`data/reddit_50_posts.csv` now contains 50 unique public r/ChatGPT text
submissions, with title plus body and separate source metadata. Of these,
44 were checked on full submission pages and six were captured from feed
text bodies before Chrome blocked further navigation. See
`data/reddit_50_collection_notes.md` for provenance, limitations, and fresh
candidate distinctions. The original 200-post target is not yet complete.

## Community

Use public **r/ChatGPT**, focusing on text submissions about experiences,
opinions, comparisons, and everyday AI use. It covers many uses over time,
rather than one show or one release. Public submission text was readable
through web search without a Reddit login or invitation. One of the seven
previously pasted examples, about AI replacing commercial software, was
located in this community:
https://www.reddit.com/r/ChatGPT/comments/1x5p4vz/

The other pasted examples do not have verified subreddit provenance. Preserve
them as exploratory examples; do not assume all seven belong to r/ChatGPT.

## Reading record and limits

The AI assistant read the available search-indexed text of **35 distinct
r/ChatGPT submissions**, in addition to the seven user-pasted examples, and
wrote one observation for each. See `data/reddit_reading_sample.csv` for the
35 texts, source URLs, and observations. These are AI-assisted reading notes;
they are not a claim that the student personally read these 35 posts.

The search queries deliberately covered everyday uses, study, experiments,
opinions, hallucinations, and cancellations to expose variation. This is an
exploratory convenience sample, not a representative sample. Search indexing
can omit or truncate material: these texts need a completeness check against
the live submissions before use as final training examples. Comment-only
results, known removed posts, and obvious image-only results were excluded.
Links, scores, and usernames are not intended as classifier inputs.

## Four candidate distinctions visible in the text

1. **Concrete evidence versus an unsupported verdict.** Some authors give a
   specific input, output, failure sequence, count, or comparison. Others say
   the model is worse or better without showing an example. R32 describes
   duplicate invoices and a cancellation timeline; R22 claims frequent
   hallucination without providing a particular wrong answer. A claimed
   invoice is evidence described by the author, not something we verified.

2. **A test someone could repeat versus an impression.** R12 names the seed
   prompt, five prompt enhancers, pairwise judging, and win/loss counts.
   R2 reports perceived deterioration without a fixed task or comparison
   procedure. Merely saying that something was tested does not make the
   procedure reproducible.

3. **A conclusion limited to the example versus a broad generalization.**
   R6 explicitly limits the detector observation to short texts. R26 claims
   a 100% hallucination rate but does not give a counted denominator in the
   available text. R13 names limitations of model judging and blinding.
   Numbers alone do not establish a reliable finding.

4. **An explained connection versus a bare reaction or request.** R11
   explains how checking generated explanations against study material fits
   into the author's learning routine. R30 simply asks whether others are
   cancelling. The difference is whether the author connects an observation
   or action to an outcome, rather than merely expressing a feeling or
   asking for responses.

These are overlapping candidate features, not final mutually exclusive
labels. A question can contain evidence, and an angry post can explain a
specific failure. Length, enthusiasm, negativity, and the presence of a
number should not determine the label by themselves. The pasted coding-tool
comparison is a useful hard case: it is emotional but includes times and
code-size comparisons. The pasted money-making post lists concrete uses but
does not show the results of those tests.

## Collecting 200 public posts

The project places collection and labeling in Milestone 4. For this milestone,
the collection target is **200 unique text submissions from r/ChatGPT**.
Use title plus complete body as one example; do not count comments as extra
posts. Include short and long texts without selecting by intended label,
upvotes, sentiment, or presence of numbers. Exclude removed/deleted text,
duplicates, pinned announcements, NSFW, spoiler-tagged, and image-only posts.
Check that retained texts are English and understandable without images or
outside context. Collect replacements for anything rejected during review.

`collect_reddit.py` implements public-community verification, paginated
collection, duplicate filtering, source URLs, and a collection manifest:

```powershell
.\.venv\Scripts\python.exe collect_reddit.py --subreddit ChatGPT --count 200 --output data/reddit_posts.csv
```

**Current access limitation:** a direct public listing request returned HTTP
403 in the initial attempt. The collector is implemented, but live retrieval of 200
posts through it is not verified and no 200-post corpus has been created. Search-indexed
reading text is not a substitute for a verified complete corpus. If direct
access remains blocked, use ordinary public browsing to copy complete text
into a CSV, keep source URLs separately, and check the count and duplicates.
No invited community, private content, or access-control bypass is needed.

Do not count the staff/practice datasets, template rows, or unverified pasted
examples toward the final community-specific 200. Leave final taxonomy,
training labels, acceptance targets, and training results to later milestones.
