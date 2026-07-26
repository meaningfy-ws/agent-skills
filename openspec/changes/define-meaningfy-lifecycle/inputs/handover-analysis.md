# Seed: Meaningfy SDLC definition is fragmented — audit findings

**Type:** secondary seed input (per `epic-planning` §Seed intake — preserved, never groomed).
**Written by:** Claude Code, from a cross-repo session (hulubul-broker) comparing `stream-coding`
against OpenSpec, which surfaced the question "where is the Meaningfy SDLC actually defined, and is
it well-defined?" This file is the answer to that question plus the gaps found. It is a seed, not a
shaped EPIC — run this through `/opsx:explore` → `epic-planning`'s elicitation before shaping
`proposal.md`. Do not skip elicitation just because this doc is detailed; several of the findings
below have more than one plausible fix and the human should choose.

---

## Where the SDLC is actually defined today (the map)

There is no single file. The full lifecycle spans two layers:

1. **P0–P3 engagement model** (the layer *above* build) — `docs/engagement/README.md` +
   `docs/engagement/phases.md`. Phase intentions are owned by
   `skills/semantic-consulting-coach/references/engagement-model.md`.
2. **P2 build tier** (what people usually mean by "the SDLC") — the **current canon** is:
   - `docs/ai-coding/two-tier-methodology.md` — the *why/what* (PROJECT tier + EPIC tier, v2)
   - `docs/ai-coding/opsx-runbook.md` — the *how* (day-to-day `/opsx:<verb>` sequence)
   - `docs/ai-coding/dod-quality-gates.md` — the gate ladder (engagement gates + build-tier DoD)
   - `docs/ai-coding/openspec-setup-guide.md` — the repo layout
3. **Deprecated v1** — `docs/ai-coding/ai-coding-methodology.md` + `docs/ai-coding/ai-coding-runbook.md`,
   both banner-marked "retained for reference... until the first real engagement closes."
4. **Machine-readable tripwire** — `tests/ownership.yaml` (single-owner capability map, guards
   against re-specifying an owned capability elsewhere).
5. **Command/skill map** — `spine/workflows.md` (verb roster, command→driving-skill table).

## Findings (evidence-cited, most load-bearing first)

1. **Two live, contradictory lifecycle definitions coexist.** `ai-coding-runbook.md` (v1) still
   describes a single-file `EPIC.md` (spec+plan+roadmap in one artifact) and routes work through
   `gherkin-writer` and `documenter` agents. `two-tier-methodology.md` §7 explicitly says both of
   those agents are **retired** and the EPIC/PLAN split is the current model. Both files are live in
   the repo today with only a one-line banner distinguishing them — a reader who opens
   `ai-coding-runbook.md` first (the more obviously-named file, no `v1` in the filename) gets the
   stale model and will try to invoke agents that no longer exist.

2. **The canonical v2 doc is *less* visual than the deprecated v1 doc.** `ai-coding-runbook.md` (v1,
   deprecated) has a full Mermaid lifecycle diagram (§1) plus a Developer-vs-Agent responsibility
   table. `two-tier-methodology.md` (v2, canon) has neither — it's prose + an ownership table. A doc
   marked "the current canon" regressing the onboarding clarity of the doc it superseded is backwards.

3. **The v1 sunset condition is vague and undated.** Both v1 files say "kept live until the first
   real engagement closes" — no owner, no tracking issue, no date. Given the engagement docs already
   describe P1/P2 as live commercial stages, it's worth checking whether that trigger condition has
   already been met and removal is simply overdue, versus genuinely still pending.

4. **`docs/ai-coding/ai-coding-methodology.md` §6 ("Development Lifecycle") is a stub that just
   points elsewhere** ("The lifecycle diagram... are in the AI Coding Runbook") — in the *deprecated*
   doc, pointing to the *other deprecated* doc. Neither half of v1's own internal cross-reference
   leads anywhere current.

5. **P3 "Partnership" phase has no content and no owning skill** — `docs/engagement/README.md`
   marks it "*to be shaped*" outright. This is an honest gap flag, not a bug, but it means the SDLC
   has no defined answer to "how do we keep this alive" once P2 delivery ends.

6. **The "commercial layer TODO" is flagged independently in two files** —
   `docs/ai-coding/dod-quality-gates.md` ("Commercial layer — TODO (to be shaped)") and
   `docs/engagement/README.md` ("The commercial layer — TODO (to be shaped)") — near-identical prose,
   duplicated rather than one file owning it and the other pointing. Minor, but the two-tier
   methodology's own rule (§6, "no double-spec") argues against it.

7. **No release/deploy step is defined at the end of the build-tier DoD.** `dod-quality-gates.md`'s
   "Definition of Done (an Epic)" ends at "verified, then synced/archived into `openspec/specs/`" —
   nothing about release or deploy. The two-tier ownership table assigns CD/release to
   `ci-cd-delivery`, marked **"(EPIC-10, future)"** — i.e. explicitly not built yet. So today's SDLC,
   as documented, has a real hole between "Epic archived" and "code running in an environment."

8. **The engagement-gate ladder in `dod-quality-gates.md` has no P3 row.** Consistent with finding 5
   (P3 unshaped), but worth deciding together: is P3 out of scope for the gate ladder entirely, or a
   placeholder row should exist so the ladder visibly shows the gap instead of silently ending at P2.

## Suggested scope for the EPIC (not prescriptive — elicit before locking this in)

- Decide: delete v1 docs now (if the two-tier migration is functionally complete), or replace the
  vague sunset line with a concrete, dated/ticketed trigger.
- Port an updated lifecycle diagram (Mermaid or equivalent) into `two-tier-methodology.md` so the
  canonical doc has at least the visual clarity the deprecated one had.
- Fix the dead internal cross-reference in `ai-coding-methodology.md` §6 (or drop it along with v1).
- Collapse the duplicated "commercial layer TODO" into one owning file with the other pointing to it.
- Decide whether `ci-cd-delivery` (EPIC-10) should be pulled forward given the DoD gap at finding 7,
  or whether the DoD should explicitly say "release is out of scope of this SDLC, owned by EPIC-10
  when it lands" so the gap is acknowledged rather than silent.
- P3: at minimum, decide whether the gate ladder should show a placeholder row for it.