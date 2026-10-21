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

TakeMeter sorts public r/ChatGPT text submissions into `analysis`, `hot_take`,
`question`, or `reaction` based on the evidence and communicative purpose in
their title and body. It distinguishes an argued conclusion from a general
verdict, a request for help or information, and a personal response. The labels
describe what the author presents; they do not establish whether the claims
are true or whether a post is good or bad.


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

**Definition:** shares a personal event, feeling, appreciation, or illustrative AI output without a supported conclusion, a general judgment, or a specific request for information or action.

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

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** [labels.csv](labels.csv) now contains 200 unique collected texts in one unsplit file. The initial 150 are public r/ChatGPT text submissions collected through Chrome from the New feed on October 20, 2026, using title plus the complete loaded body without length truncation. The longest of those rows has 25,365 characters. Comments, scores, usernames, and flairs are excluded from model input. This is a chronological convenience sample, not a random sample.

**Earlier collection and research merged:** 49 of the earlier 50 posts were already in the 150-row collection. Only the missing post, `t3_1xa76q7`, was appended; its earlier feed text is retained with `completeness_verification_pending`, because the later detail-page check did not verify it. Seven research examples were recovered from malformed quoting in labels_template.csv and appended with their original labels and `cold` notes unchanged. The two illustrative placeholder rows were excluded, and labels_template.csv itself was left unchanged. One research example has a previously recorded r/ChatGPT URL; six still require public-community/source verification, and all seven require a full-post completeness check. The 35 search-indexed exploratory texts in data/reddit_reading_sample.csv remain excluded until their completeness is checked.

**Source verification:** Source URLs, import origins, and verification flags are recorded in [data/labels_sources.json](data/labels_sources.json), with source or pending-verification notes in the CSV. Among the initial 150 posts, 89 were checked on full submission pages (44 earlier and 45 during the later collection), and 61 were captured from complete article-body elements loaded in the public feed. All 89 feed/detail comparisons matched after whitespace normalization. Feed-only records are not claimed as independently detail-page verified. The eight earlier imported records are retained for review and are not yet verified additions toward the final community-specific target. The subsequent 42-post batch was fully checked on submission pages, bringing detail-page-verified records to 131. All existing 158 rows and seven original labels were preserved unchanged.

**How I labelled them:** The current CSV has 24 labeled posts marked `cold`: 17 in the initial collection and seven imported from labels_template.csv. All existing annotations were preserved when the missing 42 posts were restored. Three initial reserved rows remain `cold_pending`, but the 20-post cold-count requirement is already exceeded if all 24 were independently labeled without AI help. There are 176 blank labels. No dataset AI pre-labeling has occurred; every later AI-proposed label needs human reading and correction. Original research decisions remain preserved for the honesty check.

**Counts per label:** Across 200 collected rows, treating surrounding label whitespace as formatting: reaction 13, hot_take 6, analysis 5, question 0, and unlabeled 176. Leading spaces in three label cells were removed during notebook setup; their classifications were preserved. These 24 labels do not establish final dataset balance. The final majority check remains pending until annotation is complete: no class may exceed 70%, and the repository criterion further requires each class to represent 15%–45%.

**Collection target and stop rule:** The file now meets the 200-row collection count after adding 42 distinct English-language text submissions through Chrome. Every new post was checked on its full public r/ChatGPT submission page, with title and complete body retained. One repost with identical text under a different ID was excluded and replaced. No stop-rule exception is needed for the row count. The eight earlier imports still need their documented source/completeness checks; replace any that fail. Keep one file, and let the notebook perform the 70/15/15 split.

**Three hard cases**

These writeups were drafted by the AI assistant after reading the full stored
posts and the current definitions in label_definitions.txt. They document
AI review decisions, not the student's original reasoning or a claim that
the student paused on these exact posts. Original cold labels in labels.csv
are preserved unchanged. The student still needs to review these rationales
and adjudicate the two proposed changes before treating them as final
annotation decisions. Row numbers below count data rows, excluding the header.

**1. A coding comparison with an emotional verdict**

- **The post:** Data row 157, `research_06`, begins “I saw a lot of comparisons here on Reddit between Codex and Claude.” The author reports that one tool left a project unfinished after five days, while another completed the same project in 30 minutes, and includes reported code-size comparisons. Its public source and completeness checks remain pending.
- **Could have been:** `hot_take` or `analysis`.
- **Original cold choice:** `hot_take`.
- **AI review choice:** `analysis`. The broad praise makes `hot_take` tempting, but the author connects the verdict to a named task and observable completion outcomes. Those details satisfy the current definition of a concrete reported test and result. The comparison is uncontrolled, and some size claims are quoted from the model, but the taxonomy does not require independent verification or rigorous experimental design. The reason is the connection between task, outcome, and conclusion—not merely the presence of numbers.
- **Review status:** Proposed change; the CSV still retains the original `hot_take` cold label.

**2. A money-making recommendation with a reported result**

- **The post:** Data row 154, `research_03`, titled “Zuck said \"Muse will Make You MONEY\"- I Tested 5 Use Cases.” It describes using a model to find newly opened restaurants without websites, recognizing one result from local coverage, contacting the business, and scheduling a meeting. Its public source and completeness checks remain pending.
- **Could have been:** `analysis` or `hot_take`.
- **Original cold choice:** `analysis`.
- **AI review choice:** `analysis`. Much of the post sounds promotional and makes unverified claims, but the restaurant example reports a particular search task, an identified result checked against the author's knowledge, and a concrete follow-up outcome. This supports the narrower conclusion that the tool can help identify business leads. It does not establish that the suggested ventures earn money or that the headline's promise is true. Under the current taxonomy, the relevant reported outcome is enough; the promotional tone does not override it.
- **Review status:** AI review agrees with the original label; human review of this rationale remains pending.

**3. Curiosity that asks for specific information**

- **The post:** Data row 1, `t3_1xb9hhz`, [using ChatGPT to decipher the Voynich Manuscript](https://www.reddit.com/r/ChatGPT/comments/1xb9hhz/i_just_got_to_wondering_if_anyone_has_tried_using/). After mentioning a possible page-order problem, the author asks whether anyone has heard of attempts to use AI to decode it.
- **Could have been:** `reaction` or `question`.
- **Original cold choice:** `reaction`.
- **AI review choice:** `question`. The personal curiosity supplies context, but the post seeks specific information about whether an experiment has been attempted. That differs from a bare invitation to share similar feelings or stories. The mention of researchers and page order does not establish `analysis`: the author does not present a test result supporting a conclusion that ChatGPT can decipher the manuscript.
- **Review status:** Proposed change; the CSV still retains the original `reaction` cold label.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** `distilbert-base-uncased`. A practice fine-tune completed successfully on the supplied fictional running-forum dataset; the r/ChatGPT project dataset has not been trained.

**Settings:** 3 epochs, learning rate 2e-5, batch size 16, maximum sequence length 128 tokens, seed 42. Training defaults retained.

**Hardware and kernel:** Ran locally on `cpu` (`CPU`), using PyTorch `2.14.1+cpu` and this project's `.venv/Scripts/python.exe` Jupyter kernel, named `TakeMeter (.venv)`. CUDA is unavailable. Processor identifier: `Intel64 Family 6 Model 170 Stepping 4, GenuineIntel`. Device details are also stored in the practice results. Hardware can affect numerical results even with the same data and seed; report the device beside later multi-seed results.

**What I trained on:** `PRACTICE = True` selects the supplied `data/practice_labels.csv`: 60 already-labeled fictional running-forum posts, with 20 each of `analysis`, `hot_take`, and `reaction`. Practice uses those three classes; the project's four-label map still includes `question`. This is a workflow rehearsal, not evidence of classifier performance on r/ChatGPT.

**Anything I changed from the defaults, and why:** No training hyperparameters changed. Filled in the results name/email from the repository's Git identity and selected the project virtual-environment kernel. Added an explicit practice switch to choose the appropriate label map, dataset, model directory, and result provenance. Section 5 uses the required results.json and test_split.csv filenames in either mode; the JSON records whether the dataset is practice or project data. Fixed the checker to reject missing labels and surrounding label whitespace, and added a guard before splitting if section 2 reports problems. The original checker silently ignored empty label cells. Removed leading spaces from three project label cells without changing classifications, notes, or post text; that formatting fix was committed before this practice run. The fine-tuned model and tokenizer are now saved for reuse.

**Data checks and split sizes:** Practice data passed all blocking checks; its 60-row size warning is expected. The notebook performed one stratified 70/15/15 split: **42 train / 9 validation / 9 test**, with **14 / 3 / 3 per class**. Every class has only three test examples, below the roughly eight-example guideline, so practice metrics are especially sensitive to seed and individual predictions. Checks verified no shared post text across the three splits. Sections 1–5 completed; sections 6–7 were not run.

**Saved practice artifacts:** The latest sections 1–5 run wrote [results.json](results.json) and [test_split.csv](test_split.csv), using the exact filenames required by the notebook workflow. These currently contain **practice data**, identified in the JSON by `run_kind: practice` and `dataset: data/practice_labels.csv`; they are not r/ChatGPT evaluation evidence. The earlier [practice_results.json](practice_results.json) and [practice_test_split.csv](practice_test_split.csv) are retained from the preceding practice run. The model and tokenizer are saved locally under `takemeter_out/practice/model/`, which Git ignores. The notebook retains the execution outputs. Metrics have not been interpreted against project criteria.

**Project dataset status:** `labels.csv` remains at 200 posts, with 24 cold labels and 176 blank labels. The previous project-data check stopped correctly on those blanks and reported no labeled `question` examples. The practice run did not change this file. The current `results.json` and `test_split.csv` describe the fictional running-forum practice run, so they must be regenerated after project data is ready before using them for the project baseline. After project labeling, review, and verification are complete, set `PRACTICE = False`, rerun from section 1, resolve section 2 findings, and record the actual project split and device. Project results will use the normal filenames.


---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:** The assistant collected and formatted the initial 150 public posts through Chrome, then merged one missing earlier collection record and seven research examples from labels_template.csv after checking overlap, and collected 42 more full-page-verified public posts in Chrome. All 24 current labels marked cold were preserved without relabeling; 176 rows remain unlabeled. The assistant also drafted three hard-case reviews from existing cold-labeled posts, proposing two different labels under the current definitions without changing labels.csv. These rationales await human review. No batch AI pre-labeling has occurred. Imported provenance, completeness, and cold-pass eligibility still need confirmation.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

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

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

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

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



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
