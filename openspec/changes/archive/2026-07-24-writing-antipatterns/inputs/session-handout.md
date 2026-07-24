# Reading, writing and register: a working handout

**Session record and reference. Hulubul V1 plan review, 23 July 2026.**

---

## How to use this

This document is written for a human reader who was not in the session. It teaches the frame before
it uses it, which is the one thing the antipatterns reference does not do.

Read it in one of three ways.

- **All of it**, once, if you intend to change how the team writes.
- **Sections 1, 4 and 9 only**, if you own the Hulubul plan and want the practical answer.
- **Sections 2, 5 and 8**, if you maintain the skill suite.

Section 7 lists every artefact produced in the session and says what each is for, so nothing has to
be reconstructed from the conversation.

---

## 0. Where this started

One question: why is this document so hard to read?

The document was a forty-page internal plan, version 0.6, in Romanian, covering marketing,
research and controlled launch for a parcel-transport product across the Moldovan diaspora. It had
an owner, a calendar, named responsibilities, a risk table and a large annex of channels and
sources. Nothing was missing. It was still close to unreadable.

That question turned out to be more interesting than it looked, because the answer is not "it was
written badly". The answer involves genre, register, organisational structure, and a gap in the
skill suite that the document had no way to avoid falling into.

---

## 1. The diagnosis

### 1.1 What the reader experiences

Roughly twenty-five tables against about a dozen paragraphs of prose. Note that figure is an
estimate from reading, not a count, and it should be verified before quoting.

The effect of that ratio is specific. A table can state *what*, but it cannot state *why*,
*therefore* or *unless*, because tables strip the connectives that carry reasoning. So nothing
accumulates as you read. You finish section 4 holding no more of a model than when you started,
which means section 5 has to be held separately, and by section 8 you are carrying eight
disconnected fragments. Most readers stop around section 5.

Three defects sit underneath that.

**One structure, walked eight times.** The stage sequence (research, alpha, analysis, beta,
controlled launch) is the document's spine, and it is traversed once per section with a different
column set each time: as conditions in section 3, as current actions in 4, as later actions in 5, as
messages in 6, as weeks in 7, as metrics in 8, then twice more in the annex as channels and
materials. Eight views of one thing, none labelled as a view.

The cost is not the repetition itself. It is that arriving at any table, the reader cannot tell
whether this is new material or a re-cut of something already read, so they diff it against the
previous seven from memory. Nobody can sustain that. There is a slower cost too: sections 4 and 5 are
both titled "action plan", sections 3 and 8 both carry transition conditions, so a change of mind
about alpha entry criteria has to be made twice, in two phrasings, and one day it will not be.

**No governing sentence.** Try to find the line you would repeat to a colleague in a corridor. There
isn't one. The nearest candidate describes what the plan organises, not what should be done. Compare
a sentence that would work: *we commit to one route for alpha, chosen on confirmed carriers rather
than diaspora size, and we spend nothing on promotion until requests arrive without it*. Same
beliefs. One of them is a position, and a position can be agreed with, argued against, or acted on.

**Nothing concrete.** Actions have had their actor removed, mostly through the reflexive passive that
Romanian administrative prose reaches for by default: *se confirmă, se evaluează, se reiau*.
"Publication and controlled distribution of the questionnaire" is an activity floating free of any
human being. "Adrian publishes the questionnaire on Monday" is a fact you can check on Tuesday.
Meanwhile the plan's own vocabulary (alpha, beta, controlled launch, resolved request, usable
response, validated route) is coined in section 1 and defined in annex D1, roughly forty pages
later. And a claim asserted a dozen times, that carriers receive incomplete requests and chase
clarifications, never once appears beside a real message, though the team has hundreds of them.

### 1.2 What is worth protecting

The document refuses to promise what it has not tested. It marks unverified sources as unverified
rather than letting them pass as confirmed. It publishes its open questions instead of hiding them.
That discipline is rarer than good formatting and every recommendation assumes it survives.

The problem is that caution spread thinly across forty pages of tables reads as indecision, while
the same caution concentrated into a page and a half of plain prose reads as discipline. Same
content, different effect.

### 1.3 The cause, which matters more than the symptoms

A review that stops at symptoms produces a v0.7 with the same shape. Three forces produced this
document and they will produce the next one unless they are named.

**It grew by accretion.** Six versions, each adding a section, none removing one. That is how you get
eight views of one spine: each was a reasonable addition in its own revision.

**It serves three readers nobody has the authority to separate.** A decision brief for the founder, a
work plan for the marketing lead, a content brief for the designer, and a source registry for
whoever verifies links. Fusing them was not laziness. It was the only option available to an author
who cannot tell three stakeholders they each get a different document.

**Its author is not the decider.** Hedging is what you write when you cannot commit on someone
else's behalf. That is why the qualifications are everywhere rather than attached to the specific
claims that need them. The fix is not stylistic. It is to give the author the authority to state
positions, or to move the positions into a document written by whoever holds that authority.

---

## 2. The frame: genre, register, and why rules invert

### 2.1 Why "good writing" is the wrong unit

Most writing advice is stated as if it were universal. Almost none of it is.

Use a concrete example beside every abstract claim. Excellent advice in an explainer. Actively
harmful in an API reference, where a worked example introduces one particular case that readers then
mistake for the general rule, and dangerous in a contract, where an illustrative example can create
an obligation nobody intended.

Name the actor in every sentence. Right in a plan, where somebody is accountable. Wrong in a
specification, where the subject is a system: "the endpoint returns 404 when the identifier is
unresolved" needs no human and gains nothing from one.

Lead with the answer. Correct in a board paper, where the reader has ten seconds. Wrong in an
architecture decision record, whose reader is a future engineer trying to work out why the rejected
option was rejected. An ADR that opens with the outcome has destroyed its only reason to exist.

So the unit is not "good writing". It is **genre**, and each genre licenses a different register.

### 2.2 The eight genres

Diátaxis gives four, covering documentation. The Meaningfy skill suite implies four more.

| Genre | Reader's job | Owner |
|-------|--------------|-------|
| Tutorial | learn by doing | technical-writing |
| How-to | complete a known task | technical-writing |
| Reference | look something up | technical-writing |
| Explanation | build understanding | explanatory-writing |
| Decision, persuasive | choose and commit now | executive-communication, proposal-writing |
| Decision record | reconstruct the reasoning later | architecture (ADR) |
| Contract or specification | be held to it | proposal-writing (SoW), architecture (OpenAPI, LinkML, use cases) |
| Coaching dialogue | think before committing | semantic-consulting-coach |

Two observations that came out of mapping this.

**Diátaxis does not cover executive communication, and that is correct rather than a gap.** Diátaxis
serves someone using a product that exists. A board paper documents nothing; its reader is choosing
a course of action. It sits outside the frame rather than in one of its cells.

**Decision splits into two genres that invert each other.** Persuasive decision writing leads with
the answer and suppresses the rejected options, because showing your working wastes the reader's ten
seconds. A decision record does the opposite: context, considered options, outcome, consequences.
Both are "decision" documents. Their structures are opposite, and confusing them produces either a
board paper nobody can act on or an ADR that is useless in two years.

### 2.3 The inversion that matters most

In the coaching skill's Exploration mode, producing a governing thought, a pyramid or a canvas is
explicitly a *defection*, not craft. The single strongest technique in the suite becomes an
antipattern one skill away.

That is not a quirk. It is the general shape of the problem. The reason a competent writer produces
an unreadable document is almost never ignorance of technique. It is applying a technique that is
correct in the genre they are fluent in, to a genre that inverts it.

---

## 3. What the writing skills specify, and what the plan lacked

### 3.1 Against executive-communication

| Requirement | Present in the plan |
|-------------|---------------------|
| Governing thought, one actionable sentence | No. A topic statement instead |
| Named decider and named decision | No. Addressed to "the team" |
| SCQA introduction | No situation, complication or question |
| Minto pyramid, three MECE subpoints | No pyramid; sections overlap horizontally |
| Vertical logic: every subpoint supported | No. Rules asserted without reasons beneath them |
| Close: implications, risks, next steps | Risks yes, implications absent, next steps unranked |
| The bland trap | Failed. Much of Part I survives a competitor-name substitution |

The skill states the useful diagnostic directly: if you cannot write the governing sentence, the
thinking is not ready, and structure will not hide that. Applied here, the missing sentence is not a
drafting failure. It is a signal that the route decision has not been made, which is exactly what
annex D6 confirms.

### 3.2 Against explanatory-writing

The craft belongs in the sections that exist to make the team understand why. Those sections carry
none of the seven moves: no controlling metaphor, no example beside any claim, not one question mark
in Part I, no short declaratives, no direct address, coined terms defined forty pages after use, and
a close that ends on filing instructions.

One detail is worth more than the whole list. The best-written pages in the document are annexes C3
and C4, the sample messages, because that is the only place the writer had to picture one specific
human being. The team can already write the other way. They stop doing it the moment the reader
becomes abstract.

### 3.3 Against technical-writing

This is the skill the plan was accidentally obeying. Its default is "direct language, no fluff,
prefer tables and lists over long prose", and that default is correct, for Reference and How-to
output, which is its scope. Its Explanation sub-mode exists precisely to switch registers when the
page is teaching rather than listing.

So the plan applied a real house rule outside the scope where it holds. That is a more interesting
failure than ignorance, and it points at section 8.

---

## 4. The project-management question

Would classical PM writing (WBS, activities, milestones, Gantt) fix this?

Partly, and it fixes a different problem than the one you have.

**Import these.** A deliverable-oriented work breakdown decomposes by noun rather than by stage and
is MECE by construction under the 100% rule. That single move kills the eight-views problem, because
you then have one decomposition and several generated views instead of eight hand-maintained lists.
Milestones give binary, dated, verifiable events. Explicit dependencies give you a critical path, so
everyone can see that the route decision gates everything downstream. A responsibility matrix ends
ownership smearing of the "Adrian; Eugen consulted" kind.

**Do not import a Gantt.** A Gantt assumes frozen scope and deterministic sequence. This project has
neither: the route is unchosen, technical capacity is unconfirmed, and the entire purpose of the
next eight weeks is to settle those questions. The plan already calls its calendar indicative rather
than committed, and that is the honest call. Bars on a chart would make the uncertainty look
resolved.

**Do not import the paperwork.** Work-package dictionaries, effort estimates and formal risk logs
are all reference material, and the document is already drowning in reference material. They make
the work more manageable and the document less readable. Those are different axes.

**The deeper point.** This is not a plan for a sequence of activities. It is a plan for a sequence of
decisions under uncertainty. For discovery-stage work the plan of record is not a schedule at all.
It is a **ranked register of open questions**, each with the evidence that would close it, the person
who owns closing it, and a date. The raw material already exists, scattered across four sections.
Consolidated and ranked, it replaces about half of Part I.

---

## 5. The antipatterns, in short

The full guarded list is in the reference file. The compressed version, and the shape of the guards:

**Four defects with no guard.** Genre fusion. The bland sentence, which stays true when you swap in
a competitor's name. Non-parallel enumeration. Prose compensating for structure that should exist as
an element, a row or a diagram relationship.

**Eleven that depend on genre.** Uncontrolled duplication, agentless construction, abstraction with
no example, label headings, deferred definitions, hedging, dense tables, answer-first, premature
structure, persuasion inside a commitment, and cardinality drift.

Each of the eleven fails in some genres and is *required* in others. Hedging is the clearest case.
As a register it fails everywhere and is banned outright in contracts and decision records. As a
per-claim marker it is required in explanation of contested material and in reference documenting
version-dependent behaviour. The rule is therefore not "hedge less". It is **hedge the claim, never
the register**: state the epistemic principle once at the top, then write declaratively beneath it.

That shape (fails as a register, required as a marker) recurs, and it is why a flat list of
prohibitions would do damage. A rule without its guard gets applied where it is wrong.

---

## 6. On metaphors, and why the choice is not decorative

Four controlling metaphors were considered for the review itself. The comparison is worth keeping,
because choosing one determines which part of the argument lands.

| Metaphor | What it makes obvious | What it hides |
|----------|----------------------|---------------|
| Warehouse and map | everything is stored, nothing guides | says little about audience |
| Orchestral score and parts | no reader needs more than a quarter, and none can tell which | does not explain the missing governing sentence |
| One model, many projections | the eight views, and that they must be generated not hand-drawn | coolest in temperature; less warm for a non-technical reader |
| A map at 1:1 | completeness itself is the defect | most literary; risks reading as clever |

The recommendation was the orchestral score, because a reader immediately locates themselves inside
it, and "you gave everyone the conductor's copy" is a sentence people repeat in meetings. The
projections version was written out in full in both English and Romanian because it is the one that
speaks to a technical audience and to a company whose own work is one model with many
serialisations.

The 1:1 map is held in reserve for the conversation where someone argues that nothing can be
removed. It is the only one of the four that reframes completeness as the flaw.

---

## 7. What was produced

| Artefact | Genre | For | Status |
|----------|-------|-----|--------|
| Readability review, executive register | Decision | the plan's owner | complete |
| Readability review, warehouse metaphor | Explanation | the plan's author | complete |
| Review in one-model-many-projections, English | Explanation | technical readers | complete |
| Review in one-model-many-projections, Romanian, no diacritics | Explanation | the team | complete |
| Antipatterns, flat list of sixteen | Reference | superseded | retired |
| Antipatterns, guarded by register | Reference | superseded | retired |
| Antipatterns v3, guarded by genre | Reference | agents at runtime | needs trimming, see section 9 |
| This handout | Explanation | anyone joining the topic | complete |

Note that the two review variants and the two language versions are not duplicates. Each targets a
different reader, and producing four of them was itself an instance of the defect under discussion:
one argument, several projections, none marked canonical. The orchestral-score version should be
designated the canonical one, or the projections version if the audience is technical.

---

## 8. Findings about the skill suite

**A correction.** An earlier claim in this session, that `technical-writing` was missing from the
suite, was wrong. It exists; it simply was not in the directory being inspected. The claim was
stated more confidently than the evidence supported.

**A real gap.** Mapping the suite against real artefacts leaves one genre unowned: the **internal
working plan**. `technical-writing` covers docs, docstrings and READMEs. `executive-communication`
covers decisions. `proposal-writing` covers client-facing commercial artefacts. Nothing owns a
team's own plan.

That gap is the full explanation for the Hulubul document. With no owning register, a plan defaults
to the safest available one, which is Reference, and Reference is exactly the register that produces
an inventory. The author did not choose badly. The author had nothing to choose from.

**The recommended addition** is a `plan-writing` skill owning four things: deliverable-based
decomposition rather than stage-based, the milestone gate as a testable predicate, single
accountability per line, and the ranked register of open decisions as the plan of record for
discovery work.

**Also observed.** `clarity-gate` is referenced from at least three skills and was never seen, so the
"lightweight clarity check" that `technical-writing` delegates has no visible definition. Worth
confirming it exists.

---

## 9. Open items

**On the plan itself.**

1. Decide who the plan is addressed to, and whether it is a decision document or a status update.
   Everything else follows from that. Owner: the plan's owner. Nobody else can settle it.
2. Write the governing sentence. If it cannot be written, the route decision is the blocker, not the
   prose.
3. Split into three artefacts: decision memo, plan of record in a tool, registry in a spreadsheet.
4. Consolidate the four scattered lists of open decisions into one ranked register at the front.
5. Convert transition conditions into testable gates (format in appendix B).
6. Ten-minute mechanical fixes: left-align tables, cut bold from labels, add a changelog, rewrite
   headings as claims.

**On the antipatterns reference.**

7. Decide its audience. It is currently written for an agent loading it at runtime, and it does not
   work as a human-facing document, because Reference register only functions when the reader
   already knows the framework. This handout is the missing Explanation layer. Once it exists, the
   reference can stay terse.
8. Trim the agent-facing version: remove the revision note, the placement discussion and the
   self-application section, all of which are conversation artefacts rather than rules.
9. Stress-test the inversion matrix. Ninety-six cells is a lot of assertion. The two weakest calls
   are "concrete example: avoid in Reference", defensible but aggressive, and "claim-style heading:
   harmful in Reference", right for API docs and probably too strong for a policy reference.
10. Decide placement: `clarity-gate/references/` if that skill exists, otherwise
    `executive-communication/references/`, with its existing "Common mistakes" section pointing here
    rather than duplicating.

---

## Appendix A: defects in this session's own output

Included because a review that does not survive its own criteria is not worth much.

- **No worked specimen.** Four reviews, all diagnosis and prescription, not one page of the plan
  actually rewritten beside the original. That is abstraction with no example, at the level of the
  whole deliverable.
- **Numbers not counted.** "Roughly twenty-five tables", "four fifths of the actions in section 4".
  Estimates presented as measurements. The house rule is to name the figure and its source.
- **Cause named late.** The first three reviews read as though the author made avoidable mistakes.
  The organisational cause only surfaced in the fourth pass, and it is the most useful part.
- **No triage.** A dozen recommendations, none costed, and no answer to "I have two hours before
  Friday".
- **No acceptance test.** Nothing states how you would know the rewrite worked. It should be
  observable: a new joiner can state the next decision after five minutes, and nobody asks in chat
  which route is being tested.
- **No reader evidence.** The whole diagnosis is textual. Asking three people where they stopped
  reading would take five minutes and beat all of it.
- **Four variants, none canonical.** Discussed in section 7.

---

## Appendix B: the milestone gate format

Replaces prose transition conditions. Five parts, four lines.

> **M3, alpha route selected.**
> *Criterion:* at least three carriers confirmed in writing, both directions, mean response time
> under 48 hours, measured over ten real messages.
> *Owner:* Adrian.
> *Target:* 9 August.
> *If not met by 16 August:* select the route on partial data, or postpone alpha.

The test is whether one person could declare it met or not met on a Friday afternoon without a
discussion. If not, it is still prose.

---

## Appendix C: quick checks

Run these before circulating any document.

1. Name the single reader and the single job. If either answer needs "and also", the document is
   fused.
2. Find the sentence you would repeat in a corridor. If there isn't one, the thinking is not
   finished.
3. List the first column of every table. Repeated value sets in a read-through document means one
   structure is being maintained by hand in several places.
4. Substitute a competitor's name into three sentences at random. Anything still true is filler.
5. For every action, ask who and by when. No name means no action.
6. Measure the gap between each coined term's first use and its definition.
7. Count tables against paragraphs.
8. Read the headings alone. Do they carry the argument, or only the topics? Which one you want
   depends on the genre.
