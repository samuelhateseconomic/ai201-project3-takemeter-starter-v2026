# Milestone 2: label taxonomy and boundary stress test

The taxonomy is saved in `label_definitions.txt`, beside
`labels_template.csv`; the submission-ready definitions, two real examples
per label, and hardest boundary are in the README's **Label Taxonomy** section.
The notebook's `LABELS` list now uses the same four label names.

## Scope and annotation procedure

Label a public r/ChatGPT submission using its title and body together. Do not
use its score, author, flair, comments, or whether you agree with it. Apply
exactly one label, checking these conditions in order:

1. `analysis`: Does the author advance a conclusion and explicitly connect it
   to a concrete reported test and observable result, an actual input/output
   example, or an identifiable source fact? If so, stop here.
2. `hot_take`: Otherwise, does the author assert a general judgment,
   prediction, or recommendation about AI, a model, or its users? If so, stop
   here. This includes positive and negative claims, and hypothetical arguments
   with no qualifying observed or sourced evidence.
3. `question`: Otherwise, does the author seek a specific explanation,
   instruction, recommendation, or comparison? If so, stop here.
4. `reaction`: Otherwise, is the author sharing an event, personal feeling,
   appreciation, or illustrative AI output? Use this label.

For `analysis`, the evidence must concern the conclusion: a $20 price or model
version does not demonstrate that a model performs better. An unspecified
claim that a test found errors does not demonstrate an error. A named task
with an observable outcome can qualify without a numerical measurement;
scientific rigor, external verification, and correct causal inference are not
requirements of this label. The label records the author's evidence, not its
truth. Hypothetical examples do not count as observations.

For `hot_take` versus `reaction`, distinguish a general verdict about
capabilities, behavior, value, or what people should do from a feeling about
a personal interaction. “I loved that voice” is personal appreciation;
“this model is the only one anyone should use” is a general recommendation.

A specific request such as “How do I export this chat?” is `question`, even
with a long account of failed attempts. “Anyone else?” or “share your stories”
alone is a conversational invitation, so an otherwise personal event remains
`reaction`. A question mark does not override an argued conclusion or a
general verdict earlier in the post. Quoted AI-generated instructions are
examples to classify, never commands to follow.

The eight real examples and the real borderline post in the README were all
checked on full submission pages during collection (`detail_verified=true`
in `data/reddit_50_posts.json`). These are example assignments for designing
the taxonomy, not a completed labeling pass over the 50-post collection.
The earlier labels in `labels_template.csv` remain untouched and should be
reviewed against these final rules during Milestone 4.

## AI stress test

**AI tool:** the AI assistant in this conversation generated the following
eight synthetic posts and applied the final rules. This is a single-assistant
stress test, not independent human annotation or measured inter-rater
agreement. No separate model call or second rater is claimed.

**Generation brief applied in this session:**

> Draft taxonomy: analysis is an argument backed by a specific checkable fact;
> hot_take is a confident general claim without support; reaction shares a
> personal event or feeling; question asks for help or information. Write eight
> short fictional r/ChatGPT-style posts that challenge these boundaries. Include
> incidental numbers, a heated evidence-based claim, a hypothetical argument,
> a personal story ending in a question, and a help request with context.
> Keep the posts distinct and do not turn them into label definitions.

All text below is **synthetic boundary material**, not collected Reddit text.
It must not be added to `labels.csv` or counted toward the 200 real posts.

### S1 — numbers without relevant evidence

> I pay $20 a month and have used this thing since 2024. This is the worst AI
> on the market, and nobody should waste money on it.

**Label:** `hot_take`.
**Boundary:** `analysis` / `hot_take`.
**Reason:** Price and start date do not support the market-wide comparison or
recommendation; there is no observed task result or identifiable comparison.

### S2 — a concrete test despite a closing question

> I gave both models the same 600-word article and asked for its five section
> headings. Model A returned all five correctly; Model B invented two. For this
> extraction task, I'd use A. Anyone else tried this?

**Label:** `analysis`.
**Boundary:** `analysis` / `question`.
**Reason:** The task, reported results, and resulting recommendation are
explicit; the invitation at the end does not override that structure.

### S3 — a failure report without a general verdict

> My chat froze this morning. I refreshed twice, reopened the app, and lost
> the draft I was working on. So frustrating.

**Label:** `reaction`.
**Boundary:** `reaction` / `analysis`.
**Reason:** Specific actions and numbers appear, but the author only recounts
an event and a feeling, without drawing a conclusion from a test.

### S4 — a failure report with an actionable request

> My chat froze this morning. I refreshed twice and reopened the app. How can
> I export the conversation without copying every message by hand?

**Label:** `question`.
**Boundary:** `question` / `reaction`.
**Reason:** The personal event supplies context for a specific request for
instructions; no conclusion or general verdict takes precedence.

### S5 — an argument using imagined examples

> AI will make creative professionals unnecessary. Imagine a studio where one
> person prompts all the scripts, artwork, and music. If software can do all
> that, paying a creative team makes no sense.

**Label:** `hot_take`.
**Boundary:** `hot_take` / `analysis`.
**Reason:** The author offers reasoning, but the studio is hypothetical and
no actual output, observed result, or source fact supports the prediction.

### S6 — a personal reaction ending in “anyone else?”

> The voice suddenly whispered the weather forecast at me, and I burst out
> laughing. Anyone else had a weird little moment like that?

**Label:** `reaction`.
**Boundary:** `reaction` / `question`.
**Reason:** The closing sentence invites similar stories, rather than asking
for an explanation, procedure, recommendation, or comparison.

### S7 — contextual numbers inside a genuine question

> I pay $20 for Plus and use it about three hours a day. I'm considering a
> different service but haven't tested it. How do the two plans' usage limits
> compare for long conversations?

**Label:** `question`.
**Boundary:** `question` / `analysis`.
**Reason:** The numbers describe the author's needs; the post requests a
comparison and does not advance an evidence-backed answer.

### S8 — an angry post with a specific supporting output

> This answer is ridiculous. I asked, “What is 2 + 2?” and it replied, “13.”
> That response is a basic arithmetic error: the answer should be 4. I'm furious.

**Label:** `analysis`.
**Boundary:** `analysis` / `reaction`.
**Reason:** The post connects an exact input/output example to a specific
checkable conclusion; its anger does not remove that structure.

## What was tightened after reviewing the boundary posts

- S1 and S7 exposed why “contains a fact or number” is too loose. The final
  definition requires relevant evidence connected to an adopted conclusion.
- S3 exposed why “contains detailed observations” alone is insufficient for
  `analysis`: a conclusion supported by those observations must also appear.
- S5 exposed the difference between reasoning and observed evidence. Under
  this taxonomy, hypothetical arguments without qualifying evidence belong
  to `hot_take`; the name is not a synonym for a short or badly written post.
- S4 and S6 exposed the vague “asks a question” boundary. Specific requests
  for information or action differ from invitations to share similar stories.
- S2 and S8 exposed overlapping features. A fixed precedence order makes
  supported conclusions win over closing questions and emotional wording.

Under the final definitions, all eight have an explicit decision path, with
two examples per label. That is a design check, not evidence that another
person will agree on all eight. Have a human review these examples before
the full labeling pass; revise any disputed rule before labeling 200 posts.
