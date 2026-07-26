# Consulting DoD: Definition of Done for advisory work

**Audience:** the Technical Consultant, and anyone reviewing whether a Deep-tier engagement is
ready to close.

## What "done" would need to answer

A real Definition of Done for advisory work would have to settle, at minimum:

- When is a gap analysis complete enough to hand to option framing, rather than kept open for one
  more round of discovery?
- What evidence distinguishes a genuinely blocking gap from one that only looks urgent to the
  client in the room?
- When is the Decision Package itself finished, as distinct from merely deliverable on schedule?

None of these questions has a settled answer in this repository today.

## Why this isn't decided yet

No advisory engagement has closed yet against a maturity-assessment or gap-analysis deliverable
specifically, so there is no lived experience in this repository to generalise a real DoD from.
This is the same discipline
[`docs/ai-coding/dod-quality-gates.md`](../ai-coding/dod-quality-gates.md) itself follows for the
build tier: it states gates it has verified, and it does not invent gates it has not. The Deep
tier's deliverable is the Decision Package: a recommendation, in/out scope, a pilot-to-scale
roadmap, and a buy/build/defer call, produced by running gap analysis against the client's
strategic ambition (a distinct, separately-sellable offering from a formal maturity assessment).
No DoD for that deliverable has been written until now, as detailed in
[`docs/ai-sales/engagement-lifecycle.md`](../ai-sales/engagement-lifecycle.md).

## What it depends on

A real consulting DoD would build on the five method docs in [`methods/`](methods/):

- [`gap-analysis.md`](methods/gap-analysis.md) is owned today, so it could inform a real DoD
  soonest.
- [`data-maturity-assessment.md`](methods/data-maturity-assessment.md),
  [`semantic-maturity-assessment.md`](methods/semantic-maturity-assessment.md),
  [`wardley-mapping.md`](methods/wardley-mapping.md), and
  [`enterprise-process-modelling.md`](methods/enterprise-process-modelling.md) have no owning
  skill yet, so a DoD covering them is blocked on the technique existing at all.

## Until then

An engagement that needs a done-ness check today should fall back to the Decision Package's own
five-part completeness check (recommendation, scope, sequenced roadmap, buy/build/defer decisions,
ready-to-contract execution brief) in the
[`decision-package`](../../skills/decision-package/SKILL.md) skill, rather than treat this gap as
leaving the engagement with no check at all.
