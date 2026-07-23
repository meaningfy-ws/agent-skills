---
name: executive-communication
description: Use when turning rough input into a clear, concise, persuasive executive message or analysis: a board paper, proposal, client recommendation, email or Slack note, spoken narrative, slide outline, or a strategic problem to be solved. Triggers include "structure this", "make this persuasive", "write this up for a board or client", "turn this into a recommendation", "tighten this message", or any request for McKinsey-style, Minto, SCQA, or pyramid communication. Not for casual chat or code.
license: Apache 2.0
version: 1.0.0
---

# Executive Communication

## Overview

Turn rough input into a clear, concise, persuasive message. **Core principle:
lead with the answer, then prove it.** A busy reader decides in seconds, so give
them the takeaway first and let the logic support it, never the other way round.

This is a reference and technique skill. The named tools below (Governing
Thought, SCQA, the pyramid) stay the same whatever you write; what changes is how
much of the apparatus you deploy. Match the weight to the artefact.

## When to use

- Drafting or tightening a board paper, proposal, client recommendation, memo, email, or Slack note.
- Preparing a spoken narrative or a slide outline.
- Solving an analytical or strategic problem and turning the findings into a recommendation.

## When NOT to use

- Casual conversation, code, or a quick factual lookup.

## Start here: diagnose before you structure

Before reaching for any framework, answer three questions. They take a minute and
they decide everything that follows.

1. **Who decides, and what decision do they face?** A message with no decision is
   a status update; write it as one and stop. A message with a decision exists to
   move that decision.
2. **What do they already believe, and what would change their mind?** This tells
   you which evidence carries weight and which objection you must pre-empt.
3. **What is the one sentence they must remember?** That sentence is your
   Governing Thought. Write it before anything else.

**If you cannot write that one sentence, the thinking is not ready, not the
message.** Do not paper over the gap with structure. Say what is missing, draft
the sharpest Governing Thought the input allows, and flag it explicitly as a
working assumption the user should confirm or correct. A flagged guess is honest;
a confident message built on mush is not.

## Match the weight to the artefact

The full apparatus below suits a decision that deserves a board's attention. Most
messages do not. Dressing a two-line answer as a board paper wastes the reader's
time and buries the point you were hired to make.

| Artefact | What to deploy |
|----------|----------------|
| Slack note, short email, opener | **SCR + Governing Thought.** No pyramid headings, no formal close. Three to five sentences. |
| Proposal, client recommendation | **SCQA + a 3-point pyramid.** Trade-offs and scope boundaries explicit. Short close. |
| Board paper, formal decision | **The full default structure below**, including logic checks and the implications / risks / next steps close. |
| One-page canvas | Governing Thought as the title; the MECE subpoints become the sections. |
| Spoken narrative | 30 to 60 seconds: Situation, Complication, then the Governing Thought as the punchline. |
| Slide outline | Roughly one slide per subpoint; the slide title states the subpoint as a full assertion, not a label. |

## Default structure (full apparatus)

Order: **Governing Thought, then SCQA (or SCR for short messages), then the Minto
Pyramid, then logic checks, then implications / risks / next steps.**

### A. Governing Thought (the key takeaway)
One concise, **actionable** sentence summarising the whole message. Assume the
reader has 10 seconds; if they remember only this, the message still works.

- Topic, not a thought: "Our regional team structure."
- Governing Thought: "Consolidate the three regional teams into one shared-services hub by Q3."

### B. Introduction: SCQA (or SCR for short messages)
Frame *why the reader should care* before the answer lands.

| Element | SCQA | What it does |
|---------|------|--------------|
| **S**ituation | Neutral, factual, indisputable context | Establishes common ground |
| **C**omplication | The tension or obstacle creating urgency | Creates the need to act |
| **Q**uestion | The natural "so what?" | Names the decision |
| **A**nswer | A brief restatement of the Governing Thought | Resolves it and sets up the body |

**SCR** (Situation, Complication, **Resolution**) is the compressed form for
30-to-60-second or 3-to-5-sentence messages: the answer lands at the end.

### C. Body: the Minto Pyramid
```
            Governing Thought (the answer)
           /            |              \
   Subpoint 1       Subpoint 2       Subpoint 3      (Level 2: MECE buckets)
   /     \          /     \          /     \
 evidence evidence ...    ...      evidence evidence  (Level 3: data, logic, examples)
```
- **Rule of 3:** default to three subpoints unless a different number is clearly better.
- Each subpoint **complete, distinct, non-overlapping** (MECE).
- **Thematic grouping:** finish one topic before the next, no topic-switching.
- Within a bucket use **either** deductive (general to specific) **or** inductive
  (specific to general) reasoning, never both inside one bucket.

### D. Logic checks (run these two as questions before delivering)
- **Vertical:** for each subpoint, ask the reader's "why should I believe that?"
  Can you answer it with the evidence sitting beneath it? If not, the subpoint is
  asserted, not supported. And does each subpoint actually advance the Governing
  Thought, or is it just true-but-irrelevant? Cut what does not earn its place.
- **Horizontal:** do the subpoints overlap or leave a gap (failing MECE)? Re-cut
  until they do not. Is their order deliberate (by importance, by sequence, or by
  cause then effect), or did it just fall out that way?

### E. Implications, risks, next steps (close a board-level message with these)
1. **Implications:** what this means for the key stakeholders, teams, clients, or organisation.
2. **Risks, assumptions, mitigations:** name the constraints and unknowns plainly, and how each is bounded.
3. **Recommended next steps:** 3 to 6 actionable steps, prioritised **Immediate / Short-term / Medium-term**.

## Problem-solving mode (for analytical or strategic tasks)

When the task is analysis, not just messaging, run the McKinsey 6-step process,
then pour the result into the structure above.

1. **Define the problem:** root causes vs. symptoms; constraints; time horizon.
2. **Dissect it:** break it into parts with a MECE logic tree or pyramid.
3. **Prioritise levers:** greatest impact first; flag what is outside our control.
4. **Work plan:** workstreams, analyses to run, stakeholders, data needed.
5. **Analyse:** present findings, or reasoned assumptions where data is absent.
6. **Synthesise into recommendations:** Governing Thought + pyramid + SCQA.

## Voice

Write in the **company voice**, not corporate-bland. The default profile is in
`references/company-voice.md` (Meaningfy's voice, grounded in its SMILE values);
apply it unless the user names another voice. Two rules matter most here:

1. **Register follows purpose.** Teaching something technical? Use the analytical,
   example-rich register. Driving a decision? Use the concise executive register.
   Either way the **structure never changes**.
2. **Concision wins for decisions.** The technical register's longer sentences
   suit explainers, not board papers. Never trade answer-first clarity for texture.

Hard constraints: British English; no em dash; plain, current vocabulary; honest
about trade-offs and unknowns. Full guidance and examples in `company-voice.md`.

For the **texture** of the technical/educational register (explainers, client teaching
material) — controlling metaphor, concrete-beside-abstract, question pivots — use
[`explanatory-writing`](../explanatory-writing/SKILL.md). Structure still wins over texture:
never trade answer-first clarity for it.

**The bland trap:** a structurally perfect message can still say nothing. Once the
scaffolding is right, read it back as the reader. If a sentence could appear in
any consultancy's deck about any client, it is filler. Replace it with the
specific number, the real trade-off, or the actual next step. Generic is a defect,
not a safe default.

## Worked example

This shows the full apparatus and the voice working together. Use it as the
pattern to imitate, not a template to copy.

**Rough input from the user:**
> "We keep rebuilding bits of our Mapping Workbench on every data-mapping
> engagement, and two clients last year asked if they could just license it. But
> we're a semantic consulting shop, not a software vendor, and productising it
> properly is real work. Leadership wants to know whether to turn it into a
> product. Write it up for the board."

**Diagnosis:** the board decides; the decision is whether to productise the
Mapping Workbench; they believe the firm is a consulting business and worry a
product would distract from delivery. What would move them is recurring revenue
plus evidence the downside is small, not a product vision. Governing Thought, in
one sentence:

> **Productise the Mapping Workbench into a licensed offering by Q4, funded from
> delivery margin and kept as our own accelerator, so it earns recurring revenue
> without turning us into a software vendor.**

**The board paper:**

> The Mapping Workbench began as an internal accelerator and has quietly become
> central to how we deliver data-mapping work. (Situation)
>
> But we rebuild parts of it on every engagement, paying for the same work twice,
> and two clients have now asked to license it outright. We are leaving recurring
> revenue on the table and have no way to say yes. (Complication)
>
> So: do we keep it as an internal tool, or productise it? (Question)
>
> **We should productise it into a licensed offering by Q4.** Here is why, in
> three parts. (Answer / Governing Thought)
>
> **1. It turns method we already own into revenue beyond billable hours.** The
> Workbench is built and proven on live engagements; a licence sells it again
> without selling more of our time, and two clients are already asking.
>
> **2. It is defensible because the moat is our mapping method, not the tool.**
> Competitors can buy a triple store; they cannot buy our mapping patterns. The
> product packages the patterns we want to scale while the bespoke method stays
> scarce.
>
> **3. The downside is bounded because we keep using it internally regardless.**
> We fund productisation from delivery margin and time-box a first release to two
> reference clients. Even if licensing stalls, the accelerator keeps paying for
> itself in faster delivery.
>
> *Implications:* this adds a product and licensing line alongside advisory,
> shifting part of our revenue from hours to assets; delivery teams gain a
> maintained accelerator instead of ad-hoc rebuilds.
>
> *Risks:* productisation is a different discipline from consulting and can pull
> focus from delivery. We bound this by funding it from margin, not new hires, and
> proving demand with two reference clients before any broader launch.
>
> *Next steps:* Immediate, name a product owner and pick the two reference
> clients. Short-term, define the licensable boundary, what ships versus what stays
> bespoke method. Medium-term, set licence pricing and a launch date.

Note what the example does: the answer arrives before the proof; each subpoint is
distinct (revenue, defensibility, bounded downside do not overlap); each is backed
by a reason the board can check; the close names a real risk and bounds it; and
the language is plain, with no em dash and no throat-clearing.

## Common mistakes

- **Burying the answer:** building up to the conclusion instead of leading with it. Lead with the Governing Thought.
- **A topic, not a thought:** "our pricing" is a topic; "raise list price 8% and grandfather existing clients" is a Governing Thought.
- **Over-structuring a short message:** SCQA headings and a formal close on a three-line Slack note. Match the weight to the artefact.
- **Overlapping buckets:** subpoints that double-count. Re-cut until MECE.
- **Mixed reasoning in one bucket:** deductive and inductive jumbled. Pick one per bucket.
- **No close on a board message:** stopping at the argument without implications, risks, and next steps.
- **Structurally perfect, substantively empty:** see the bland trap above.

## Boundary & Related Skills

**Owns:** the persuasive-communication method — Governing Thought, SCQA, the Minto pyramid, answer-first
structure, and the Meaningfy company voice (`references/company-voice.md`).
**Delegates:** spec/EPIC readiness → `clarity-gate`; doc prose mechanics → `technical-writing`.
**Related:** `proposal-writing`, `decision-package`, `semantic-consulting-coach`, `technical-writing`, `explanatory-writing`, `writing-antipatterns` (Decision/Decision-record genre failure modes).
