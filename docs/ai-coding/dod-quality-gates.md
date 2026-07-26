# Definition of Done & Quality Gates

**Audience:** Meaningfy developers and agents working under the two-tier method.

**Purpose:** the single authority for the **build-tier**, **Builder's-DoD-only** quality-gate
ladder: the Definition of Done for one Epic and its automated gates. Other docs summarise these
definitions rather than restating them. See [build-lifecycle.md](build-lifecycle.md) for the model
and [opsx-runbook.md](opsx-runbook.md) for the flow.

For the commercial-plane Shipper's DoD (contract conformance), see
[`docs/ai-sales/sales-dod.md`](../ai-sales/sales-dod.md) (a different audience, cadence, and
accountable role, owned and defined there, not here). For the business-side (human/commercial)
stage gates (the Discovery & Onboarding safeguards, for example), see
[`docs/ai-sales/engagement-lifecycle.md`](../ai-sales/engagement-lifecycle.md).

## The build-tier gate set

| Gate | Nature | Owner | Pass condition |
|------|--------|-------|----------------|
| **Clarity gate** | semantic | [`clarity-gate`](../../skills/clarity-gate/SKILL.md) | The PLAN (`design.md` + `tasks.md`) scores **≥ 9/10** on the rubric before implementation |
| **`openspec validate --strict`** | structural | spine ([`spec-stewardship`](../../skills/spec-stewardship/SKILL.md)) | Artifact shape + spec deltas are well-formed |
| **Tests green** | content | [`cosmic-python`](../../skills/cosmic-python/SKILL.md) + `superpowers:test-driven-development` | Full suite passes; design-failures fix the spec, not the code |
| **Coverage** | content | CI pipeline | **≥ 80%** on production code, higher on new/critical code |
| **Architecture check** | structural | [`cosmic-python`](../../skills/cosmic-python/SKILL.md) + import-linter | Layer direction respected (`entrypoints → services → models`, `adapters → models`); no forbidden imports |
| **Code review** | content | [`meaningfy-code-review`](../../skills/meaningfy-code-review/SKILL.md) | No unaddressed Critical findings (architecture, security, spec conformance) |

## The automation boundary (single source: other docs reference this)

- **`openspec validate --strict` is CI-automated:** it runs structurally in the pipeline (and in
  `make validate-spine`).
- **`clarity-gate` is a human/agent gate, NOT CI-automated.** It is semantic judgement; it cannot
  be reduced to a deterministic CI check. Do not assume CI enforces it.

Guardrails ([`guardrails`](../../skills/guardrails/SKILL.md)) reuse these same gates for
output validation; they do not add a parallel enforcement stack.

## Delivery & Release

Delivery & Release is two parallel lanes converging on one gate; neither lane is ever subordinate
to the other.

**The Builder's DoD** (build-plane, Builder-side): the accountability that the shipped increment
conforms to the Epic and the architecture:

- **Built right (verification):** tests green, coverage met, architecture check clean, review passed.
- **Right thing built (validation):** acceptance criteria and `.feature` scenarios, written from
  the Epic, demonstrably pass; the delivered behaviour matches the shaped bet.

Accountability: the **Builder** role, defined in
[`docs/roles-and-raci.md`](../roles-and-raci.md#solution-builder), not
restated here.

**The Shipper's DoD (contract conformance)** is whether the shipped increment matches what was
promised to the client. It closes together with the Builder's DoD, on a different, commercial plane.
Its definition, the document trail it checks against, and its human-sign-off nature are owned by
[`docs/ai-sales/sales-dod.md`](../ai-sales/sales-dod.md), not restated here.

Neither DoD substitutes for the other.

**Disagreement rule:** when the Builder's DoD and the Shipper's DoD disagree, neither verdict
overrides the other: the mismatch means the Epic and the contract have drifted apart, resolved by
a logged re-shape. This rule is stated once, here, and applies to **both** DoDs; any other document
cites it rather than restating it.

**Release mechanics** (how, not what's checked here):
[`ci-cd-delivery`](../../skills/ci-cd-delivery/SKILL.md) (CD/deploy),
[`meaningfy-release`](../../skills/meaningfy-release/SKILL.md) (versioning/changelog/publish),
[`meaningfy-git-workflow`](../../skills/meaningfy-git-workflow/SKILL.md) (branch/commit/PR).

## Definition of Done (a task)

A task is done when **all** hold:

- [ ] Implements its Epic's acceptance criteria; no undocumented divergence from the spec.
- [ ] Unit tests per affected layer (models, adapters, services, entrypoints); BDD scenarios covered.
- [ ] Tests green; coverage ≥ 80% (and not lower than before).
- [ ] Architecture check passes (import-linter).
- [ ] Code review passed with no open Critical findings.
- [ ] Committed only with explicit developer consent.

## Definition of Done (an Epic)

- [ ] Every task in the breakdown is done by the above.
- [ ] Clarity-gate history recorded (the PLAN reached ≥ 9/10 before implementation).
- [ ] `openspec validate --strict` passes on the change's deltas.
- [ ] All `.feature` scenarios pass; error-matrix scenarios covered.
- [ ] Change verified, then synced/archived into `openspec/specs/`.

## The three questions across both lanes

Both DoDs, taken together, answer exactly three questions. The Builder's two, **built right
(verification)** and **right thing built (validation)**, are defined in full under
[Delivery & Release](#delivery--release) above and are not restated here. The third belongs to the
Shipper: **did we deliver what was promised (contract conformance)**, answered by the document-trail
sign-off defined in [`docs/ai-sales/sales-dod.md`](../ai-sales/sales-dod.md), not this doc.
