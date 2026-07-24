# Why writing rules invert, and how to use this catalogue

**Audience:** a human reader who wants the teaching layer before the terse reference. The rest of
this skill (`SKILL.md`, `inversion-matrix.md`, the per-genre files) is written in Reference
register — it works once you already hold this frame; this page builds the frame.

## Why "good writing" is the wrong unit

Most writing advice is stated as if it were universal. Almost none of it is.

Use a concrete example beside every abstract claim. Excellent advice in an explainer. Actively
harmful in an API reference, where a worked example introduces one particular case that readers
then mistake for the general rule, and dangerous in a contract, where an illustrative example can
create an obligation nobody intended.

Name the actor in every sentence. Right in a plan, where somebody is accountable. Wrong in a
specification, where the subject is a system: "the endpoint returns 404 when the identifier is
unresolved" needs no human and gains nothing from one.

Lead with the answer. Correct in a board paper, where the reader has ten seconds. Wrong in an
architecture decision record, whose reader is a future engineer trying to work out why the
rejected option was rejected. An ADR that opens with the outcome has destroyed its only reason to
exist.

So the unit is not "good writing." It is **genre**, and each genre licenses a different register.

## Diátaxis does not cover executive communication, and that is correct rather than a gap

Diátaxis serves someone using a product that exists: learning it, doing something with it, or
looking something up in it. A board paper documents nothing; its reader is choosing a course of
action. It sits outside the frame rather than in one of its cells — which is why this catalogue
adds four more genres (Decision, Decision record, Contract, Coaching) rather than trying to force
executive and consulting writing into one of the original four.

**Decision splits into two genres that invert each other.** Persuasive decision writing leads with
the answer and suppresses the rejected options, because showing your working wastes the reader's
ten seconds. A decision record does the opposite: context, considered options, outcome,
consequences. Both are "decision" documents. Their structures are opposite, and confusing them
produces either a board paper nobody can act on, or an ADR that is useless in two years.

**The inversion that matters most.** In the coaching skill's Exploration mode, producing a
governing thought, a pyramid, or a canvas is explicitly a *defection*, not craft. The single
strongest technique in the suite becomes an antipattern one skill away. That is not a quirk — it is
the general shape of the problem. The reason a competent writer produces an unreadable document is
almost never ignorance of technique. It is applying a technique that is correct in the genre they
are fluent in, to a genre that inverts it.

## On metaphors, and why the choice is not decorative

A controlling metaphor is required in Explanation and harmful in Reference (A10). Choosing one is
not a stylistic flourish — the metaphor determines which part of the argument a reader can hold in
their head. Four candidate metaphors for the *idea that one underlying structure gets read from
several different angles*, compared:

| Metaphor | What it makes obvious | What it hides |
|----------|----------------------|---------------|
| Warehouse and map | everything is stored, nothing guides | says little about audience |
| Orchestral score and parts | no reader needs more than a quarter, and none can tell which | doesn't explain a missing governing sentence |
| One model, many projections | the many views, and that they must be generated, not hand-drawn | cooler in temperature; less warm for a non-technical reader |
| A map at 1:1 scale | completeness itself can be the defect | most literary; risks reading as clever |

None of these is "correct" independent of the reader. The orchestral-score version speaks to
someone who needs to locate themselves in a large document quickly; the one-model-many-projections
version speaks to a technical audience already comfortable with the idea of serialisation. Choosing
badly doesn't make the prose wrong, it makes the argument land somewhere the reader wasn't standing.

## Using the catalogue

1. Name the single genre the prose belongs to (`SKILL.md`'s genre map). If you can't answer in one
   word, the artefact may already be fused (U1).
2. Apply the unguarded defects (U1–U6) without further judgement — they hold regardless of genre.
3. For anything genre-conditional, open that genre's reference file, not the full matrix — you
   only need the ~13 rows relevant to the genre you're in, not all of them.
4. When a rule from a different genre seems to apply, check the guard question before applying
   it — that's the whole point of the guard: it's the test that tells the two cases apart.

## A worked self-check, generalised

A catalogue that documents writing defects and does not survive its own criteria is not worth
much. Run it against your own output before shipping:

- **No worked specimen.** Diagnosis and prescription without one page of the actual document
  rewritten beside the original is abstraction with no example (A3), at the scale of the whole
  deliverable.
- **Numbers not counted.** "Roughly twenty-five tables," "most of the actions" — estimates
  presented as measurements. Name the figure and its source, or mark it explicitly as an estimate.
- **Cause named late, or never.** A review that stops at symptoms (a document is disorganised)
  without naming why (it grew by accretion; it serves readers nobody had authority to separate; its
  author isn't the decider) produces a v0.7 with the same shape.
- **No triage.** Recommendations with no cost attached and no answer to "I have two hours before
  Friday" don't get acted on.
- **No acceptance test.** State how you'd know a rewrite worked — observably, not "it reads
  better." ("A new reader can state the next decision after five minutes" is a testable version of
  that claim.)
- **No reader evidence.** A diagnosis built entirely from re-reading the text, with no one asked
  where they actually stopped reading, is missing the cheapest and most reliable signal available.
- **Several variants, none canonical.** Producing multiple framings of the same argument for
  different audiences is legitimate (a technical version and an executive version genuinely serve
  different readers) — but exactly one of them should be marked as the source of record, or the
  fan-out becomes the very antipattern (A1) the catalogue exists to catch.
