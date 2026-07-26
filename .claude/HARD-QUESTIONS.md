# HARD questions — parked for Eugeniu

> Running log of genuine open decisions surfaced while implementing the Skillery
> v2 EPIC series autonomously. These are **not** blockers I guessed past silently
> — each has a recorded working assumption so the build proceeds, but each
> deserves a real decision. Answer inline under **Answer:** and I'll absorb it
> (revise the owning EPIC/PLAN, re-gate, propagate).

---

## From the catalogue-UX & docs reorg (branch `feat/catalogue-ux-and-docs`)

### HQ-UX.1 — Publish the durable canon to GitHub Pages via AsciiDoc + Antora?
The catalogue-UX brainstorm decided (D7) to dogfood the split-by-churn standard: keep high-churn
agent-loop docs (`docs/ai-coding/`, `.claude/`, `docs/ai-sales/`) as Markdown, but migrate the
**durable canon** (`docs/engineering-standards/`, `docs/philosophy/`, architecture/ADRs) to
**AsciiDoc + Antora** and publish it to **GitHub Pages** — skillery applying its own documentation
standard to itself. This is a substantial migration (Antora playbook, `.adoc` conversion, a Pages CI
workflow) and was **deferred to its own follow-up EPIC**. The README "Documentation" section already
points at where the Pages site will live.
**Working assumption:** defer; do it as a focused EPIC when there's appetite. Confirm priority/timing.

**Answer:** well, in fact we shall propose this migration as per our dogfood. And execute later. 

---

## From EPIC-02 (the spine)

### HQ-02.1 — The golden-thread chain is provisional. When/how do we harden it?
Q2.3's answer flagged the `requirement → ADR → model-entity → epic → change →
task → test → commit` chain as possibly dangerous: ADRs/model-entities are only
*parts* of architecture, and the architecture-documentation standard is not yet
specified. I made the chain deliberately coarse (see
[`../spine/golden-thread.md`](../spine/golden-thread.md)):
`product/requirement spec → architecture (scenarios, ADRs, use cases, C4 +
ArchiMate, contracts, …) → epic/change → task → test → commit`.
**Working assumption:** keep it coarse; harden after the architecture-doc
standard exists (likely an EPIC-05/EPIC-06 follow-on) and after the dogfood.

**Answer:** plan working on architecture standards and templates, this shall include also decission on teh golden-thread (and variants where the architecture is missing and the project is more agile) 

### HQ-02.2 — Should EPIC and OpenSpec "change" ever diverge, or stay one artifact?
Q2.3 raised that an EPIC is a Shape-Up *work shape* while a plain OpenSpec change
may want other structure. I mapped EPIC ≡ `proposal.md` (one artifact, two faces)
to prevent proliferation. **Working assumption:** one artifact; the EPIC's
Shape-Up sections live inside `proposal.md`. Revisit only if a real engagement
shows the two genuinely need different structures.

**Answer:** 

### HQ-02.3 — Do we ever need a generated orientation index beyond `specs/` + `context:`?
Q2.4 preferred dropping `MEMORY.md` (path C) and falling back to a deterministic
generator (path A) only if needed. OpenSpec offers no generator; its native
surface is `config.yaml: context:` + the `specs/` corpus. **Working assumption:**
truth = `openspec/specs/`; orientation = hand-written `config.yaml: context:`;
**defer** building any generator until EPIC-03/dogfood proves `specs/` + `context:`
is insufficient. If proven needed, regenerate into `context:`, not a parallel file.
**Answer:**

### HQ-02.4 — Profile: stay on `core`, or adopt the expanded `/opsx` set repo-wide?
The real profile enum is `core | custom` (not the `expanded` preset EPIC-02 R6
assumed). I shipped the spine on **core** (5 verbs) for deterministic install.
**Working assumption:** core by default; expanded set opt-in per repo via
`openspec config`. Confirm this is the right default for projected repos (EPIC-09).
**Answer:**

### HQ-02.5 — Post-series fork housekeeping (you asked for this in Q2.1).
You noted: after all EPICs land, revisit the fork logic — check the workflow is
solid and the schema is proper, do housekeeping. **Parked as a standing
end-of-series task**, not a blocker.
**Answer:**

---

## From EPIC-04 (catalogue reorg)

### HQ-04.1 — A real trigger-precision harness (beyond the non-blocking stub)?
Q4.2=B asked for a non-blocking trigger-probe harness. I shipped a deterministic
stub: `tests/trigger_probes.yaml` (probe → expected skill) + a reporter that
checks every probe names a real skill and every skill has a probe. It does **not**
actually run an LLM to confirm the probe *fires* the expected skill (that's
non-deterministic in CI). **Working assumption:** the stub is enough for now; a
real LLM-matching harness (run locally / nightly, not in blocking CI) is a future
nice-to-have. Confirm whether you want the real harness built later.
**Answer:**

---

## From EPIC-08 (engagement layer)

### HQ-08.1 — The commercial layer is unshaped.
Q8.2's note: the wider commercial mechanics — qualification, pre-sale, sale,
marketing, CRM & lead communication, service packaging, fit-for-market — are
**still to be developed, brainstormed, debated, and crystallised**. I stubbed a
clearly-labelled "Known gaps" section in `docs/ai-sales/engagement-lifecycle.md` and the DoD
ladder rather than inventing it. **This is a whole future workstream** (a possible
EPIC-11+). Decide when/how to shape it.
**Answer:**

---

## From the campaign framing (EPIC-00 build order)

### HQ-00.1 — Dogfood gate vs "complete all EPICs now".
EPIC-06 (conceptual-modelling) and EPIC-07 (decision-package) are gated on a
**real client engagement** (Q0.1=B, Q0.3=C) that does not exist yet. Your AFK
instruction is "complete all EPICs". **Working assumption:** I author 06/07 (and
08, which depends on 07) as **provisional** skills drafted from the research
syntheses, clearly marked "dogfood-gated — revise after first real engagement",
rather than skipping them. EPIC-09 projection proceeds on the internal dogfood
(Q0.3=C). Confirm you want the provisional drafts vs. holding 06/07/08 entirely.
**Answer:**
