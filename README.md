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

**Where the posts came from:**

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:**

| Label | Count | Share |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
| **Total** |  | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**2.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

**3.**
> *The post:*
>
> *Could have been:*
>
> *I chose, because:*

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



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

**Pre-labelling disclosure:**

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
