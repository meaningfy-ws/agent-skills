> Parent: `proposal.md` (DEC-1 through DEC-13)

## Context

Four input documents (`inputs/`) — three converging drafts of an antipattern catalogue plus a
human-facing session handout — were produced against a real 40-page plan review. The third draft
(`antipatterns-guarded.md`) supersedes the first two by its own revision note and is the design
basis here, corrected in three ways: (1) a factual overreach about `architecture`'s ADR-count
guidance (DEC-7), (2) four inversion-matrix rows with no corresponding prose entry (DEC-10), (3)
two well-known antipatterns absent from all three drafts, found by web research and cross-checked
against named sources (DEC-11: curse of knowledge — Pinker; weasel words — distinct from the
drafts' existing Hedging entry; terminology drift).

## Goals / Non-Goals

**Goals:**
- One canonical, non-duplicated catalogue entry per antipattern, tagged by which of 8 genres it
  fires in and how (`required`/`welcome`/`avoid`/`harmful`/`n/a`).
- Per-genre reference files that a producing skill can link to directly, without the reader
  loading all 8 genres' worth of material.
- Every claim about another skill's content (architecture's ADR counts, technical-writing's table
  default, proposal-writing's SoW discipline) verified against that skill's actual `SKILL.md`
  before being cited.

**Non-Goals:**
- No generation tooling. The entry count (19: 13 guarded + 6 unguarded) is hand-maintained, same
  discipline as every other skill's `Owns:`/`Related:` table in this repo.
- No `plan-writing` skill (DEC-12), no sales/PM/BI/architecture/modelling "genres" (DEC-13 — those
  are domain flavours of existing genres, or a different axis entirely, owned elsewhere).
- No rewriting of the Hulubul-specific plan review; only the generalizable frame is vendored in.

## Decisions

(Settled in the EPIC — cited, not re-argued: DEC-1 placement, DEC-2 genre-as-single-axis, DEC-3
inversion-matrix mechanism, DEC-4 unguarded/guarded split, DEC-5 idiom reuse, DEC-9 bundle.)

New, made while designing:

- **The per-genre file is a pointer table, not prose.** Format per genre file: register signature
  (one line) + owning skill (link) + a table of `Move | Status | Full entry`, where `Status` is
  the cell value and `Full entry` links to the anchor in `inversion-matrix.md`. This is the
  concrete mechanism that keeps DEC-3 from becoming DEC-6's own defect (uncontrolled duplication)
  in the new skill's own output.
- **`explainer.md`'s content boundary.** Keep from `session-handout.md`: section 2 (the frame: why
  rules invert), section 6 (on metaphors — a good worked example of the genre-map's stakes), and
  Appendix C (quick checks) verbatim. Drop: the Hulubul-specific diagnosis (§0, §1, §3–4), the
  artefact-status table (§7), the skill-suite findings and open items (§8–9) — those are
  session/meta content, not durable teaching material. Appendix A (defects in the session's own
  output) is folded into `explainer.md`'s closing as a worked self-application example, generalised
  (no Hulubul specifics), because it is the single best demonstration that the checklist applies to
  its own authors too.
- **Final entry set.** 6 unguarded (fire everywhere, no lookup) + 13 guarded (genre-conditional).
  Listed in full below — this section *is* the content that `apply` transcribes into
  `references/inversion-matrix.md` and the 8 per-genre files.

## Algorithm / approach

### The genre map (→ `SKILL.md`)

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

Note (DEC-13, stated in `SKILL.md` itself): a sales pitch, PM status update, or BI insight memo is
a domain flavour of one of these eight, not a ninth genre. Model/diagram-correctness antipatterns
(`modelling-conventions/references/anti-patterns.md`, `architecture`'s own `Smell:`/`Fix:` set) are
a separate axis (model structure, not prose) — cited, never duplicated.

### Unguarded defects (→ `SKILL.md`, stated in full — short enough not to need a reference file)

**U1. Genre fusion.** Two or more genres bound into one artefact, one register.
*Cue:* name the single reader and the single job; either answer needing "and also" means fused.
*Fix:* split, then link. *Licensed exception:* paired artefacts (proposal + SoW, White + Blue use
cases) — separate documents, single-sourced shared content, each with a named reader. Pairing is
not fusion.

**U2. The bland sentence.** Stays true if you swap in a competitor's name.
*Cue:* substitute the org name; if nothing breaks, cut it. Reference is allowed to be dry
(precision without ornament), never bland (ornament without content) — the two are not the same
thing.

**U3. Non-parallel enumeration.** List items switch grammatical form (a noun, a nominalisation, a
participle, chained by semicolons).
*Cue:* read the first word of every list item; same part of speech, or not.

**U4. Prose compensating for missing structure.** Meaning smuggled into a label or sentence because
the artefact lacks an element to carry it — a comma-spliced sentence doing the work of three table
rows, a paragraph doing the work of a decision register.
*Fix:* create the missing element — one relationship per modality, one row per decision, one
sentence per claim.

**U5. Weasel words / unattributed authority.** "Studies show," "some experts believe," vague
quantifiers ("significant," "many") — a claim asserted while dodging accountability for it by
attributing it to nobody in particular. **Distinct from Hedging (guarded, A6):** hedging qualifies
the *author's own* claim; a weasel word launders a claim through an unnamed source. Independently
documented (not in any input draft) — see Wikipedia's "Weasel word" and JHU's writing-style guidance.
*Cue:* for every claim of the form "X shows/suggests/believes Y," can you name X? If not, it's a
weasel word.
*Fix:* name the source and the figure, or drop the claim — ties directly to `company-voice.md`'s
existing "grounded; name the figure and its source."

**U6. Terminology drift.** The same referent named three different ways across one document
(feature/tool/functionality; capitalisation drift). Independently documented as a common technical-
writing mistake (not in any input draft).
*Cue:* grep for near-synonyms pointing at the same referent; if a reader must infer they're the
same thing, it's drift.
*Fix:* one term, defined once — see the guarded entry on deferred definitions (A5), which is about
*when* a term is defined; this is about whether it *stays* the same term.

### Guarded (genre-conditional) entries — canonical, → `references/inversion-matrix.md`

Each states: smell, where it fails, where the same move is required, the guard question, the
detection cue, the fix.

**A1. Duplication & cardinality.** *(merges "uncontrolled duplication" + "cardinality drift")*
Smell: one structure restated by hand across sections, unlabelled as a view — or a set that has
outgrown its natural granularity. Fails in Explanation, Decision (linear reading, can't tell a
re-cut from new material; a MECE set like ADRs/priorities/scope-exclusions with too many members
signals conflated decisions). Required in Reference (every entry stands alone on random entry) and
the proposal/SoW pair (the exclusions list is one list in two documents — licensed exception, U1).
Guard: is the artefact entered at one point or many? Generated from one source, or hand-maintained?
Is this set a decomposition (natural size) or a catalogue (no natural size)? Cue: list the first
column of every table — 3+ identical value sets in a read-through document is the defect; for
cardinality, is the count domain-driven (catalogue) or convention-driven (decomposition — see
`architecture`'s per-C4-level typical counts, corrected per DEC-7, not a flat threshold)? Fix: one
master table/source; compress a decomposition that has outgrown its natural size.

**A2. Agentless construction.** Smell: nominalised verb forms and reflexive passives opening a
sentence, deleting the actor ("Publication and controlled distribution of the questionnaire"; *se
confirmă, se evaluează*). Independently named "zombie nouns" (Helen Sword, popularised in Pinker's
*The Sense of Style*) — the same defect documented outside these drafts. Fails in Decision, How-to,
Contract — an obligation must attach to a named party and date. Required in Reference and
architecture models, where the subject is a system ("the endpoint returns 404..."). Guard: is a
human accountable for this sentence becoming true? Cue: nominalised forms opening a list item;
reflexive passives.

**A3. Abstraction with no example, and persuasion inside a commitment.** *(merges two entries —
both are "material creating unintended obligation")* Smell: an abstract claim with no concrete
instance beside it; or marketing prose / benefit framing / rhetorical questions inside a document
that will be enforced or audited later. Fails in Explanation, Tutorial (unexampled claim can't be
checked; the example is the learning) as abstraction; in Contract, Decision record (persuasion
reads as an unintended promise, argued with adversarially later) as persuasion. Required in
Reference (a worked example there gets mistaken for the general rule, so omit it) and in Decision
persuasive (a proposal that doesn't persuade has failed). Guard: is the reader understanding
(needs the instance) or being held to it (an instance creates a false precedent)? Will this
document be argued with now, or enforced later? Cue: named examples per page (zero across an
arguing section is the defect); scan Contract/Decision-record for benefit-framing language. Fix:
add one real artefact for Explanation; strip benefit framing into the paired Decision document
(`proposal-writing` already keeps executive voice in the proposal, "precise, enumerated, no
marketing prose" in the SoW).

**A4. Label headings.** Smell: headings name a topic, not a conclusion. Fails in Decision,
Explanation (contents page should carry the argument). Required in Reference, How-to (reader scans
for a noun or a task — "Authentication" beats "Authentication uses bearer tokens"). Guard: read in
sequence, or scanned for a match? Cue: does every heading contain a verb and a claim? Nouns-only is
the defect in Decision; verbs-and-claims is the defect in Reference.

**A5. Deferred definitions.** Smell: a term coined early, defined many pages later. Fails in any
linearly-read artefact. Required in Reference (one canonical glossary entry, linked from every use,
beats inline repetition). Guard: define at first use when read through; link at every use when
entered at random. Cue: gap between first use and definition; >1 page in a linear document is the
defect.

**A6. Hedging.** Smell: *relevant, usable, sufficient, realistic, indicative, provisional*
recurring on every page. Fails as a register everywhere (recurrence reads as indecision, the
opposite of the intended honesty); fails outright in Contract, Decision record. Required as a
per-claim marker in Explanation of contested material, in Reference documenting version-dependent
behaviour, and in `estimation`'s uncertainty ranges, where naming the range honestly is the entire
job. Guard: hedge the claim, never the register — state the epistemic principle once, then write
declaratively beneath it. Cue: hedging adjectives per hundred words; recurrence (same three words
everywhere), not frequency, is the tell. **Distinct from U5** (weasel words qualify an unnamed
source's claim; this qualifies the author's own).

**A7. Direct address ("you").** Smell: second person used, or avoided, without regard to genre.
Required in Tutorial, How-to (instructing a reader) and Coaching dialogue (built on direct
engagement). Welcome in Explanation ("you" collapses social distance). Wrong in Reference
(describes a system) and Decision ("we" carries organisational commitment; "you" sounds like advice
handed across a desk). Guard: am I instructing, teaching, or committing an organisation?

**A8. Dense tables in place of prose.** Smell: a table strips connectives, stating *what* but never
*why*/*therefore*. Fails in Explanation, Decision (nothing accumulates as the reader moves down
it). Required in Reference, How-to (`technical-writing`'s "prefer tables and lists" default,
correctly scoped to these two quadrants). Guard: does the reader need the relations between items,
or the items themselves? Cue: real second dimension, or a list with a label column? Tables against
paragraphs — 25:12 is not a document.

**A9. Answer/goal first.** Smell: the governing thought or the goal arrives late. Required in
Decision (ten seconds) and How-to (goal before steps). Fails in Decision record (context →
considered options → outcome → consequences; opening with the outcome destroys the ADR's reason to
exist) and Tutorial (arriving at the result is the experience). Guard: deciding/acting now, or
auditing/discovering? Explanation sits with Decision here — structure outranks texture
(`explanatory-writing`'s own precedence rule). Independently corroborated: "burying the lede" names
the same failure outside these drafts.

**A10. Controlling metaphor / figurative material.** Smell: no organising image where one is
needed, or three competing half-metaphors where none should compete. Required in Explanation (one
metaphor, start to finish). Welcome in Tutorial, Decision. Harmful in Reference (a metaphor
introduces the ambiguity Reference exists to remove) and Contract (bloats a recipe / creates
unintended obligation, ties to A3). Guard: mental model, or a fact? One metaphor or none — three
half-metaphors read as noise in every genre (the one piece of this entry that is itself unguarded).

**A11. Premature structure.** Smell: producing a framework, canvas, or pyramid before the thinking
is settled ("they called me the expert and asked me to design it" — named directly in
`semantic-consulting-coach`'s own defection table). Fails in Coaching dialogue (structure ends
exploration, anchors on an untested shape) and in Decision when the governing thought cannot yet be
written (`executive-communication` requires naming the gap, not papering over it). Required in
Decision, Contract, once alignment is confirmed. Guard: has the user explicitly asked for
synthesis, and is alignment confirmed? Being asked to "design" or "build" is not that trigger.

**A12. Options shown, not just the choice.** *(new prose for a matrix row no draft ever wrote up)*
Smell: only the chosen option appears; rejected alternatives, and why they lost, are invisible.
Fails in Decision persuasive (showing your working wastes the reader's ten seconds). Required in
Decision record (an ADR's whole reason to exist, years later, is letting a future engineer see what
was rejected and why) and, more lightly, in Coaching dialogue (the user needs live options, not a
foreclosed one). Guard: is the reader committing now (suppress alternatives), or
reconstructing/still-deciding (show them)? Cue: does the document name at least one rejected option
and why? Zero is the defect in Decision record; more than the one chosen path competing for
attention is the defect in Decision.

**A13. Curse of knowledge.** *(new — Pinker,* The Sense of Style*; not in any input draft)* Smell:
the writer can't reconstruct not already knowing the material, so necessary scaffolding is skipped
and jargon lands unglossed. Fails in Tutorial (must assume zero prior knowledge) and Explanation
(must build understanding from an accessible start — ties to `explanatory-writing`'s
coin-and-explain move). Required/acceptable in Reference, Contract, where assuming domain fluency
*is* the explicit contract with that reader. Guard: does this genre's reader arrive already
fluent, or is fluency what they're building right now? Cue: read the opening as someone one level
less expert; loses them in Tutorial/Explanation = defect, expected in Reference/Contract.

### Anti-patterns

- ❌ Restating a guarded entry's full smell/fix/cue text inside a per-genre file. Per-genre files
  link to the canonical entry; they do not copy it (this is A1, committed by the very skill that
  documents it).
- ❌ Citing another skill's rule from memory. Every cross-skill claim in this design was checked
  against that skill's actual `SKILL.md` (`architecture`'s ADR counts, `technical-writing`'s table
  default, `proposal-writing`'s SoW discipline, `semantic-consulting-coach`'s defection table) —
  `apply` must do the same for anything not already verified here.
- ❌ Treating a domain (sales, PM, BI) as a new genre column (DEC-13). If a future contributor is
  tempted to add one, the fix is checking the genre map first, not extending it by default.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| A future contributor wants to add a new antipattern | Add one row to `inversion-matrix.md`, one line to each affected per-genre pointer table. No new file, no schema change. |
| A future contributor wants to add a new genre | Add one column to the matrix, one new per-genre file, one row to the genre map with an owning skill named. If no skill owns it yet, that's a signal a new skill is needed first (as with the deferred `plan-writing` gap) — not a reason to invent an orphan genre. |
| The entry count keeps growing past ~19 | Apply this catalogue's own guard (A1): is the growing set a decomposition (compress) or a catalogue (let it grow, but keep per-genre filtering so no single page shows more than ~6 entries). |
| A cited external skill's rule changes (e.g. `architecture` revises ADR counts) | The citation in `inversion-matrix.md` goes stale silently (no generation/drift-gate exists for this skill, per the Non-Goals). Acceptable for a hand-maintained reference table at this size; revisit if it recurs. |

## Risks / Trade-offs

- **[Risk]** 19 entries is more than the drafts' own self-flagged ceiling (~15, by loose analogy
  to `architecture`'s ADR-count guidance). → **Mitigation**: per-genre filtering means no reader-
  facing page shows more than the ~4–6 entries relevant to one genre; the full 19 only appear
  together in the one canonical `inversion-matrix.md`, which is a lookup document (Reference
  genre), where density is the correct register per this catalogue's own A8.
- **[Risk]** Hand-maintained per-genre pointer tables can drift from the canonical matrix. →
  **Mitigation**: accepted per Non-Goals; the table is small (13 rows × 8 genres) and reviewed
  same as any other reference table in this repo.

## Open Questions

None blocking. Follow-up candidates, not for this change: a `plan-writing` skill (DEC-12); whether
a later pass should add a lightweight freshness check if the per-genre tables start drifting in
practice.
