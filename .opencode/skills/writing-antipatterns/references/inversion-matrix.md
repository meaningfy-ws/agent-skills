# The inversion matrix

The canonical, single-sourced list of genre-conditional antipatterns. Per-genre files
(`tutorial.md`, `how-to.md`, `reference.md`, `explanation.md`, `decision.md`,
`decision-record.md`, `contract.md`, `coaching.md`) link to entries here; they do not restate them.
See [`../SKILL.md`](../SKILL.md) for the genre map and the unguarded defects (U1–U6).

## Compact form

Required · welcome · avoid · harmful · n/a. Bold marks the reversals worth memorising.

| Move | Tutorial | How-to | Reference | Explanation | Decision | Decision record | Contract | Coaching |
|------|----------|--------|-----------|-------------|----------|-----------------|----------|----------|
| A1 Duplication & cardinality | avoid | welcome | **required** | avoid | avoid | welcome | **required** | n/a |
| A2 Agentless construction | avoid | avoid | **required** | avoid | **harmful** | welcome | **required** | n/a |
| A3 Abstraction / unintended obligation | required | required | **avoid** | **required** | welcome | **harmful** | **harmful** | avoid |
| A4 Label headings | avoid | avoid | **harmful** | welcome | **required** | avoid | avoid | n/a |
| A5 Deferred definitions | required | welcome | link instead | required | required | link instead | **required** | n/a |
| A6 Hedging | avoid | avoid | required | required | welcome | **harmful** | **harmful** | required |
| A7 Direct address ("you") | required | required | avoid | welcome | avoid | avoid | avoid | **required** |
| A8 Dense tables vs prose | avoid | welcome | **required** | **harmful** | avoid | welcome | required | harmful |
| A9 Answer/goal first | welcome | required | n/a | welcome | **required** | **harmful** | welcome | **harmful** |
| A10 Controlling metaphor | welcome | avoid | **harmful** | **required** | welcome | avoid | **harmful** | avoid |
| A11 Premature structure | n/a | n/a | n/a | welcome | welcome | welcome | required | **harmful** |
| A12 Options shown, not just the choice | avoid | avoid | n/a | welcome | avoid | **required** | avoid | required |
| A13 Curse of knowledge | **harmful** | avoid | required | **harmful** | welcome | welcome | required | avoid |

---

## A1. Duplication & cardinality

**Smell:** one structure restated by hand across sections, unlabelled as a view — or a set that has
outgrown its natural granularity.

**Fails in** Explanation, Decision — read linearly, the reader cannot tell a new section from a
re-cut of the previous one; a set meant to be MECE (ADRs, priorities, scope exclusions) with too
many members signals conflated decisions.

**Required in** Reference, entered at random, where every entry must stand alone — and the
proposal/SoW pair, where the exclusions list is **one list in two documents** (licensed exception,
`SKILL.md` U1).

**Guard:** is the artefact entered at one point or many? Are repeated views generated from one
source, or hand-maintained? Is this set a decomposition (has a natural size) or a catalogue (does
not)?

**Cue:** list the first column of every table — three or more identical value sets in a
read-through document is the defect. For cardinality: is the count domain-driven (a catalogue) or
convention-driven (a decomposition — see [`architecture`](../../architecture/SKILL.md)'s
per-C4-level typical counts: L1 2–3, L2 3–5, L3 2–4, L4 1–2 per system/container, summing to
roughly 8–14 — a range, not a flat "14+ is too many" threshold).

**Fix:** one master table or generated source; compress a decomposition that has outgrown its
natural size.

## A2. Agentless construction

**Smell:** nominalised verb forms and reflexive passives opening a sentence, deleting the actor
("Publication and controlled distribution of the questionnaire"; Romanian *se confirmă, se
evaluează*). Independently named "zombie nouns" (Helen Sword, popularised in Steven Pinker's *The
Sense of Style*) — the same defect documented well outside this catalogue's own source material.

**Fails in** Decision, How-to, Contract — an obligation must attach to a named party and a date.

**Required in** Reference and architecture models, where the subject is a system, not a person
("the endpoint returns 404 when the identifier is unresolved").

**Guard:** is a human being accountable for this sentence becoming true? If yes, name them.

**Cue:** nominalised forms (*-tion*, *-ment*, Romanian *-are/-ire*) opening a list item; reflexive
passives.

## A3. Abstraction with no example, and persuasion inside a commitment

**Smell:** an abstract claim with no concrete instance beside it; or marketing prose, benefit
framing, rhetorical questions inside a document that will be enforced or audited later — both are
ultimately "material that creates an unintended obligation."

**Fails in** Explanation, Tutorial (an unexampled claim can't be checked against experience; the
example *is* the learning) as abstraction; in Contract, Decision record (persuasion reads as an
unintended promise, argued with adversarially later) as persuasion.

**Required in** Reference (a worked example there gets mistaken for the general rule, so omit it)
and Decision persuasive (a proposal that does not persuade has failed).

**Guard:** is the reader trying to understand (needs the instance), or being held to this later (an
instance can create a false precedent or an unintended promise)? Will this document be argued with
now, or enforced later?

**Cue:** named examples per page — zero across an arguing section is the defect. Scan
Contract/Decision-record text for benefit-framing language; if present, persuasion has bled into a
commitment.

**Fix:** add one real artefact for Explanation. Strip benefit framing out of Contract/Decision
record into the paired Decision document instead —
[`proposal-writing`](../../proposal-writing/SKILL.md) already keeps executive voice in the
proposal and "precise, enumerated, no marketing prose" in the SoW.

## A4. Label headings

**Smell:** headings name a topic, not a conclusion.

**Fails in** Decision, Explanation, where the contents page should carry the argument
("Choosing the route" tells a reader nothing; "We choose one route, on confirmed carriers rather
than diaspora size" does).

**Required in** Reference, How-to, where the reader scans for a noun or a task ("Authentication"
beats "Authentication uses bearer tokens" — the reader is hunting a label, not reading a claim).

**Guard:** will the reader read headings in sequence, or scan them for a match?

**Cue:** does every heading contain a verb and a claim? Nouns-only is the defect in Decision;
verbs-and-claims is the defect in Reference.

## A5. Deferred definitions

**Smell:** a term coined early, defined many pages later.

**Fails in** any linearly-read artefact — every term becomes a loan the reader takes out early and
repays at the end, guessing in between.

**Required in** Reference, where one canonical glossary entry, linked from every use, beats
repeating the definition inline.

**Guard:** define at first use when the document is read through; link at every use when it is
entered at random.

**Cue:** measure the gap between a term's first use and its definition — more than a page, in a
linear document, is the defect.

## A6. Hedging

**Smell:** *relevant, usable, sufficient, realistic, indicative, provisional* recurring on every
page.

**Fails as a register** everywhere (recurrence turns intended honesty into the appearance of
indecision); **fails outright** in Contract and Decision record.

**Required as a per-claim marker** in Explanation of contested material, in Reference documenting
version-dependent behaviour, and in [`estimation`](../../estimation/SKILL.md)'s uncertainty ranges,
where naming a range honestly is the entire job.

**Guard:** hedge the specific claim, never the register. State the epistemic principle once at the
top, then write declaratively beneath it.

**Cue:** count hedging adjectives per hundred words; recurrence of the same three words everywhere,
not frequency, is the tell.

**Distinct from** `SKILL.md` U5 (weasel words): hedging qualifies the *author's own* claim; a
weasel word launders a claim through an unnamed source.

## A7. Direct address ("you")

**Smell:** second person used, or avoided, without regard to genre.

**Required in** Tutorial, How-to (instructing a reader) and Coaching dialogue (built on direct
engagement).

**Welcome in** Explanation ("you" collapses social distance).

**Wrong in** Reference (describes a system, not a person) and Decision ("we" carries organisational
commitment; "you" sounds like advice handed across a desk).

**Guard:** am I instructing a reader, teaching a reader, or committing an organisation?

## A8. Dense tables in place of prose

**Smell:** a table strips connectives, so it states *what* but never *why* or *therefore* — nothing
accumulates as the reader moves down it.

**Fails in** Explanation, Decision.

**Required in** Reference, How-to —
[`technical-writing`](../../technical-writing/SKILL.md)'s own "prefer tables and lists over long
prose" default, correctly scoped to these two quadrants.

**Guard:** does the reader need the relations between the items, or the items themselves?

**Cue:** does the table have a real second dimension, or is it a list with a label column? Count
tables against paragraphs — twenty-five to a dozen is not a document.

## A9. Answer/goal first

**Smell:** the governing thought, or the goal, arrives late.

**Required in** Decision (the reader has ten seconds) and How-to (the goal is stated before the
steps).

**Fails in** Decision record (context → considered options → outcome → consequences; an ADR that
opens with the outcome has destroyed its only reason to exist) and Tutorial (arriving at the result
is the experience; giving it away up front removes the reason to follow the steps).

**Guard:** is the reader deciding/acting now, or auditing/discovering? Explanation sits with
Decision here, because structure outranks texture —
[`explanatory-writing`](../../explanatory-writing/SKILL.md)'s own precedence rule: lead with the
answer, apply slow-burn texture beneath it.

Independently corroborated outside this catalogue's source material: "burying the lede" names the
same failure in journalism and business-writing craft.

## A10. Controlling metaphor / figurative material

**Smell:** no organising image where one is needed, or three competing half-metaphors where none
should compete.

**Required in** Explanation — one controlling metaphor, carried start to finish.

**Welcome in** Tutorial, Decision.

**Harmful in** Reference (a metaphor introduces exactly the ambiguity Reference exists to remove)
and Contract (bloats a recipe, or creates the unintended obligation described in A3).

**Guard:** does the reader need a mental model, or a fact? One metaphor or none — three
half-metaphors read as noise in every genre (the one piece of this entry that holds regardless of
genre).

## A11. Premature structure

**Smell:** producing a framework, canvas, or pyramid before the thinking is settled — named
directly in [`semantic-consulting-coach`](../../semantic-consulting-coach/SKILL.md)'s own defection
table: "they called me the expert and asked me to design it, so I should produce it."

**Fails in** Coaching dialogue (structure ends exploration, anchors the user on a shape they have
not tested) and in Decision when the governing thought cannot yet be written
(`executive-communication` requires naming the gap, not papering over it).

**Required in** Decision and Contract, once alignment is confirmed.

**Guard:** has the user explicitly asked for synthesis, and is alignment confirmed? Being asked to
"design" or "build" is not that trigger.

## A12. Options shown, not just the choice

**Smell:** only the chosen option appears; rejected alternatives, and why they lost, are invisible.

**Fails in** Decision persuasive — showing your working wastes the reader's ten seconds.

**Required in** Decision record — an ADR's whole reason to exist, years later, is letting a future
engineer see what was rejected and why. Required, more lightly, in Coaching dialogue, where the
user needs live options in front of them, not a foreclosed one.

**Guard:** is the reader committing now (suppress the alternatives), or reconstructing/still
deciding later (show them)?

**Cue:** does the document name at least one rejected option and why? Zero is the defect in
Decision record; more than the one chosen path competing for the reader's attention is the defect
in Decision.

## A13. Curse of knowledge

**Smell:** the writer cannot reconstruct not already knowing the material, so necessary scaffolding
is skipped and jargon lands unglossed. Named by Steven Pinker (*The Sense of Style*) — not present
in this catalogue's original source drafts, added after independent verification.

**Fails in** Tutorial (must assume zero prior knowledge) and Explanation (must build understanding
from an accessible starting point — ties to
[`explanatory-writing`](../../explanatory-writing/SKILL.md)'s coin-and-explain craft move).

**Required/acceptable in** Reference and Contract, where assuming domain fluency *is* the explicit
contract with that reader — that assumption is what makes Reference fast to use.

**Guard:** does this genre's reader arrive already fluent, or is fluency what they are building
right now?

**Cue:** read the opening as someone one level less expert than you. Losing them is the defect in
Tutorial/Explanation; it is expected, and correct, in Reference/Contract.
