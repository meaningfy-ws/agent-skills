---
name: writing-antipatterns
description: The register/genre-conditional catalogue of how writing fails — a genre map (Tutorial, How-to, Reference, Explanation, Decision, Decision record, Contract/specification, Coaching dialogue), a short list of defects that apply regardless of genre, and an inversion matrix of antipatterns whose correctness depends on genre (a rhetorical question is craft in an explainer and a defect in an ADR). Use when reviewing prose for a specific genre, when a rule from one writing skill seems to be misapplied in another context, or when asked "why does this read badly" for a document that mixes genres. Trigger on "antipattern", "why is this hard to read", "review this document/plan", "does this rule apply here", "genre mismatch". Cited by every writing-family skill; never restated by them.
license: Apache 2.0
metadata:
  category: writing
---

# Writing Antipatterns

## Overview

Most writing advice is stated as if it were universal. Almost none of it is. "Lead with a concrete
example" is excellent advice in an explainer and actively harmful in an API reference, where a
worked example gets mistaken for the general rule. "Name the actor in every sentence" is right in a
plan and wrong in a specification, where the subject is a system. The unit that decides whether a
move is craft or a defect is not "good writing" — it is **genre**.

This skill owns the catalogue of how writing fails, tagged by genre: a short list of defects that
hold everywhere (no lookup needed), and a longer list whose correctness inverts depending on which
of eight genres the prose belongs to. It does not own the positive craft each genre practises —
that stays with the skill that owns the genre (`technical-writing`, `explanatory-writing`,
`executive-communication`, `architecture`, `semantic-consulting-coach`). This skill is the
negative space: what not to do, and why the same move is sometimes exactly what to do one genre
over.

## The genre map

Diátaxis gives four genres, all documentation. It has nothing to say about a board paper, because a
board paper documents nothing — its reader is choosing, not learning, doing, or looking up. The map
below is Diátaxis plus the four genres the rest of the Meaningfy skill suite implies.

| Genre | Reader's job | Owning skill | Register signature |
|-------|--------------|---------------|--------------------|
| Tutorial | learn by doing | `technical-writing` | second person, literal steps, low surprise |
| How-to | complete a known task | `technical-writing` | terse, imperative, goal stated first |
| Reference | look something up | `technical-writing` | agentless declarative, tables, exhaustive |
| Explanation | build understanding | `explanatory-writing` | one metaphor, example beside claim, rhythm |
| Decision (persuasive) | choose and commit now | `executive-communication`, `proposal-writing` | answer first, MECE pyramid, hedging banned |
| Decision record | reconstruct the reasoning later | `architecture` (ADR) | context first, options visible, consequences named |
| Contract / specification | be held to it | `proposal-writing` (SoW), `architecture` (OpenAPI/LinkML/use cases) | enumerated, precise, no persuasion, no metaphor |
| Coaching dialogue | think before committing | `semantic-consulting-coach` | questions over statements, no structure until asked |

Two consequences worth acting on:

- **Decision splits into two genres that invert each other.** Persuasive decision writing leads
  with the answer and suppresses rejected options (the reader has ten seconds). A decision record
  does the opposite: context, considered options, outcome, consequences. An ADR that opens with the
  outcome has destroyed its only reason to exist.
- **Coaching inverts the whole executive method.** In `semantic-consulting-coach`'s Exploration
  mode, producing a governing thought, a pyramid, or a canvas before alignment is confirmed is
  explicitly a *defection*, not craft — the strongest technique in the suite becomes an antipattern
  one skill away.

**Domain is not genre.** A sales pitch, a PM status update, or a BI insight memo is a domain
flavour of one of the eight genres above, not a ninth genre — a sales pitch is Decision; a BI memo
is Explanation or Decision depending on its job. The one genuine gap is the **internal working
plan** (no current skill owns a team's own working plan; it defaults to Reference by default and
reads as inventory) — noted here, not solved here; a future `plan-writing` skill is the fix.
Model- and diagram-structure antipatterns (free strings where a controlled vocabulary belongs,
god-classes, unlabelled duplication in a C4 diagram) are a **different axis** — prose vs model
structure — owned by [`modelling-conventions`](../modelling-conventions/SKILL.md) and
[`architecture`](../architecture/SKILL.md) respectively, cited here, never duplicated.

## Unguarded defects — apply in every genre, no lookup needed

**U1. Genre fusion.** Two or more genres bound into one artefact, one register.
*Cue:* name the single reader and the single job; either answer needing "and also" means fused.
*Fix:* split, then link. *Licensed exception:* paired artefacts (proposal + SoW, a White use case
and its Blue realisation) — separate documents, single-sourced shared content, each with a named
reader. Pairing is not fusion.

**U2. The bland sentence.** Stays true if you swap in a competitor's name.
*Cue:* substitute the org name; if nothing breaks, cut it. Reference is allowed to be dry
(precision without ornament) — that is not the same as bland (ornament without content).

**U3. Non-parallel enumeration.** List items switch grammatical form (a noun, a nominalisation, a
participle, chained by semicolons).
*Cue:* read the first word of every list item — same part of speech, or not.

**U4. Prose compensating for missing structure.** Meaning smuggled into a label or sentence because
the artefact lacks an element to carry it — a comma-spliced sentence doing the work of three table
rows, a paragraph doing the work of a decision register.
*Fix:* create the missing element — one relationship per modality, one row per decision, one
sentence per claim.

**U5. Weasel words / unattributed authority.** "Studies show," "some experts believe," vague
quantifiers ("significant," "many") — a claim asserted while dodging accountability for it by
attributing it to nobody in particular. Distinct from the guarded **Hedging** entry: hedging
qualifies the *author's own* claim; a weasel word launders a claim through an unnamed source.
*Cue:* for every claim shaped "X shows/suggests/believes Y," can you name X? If not, it's a weasel
word.
*Fix:* name the source and the figure, or drop the claim — the same discipline as
`company-voice.md`'s "grounded; name the figure and its source."

**U6. Terminology drift.** The same referent named three different ways across one document
(feature/tool/functionality; capitalisation drift).
*Cue:* grep for near-synonyms pointing at the same referent; if a reader must infer they're the
same thing, it's drift.
*Fix:* one term, defined once — see the guarded **Deferred definitions** entry, which is about
*when* a term is defined; this is about whether it *stays* the same term.

## Guarded (genre-conditional) antipatterns

Thirteen entries, each stating where a move fails, where the same move is required, the guard
question that tells them apart, and the fix — full text in
[`references/inversion-matrix.md`](references/inversion-matrix.md). Load only the genre you need:

| Genre | Reference file |
|-------|-----------------|
| Tutorial | [`references/tutorial.md`](references/tutorial.md) |
| How-to | [`references/how-to.md`](references/how-to.md) |
| Reference | [`references/reference.md`](references/reference.md) |
| Explanation | [`references/explanation.md`](references/explanation.md) |
| Decision (persuasive) | [`references/decision.md`](references/decision.md) |
| Decision record | [`references/decision-record.md`](references/decision-record.md) |
| Contract / specification | [`references/contract.md`](references/contract.md) |
| Coaching dialogue | [`references/coaching.md`](references/coaching.md) |

Each per-genre file is a **pointer table only** (move, status, link to the canonical entry) — it
does not restate an entry's smell/fix/cue text. That restraint is deliberate: this catalogue would
otherwise commit its own **Duplication & cardinality** antipattern (`inversion-matrix.md`, entry
A1).

For the teaching version of this frame — why the rules invert, worked examples, and a
self-application check against the catalogue's own output — see
[`references/explainer.md`](references/explainer.md).

## Self-check

- Have you named the single genre this prose belongs to, before applying any rule from this
  catalogue?
- Does the fix you're about to apply come from the guarded entry's *guard question*, or are you
  pattern-matching from a different genre you're more fluent in?
- If you're adding a new antipattern: is it one row in `inversion-matrix.md`, with pointer-table
  rows added to the affected per-genre files — not prose copied into each?
- If you're tempted to add a new genre: does it already map onto one of the eight (see "Domain is
  not genre" above)?

## Boundary & Related Skills

**Owns:** the genre map (the cross-cutting synthesis no other skill states), the unguarded defect
list, and the canonical inversion matrix of genre-conditional antipatterns.

**Does NOT own:** the voice profile ([`company-voice.md`](../executive-communication/references/company-voice.md)),
the Diátaxis quadrant definitions or the craft moves that realise them
([`explanatory-writing`](../explanatory-writing/SKILL.md)), doc placement/form
([`technical-writing`](../technical-writing/SKILL.md)), the persuasive structure method
([`executive-communication`](../executive-communication/SKILL.md)), or model/diagram-structure
antipatterns ([`modelling-conventions`](../modelling-conventions/SKILL.md),
[`architecture`](../architecture/SKILL.md)).

**Related:** `technical-writing`, `explanatory-writing`, `executive-communication`,
`proposal-writing`, `decision-package`, `architecture`, `semantic-consulting-coach`.
