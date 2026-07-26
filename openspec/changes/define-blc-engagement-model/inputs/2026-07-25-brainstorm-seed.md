# Seed — BLC/SDLC redefinition brainstorm (excerpt for `define-blc-engagement-model`)

**Status: SEED — secondary, preserved, never groomed.** This is the raw human input the EPIC was
shaped from. `proposal.md` supersedes it as the *primary, shaped* truth but does not replace it:
when the two disagree, the proposal is authoritative and the disagreement should be traceable to a
`DEC-` in the proposal. Do not edit, condense, or "update" this file — it is a dated record.

**Provenance:** a long `/opsx:explore` session between Claude Code and Eugeniu Costetchi
(2026-07-25), auditing `docs/ai-coding/`, `docs/engagement/`, `docs/engineering-standards/`,
`docs/philosophy/`, and the 23-skill catalogue. The full synthesis covers five parallel epics; the
excerpt below is the slice that this change is shaped from — **§1 (why the work exists), §2 (the
corrected commercial model), and the §8 scope slice** naming this epic, its siblings, the parked
item, and the round's scope discipline. Sections 3–7 of the synthesis (the SDLC/MDLC/CBLC planes,
the two bridge ambiguities, the five roles, the draft RACI, the v1/v2 doc findings) belong to the
sibling epics `define-meaningfy-lifecycle`, `define-delivery-release-lifecycle`,
`define-roles-and-raci`, and `define-lifecycle-playbooks` and are deliberately not reproduced here.

**Ground rule stated in the source, honoured in the shaping:** do not ask the user anything; where a
point is open, make the most reasonable call and record it as a `DEC-` or in Rabbit-holes/No-gos.
The human made these calls across five conversational rounds and asked for autonomous shaping.

---

## §1 — Why this work exists (verbatim)

Today's SDLC/engagement documentation is fragmented across a v1 (deprecated but still live) and v2
("two-tier") layer, plus a separate P0–P3 engagement model, with real duplication, staleness, and
missing steps. A full audit (see prior artifact, not reproduced here) found the fragmentation is
**80% a narrative/wiring problem** — most needed capabilities already exist as mature skills — and
**20% real new ground** (a genuine capability gap, a business-model correction, and new synthesis
docs that don't exist yet).

**Terminology ground rules, decided by the human:**
- Retire the word **"canon"** — ambiguous, replace with plain wording ("guide", "model", "doc").
- Retire **"two-tier"** as the top-level name — it undercounts the real structure now that business/
  commercial, architecture, modelling, building, and delivery are all distinct concerns.
- **"SDLC" should be scoped specifically to the EPIC-tier build loop** (shape EPIC → PLAN →
  clarity-gate → BDD → TDD implement → review → archive) — not used as a catch-all for the whole
  P2 execution stage the way the old docs did.

---

## §2 — The corrected commercial model (free/paid boundary) (verbatim)

**Correction, stated directly by the human: "nothing is free, only presale work is free, which is
mainly business and relationship building."** This revises `docs/engagement/phases.md`'s stated
"orientation is free" spine rule — that rule was wrong as previously written.

The corrected funnel:

```
PRESALE (free)              →  P0-advisory (paid, 1-2d)  →  P1 Decision (paid, 4-6wk)  →  direct-to-build
relationship/qualification     short orientation product     roadmap + Decision Package    (skip hand-holding
only — "is this relevant?"                                                                   entirely — precise
no deliverable                                                                                ask, straight to
                                                                                                a build contract)
```

- **Presale** — free, bounded, relationship-building and qualification only. No deliverable. This is
  the *only* free thing in the model.
- **P0-advisory** — a **new, paid, short (1-2 day) product** — a named, sellable orientation package.
  Distinct from presale. (This directly answers the existing "Service packaging — how P0–P3 bundle
  into named, sellable offers" TODO already flagged in `docs/engagement/README.md`.)
- **P1 Decision** — unchanged in spirit from today's docs: paid, 4-6 weeks, produces a strategic
  roadmap, data-governance recommendations, semantic-layer architecture sketch, etc. — assessments
  and documents, no building yet. Deliverable: the Decision Package.
- **Direct-to-build** — a client who already knows exactly what they want can skip all hand-holding
  and go straight to a build contract. Today's docs don't allow this path at all ("P2 valid only
  once P1 is complete") — that constraint is now wrong and should be relaxed.
- **P2 — a separate, later contract** for actual delivery. Not monolithic "software build" — it is a
  **family of possible service-line contracts**: (a) ontology/model development, (b) software
  development, (c) teaching/training. A client buys one (or more) of these as its own engagement.
- **Partnership is NOT a phase/stage.** It is a **status label** that attaches to a client relationship
  once they have closed **≥2 contracts** with Meaningfy. It can be true concurrently with any future
  P0/P1/P2 engagement — it does not come "after" P2 in sequence. The existing `docs/engagement/`
  framing of P3 as a fourth sequential phase is wrong; the *content* that was going to live in "P3"
  (governance support, semantic-ops, capability building) is still real, but it's better understood
  as **the kind of work an executive-communication-led relationship does with a Partner-labelled
  client**, not a lifecycle stage everyone passes through.
- Owner of the partnership/account-nurture work: the human explicitly named `executive-communication`
  as its natural owner ("partnership is still part of the business/commercial layer, and is for the
  executive communicators").

---

## §8 — Scope slice: this epic among the five (verbatim excerpt)

> Ordered by real dependency; each item names its change-id, its bet, and what it explicitly does
> **not** cover (the other four epics own those pieces — cite, don't restate).

1. **`define-blc-engagement-model`** — Rewrite `docs/engagement/README.md` + `phases.md` and
   `semantic-consulting-coach/references/engagement-model.md` for the corrected commercial model
   (§2). Does not touch `docs/ai-coding/`.

The four sibling epics, named here for citation only (their content is owned by their own
proposals): `define-meaningfy-lifecycle` (retire v1, rewrite `two-tier-methodology.md`, resolve
Requirements & UC depth), `define-delivery-release-lifecycle` (restructure `dod-quality-gates.md`,
Builder/Shipper dual DoD, fix the stale ownership-table line), `define-roles-and-raci` (the five
roles + RACI, with the Work-Shaper ambiguity and the agent-wrapper fork left open), and
`define-lifecycle-playbooks` (the integrative flow doc + one playbook per role).

Two further items from §8 that bind this epic:

> **Parked, explicitly not one of the five, do not shape it now:**
> 6. MDLC-standalone — an ontology/application-profile development methodology skill (§3). Real new
>    skill-authorship, its own shaping cycle later.

> **Scope discipline that applies to all five:** this round of work is **shaping only** — produce
> `proposal.md` (the Shape-Up bet: Appetite / Why / Solution outline / Key decisions / Rabbit-holes /
> No-gos / What Changes / Capabilities / Impact) per
> `openspec/schemas/meaningfy/templates/proposal.md`. Do **not** derive `design.md`/`tasks.md` (the
> PLAN), do **not** implement, do **not** edit any file outside `openspec/changes/<id>/`. No new skills,
> no new agent stubs, in any of the five.

---

## Two further seed lines this epic depends on (from §7, quoted for traceability)

The commercial-layer material currently lives in two places, and the human wants the duplication
resolved in `docs/engagement/`'s favour:

> **`dod-quality-gates.md` currently blends engagement gates and build-tier DoD in one file by an
> explicit past decision** (the file cites "Q8.2=A": "so the hand-off from selling to building is a
> single, legible sequence"). **The human wants this reversed** — engagement gates and the
> "Commercial layer — TODO" block (today duplicated near-verbatim in both `dod-quality-gates.md` and
> `docs/engagement/README.md`) should move fully into `docs/engagement/`, leaving
> `dod-quality-gates.md` as pure build-tier DoD […]

The *removal* side of that move is owned by `define-delivery-release-lifecycle`; this epic owns the
surviving copy in `docs/engagement/`.

---

## Points the seed leaves open (resolved in `proposal.md`, not here)

Recorded so a later reader can see what was inferred rather than given:

1. The seed calls the paid short product **"P0-advisory"** while today's `P0` means *free
   orientation* — it does not say whether to renumber the phases or redefine the labels.
2. It does not say what **P0-advisory delivers** (only that presale has no deliverable, and that P1
   delivers the Decision Package).
3. It does not say **which file owns** the corrected model now that both `docs/engagement/` and the
   coach's `references/engagement-model.md` describe it, nor what happens to the coach reference's
   "treat these specifics as a working draft to pressure-test, not doctrine" framing.
4. It does not enumerate the **other live files** that restate the now-wrong "orientation is free"
   rule (`decision-package/SKILL.md`, `proposal-writing/SKILL.md`,
   `semantic-consulting-coach/SKILL.md`, `semantic-consulting-domain.md`, root `README.md`).
5. It does not say whether the corrected model should be captured as a normative
   `openspec/specs/` capability.
