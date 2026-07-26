# Semantic maturity assessment

## What it is

A structured scoring of how well an organisation's terms, models, and definitions are shared and
reused across its systems, rated against a defined scale rather than judged by impression.

## Why it matters in a Deep-tier engagement

A scored baseline would sharpen the option-framing step of discovery: an engagement could point to
a specific score for how fragmented or reconciled a client's shared vocabulary already is, and use
that score to decide how much of the recommendation should be modelling / ontology work (see
[`docs/ai-sales/services/semantic-ontology-modelling.md`](../../ai-sales/services/semantic-ontology-modelling.md))
versus other building blocks.

## Current status

**No skill in this repo owns semantic-maturity assessment today.** A search of every skill under
`skills/` for maturity, scoring, or assessment-rubric content found none. `decision-package` is
explicit that its own flow is not one ("the package is the output of a structured flow, not a
maturity assessment or open-ended discovery", see
[`skills/decision-package/SKILL.md`](../../../skills/decision-package/SKILL.md)), and the
[modelling / ontology](../../ai-sales/services/semantic-ontology-modelling.md) service page has no
scoring step of its own to fall back on either.

## Where it would fit

If this technique existed, it would slot into `discovery-flow.md`'s option-framing step (see
[§4](../../../skills/decision-package/references/discovery-flow.md#4-option-framing)) and
[`advisory-runbook.md`](../advisory-runbook.md)'s step 4, giving the recommendation a specific score
for how fragmented a client's shared vocabulary is instead of a qualitative read.
[`consulting-dod.md`](../consulting-dod.md) would still need it written before a scored engagement's
done-ness check could exist.
