<!-- PLAN (tasks half). PLAN = design.md + this file. The apply phase parses `- [ ]` checkboxes. -->

> Derived from EPIC: define-meaningfy-lifecycle (openspec/changes/define-meaningfy-lifecycle/proposal.md)

## 1. Rename and rewrite the successor doc

- [ ] 1.1 `git mv docs/ai-coding/two-tier-methodology.md docs/ai-coding/build-lifecycle.md`.
- [ ] 1.2 Retitle the doc and remove the "two-tier" framing from its title and prose (DEC-1); keep the
      PROJECT-tier/EPIC-tier nesting itself.
- [ ] 1.3 Expand the PROJECT tier into named steps, each citing exactly one owning skill: Requirements
      & UC at two depths (DEC-6), ADLC → `architecture` (DEC-4), MDLC-lite →
      `conceptual-modelling` + `linkml-engineering`, cross-checked by `modelling-conventions`, plus a
      one-line MDLC-standalone gap note (DEC-5), project/repo setup → `project-setup`.
- [ ] 1.4 Scope the SDLC label to the EPIC-tier build loop only (shape → derive PLAN → clarity-gate →
      BDD → TDD → review → archive); do not use it as a synonym for the whole build contract (DEC-3).
- [ ] 1.5 Add the method-spine passage citing `stream-coding` (external), the OpenSpec artifact
      vocabulary, and the build-skill roster (`bdd-gherkin`, `cosmic-python`, `meaningfy-code-review`,
      `clarity-gate`) as pointers only (DEC-17).
- [ ] 1.6 Add the opening "Light steering, heavy agents, cheap verification" governance paragraph,
      citing `guardrails` and `stream-coding`; keep it to one paragraph, no per-step column (DEC-18).
- [ ] 1.7 Redraw the Mermaid lifecycle diagram for current reality: EPIC ≡ `proposal.md`, PLAN ≡
      `design.md` + `tasks.md`, three-wrapper roster, OpenSpec-native paths, seeds under
      `changes/<id>/inputs/`, no `MEMORY.md`-as-truth; one diagram, PROJECT + EPIC tier together, with
      Delivery & Release as a single terminal node pointing at `dod-quality-gates.md` (DEC-8, DEC-9).
- [ ] 1.8 Rebuild the developer-vs-agent responsibility table against the new steps; no role names
      beyond "Developer"/"agent" (DEC-10).
- [ ] 1.9 (DEC-11, superseded) Make no content edit to the ownership table's `CD / release` row —
      that row is `define-delivery-release-lifecycle`'s to correct (its DEC-6/DEC-7). If that change
      has not landed yet when this task runs, only strip the false `(EPIC-10, future)` qualifier from
      the existing row text, leaving the row otherwise as-is for epic 3 to replace; if it has already
      landed, skip this task entirely — there is nothing left to touch.
- [ ] 1.10 Carry forward v2's correct sections in substance: labelled Shape-Up divergence, guardrails
      pointer, model tiering, no-double-spec layering (EARS dropped), agent roster reconciliation,
      optional SEED/AgOCQs++ elicitation aids (DEC-15).
- [ ] 1.11 Self-check: grep the rewritten file for `EPIC.md`, `gherkin-writer`, `documenter`,
      `MEMORY.md` — zero hits outside historical/contrast prose that explicitly says "no longer".

## 2. Retarget the six inbound links

- [ ] 2.1 `docs/engagement/README.md` line 22 and line 30: retarget
      `../ai-coding/two-tier-methodology.md` → `../ai-coding/build-lifecycle.md` (link only, no prose
      change — epic 1 owns this file's content).
- [ ] 2.2 `docs/engagement/phases.md` line 60: retarget the same link, same constraint.
- [ ] 2.3 `docs/ai-coding/opsx-runbook.md` line 6: retarget `two-tier-methodology.md` →
      `build-lifecycle.md`.
- [ ] 2.4 `docs/ai-coding/openspec-setup-guide.md` line 9: retarget the same link.
- [ ] 2.5 `docs/ai-coding/dod-quality-gates.md` line 8: retarget the same link (link only — no other
      edit to this file; its content is epic 3's).
- [ ] 2.6 Verify: `grep -rn "two-tier-methodology" docs/ README.md` returns zero matches (outside
      `openspec/changes/*/inputs/` historical seeds, which are preserved records).

## 3. Delete the three v1 files

- [ ] 3.1 `git rm docs/ai-coding/ai-coding-methodology.md docs/ai-coding/ai-coding-runbook.md docs/ai-coding/ai-coding-setup-guide.md`
      (DEC-7) — only after tasks 1 and 2 are complete, so no link ever points at a missing or
      stale-content file.

## 4. Update tools/repo_lint/lint.py

- [ ] 4.1 Change `FROZEN_GLOBS = ("docs/ai-coding/",)` to `FROZEN_GLOBS = ()`; update the comment
      above it to say `docs/ai-coding/` was the only frozen path and is no longer frozen as of this
      change, and why (DEC-12).
- [ ] 4.2 In `orphan_agent_references`, extend the existing skip condition
      (`_is_frozen(repo, f) or f.name.startswith("EPIC-setup") or f.name == "environment-setup.md"`)
      with `or str(f.relative_to(repo)).startswith("openspec/changes/")` so active change trees are
      exempt, matching the existing archive-level exemption (DEC-16).
- [ ] 4.3 Run the full `repo_lint` check suite; confirm `broken_links` and `orphan_agent_references`
      are both green, and note (do not fix) any new `duplicate_fact_candidates` findings against the
      now-unfrozen `docs/ai-coding/` for the owning sibling epics to pick up.

## 5. Fix the two stale cross-references

- [ ] 5.1 `docs/environment-setup.md` §6: correct the sentence claiming "the `docs/ai-coding/` runbook
      … still names the older agents" — it no longer does (DEC-13). Keep the old→new mapping table.
- [ ] 5.2 Root `README.md` docs table row for `docs/ai-coding/`: update the description off "two-tier
      method" framing and confirm the link still resolves (it points at the directory, not the
      renamed file, so no path change is required — verify only).

## 6. Spec delta and inputs

- [ ] 6.1 Add `openspec/changes/define-meaningfy-lifecycle/specs/build-lifecycle/spec.md` with `##
      ADDED Requirements` (done — see spec.md in this change).
- [ ] 6.2 Confirm `inputs/2026-07-26-handbook-findings.md` is present under this change's `inputs/`
      (already written per the EPIC; no edit, no grooming — preserved record).

## 7. Named-only gaps (no file changes)

- [ ] 7.1 Confirm GAP-1 ("Improvements Outside Contract") and GAP-2 (Redelivery Policy) remain named
      only in `proposal.md`'s Known Gaps section — no new section, template, or skill edit added
      anywhere for either.

## Roadmap

- [ ] 1.1 · [ ] 1.2 · [ ] 1.3 · [ ] 1.4 · [ ] 1.5 · [ ] 1.6 · [ ] 1.7 · [ ] 1.8 · [ ] 1.9 · [ ] 1.10 ·
  [ ] 1.11 · [ ] 2.1 · [ ] 2.2 · [ ] 2.3 · [ ] 2.4 · [ ] 2.5 · [ ] 2.6 · [ ] 3.1 · [ ] 4.1 · [ ] 4.2 ·
  [ ] 4.3 · [ ] 5.1 · [ ] 5.2 · [ ] 6.1 · [ ] 6.2 · [ ] 7.1

## Verification

`openspec validate --strict` on this change plus a full `tools/repo_lint` run (`broken_links`,
`orphan_agent_references`, and a review of any new `duplicate_fact_candidates` findings) — both must
be green (the latter's advisory findings reviewed, not required to be zero).
