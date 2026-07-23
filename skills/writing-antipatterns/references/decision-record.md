# Decision record

**Register signature:** context first, options visible, consequences named. **Owning skill:**
[`architecture`](../../architecture/SKILL.md) (ADR).

Pointer table only — full entries live in [`inversion-matrix.md`](inversion-matrix.md). See
[`../SKILL.md`](../SKILL.md) for the unguarded defects (U1–U6), which apply here too.

| Move | Status | Entry |
|------|--------|-------|
| Duplication & cardinality | welcome | [A1](inversion-matrix.md#a1-duplication--cardinality) |
| Agentless construction | welcome | [A2](inversion-matrix.md#a2-agentless-construction) |
| Abstraction with no example | **harmful** — reads as an unintended promise, argued with later | [A3](inversion-matrix.md#a3-abstraction-with-no-example-and-persuasion-inside-a-commitment) |
| Label headings | avoid | [A4](inversion-matrix.md#a4-label-headings) |
| Deferred definitions | link instead of repeating inline | [A5](inversion-matrix.md#a5-deferred-definitions) |
| Hedging | **harmful** — fails outright | [A6](inversion-matrix.md#a6-hedging) |
| Direct address ("you") | avoid | [A7](inversion-matrix.md#a7-direct-address-you) |
| Dense tables vs prose | welcome | [A8](inversion-matrix.md#a8-dense-tables-in-place-of-prose) |
| Answer/goal first | **harmful** — opening with the outcome destroys the ADR's reason to exist | [A9](inversion-matrix.md#a9-answergoal-first) |
| Controlling metaphor | avoid | [A10](inversion-matrix.md#a10-controlling-metaphor--figurative-material) |
| Premature structure | welcome | [A11](inversion-matrix.md#a11-premature-structure) |
| Options shown, not just the choice | **required** — the ADR's whole reason to exist, years later | [A12](inversion-matrix.md#a12-options-shown-not-just-the-choice) |
| Curse of knowledge | welcome — the reader is a future engineer, already fluent | [A13](inversion-matrix.md#a13-curse-of-knowledge) |
