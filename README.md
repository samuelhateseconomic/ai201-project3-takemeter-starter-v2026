# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

TakeMeter is designed to classify public r/ChatGPT text submissions as
`analysis`, `hot_take`, `question`, or `reaction`, using the title and body
together. It distinguishes conclusions supported by concrete reported evidence,
general judgments without that evidence, specific requests for information,
and personal responses. These labels describe the post's evidence and purpose;
they do not establish whether its claims are true or whether it is a good post.
The current project dataset contains 200 fully AI-reviewed posts. A practice run completed earlier. On October 21, the user explicitly authorized a demonstration run on AI-reviewed project labels without further human review.


---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

Apply one label per post, reading the title and body together, in this order:
`analysis` → `hot_take` → `question` → `reaction`.
Definitions are also saved in [label_definitions.txt](label_definitions.txt),
beside [labels_template.csv](labels_template.csv).

### `analysis`

**Definition:** advances a claim, explanation, or recommendation and explicitly supports it with a concrete reported test and result, input/output example, or identifiable source fact relevant to that conclusion.

**Example 1:** [Tarot reading and memory](https://www.reddit.com/r/ChatGPT/comments/1xaoeiu/i_asked_ai_for_a_tarot_reading_and_it_almost_made/) (`t3_1xaoeiu`).
The author connects the apparently personal reading to earlier chat history,
quotes the model's memory explanation, and contrasts it with a later
script-based random draw. Those observations support the warning about
personalized readings; the model's own percentages are not independently
verified facts.

**Example 2:** [New ChatGPT voices](https://www.reddit.com/r/ChatGPT/comments/1xanz2w/what_do_you_think_of_the_new_chatgpt_voices/) (`t3_1xanz2w`).
The author supports the claim that voices work across languages by naming
Indian and Japanese voices tested in English and German and describing the
observed accents. The closing preference question does not remove that claim
and its supporting test.

### `hot_take`

**Definition:** asserts a general judgment, prediction, or recommendation about AI, a model, or its users without the concrete supporting evidence required for analysis.

**Example 1:** [A sweeping model complaint](https://www.reddit.com/r/ChatGPT/comments/1xao1t8/im_honestly_amazed_at_how_stupid_gpt6_is/) (`t3_1xao1t8`).
The title judges the model's intelligence and the body calls everything a
disaster; it describes symptoms but supplies no particular instruction,
source-file fact, or incorrect output that demonstrates the verdict.

**Example 2:** [The Beautiful Collaboration](https://www.reddit.com/r/ChatGPT/comments/1xavvtk/the_beautiful_collaboration_exploring_how_humans/) (`t3_1xavvtk`).
The author asserts that AI unlocks talent and that collaboration produces
distinctive work, using imagined musicians, writers, and programmers rather
than a reported test, actual output, or identifiable source fact. A thoughtful,
positive, long argument can still fit this label under the evidence rule.

### `question`

**Definition:** requests a specific explanation, instruction, recommendation, or comparison without advancing a supported conclusion or an unsupported general judgment of its own.

**Example 1:** [Roku App Development](https://www.reddit.com/r/ChatGPT/comments/1xauqnr/roku_app_development/) (`t3_1xauqnr`).
The whole body asks whether ChatGPT is the best tool to create a Roku app and
what alternatives people suggest; the author does not assert which is best.

**Example 2:** [Comparing two $20 plans](https://www.reddit.com/r/ChatGPT/comments/1xaqamq/has_anyone_tried_both_claude_pro_20_and_chatgpt/) (`t3_1xaqamq`).
The author gives usage context and asks for real-world limit comparisons;
the prices and reported hearsay set up the question rather than support an
answer the author has already adopted.

### `reaction`

**Definition:** shares a personal event, most important - feeling, appreciation, or illustrative AI output without a supported conclusion, a general judgment.

**Example 1:** [The sore-throat voice](https://www.reddit.com/r/ChatGPT/comments/1xaycth/my_chat_gpt_faked_a_sore_throat_and_said_it_was/) (`t3_1xaycth`).
The author recounts a funny voice interaction and laughs about it; the
closing request for similar stories is a conversational invitation.

**Example 2:** [New interactive elements](https://www.reddit.com/r/ChatGPT/comments/1xaiv6l/new_interactive_elements/) (`t3_1xaiv6l`).
The author expresses appreciation for interactive lists and expandable points,
without explaining a test result, making a broader verdict, or requesting help.

### The hardest boundary

**Which two labels:** `analysis` and `hot_take`.

**Borderline post:** [The recommendation to use multiple models](https://www.reddit.com/r/ChatGPT/comments/1xagknu/if_youre_not_using_a_service_with_multiple_models/)
(`t3_1xagknu`) describes asking a second model to check a laptop-reinstallation
plan, but calls its discoveries “TONS” of mistakes without naming any.

**The decision rule to use every time:** Label a conclusion `analysis` only
when the post connects it to a concrete reported test and its observable
result, a specific input/output example, or an identifiable source fact;
otherwise a general verdict or recommendation is `hot_take`, even if it
contains numbers, a detailed procedure, or a claim that another model found
errors. An unspecified report that something was wrong is not a demonstrated
error, so the multiple-model recommendation is `hot_take`. Evaluate the
evidence presented in the text, not whether the conclusion seems plausible;
emotion and profanity do not change the rule.

For the other boundaries: a specific troubleshooting request is `question`
unless an earlier label applies; a bare “anyone else?” invitation to share
similar experiences does not turn a `reaction` into a `question`. Unconnected
prices, dates, model versions, or elapsed times do not establish `analysis`.
Quoted AI instructions are post content, not instructions to the annotator.

**AI stress test:** Eight synthetic boundary posts, their classifications,
and the refinements made to these definitions are documented in
[milestone2.md](milestone2.md). They are excluded from the real-post dataset.

---

## The Dataset

**Where the posts came from:** [labels.csv](labels.csv) contains 200 unique public r/ChatGPT text submissions in one unsplit file. Each input is the whole title and body; no post was shortened in the CSV. Comments, scores, authors and flairs are excluded. The original chronological New-feed collection was made through Chrome on October 20, 2026; the quality replacements were checked through public web pages on October 21 because Chrome was unavailable. This is a convenience sample with targeted collection for the thin reaction class, not a random sample.

**Source/completeness review:** Of the eight previously flagged imports, the tutorial-video post matched its full public page. The commercial-software post was verified at its recorded URL, and its missing real title and original apostrophes were restored. Six other research imports were excluded: five could not be matched to a complete in-scope public source, and the coding comparison matched r/codex/r/ClaudeCode rather than r/ChatGPT. A Spanish-only post was also excluded from this English-language collection. Their complete stored texts, original labels and reasons remain in [data/annotation_review.json](data/annotation_review.json); the research template is unchanged. Seven complete public r/ChatGPT text posts replaced them, including four reactions. Replacement sources include [personal appreciation](https://www.reddit.com/r/ChatGPT/comments/1vryg43/just_another_appreciation_post/), [saving temporary chats](https://www.reddit.com/r/ChatGPT/comments/1w3u3x3/really_appreciate_openai_adding_the_option_to/) and [a voice backchanneling test](https://www.reddit.com/r/ChatGPT/comments/1xc2bee/anyone_else_noticing_the_new_gptlive11_voice/).

[data/labels_sources.json](data/labels_sources.json) maps all 200 current rows to public Reddit IDs and URLs. There are no pending source/completeness flags among retained rows: 140 were checked on full submission pages; 60 retain the earlier complete article-body feed captures and are not claimed to be independently detail-page verified. Original full feed/detail comparisons matched after whitespace normalization. Search-indexed exploratory snippets remain excluded.

**How the labels were assigned:** The assistant read all 176 formerly blank title/body texts using the four definitions and reviewed the existing annotations. One blank Spanish-only row was replaced. It assigned 175 retained blank rows and seven replacements, reviewed all 200 final labels, and documented a reason for each. Every final row is marked ai_pre_labeled, ai_reviewed and human_review_pending in note. The user subsequently approved all 200 proposed labels on October 21, 2026. That approval is recorded as user_approved for each final row in the audit JSON; it does not change the annotations into independent cold labels or establish independent human agreement. CSV notes describe the frozen training-time status.

**Cold-label honesty record:** The on-disk file at the start of this review contained 24 cold annotations, including six question examples; the earlier README claim of zero questions was stale. All 24 original texts, labels and notes are preserved in the audit JSON. Six cold imports were excluded for source/scope reasons, leaving 18 retained cold-origin rows. Nine retained cold decisions were changed by AI review; their original labels remain in note and the audit, so they are not presented as independent final cold labels. The user waived additional human review for this demonstration; the final eligible file does not supply 20 untouched cold labels. New AI annotations cannot be retroactively called cold.

**Counts and quality checks:** analysis 54 (27%), hot_take 60 (30%), question 56 (28%), reaction 30 (15%). All four meet the filed 15%–45% target (30–90 of 200); none exceeds 70%. There are no blank/invalid labels or duplicate IDs/texts after Unicode NFKC normalization, case folding and whitespace collapse. The retained posts were not relabeled to reach a quota; new in-scope posts were collected for the thin class. The ordered dataset SHA-256 is 9f612b5d8bd0e9901a53ab87c717d49cfc5118d97503feb54fac2688903c1a8c. This records the frozen AI-reviewed training snapshot. The user subsequently approved the labels; the approval record is separate so the training/evaluation hashes remain valid.

**Three hard cases — AI review, awaiting human review**

1. **Voynich Manuscript, row 1:** reaction versus question. The personal curiosity frames a specific request: has anyone tried AI decoding? AI chose question, changing the original reaction. Unlike a bare “anyone else?”, this asks for information about a particular experiment. [Source](https://www.reddit.com/r/ChatGPT/comments/1xb9hhz/i_just_got_to_wondering_if_anyone_has_tried_using/).
2. **Ecological regeneration, row 4:** hot_take versus analysis. The long optimistic essay could look like unsupported advocacy, but it identifies a Fraunhofer augmented-reality application and IEA/UNEP findings and connects them to its argument about technological possibilities. AI chose analysis, changing the original hot_take. That label records evidence offered, not independent verification of its claims. [Source](https://www.reddit.com/r/ChatGPT/comments/1xb7x3b/the_future_does_not_belong_to_fear_or_speed_on/).
3. **Collaborative Reasoning Mode proposal, row 7:** analysis versus hot_take. The proposed method and evaluation metrics are detailed, but the example is hypothetical and no comparative test result is reported. AI chose hot_take, changing the original analysis. A plan to evaluate a recommendation is not evidence that it works. [Source](https://www.reddit.com/r/ChatGPT/comments/1xb7f8q/proposal_idea_by_me_refined_by_ai/).

These are AI-drafted adjudications. The earlier Muse/coding hard cases concerned excluded imports; their original texts and annotations remain archived, not final training examples.

---

## The Training Run

**Completed project run:** Sections 1–5 completed on October 21, 2026 with PRACTICE = False. The user explicitly authorized this demonstration run on AI-reviewed labels without additional human review, using ALLOW_AI_REVIEWED_LABELS = True. This does not claim human-reviewed gold or independent agreement. Sections 6–7 were not run.

**Model and settings:** distilbert-base-uncased; 3 epochs, learning rate 2e-5, batch size 16, maximum length 128 tokens, seed 42. Training defaults were unchanged.

**Actual kernel/device:** This project's .venv/Scripts/python.exe kernel, named TakeMeter (.venv); CPU, PyTorch 2.14.1+cpu; processor Intel64 Family 6 Model 170 Stepping 4, GenuineIntel. CUDA was unavailable. Hardware can change numerical results even with the same data and seed.

**Data checks and actual split:** All 200 rows have allowed labels, no normalized duplicate texts/IDs, and class shares within 15%–45%. The notebook performed the only saved stratified split: 139 train / 31 validation / 30 test. Its unchanged validation-size calculation rounds up. Train counts are analysis 38, hot_take 42, question 39, reaction 20; validation counts are 8, 9, 9, 5; test counts are 8, 9, 8, 5. No texts overlap between splits. Reaction has only five test examples, below the roughly eight-example guideline, so its metrics are especially sensitive to individual posts and seed.

**Input-length limitation:** Full posts remain in labels.csv. The default 128-token model window truncates 66 training, 16 validation and 16 test posts (98 of 200 total). Evidence or a request late in a post can therefore be present for annotation but absent from the trained model's input. No length setting was changed after seeing test results.

**Saved project artifacts:** [results.json](results.json) now records run_kind: project and dataset: labels.csv, all four classes, device/settings, dataset and definition hashes, per-post predictions/confidence and truncation counts. [test_split.csv](test_split.csv) contains the 30 project test posts used for both trained and baseline scoring. The model and tokenizer are saved locally under takemeter_out/project/model/ (ignored by Git). The notebook retains execution outputs. Earlier practice_results.json and practice_test_split.csv remain clearly separate practice evidence.

**Validation:** Notebook sections 1–5 finished without error, the saved kernel path and four-class map were verified, and split membership was checked for leakage. [data/dataset_validation.json](data/dataset_validation.json) records the data checks and demonstration authorization. The filed acceptance targets have not been lowered. The three-seed run and project-taxonomy comparison are now recorded below; project-label agreement was 15/30 and MISSED, with the caveat that the primary labels were AI-reviewed before approval.

---

## How I Used AI

**Moment 1 — merging collections and resolving source quality**

I asked AI to merge my earlier 50-post collection and research examples, then collect 42 more public posts. It found 49 of the earlier posts already present, recovered seven research texts from malformed CSV quoting, and replaced a duplicate repost. In the later quality review, it verified two flagged imports, restored a missing real title, excluded six unverifiable/out-of-scope research imports and one Spanish-only post, and collected seven complete replacements. I kept one unsplit dataset and a source/audit record instead of counting every import as eligible.

**Moment 2 — checking training evidence before comparison**

I asked AI to run notebook sections 1–5 in the project virtual environment. It found that the original checker ignored missing labels, added explicit checks, and completed an authorized practice run when project labels were unfinished. I later asked for project training and the baseline comparison. AI prepared the four-label project configuration and added baseline compatibility checks. Automatic review initially blocked execution because human review was pending; I then explicitly waived that review for this demonstration. The assistant completed sections 1–5 on the project data with the default settings and regenerated the required result files and completed the baseline on the same 30 held-out posts.

**Pre-labeling disclosure:** In this review, AI read the complete stored title/body of all 176 blank posts, assigned labels to the 175 retained blank rows and seven replacements, and reviewed every final row against the definitions. It also revised nine retained cold-origin labels. All 200 final rows disclose AI involvement and pending human review in note. The 24 original cold annotations remain separately archived with unchanged text, labels and notes; 18 of those sources remain eligible in the current CSV. The per-post rationales and exclusions are in data/annotation_review.json. I authorized training with AI-reviewed labels for this demonstration and subsequently approved those proposed labels. This approval is recorded as user_approved; it is not a claim that the labels were assigned cold before seeing AI suggestions. The assistant's reread does not satisfy the course's human-review or independent-agreement requirement.

**Moment 3 — comparing errors and recording the improvement:** I asked AI to
compare the three-seed confusion matrices and metrics. It highlighted that the
model never predicted `reaction` in any before-run seed, which led me to choose
inverse-frequency class weighting as one targeted change. AI ran the same
three seeds and helped summarize the result: `reaction` F1 improved in only one
seed, while `hot_take` errors increased there, so the change did not help
consistently. I also used AI to match the second reader's labels to the 30
sampled project posts and calculate the pre-adjudication rate; it found 15/30
agreement and recorded the primary-label provenance caveat. I reviewed the
calculation and kept the result separate from the 30/30 staff-taxonomy check.

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

Completed with the project .venv: python baseline.py --trained results.json. Both models scored the same ordered 30 project test posts with all four labels; the old practice comparison has been replaced. Evidence: [baseline_results.json](baseline_results.json) and [results.json](results.json). The baseline used facebook/bart-large-mnli on CPU with label_definitions.txt, without training examples. Its default input window differs from the trained model’s 128-token window.

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.300 | 0.500 | +0.200 |
| Macro F1 | 0.217 | 0.411 | +0.194 |
| F1 — `analysis` | 0.424 | 0.533 | +0.109 |
| F1 — `hot_take` | 0.000 | 0.588 | +0.588 |
| F1 — `question` | 0.000 | 0.522 | +0.522 |
| F1 — `reaction` | 0.444 | 0.000 | -0.444 |


**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

### Metrics by seed

| Measure | Seed 42 | Seed 7 | Seed 2024 | Spread |
|---|---:|---:|---:|---:|
| Overall accuracy | 0.500 | 0.433 | 0.367 | 0.133 |
| Macro F1 | 0.411 | 0.315 | 0.273 | 0.138 |
| F1 — `analysis` | 0.533 | 0.222 | 0.222 | 0.311 |
| F1 — `hot_take` | 0.588 | 0.538 | 0.435 | 0.153 |
| F1 — `question` | 0.522 | 0.500 | 0.435 | 0.087 |
| F1 — `reaction` | 0.000 | 0.000 | 0.000 | 0.000 |

Test support was the same for each seed: `analysis` 8, `hot_take` 9,
`question` 8, `reaction` 5. Accuracy ranged from 0.367 to 0.500, a 0.133
(13.3 percentage-point) spread—more than ten points. The dataset is too small
or too lopsided for a stable accuracy measure.

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | >= 0.70 | 0.500 | 0.433 | 0.367 | MISSED |
| 2. F1 for every label | >= 0.60 | analysis 0.533; hot_take 0.588; question 0.522; reaction 0.000 | analysis 0.222; hot_take 0.538; question 0.500; reaction 0.000 | analysis 0.222; hot_take 0.435; question 0.435; reaction 0.000 | MISSED |
| 3. Dataset balance | >= 200 rows; each label 15%–45% | 200 rows; 54/60/56/30 | 200 rows; 54/60/56/30 | 200 rows; 54/60/56/30 | MET |
| 4. Independent agreement | >= 24/30 | 15/30 (single check) | — | — | MISSED |
| 5. Confidence | Most-confident third >= 0.80 and >= 0.10 above least-confident third | 0.700 vs 0.300 (gap 0.400) | 0.600 vs 0.300 (gap 0.300) | 0.500 vs 0.300 (gap 0.200) | MISSED |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted | analysis | hot_take | question | reaction |
|---|---:|---:|---:|---:|
| **analysis** | 4 | 1 | 3 | 0 |
| **hot_take** | 1 | 5 | 3 | 0 |
| **question** | 0 | 2 | 6 | 0 |
| **reaction** | 2 | 0 | 3 | 0 |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->

The largest off-diagonal count is tied at 3 for `analysis`, `hot_take`, and
`reaction` posts called `question`; for the section-7 tie-break pair, 3 real
`analysis` posts were called `question` and 0 real `question` posts were called
`analysis`, so that confusion is asymmetric.

---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Overall accuracy | >= 0.70 on every seed | MISSED | 0.500, 0.433, and 0.367; none reaches 0.70. |
| 2 | F1 for every label | >= 0.60 for all labels and seeds | MISSED | No seed meets all four F1 floors; `reaction` is 0.000 in all three. |
| 3 | Dataset balance | >= 200 rows; every label 15%–45% | MET | 200 eligible rows; counts 54/60/56/30 are 27%/30%/28%/15%. |
| 4 | Independent agreement on our taxonomy | >= 24/30 with a second human reader | MISSED | The second reader matched 15/30 sampled project posts (50%), below 24/30. My primary labels were AI-prelabeled/reviewed and user-approved, not an independent cold human pass, so interpret this as agreement with the frozen labels rather than a clean human-human reliability estimate. |
| 5 | Confidence | Most-confident third >= 0.80 and >= 0.10 above least-confident third, on every seed | MISSED | Gaps pass (0.400, 0.300, 0.200), but most-confident-third accuracy is only 0.700, 0.600, and 0.500. |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->

**1. Overall accuracy — MISSED.** All three scores are below 0.70, and they
span 0.133 on only 30 held-out posts per seed. The seed-42 matrix shows errors
between `analysis`/`hot_take` and `question`, and every `reaction` post is
misclassified; the different seeds move those errors around. This points to a
small test set and a model that has not reliably separated these labels, not a
single isolated boundary. The second-reader comparison matched only 15/30
sampled project posts, which flags substantial disagreement with the frozen
labels; however, because those primary labels were AI-reviewed rather than
independently cold-labeled by me, the comparison does not isolate whether the
disagreements come from my labeling or the second reader's interpretation.

**2. Per-label F1 — MISSED.** `reaction` has F1 0.000 for every seed: the model
never predicts `reaction`, despite five gold reaction posts in each test split.
There are only 30 reaction examples in the full dataset and 20 in the
seed-42 training split, so too few examples for this class are a concrete
limitation. The model instead sends reaction posts to `question`, `analysis`,
or `hot_take`, depending on the seed. `analysis` is also unstable: its recall
falls to 0.125 for seeds 7 and 2024, when most true analysis posts become
`question` or `hot_take`. The project-taxonomy second-reader comparison is
only 15/30, which is evidence that the frozen labels and second reader often
disagree on this sample. Since my primary labels were AI-reviewed and then
user-approved, this comparison cannot by itself establish which reader is
right or separate annotation disagreement from model error. The evidence
supports class scarcity and confusable boundaries; it does not isolate one as
the only cause.

**3. Dataset balance — MET.** The 200-row dataset meets the 15%–45% limits:
`analysis` 54 (27%), `hot_take` 60 (30%), `question` 56 (28%), and `reaction`
30 (15%). Meeting this count target does not mean each class has enough
examples to learn reliably; the reaction results show that it may not.

**4. Independent agreement — MISSED.** On the 30 posts selected from my
project dataset, the second reader matched the frozen primary labels on
15/30 (50%), below the 24/30 target. The reader assigned no posts to
`question` (their counts were analysis 9, hot_take 4, reaction 17), which
accounts for several of the disagreements. This is a real mismatch signal,
but the primary labels were AI-prelabeled and AI-reviewed before I approved
them; this is not a clean comparison between two independent human labeling
passes. The staff-taxonomy 30/30 result is separate and does not change this
project-taxonomy rate.

**5. Confidence — MISSED.** The most-confident third is below the required
0.80 in every seed: 7/10 correct for seed 42, 6/10 for seed 7, and 5/10 for
seed 2024. The confidence gap does exceed 0.10 each time, so ranking separates
the easier cases somewhat, but even the selected high-confidence cases are
not accurate enough. With ten posts in each third, a single post changes the
rate by 0.10; this small evaluation set and the underlying classification
errors limit how firmly confidence can be judged. The staff-taxonomy
agreement does not test confidence or validate the project labels.

None of the targets was lowered or revised. The project-label comparison is
15/30 and therefore below the filed agreement target, with the caveat that my
primary labels were AI-reviewed and user-approved rather than an independent
cold human pass. The separate 30/30 staff-taxonomy agreement only shows a
match under the staff definitions; it does not change this project-taxonomy
result.


---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** 30 / 30 = 100%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

There were no disagreements to adjudicate.

**What the pattern in my disagreements tells me:**

All 30 labels matched staff under the staff taxonomy, so this check found no
inconsistencies on this selected set. It does not independently validate the
labels on the separate 200-post project dataset.

### Project-Taxonomy Agreement

**Agreement rate:** 15 / 30 = 50% — **MISSED** against the 24/30 target.

The 30 sampled posts are in
[data/project_agreement_sample.csv](data/project_agreement_sample.csv); the
second reader's matched labels are in
[data/project_agreement_second_reader.csv](data/project_agreement_second_reader.csv).
The matched original labels, comparison, and disagreements are saved in
[project_agreement_results.json](project_agreement_results.json). The comparison
was computed before discussion or adjudication. My primary labels were
AI-prelabeled and AI-reviewed, then user-approved; therefore this measures
agreement with the frozen project labels but is not a fully independent
human-versus-human reliability check.

| Source ID | Primary label | Second reader |
|---|---|---|
| t3_1w3u3x3 | `reaction` | `analysis` |
| t3_1x8lvt8 | `hot_take` | `analysis` |
| t3_1x8uj5f | `hot_take` | `reaction` |
| t3_1x9914y | `question` | `reaction` |
| t3_1x9au4s | `reaction` | `hot_take` |
| t3_1x9kde1 | `question` | `reaction` |
| t3_1xabzal | `question` | `reaction` |
| t3_1xaod5p | `question` | `reaction` |
| t3_1xaoh8e | `hot_take` | `reaction` |
| t3_1xaqamq | `question` | `reaction` |
| t3_1xatizb | `question` | `reaction` |
| t3_1xb11xr | `question` | `analysis` |
| t3_1xb1vts | `question` | `reaction` |
| t3_1xb33a6 | `question` | `reaction` |
| t3_1xb4h8o | `analysis` | `reaction` |

---

## The Improvement

**What I changed:** I used inverse-frequency class weights in the training loss,
calculated separately from each seed's training split. This gives more weight
to labels with fewer training examples; for these stratified splits, `reaction`
received weight 1.738, compared with 0.827–0.914 for the other labels. The
dataset, splits, seeds, model, and other training settings stayed fixed.

**Which diagnosis pointed at it:** `reaction` had F1 = 0.000 in all three
before-run seeds, with only 30 training examples in the full dataset and 20 in
each training split. Class weighting directly tested whether increasing the
loss for that underrepresented label would help.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Overall accuracy | >= 0.70 | 0.333 | 0.467 | 0.400 | MISSED |
| 2. F1 for every label | >= 0.60 | analysis 0.500; hot_take 0.000; question 0.400; reaction 0.348 | analysis 0.714; hot_take 0.333; question 0.522; reaction 0.000 | analysis 0.500; hot_take 0.250; question 0.519; reaction 0.000 | MISSED |
| 3. Dataset balance | >= 200 rows; each label 15%–45% | 200 rows; 54/60/56/30 | 200 rows; 54/60/56/30 | 200 rows; 54/60/56/30 | MET |
| 4. Independent agreement | >= 24/30 on the same project posts | 15/30 (single check) | — | — | MISSED |
| 5. Confidence | Most-confident third >= 0.80 and >= 0.10 above least-confident third | 0.400 vs 0.300 (gap 0.100) | 0.800 vs 0.300 (gap 0.500) | 0.500 vs 0.200 (gap 0.300) | MISSED |

### Before / After Comparison

Each cell shows `before → after`; the after run changes only the loss to use
inverse-frequency class weights.

| Measure | Seed 42 | Seed 7 | Seed 2024 |
|---|---:|---:|---:|
| Overall accuracy | 0.500 → 0.333 | 0.433 → 0.467 | 0.367 → 0.400 |
| Macro F1 | 0.411 → 0.312 | 0.315 → 0.392 | 0.273 → 0.317 |
| F1 — `analysis` | 0.533 → 0.500 | 0.222 → 0.714 | 0.222 → 0.500 |
| F1 — `hot_take` | 0.588 → 0.000 | 0.538 → 0.333 | 0.435 → 0.250 |
| F1 — `question` | 0.522 → 0.400 | 0.500 → 0.522 | 0.435 → 0.519 |
| F1 — `reaction` | 0.000 → 0.348 | 0.000 → 0.000 | 0.000 → 0.000 |
| Most-confident-third accuracy | 0.700 → 0.400 | 0.600 → 0.800 | 0.500 → 0.500 |

**Did it help, and how do I know:** Not reliably. `reaction` F1 rose from
0.000 to 0.348 for seed 42, but stayed at 0.000 for seeds 7 and 2024. Seed
42's `hot_take` F1 fell from 0.588 to 0.000 as eight true `hot_take` posts
were predicted as `reaction`; overall accuracy also fell from 0.500 to 0.333.
Accuracy improved slightly for seeds 7 and 2024, but all three remain below
0.70, and macro F1 moved in different directions (0.312, 0.392, 0.317 versus
0.411, 0.315, 0.273 before). The 0.133 accuracy spread is still greater than
ten percentage points. The weight change shifted errors between labels rather
than producing a consistent improvement.

The after-run keeps the same 30-post test support per seed: `analysis` 8,
`hot_take` 9, `question` 8, and `reaction` 5. The detailed per-seed metrics,
confusion matrices, confidence results, and class weights are saved in
`results_three_seeds_after.json`.

---

## What's Still Broken

**Overall accuracy — MISSED.** All three after-run scores (0.333, 0.467, and
0.400) remain below 0.70, with a 0.133 spread. The next step would be a larger,
independently reviewed dataset followed by a fresh fixed three-seed evaluation;
I stopped after the one class-weighting change required for this iteration
rather than make additional changes whose effects could not be separated.

**Per-label F1 — MISSED.** `reaction` remains at F1 = 0.000 in two seeds and
reaches only 0.348 in the third; `hot_take` is below 0.60 in every seed. The
next step would be to collect and human-review more examples for the weak
`reaction`/`hot_take` boundary, not simply increase its loss weight again. I
stopped because adding data is a separate improvement and the current set
needs independent review before it is suitable for retraining.

**Independent agreement — MISSED in the measured comparison; formal
human-to-human agreement remains unverified.** The second reader matched the
frozen labels on 15/30 posts, below 24/30. The sample, second-reader labels,
and pre-adjudication comparison are saved in
[data/project_agreement_sample.csv](data/project_agreement_sample.csv),
[data/project_agreement_second_reader.csv](data/project_agreement_second_reader.csv),
and [project_agreement_results.json](project_agreement_results.json). Because
the primary labels were AI-prelabeled/reviewed before user approval, the next
step would be a new blinded primary-human labeling pass and a second-reader
pass on the same posts. I stopped without claiming that result: the primary
labels were not made independently or cold, and relabeling after seeing the
existing labels would not recreate a blind pass.

**Confidence — MISSED.** Only seed 7 reaches 0.80 in the most-confident third;
seeds 42 and 2024 reach 0.400 and 0.500. The confidence gap passes, but the
accuracy threshold must also hold in every seed. A next step would be a
separately justified confidence-calibration experiment on validation data,
then evaluation on a new held-out set. I stopped because this iteration's one
change targeted class imbalance, not confidence, and I did not tune against
the small test sets.

**The gap between what I meant my labels to capture and what the model
learned:**

The before-run confusion matrix tied at three errors for `analysis`, `hot_take`,
and `reaction` posts predicted as `question`, while class weighting sent eight
of nine true `hot_take` posts to `reaction` in seed 42, showing the model's
errors shift by seed rather than resolving one stable boundary. The 15/30
second-reader match also shows substantial disagreement with the frozen labels,
but because those primary labels were AI-reviewed, it does not establish which
reader's interpretation is correct.



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
