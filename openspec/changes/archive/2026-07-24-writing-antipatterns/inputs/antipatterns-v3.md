# Antipatterns, guarded by genre

Supersedes both earlier drafts. Written in Reference register: label headings, tables over prose,
no controlling metaphor, no direct address. That is deliberate, and it is the point of the file.

## Revision note

Three corrections after reading `technical-writing`, `semantic-consulting-coach`,
`proposal-writing` and `architecture`.

1. **`technical-writing` exists.** The earlier draft claimed it was missing because it is not under
   `/mnt/skills/user/`. It is present, it owns Reference and How-to, and its terse/tables default
   plus its Explanation sub-mode already encode the central guard of this file. The earlier claim
   was wrong. `clarity-gate` remains unseen.
2. **Diátaxis plus Decision was too small a frame.** The suite carries at least eight genres, three
   of which invert rules the other five treat as mandatory.
3. **The house already has an antipattern idiom.** `architecture` uses *Smell / Fix*;
   `semantic-consulting-coach` uses a defection table of *the pull you will feel / why it is wrong*.
   This file adopts both rather than inventing a third.

## 1. The genre map

| Genre | Reader's job | Owning skill | Register signature |
|-------|--------------|--------------|--------------------|
| Tutorial | learn by doing | `technical-writing` | second person, literal steps, low surprise |
| How-to | complete a known task | `technical-writing` | terse, imperative, goal stated first |
| Reference | look something up | `technical-writing` | agentless declarative, tables, exhaustive |
| Explanation | build understanding | `explanatory-writing` | one metaphor, example beside claim, rhythm |
| Decision (persuasive) | choose and commit | `executive-communication`, `proposal-writing` | answer first, MECE pyramid, hedging banned |
| Decision record | reconstruct why later | `architecture` (ADR) | context first, options visible, consequences named |
| Contract / specification | be held to it | `proposal-writing` (SoW), `architecture` (OpenAPI, LinkML, use cases) | enumerated, precise, no persuasion, no metaphor |
| Coaching dialogue | think before committing | `semantic-consulting-coach` | questions over statements, no structure until asked |

Two consequences.

**Decision splits in two, and they invert.** A board paper leads with the answer because the reader
has ten seconds. An ADR leads with context and considered options because its reader is a future
engineer asking why the rejected option was rejected. Answer-first in an ADR destroys the artefact's
only purpose. Both are "decision" genres; their structures are opposite.

**Coaching inverts the whole executive method.** In `semantic-consulting-coach` Exploration mode,
governing thoughts, pyramids and canvases are explicitly *defections*, not craft. The strongest
technique in the suite is an antipattern one skill away.

## 2. Unguarded defects

Four things wrong in every genre above. Apply without judgement.

### U1. Genre fusion

**Smell:** the artefact changes job partway through without saying so. Naming its reader requires
"and also".
**Fix:** split, then link. Note the licensed exception below (X1).

### U2. The bland sentence

**Smell:** substituting a competitor's name leaves the sentence true.
**Fix:** replace with the figure, the trade-off, or the next step. Reference is allowed to be dry.
Dry is precision without ornament; bland is ornament without content.

### U3. Non-parallel enumeration

**Smell:** a list whose items switch part of speech, or a cell chaining a noun, a nominalisation and
a participle with semicolons.
**Fix:** one grammatical form per list.

### U4. Prose compensating for missing structure

**Smell:** meaning smuggled into a label or a sentence because the artefact lacks an element to
carry it. `architecture` names the diagram case directly: "validates requests, transforms data,
stores state" on one relationship. The prose equivalent is a comma-spliced sentence doing the work
of three rows, or a paragraph doing the work of a decision register.
**Fix:** create the missing element. One relationship per modality, one row per decision, one
sentence per claim.

## 3. Guarded defects

Each states the smell, where it fails, where the same move is required, and the test that
distinguishes them.

### G1. Uncontrolled duplication

**Smell:** one structure restated across sections by hand, unlabelled as a view.
**Fails in** Explanation and Decision, read linearly.
**Required in** Reference, entered at random, where every entry must stand alone, and in the
proposal/SoW pair, where `proposal-writing` mandates that the SoW exclusions and the estimate
exclusions are *one list in two documents*.
**Guard:** duplication is legitimate when it is single-sourced and the copies cannot drift.
Illegitimate when it is hand-maintained across sections of one linearly read artefact.
**Cue:** list the first column of every table. Repeated value sets in a read-through document, with
no generator, is the defect.

### G2. Agentless construction

**Smell:** nominalisations and reflexive passives opening list items. *Se confirmă, se evaluează.*
**Fails in** Decision, How-to and Contract, where an obligation must attach to a party.
**Required in** Reference and in architecture models, where the subject is a system. "The endpoint
returns 404" needs no actor.
**Guard:** is a party accountable for this sentence becoming true? If yes, name them.

### G3. Abstraction with no example

**Fails in** Explanation and Tutorial.
**Required in** Reference, where a worked example introduces a particular case readers mistake for
the general rule, and in Contract, where an illustrative example creates an unintended obligation.
**Guard:** understanding needs the instance; lookup and commitment are slowed or endangered by it.

### G4. Label headings

**Fails in** Decision and Explanation, where the contents page should carry the argument.
**Required in** Reference and How-to, where the reader scans for a noun or a task. "Authentication"
beats "Authentication uses bearer tokens".
**Guard:** will the headings be read in sequence, or scanned for a match?

### G5. Deferred definitions

**Fails in** any linearly read artefact.
**Required in** Reference, where one canonical glossary entry linked from every use beats inline
repetition, and in `architecture`, where actor names bind to the glossary by convention.
**Guard:** define at first use when read through; link at every use when entered at random.

### G6. Hedging

**Smell:** *relevant, usable, sufficient, realistic, appropriate, best effort* recurring on every
page.
**Fails as a register** everywhere, and **fails outright** in Contract and Decision Record.
`proposal-writing` states scope boundaries are "never hedged"; `architecture` treats vague terms in
an ADR as hand-waving to be replaced with structure.
**Required as a per-claim marker** in Explanation of contested material and in Reference where
behaviour is version-dependent.
**Guard:** hedge the claim, never the register. State the epistemic principle once, then write
declaratively beneath it.
**Cue:** recurrence, not frequency. The same three qualifiers everywhere is the tell.

### G7. Dense tables in place of prose

**Fails in** Explanation and Decision. Tables strip connectives, so they state what but never why or
therefore, and nothing accumulates.
**Required in** Reference and How-to. `technical-writing` sets "prefer tables and lists over long
prose" as its default, and scopes that default to those two quadrants.
**Guard:** does the reader need the relations between items, or the items themselves?
**Cue:** tables against paragraphs. Twenty-five to twelve is not a document.

### G8. Answer first

**Required in** Decision. The governing thought lands in the first ten seconds.
**Fails in** Decision Record, where the ADR order is context, considered options, outcome,
consequences, because the reader is reconstructing rejected options. Also fails in Tutorial, where
arriving at the result is the experience.
**Guard:** is the reader committing now, or auditing a commitment already made?

### G9. Premature structure

**Smell:** producing a framework, canvas or pyramid before the thinking is settled. From the
defection table: "they called me the expert and asked me to design it, so I should produce it."
**Fails in** Coaching dialogue, where structure ends exploration and anchors the user on a shape they
have not tested. Also fails in Decision when the governing thought cannot yet be written, in which
case `executive-communication` requires naming the gap rather than papering over it.
**Required in** Decision and Contract once alignment is confirmed.
**Guard:** has the user explicitly asked for synthesis, and is alignment confirmed? Being asked to
"design" or "build" is not that trigger.

### G10. Persuasion in a commitment

**Smell:** marketing prose, benefit framing or rhetorical questions inside a SoW, ADR, spec or use
case.
**Fails in** Contract and Decision Record, which are read adversarially and later.
**Required in** Decision, where a proposal that does not persuade has failed.
**Guard:** will this document be argued with now, or enforced later? `proposal-writing` keeps the
pair explicitly separate: executive voice in the proposal, "precise, enumerated, no marketing prose"
in the SoW.

### G11. Cardinality drift

**Smell:** a list that has outgrown its natural granularity. `architecture` sets the benchmark
directly: five to eight ADRs is typical, and fourteen or more signals decisions are conflated or
redundant.
**Fails** wherever a set is meant to be MECE: ADRs, priorities, subpoints in a pyramid, scope
exclusions.
**Required** where the set is an inventory: a glossary, a link registry, a parameter table.
**Guard:** is this set a decomposition or a catalogue? Decompositions have a natural size; catalogues
do not.

## 4. Licensed exceptions

### X1. Paired artefacts

Two genres may be produced together provided each is a separate document with a named reader, and
any shared content is single-sourced. Proposal plus SoW is the canonical pair. White plus Blue use
cases is another, and `architecture` states its discipline explicitly: the Blue case cross-references
its White parent and states only realisation deltas, never restating shared guarantees. Pairing is
not fusion. Fusion is one document with two registers.

## 5. The inversion matrix

Required · welcome · avoid · harmful. Bold marks the reversals worth memorising.

| Move | Tutorial | How-to | Reference | Explanation | Decision | Decision record | Contract | Coaching |
|------|----------|--------|-----------|-------------|----------|-----------------|----------|----------|
| Answer or goal first | welcome | required | n/a | welcome | **required** | **harmful** | welcome | **harmful** |
| One controlling metaphor | welcome | avoid | **harmful** | **required** | welcome | avoid | **harmful** | avoid |
| Concrete example beside claim | required | required | **avoid** | **required** | welcome | welcome | **harmful** | avoid |
| Direct address ("you") | required | required | avoid | welcome | avoid | avoid | avoid | **required** |
| Agentless declarative | avoid | avoid | **required** | avoid | harmful | welcome | **harmful** | n/a |
| Dense table | avoid | welcome | **required** | **harmful** | avoid | welcome | required | harmful |
| Claim-style heading | avoid | avoid | **harmful** | welcome | **required** | avoid | avoid | n/a |
| Define at first use | required | welcome | link instead | required | required | link instead | **required** | n/a |
| Per-claim hedge | avoid | avoid | required | required | welcome | **harmful** | **harmful** | required |
| Deliberate redundancy | avoid | welcome | **required** | avoid | harmful | avoid | **required** | n/a |
| Options shown, not just the choice | avoid | avoid | n/a | welcome | avoid | **required** | avoid | required |
| Structure before alignment | n/a | n/a | n/a | welcome | welcome | welcome | required | **harmful** |

Six moves reverse completely between Reference and Explanation, which is why a plan written by
someone with a reference habit reads as inventory. Four reverse between Decision and Decision
Record, which is why an ADR written by someone with a board-paper habit is useless in two years.

## 6. Coverage gap

Mapping the suite against real Meaningfy artefacts leaves one genre unowned: the **internal working
plan**. `technical-writing` covers docs, docstrings and READMEs. `executive-communication` covers
decisions. `proposal-writing` covers client-facing commercial artefacts. `epic-planning` is
referenced for specs. Nothing owns a team's own working plan, and that is precisely the artefact
that goes wrong, because with no owning register it defaults to the safest one available, which is
Reference. Hence a plan that reads as an inventory.

Recommended addition, whether as a skill or a section: **plan-writing**, owning the decomposition
(deliverable-based, not stage-based), the milestone gate as a testable predicate with owner, date
and failure branch, single accountability per line, and the ranked register of open decisions. That
register is the plan for any discovery-stage work; a schedule is not.

## 7. Placement and self-application

Suggested home: `clarity-gate/references/antipatterns.md`, since this is a check rather than a
technique, with links from `executive-communication`, `explanatory-writing` and `technical-writing`.
If `clarity-gate` remains unwritten, `executive-communication/references/` is the fallback, and its
existing "Common mistakes" section should then point here rather than duplicate.

Applying G11 to this file: fifteen numbered entries is above the point at which `architecture` warns
of conflation. Four are unguarded, eleven are guarded, and the guarded set is a decomposition, not a
catalogue, so it should compress further with use. Candidates for merging on the next pass are G3
with G10, both of which are ultimately about material that creates unintended obligation, and G1 with
G11, both of which are about sets that have lost their single source.
