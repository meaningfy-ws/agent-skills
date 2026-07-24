# explanatory-writing Specification

## Purpose

Define the `explanatory-writing` skill: who owns the voice/texture craft of Explanation-quadrant
prose, how it inherits (not forks) the Meaningfy house voice, and the single-home reference
discipline that keeps writing knowledge in the writing-skill family. Governs what the catalogue
SHALL ship for clear explanatory writing and what stays deferred to a future corpus-gated change.

## Requirements
### Requirement: explanatory-writing owns the voice/texture craft for explanatory prose

The catalogue SHALL provide a `explanatory-writing` skill in `meaningfy-core` that owns the
topic-independent craft of explanatory prose — one controlling metaphor, concrete-beside-abstract,
self-answered question pivots, short declaratives, direct address, coin-and-explain, and a confident
grounded close. It SHALL carry a **Diátaxis fit-map** (Explanation = home, Tutorial = partial,
How-to / Reference = off), an **8-axis voice schema**, a **knob-gate of positive defaults**, a
**variant-batch self-check**, and a **boundary** section with a precedence rule and a worked routing
trace. It SHALL NOT own document structure (`executive-communication`), doc placement
(`technical-writing`), or the clarity check (`clarity-gate`).

#### Scenario: Craft is offered for an Explanation page but declined for Reference

- **WHEN** a drafting request is classified as Explanation-quadrant prose
- **THEN** the skill applies the craft moves under the knob defaults
- **WHEN** a drafting request is Reference or How-to
- **THEN** the fit-map declines and points back to `technical-writing` / how-to form

#### Scenario: A competing-directive request resolves by precedence

- **WHEN** an explainer is also a client recommendation, so `executive-communication`'s answer-first
  structure competes with the essay's slow-burn metaphor lede
- **THEN** the boundary's precedence rule (structure > clarity > texture) leads with the answer and
  applies texture beneath it

### Requirement: The new skill inherits the house voice rather than forking it

The knob defaults SHALL be cross-linked to their authoritative house sources — primary
[`company-voice.md`](../../../skills/executive-communication/references/company-voice.md),
secondary the Writing-style section of
[`technical-writing/SKILL.md`](../../../skills/technical-writing/SKILL.md) and
[`clarity-gate/SKILL.md`](../../../skills/clarity-gate/SKILL.md) — and SHALL NOT restate them.
`company-voice.md` owns *what the voice is* (including register selection); `explanatory-writing` owns
*how to execute the craft* within the technical/educational register and introduces no parallel
register dial. Where a default and its linked source disagree, the linked source SHALL win. Every
before/after example the skill ships SHALL be vetted against `company-voice.md` and pass `clarity-gate`.

#### Scenario: A knob default contradicts its linked source

- **WHEN** a positive default conflicts with its linked house source
- **THEN** the linked source wins and the default is corrected, not the source

#### Scenario: A shipped example drifts from the house standard

- **WHEN** a before/after example reads punchier than the current house voice
- **THEN** the anti-dilution vetting rejects it and it is re-authored against the linked sources

#### Scenario: Register selection defers to the existing profile

- **WHEN** a request could be either teaching or decision-driving
- **THEN** the skill defers register selection to `company-voice.md`'s rule (teach →
  technical/educational; decide → general/executive) and introduces no parallel register dial

### Requirement: Writing knowledge has a single home; consumers reference it

Reusable writing guidance SHALL live only in the writing-skill family — `technical-writing`,
`executive-communication` (incl. the `company-voice.md` profile), `explanatory-writing`, and
`writing-antipatterns`. Any other skill that produces prose SHALL reference the relevant family
skill and SHALL NOT restate its guidance. No writing/communication bundle SHALL be (re)introduced;
the role-bundle taxonomy is unchanged.

#### Scenario: A consumer skill needs writing guidance

- **WHEN** a skill such as `epic-planning`, `proposal-writing`, `decision-package`, `spec-stewardship`,
  or `bdd-gherkin` needs writing guidance
- **THEN** it links to the relevant writing-family skill and does not restate that guidance inline

#### Scenario: A consumer skill needs antipattern guidance

- **WHEN** a skill needs to know how a genre-conditional rule inverts, or which defects apply
  regardless of genre
- **THEN** it links to `writing-antipatterns` and does not restate the guarded/unguarded entries
  inline

#### Scenario: The audit finds restated guidance

- **WHEN** the reference audit finds a consumer that restates writing guidance
- **THEN** the restated guidance is replaced with a link to the family skill, and no other consumer
  content is changed

### Requirement: Deferred scope is not shipped in this change

This change SHALL NOT introduce the capture method, a profile store, the `meaningfy-writing` bundle,
a standalone Doc, or the Layer 0–3 architecture; those are deferred to a follow-up EPIC gated on a
real Meaningfy corpus.

#### Scenario: The validator finds no deferred artefact

- **WHEN** `make validate` runs over the change
- **THEN** `explanatory-writing` resolves under `meaningfy-core`, and no new bundle, no
  `references/profiles/` store, and no standalone writing-system Doc are present

