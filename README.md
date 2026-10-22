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

**Validation:** Notebook sections 1–5 finished without error, the saved kernel path and four-class map were verified, and split membership was checked for leakage. [data/dataset_validation.json](data/dataset_validation.json) records the data checks and demonstration authorization. The filed acceptance targets have not been lowered; one seed does not evaluate the required three-seed criteria, and independent human agreement remains NOT EVALUATED.

---

## How I Used AI

**Moment 1 — merging collections and resolving source quality**

I asked AI to merge my earlier 50-post collection and research examples, then collect 42 more public posts. It found 49 of the earlier posts already present, recovered seven research texts from malformed CSV quoting, and replaced a duplicate repost. In the later quality review, it verified two flagged imports, restored a missing real title, excluded six unverifiable/out-of-scope research imports and one Spanish-only post, and collected seven complete replacements. I kept one unsplit dataset and a source/audit record instead of counting every import as eligible.

**Moment 2 — checking training evidence before comparison**

I asked AI to run notebook sections 1–5 in the project virtual environment. It found that the original checker ignored missing labels, added explicit checks, and completed an authorized practice run when project labels were unfinished. I later asked for project training and the baseline comparison. AI prepared the four-label project configuration and added baseline compatibility checks. Automatic review initially blocked execution because human review was pending; I then explicitly waived that review for this demonstration. The assistant completed sections 1–5 on the project data with the default settings and regenerated the required result files and completed the baseline on the same 30 held-out posts.

**Pre-labeling disclosure:** In this review, AI read the complete stored title/body of all 176 blank posts, assigned labels to the 175 retained blank rows and seven replacements, and reviewed every final row against the definitions. It also revised nine retained cold-origin labels. All 200 final rows disclose AI involvement and pending human review in note. The 24 original cold annotations remain separately archived with unchanged text, labels and notes; 18 of those sources remain eligible in the current CSV. The per-post rationales and exclusions are in data/annotation_review.json. I authorized training with AI-reviewed labels for this demonstration and subsequently approved those proposed labels. This approval is recorded as user_approved; it is not a claim that the labels were assigned cold before seeing AI suggestions. The assistant's reread does not satisfy the course's human-review or independent-agreement requirement.

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

This is a seed-42 demonstration against AI-reviewed labels, not independently human-reviewed gold. No training settings were changed in response to the test scores.

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
