# Antipatterns, guarded by register

Supersedes the flat sixteen-item list. The change is not cosmetic. Most writing rules are not
rules at all, they are register-conditional, and a rule stated without its guard will be applied
where it does damage. A metaphor is mandatory in an explainer and a bug in an API reference.
Agentless prose deletes accountability in a plan and is exactly right in a specification.

So this file has two halves. Four defects that hold everywhere, stated flatly. Then ten that flip,
each stated as a guard rather than a prohibition.

---

## The frame

Diátaxis covers documentation, which serves someone learning, doing or looking up. It has nothing
to say about a board paper, because a board paper documents nothing. Its reader is neither
studying nor working. They are choosing.

So the frame here is Diátaxis plus one genre it does not reach:

| Genre | Reader is | Owning skill |
|-------|-----------|--------------|
| **Tutorial** | learning by doing | `technical-writing` (Explanation sub-mode borrowed for framing) |
| **How-to** | completing a known task | `technical-writing` |
| **Reference** | looking something up | `technical-writing` |
| **Explanation** | building understanding | `explanatory-writing` |
| **Decision** | choosing a course of action | `executive-communication` |

Two consequences worth acting on.

First, `technical-writing` and `clarity-gate` are referenced from both existing skills and neither
exists in the skills directory. Three of the five genres above currently have no owner, which is
why Reference and How-to material keeps getting written in Explanation register. Until that skill
exists, this file is the closest thing to its specification.

Second, precedence. Where genres conflict inside one artefact, the order is **structure, then
clarity, then texture**, and Decision structure outranks Explanation texture. That rule already
sits in `explanatory-writing`. It is repeated here because the guards below assume it.

---

## Part one: defects with no guard

Four things that are wrong in every genre. If a rule has a guard, it is in part two. If it is
here, apply it without judgement.

### U1. Genre fusion

Two or more genres bound into one artefact under a single register.

*Why it has no guard:* every register that suits one part actively harms the others. There is no
combination where fusion is correct, only combinations where it is survivable.

*Cue:* name the single reader and the single job. If either answer needs "and also", the artefact
is fused.

*Fix:* split by genre, then link. A decision memo, a plan of record in a tool, a registry in a
spreadsheet.

### U2. The bland sentence

A sentence that stays true when you swap in a competitor's name.

*Why it has no guard:* Reference is allowed to be dry, never generic. Dryness is precision without
ornament. Blandness is ornament without content.

*Cue:* substitute the organisation name. If nothing breaks, cut the sentence.

### U3. Non-parallel enumeration

A list or cell whose items switch grammatical form: a noun, then a nominalisation, then a
participle.

*Why it has no guard:* parallelism is what lets the eye treat a list as a set. It costs nothing in
any register.

*Cue:* read the first word of every item in a list. Same part of speech, or not.

### U4. Universal emphasis

Bold, capitals or colour on every label.

*Why it has no guard:* emphasis is relative by definition. Reference tolerates heavier structural
markup, which is not the same as heavier emphasis.

*Cue:* what share of lines carries bold? Above roughly a fifth it has stopped signalling.

*Minor mechanicals, same category, not worth their own entries:* centred text columns, a version
number with no changelog, tables with no caption or number so nothing can reference them.

---

## Part two: the guarded ten

Each states where the move fails, where the same move is correct, and the test that tells them
apart. The guard is the useful part. The prohibition on its own will get misapplied.

### G1. Redundant restatement of one structure

**Fails in** Explanation and Decision, where a document is read start to finish and the reader
cannot tell a new section from a re-cut of the previous one.
**Correct in** Reference, where the reader arrives at a random entry and every entry must stand
alone. An API reference repeats the authentication note on every endpoint on purpose.
**Guard:** is the artefact entered at one point or at many? And are the repeated views generated
from one source, or maintained by hand? Hand-maintained repetition in a linear document is the
defect. Generated repetition in a lookup document is the feature.
**Cue:** list the first column of every table. Three or more identical value sets, in a document
meant to be read through, is the defect.

### G2. Agentless construction

**Fails in** Decision and How-to, where an action must attach to a person and a date. "Publication
and controlled distribution of the questionnaire" cannot be verified on Tuesday.
**Correct in** Reference, where the subject is a system, not a person. "The endpoint returns 404
when the identifier is unresolved" needs no actor and gains nothing from one.
**Guard:** is a human being accountable for this sentence coming true? If yes, name them. If the
sentence describes behaviour rather than assigns work, agentless is right.
**Cue:** nominalised verb forms opening a list item, and reflexive passives. In Romanian, *se
confirmă, se evaluează, se reiau* is the default setting of the administrative register, so
avoiding it takes deliberate effort.

### G3. Abstraction with no example beside it

**Fails in** Explanation, where an unexampled claim cannot be checked against experience, and in
Tutorial, where the example is the learning.
**Correct in** Reference, where a worked example introduces a particular case that readers then
mistake for the general rule. Precision without illustration is what reference is for.
**Guard:** is the reader trying to understand this, or to look it up? Understanding needs the
instance. Lookup is slowed by it.
**Cue:** named examples per page. Zero across an arguing section is the defect.

### G4. Label headings

**Fails in** Decision and Explanation, where the contents page should carry the argument and
"Choosing the route" tells you nothing that "We choose one route, on confirmed carriers rather
than diaspora size" tells you.
**Correct in** Reference and How-to, where the reader scans for a noun or a task. "Authentication"
beats "Authentication uses bearer tokens", because the reader is hunting a label, not reading a
claim.
**Guard:** will the reader read the headings in sequence, or scan them for a match?
**Cue:** does every heading contain a verb and a claim? In a decision document, nouns-only is the
defect. In a reference, verbs-and-claims is.

### G5. Deferred definitions

**Fails in** any linearly read artefact, where a term coined in section 1 and defined in annex D1
is a loan the reader carries for forty pages.
**Correct in** Reference, where a single canonical glossary entry, linked from every use, beats
repeating the definition inline.
**Guard:** define at first use when the document is read through. Link at every use when it is
entered at random.
**Cue:** for each glossary term, measure the gap between first use and definition. More than a
page, in a linear document, is the defect.

### G6. Hedging

**Fails as a register.** When *relevant, usable, sufficient, realistic, indicative, provisional*
recur on every page, caution has stopped being a signal and become the prose. It then reads as
indecision, which is the opposite of what an honest author intended.
**Correct as a per-claim marker,** and required in Explanation of contested material, in research
reporting, and in Reference where behaviour is version-dependent.
**Guard:** hedge the specific claim, never the register. State the epistemic principle once at the
top, then write declaratively underneath it.
**Cue:** count hedging adjectives per hundred words, and check whether the same three recur
everywhere. Recurrence, not frequency, is the tell.

### G7. Direct address

**Required in** Tutorial and How-to. Welcome in Explanation, where "you" collapses social distance.
**Wrong in** Reference, which describes a system rather than instructing a person, and wrong in
Decision, where "we" carries organisational commitment and "you" sounds like advice being handed
across a desk.
**Guard:** am I instructing a reader, teaching a reader, or committing an organisation?

### G8. Dense tables in place of prose

**Fails in** Explanation and Decision. A table strips the connectives, so it can state what but
never why or therefore, and nothing accumulates as the reader moves down it.
**Correct in** Reference, where the connectives are noise and the grid is the point.
**Guard:** does the reader need the relations between the items, or the items themselves?
**Cue:** does the table have a real second dimension, or is it a list with a label column? And
count tables against paragraphs. Twenty-five tables to a dozen paragraphs is not a document.

### G9. Burying the answer

**Fails in** Decision, where the reader has ten seconds and the governing thought must land first.
**Correct in** Tutorial, where arriving at the result is the experience, and giving it away up
front removes the reason to follow the steps.
**Guard:** is the reader deciding, or discovering? Note that Explanation sits with Decision here,
because structure outranks texture: lead with the answer, then apply the slow-burn texture
beneath it.

### G10. Figurative material

**Required in** Explanation, one controlling metaphor carried start to finish.
**Harmful in** Reference, where a metaphor introduces exactly the ambiguity the document exists to
remove, and in How-to, where it bloats a recipe.
**Guard:** does the reader need a mental model, or a fact? Also, one metaphor or none. Three half
metaphors read as noise in every genre, which makes that half of the rule an unguarded defect.

---

## The inversion matrix

The compact form. Required, welcome, avoid, harmful.

| Move | Tutorial | How-to | Reference | Explanation | Decision |
|------|----------|--------|-----------|-------------|----------|
| Answer or goal stated first | welcome | required | n/a | welcome | **required** |
| One controlling metaphor | welcome | avoid | **harmful** | **required** | welcome |
| Concrete example beside claim | required | required | **avoid** | **required** | welcome |
| Direct address ("you") | required | required | **avoid** | welcome | avoid |
| Agentless declarative | avoid | avoid | **required** | avoid | **harmful** |
| Dense table | avoid | welcome | **required** | **harmful** | avoid |
| Claim-style heading | avoid | avoid | **harmful** | welcome | **required** |
| Define at first use | required | welcome | link instead | required | required |
| Per-claim hedge | avoid | avoid | required | required | welcome |
| Deliberate redundancy across sections | avoid | welcome | **required** | avoid | **harmful** |
| Short declaratives for rhythm | welcome | required | neutral | required | welcome |

Read the bold cells as the inversions worth remembering. Six moves reverse completely between
Reference and Explanation, which is why a plan written by someone with a reference habit reads as
inventory, and a specification written by someone with an explanatory habit reads as waffle.

---

## Using this

Run part one without thought. Run part two only after you have named the genre, because every
entry there is answerable only once you know which column of the matrix you are in.

And keep one thing in view that no checklist catches. These defects cluster, and clustering has a
cause: an artefact that grew by accretion, or serves readers nobody has the authority to separate,
or is written by someone who cannot make the decision the artefact keeps deferring. Fix the prose
without naming the cause and the same shape returns two revisions later.
