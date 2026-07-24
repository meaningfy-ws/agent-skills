---
name: explanatory-writing
description: Apply explanatory craft so that Explanation-quadrant prose reads clearly — one controlling metaphor, a concrete example beside every abstract claim, self-answered question pivots, short declaratives, coin-and-explain, a confident grounded close. Use when writing or improving an explainer, a blog-style or internal explanation, or broad-audience teaching prose (Diátaxis Explanation; not Reference or How-to). Trigger on "make this explainer clearer", "why does this read flat", "write a blog-style explanation", "add a worked example or metaphor", "tighten the rhythm of this prose". Executes the Meaningfy technical/educational register from `company-voice.md`. Owns texture, not document structure (`executive-communication`) or doc placement (`technical-writing`).
license: Apache 2.0
metadata:
  category: ai-coding
---

# Explanatory Writing

## Overview

The craft that makes explanatory prose read clean: coherent, concrete, with momentum and warmth.
It owns **texture** — how the sentences land — not structure and not placement. It executes the
**technical/educational register** already defined in the Meaningfy house voice
([`company-voice.md`](../executive-communication/references/company-voice.md)); it adds the
*how-to-write-it-well* layer that the voice profile does not carry, and restates none of its rules.

The voice baseline is inherited, never forked. Where a knob default and its linked house source
disagree, **the source wins** (see [`references/knobs.md`](references/knobs.md)).

## When to use — the Diátaxis fit-map

| Quadrant | Use the craft? | Why |
|----------|----------------|-----|
| **Explanation** (explainers, blog posts, internal notes, broad-audience teaching) | **Yes — home** | Understanding-oriented prose is exactly what these moves serve. |
| **Tutorial** (framing/intro only) | Partial | Borrow direct address and "imagine…"; keep the steps literal and low-surprise. |
| **How-to** (recipes) | No | Terse, goal-oriented. The texture bloats it. Keep only direct address + concrete naming. |
| **Reference** (lookup) | No | Must stay dry and declarative. The craft is actively harmful here. |

If the request is Reference or How-to, decline and point back to
[`technical-writing`](../technical-writing/SKILL.md) / how-to form.

## The craft moves

The seven moves, each with a vetted before/after example, live in
[`references/craft-moves.md`](references/craft-moves.md). In short: one controlling metaphor ·
concrete-beside-abstract · self-answered question pivots · short declaratives · direct address ·
coin-and-explain · a confident grounded close.

## The voice it executes

- **Register selection is not ours.** Follow `company-voice.md`'s rule: *teach → technical/educational;
  decide → general/executive.* This skill executes the **technical/educational** register and
  introduces no parallel dial.
- **Knobs are positive defaults, cross-linked** to the house sources (primary `company-voice.md`;
  secondary the Writing-style section of [`technical-writing`](../technical-writing/SKILL.md) and
  [`clarity-gate`](../clarity-gate/SKILL.md)) — see [`references/knobs.md`](references/knobs.md).
- **The 8-axis voice schema** (the diffable structure of a voice) is in
  [`references/voice-schema.md`](references/voice-schema.md).

## Self-check

Two scopes, do not confuse them:

- **Calibrating the skill (variant-batch).** When tuning the rules or onboarding, generate **3–5
  variants** of the same piece, collect **~20–30** across a few prompts, and inspect the batch for
  drift against the fit-map and the knobs. Calibrate on accept/reject: when a variant reads punchier
  than the house standard, name what gave it away and tighten the rule. Runs today on existing
  Meaningfy docs; needs no corpus-capture project.
- **Checking one piece.** For a single draft, the per-piece quick check below suffices.

Per-piece quick check:

- One controlling metaphor, carried start to finish (not three half-metaphors)?
- A concrete, named example beside every abstract claim?
- At least one self-answered question as a pivot?
- Short declaratives breaking the rhythm?
- British English, no em dash, no overclaiming (knobs)? On short prose, British spelling often passes
  by absence of US forms; land at least one British marker where it falls naturally, rather than
  assuming "no violation" proves the register.
- Register correct for purpose (teach vs decide)?

## Boundary & Related Skills

**Owns:** the *texture* of Explanation-quadrant prose — the craft moves, the fit-map, the 8-axis
schema, the positive-default knobs, and variant-batch validation.

**Does NOT own:** document **structure** / answer-first persuasion
([`executive-communication`](../executive-communication/SKILL.md)); doc **placement, format, and type**
([`technical-writing`](../technical-writing/SKILL.md)); the **voice profile** itself
([`company-voice.md`](../executive-communication/references/company-voice.md), owned by
`executive-communication`); the **clarity check** ([`clarity-gate`](../clarity-gate/SKILL.md)).

**Precedence when directives compete:** **structure > clarity > texture.** If answer-first structure
conflicts with a slow-burn metaphor lede, structure wins: lead with the answer, then apply texture
beneath it.

**Worked routing trace** — request: *"Write an explainer of how eVault sync works, for the docs site."*

| Skill | Owns | Decides |
|-------|------|---------|
| `technical-writing` | placement & form | a `docs/` Explanation page (AsciiDoc/Antora), not Reference; invokes the Explanation sub-mode |
| `explanatory-writing` | texture | the metaphor, example-beside-claim, the question pivot, the rhythm, the close — under the knobs |
| `clarity-gate` | the check | actionable · current · specific refs · single-source |
| `executive-communication` | structure | *not invoked here* (no decision). If it were a recommendation, its answer-first pyramid would win by precedence |

**Related:** `technical-writing`, `executive-communication`, `clarity-gate`, `writing-antipatterns` (genre-conditional failure modes, including where this skill's own craft moves invert).
