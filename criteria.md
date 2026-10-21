# Acceptance criteria — TakeMeter

Written on October 20, 2026, before training or examining model results.
These targets apply to the four labels in `label_definitions.txt`:
`analysis`, `hot_take`, `question`, and `reaction`.

The planned dataset contains at least 200 unique public r/ChatGPT posts;
200 collected texts are currently retained (eight appended imports still need
source/completeness review); 24 current cold labels are preserved, and
final label counts are not yet known.
The notebook uses a stratified 70% training / 15% validation / 15% test split,
so 200 posts produce approximately 140 / 30 / 30 examples.

---

## Measurement rules

Evaluate model criteria 1, 2, and 5 separately for seeds **42, 7, and 2024**,
using each run's untouched held-out test split. A model criterion is MET only
if its full target holds for **all three seeds**, not just their average.
Use unrounded metrics for the verdict and report test-set label counts.

Freeze `labels.csv`, the taxonomy, the ordered dataset, and a source-ID
mapping before training. The reference answer (gold label) is the final
human-reviewed label recorded in that frozen dataset, not a model prediction;
record any AI pre-labeling separately. Use the same frozen dataset and
training settings for all three seeds, with the notebook's split procedure
and label order `analysis`, `hot_take`, `question`, `reaction`.

Keep the dataset version/commit and, for each seed, the ordered test posts,
gold labels, predicted labels, and maximum softmax scores. Keep the per-seed
metrics and confusion matrices too. These are required evaluation records
to produce during training, not files claimed to exist already. With these
records, a reviewer can recompute criteria 1, 2, and 5 without asking which
posts or answers were used.

Check balance on the complete labeled dataset before splitting. Check
agreement on our own taxonomy separately from the later staff-taxonomy
exercise. Do not train on synthetic stress-test posts, tune against the test
set, or change these targets after seeing results; record and diagnose misses.
Report each criterion as MET, MISSED, or NOT EVALUATED; missing required
records mean NOT EVALUATED, never MET. An actually measured value below the
target is MISSED even when the sample is small.

---

## 1. Overall accuracy is at least 0.70

The classifier must correctly label **at least 70%** of held-out posts in
each seed's run; on a 30-post test set, that means at least **21 correct**.

**How to check:** Divide the number of exact predicted-label/gold-label
matches by the total number of test posts, including every test post. The
criterion is MET only when this fraction is at least 0.70 for all three seeds.

**Why this target:** With four labels, uniform random guessing averages 25%
accuracy, and criterion 3 limits the majority class to 45%. A 70% target
requires the model to distinguish the substantial overlap between evidence,
general opinions, personal reactions, and questions rather than mostly
predicting a common label.

---

## 2. Every label has F1 of at least 0.60

For **each of the four labels**, held-out F1 must be **at least 0.60** in
each seed's run, using F1 = 2 × precision × recall / (precision + recall)
and treating an undefined F1 as zero.

**How to check:** For each label, count true positives (TP), false positives
(FP), and false negatives (FN), treating that label as positive and all other
labels as negative; compute **F1 = 2TP / (2TP + FP + FN)**. Use zero when
the denominator is zero, and also mark this criterion MISSED if any label
has no gold examples in a test split. All **12 label/seed combinations** must
meet 0.60; a macro average cannot substitute for an individual label's F1.

**Why this target:** Overall accuracy could hide a model that confuses
`analysis` with `hot_take` or treats every conversational question as
`question` instead of `reaction`. I chose a lower floor than overall accuracy
because a label with 30 examples would contribute only about 4–5 test posts,
making its F1 sensitive to individual mistakes and the split seed; these are
planned minimum counts, not observed label counts.

---

## 3. Each label represents 15%–45% of at least 200 posts

The final dataset must contain **at least 200 unique real posts**, with
**every label accounting for at least 15% and at most 45%** of the rows;
for exactly 200 posts, that is **30–90 posts per label**.

**Why this target:** The exploratory collection contains many support
questions and reactions, so these could overwhelm evidence-based arguments
and general opinions. A 15% floor preserves a meaningful minority label,
while the 45% ceiling prevents a single label from dominating without
requiring an artificial 25% / 25% / 25% / 25% split.

Count full posts once, excluding duplicates, synthetic examples, and staff
practice data. Identify a submission by its Reddit post ID, regardless of
URL query strings; also remove repeated title-plus-body text after Unicode
NFKC normalization, case folding, and collapsing whitespace. Each retained
row must have exactly one of the four allowed labels and a source ID; posts
still awaiting a full-text completeness check are not eligible final rows.

**How to check:** On the frozen eligible dataset, let N be its row count and
n be the count for a given label. Require N >= 200 and, for every label,
**ceil(0.15 × N) <= n <= floor(0.45 × N)**. Do not round displayed percentages
to make a failing count pass; missing labels have count zero.

If the natural collection misses this target, report the
miss and expand public collection rather than changing labels to meet a quota.

---

## 4. Independent agreement is at least 80% on 30 posts

An independent human reader and the primary annotator must assign the same
label to **at least 24 of 30 posts (80%) before adjudication**, using only
the written taxonomy and decision rules.

**Why this target:** The `analysis` / `hot_take` evidence rule and the
`question` / `reaction` distinction should be usable by another reader,
not just familiar to their author. Allowing up to six disagreements makes
room for genuinely mixed posts, while a lower rate would suggest the
definitions still need work before model errors can be interpreted.

**How to check:** After the initial labeling pass, sort rows by source ID
and initialize one Python `random.Random(42)` generator. In the label order
`analysis`, `hot_take`, `question`, `reaction`, use that generator's `sample`
to draw five posts without replacement per label; then draw ten more from
the unused rows in source-ID order using the same generator. Save the selected
30 IDs so the actual sample is auditable; if any label has fewer than five
posts, report this agreement criterion as NOT EVALUATED and balance as MISSED.

Give a second human reader who did not produce the primary labels the
frozen taxonomy and the selected titles/bodies, without existing labels or
model predictions. The second reader must label all 30 without consulting
the primary annotator. Save both original label sets and compute exact
matches / 30 **before** discussion or correction. Do not substitute
adjudicated agreement, model agreement, or agreement under the staff taxonomy.
If there is no second reader or any of their labels is missing, report
NOT EVALUATED, not MET.

---

## 5. The most-confident third is at least 80% accurate and 10 points better

In each seed's held-out test set, the **most-confident third must have
accuracy of at least 0.80**, and its accuracy must exceed the least-confident
third's accuracy by **at least 0.10 (10 percentage points)**.

**Why this target:** Mixed questions and reactions, and opinions with weak
support, should be harder than clear cases under this taxonomy. With about
30 test posts, the most-confident group contains ten posts, so requiring
eight correct and at least one more correct than the least-confident group
tests whether confidence is useful for choosing posts that need human review.

**How to check:** Confidence is the maximum softmax probability across the
four labels, not a verbal claim of certainty. For each seed, preserve test
row order and sort by confidence ascending with stable ties (equal scores
keep their original test-row order); the notebook uses
`numpy.argsort(confidence, kind="stable")`. Let k = floor(N_test / 3), take
the first k rows as the least-confident group and the last k as the
most-confident group, and exclude any middle rows from these two groups.

Let H and L be the correct-prediction counts in those two equally sized
groups. Check **H >= ceil(0.80 × k)** and **H - L >= ceil(0.10 × k)**; both
conditions must hold for every seed. For k = 10, H = 8 and L = 7 passes;
H = 8 and L = 8 fails the gap requirement, and H = 7 and L = 5 fails the
80% requirement. If all confidence scores are equal, mark MISSED because
there is no confidence ranking; if scores were not saved, mark NOT EVALUATED.
This tests ranking usefulness, not probability calibration.

---

## AI checkability review before training

Review question: **Could someone check each criterion without asking its
author what it meant?** The AI assistant in this conversation performed this
review; it was not an independent human validation or a second model call.

- **1 — retained 0.70:** added an explicit denominator, exact-label matching,
  frozen gold labels, and the evaluation records needed to recompute it.
- **2 — retained 0.60 per label:** replaced potentially ambiguous averaging
  with one-versus-rest counts, all 12 required checks, and a missing-label rule.
- **3 — retained 200 posts and 15%–45%:** defined duplicate detection, eligible
  complete rows, and integer count limits so rounding cannot change a verdict.
- **4 — retained 24/30 independent matches:** specified reproducible sampling,
  reader independence, saved original labels, and incomplete-review handling.
- **5 — retained 0.80 and a 0.10 gap:** defined confidence, group size, tie
  handling, saved records, and count-based checks to avoid decimal subtraction
  changing a boundary verdict. The notebook's tie sorting was aligned with it.

These replace the earlier measurement wording before training. No numerical
target was lowered, and no model results were used to select the refinements.
These remain AI-assisted proposed targets for the student to understand and
defend; this file does not claim that the student independently authored them.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
