<!-- PLAN (design half). PLAN = this file + tasks.md. The clarity gate scores the pair (≥9/10).

     ALTITUDE — the reasoning: HOW + why-this-how. Cite the EPIC's DEC-n; never re-explain a settled bet.
     Acceptance criteria live in the spec deltas as GWT scenarios (WHEN/THEN), NOT here. -->

> Parent: openspec/changes/define-meaningfy-lifecycle/proposal.md

## Context

`docs/ai-coding/` today holds two live, contradictory build-plane docs: `ai-coding-runbook.md` (+
`ai-coding-methodology.md`, `ai-coding-setup-guide.md`) describing a retired single-file `EPIC.md`
model and naming two agents (`gherkin-writer`, `documenter`) that no longer exist in `agents/`; and
`two-tier-methodology.md`, which is right about artifacts but has no diagram, a four-bullet PROJECT
tier, and a stale `CD / release | ci-cd-delivery (EPIC-10, future)` ownership row. Six live files link
into `two-tier-methodology.md` by name (verified by grep): `docs/engagement/README.md` (lines 22,
30), `docs/engagement/phases.md` (line 60), `docs/ai-coding/opsx-runbook.md` (line 6),
`docs/ai-coding/openspec-setup-guide.md` (line 9), `docs/ai-coding/dod-quality-gates.md` (line 8).

`tools/repo_lint/lint.py` currently: (a) lists `docs/ai-coding/` in `FROZEN_GLOBS` (a 1-tuple), which
exempts the whole directory from prose checks including `orphan_agent_references`; (b)
`orphan_agent_references` (line ~255) already skips frozen paths, `EPIC-setup*` files, and
`environment-setup.md` by name, but has **no exemption for active `openspec/changes/` trees** — only
`openspec/changes/archive/` is skipped entirely, at the `_iter_text_files` level (`_ARCHIVE_PREFIX`).
This change's own preserved seed `inputs/handover-analysis.md` names both retired agents, so the
check is red on this branch today (verified — DEC-16 in the EPIC).

This EPIC is the second of five siblings shaping the same lifecycle round; `define-delivery-release-lifecycle`
owns `dod-quality-gates.md`'s content **and** the ownership-table `CD / release` row correction (its
DEC-6/DEC-7 — DEC-11 here was superseded during the cross-epic consistency pass, since it duplicated
that claim with contradictory content). This change's diagram terminal node still points at
`dod-quality-gates.md` (DEC-9, unaffected) and this change inherits any advisory findings the
FROZEN_GLOBS un-freeze surfaces there (out of scope here per the EPIC's rabbit-holes).

## Goals / Non-Goals

**Goals:**
- Land the rewritten, renamed successor doc and retarget all six inbound links in one change, so
  `repo_lint.broken_links` never observes a dangling link to the old filename.
- Make the two `tools/repo_lint/lint.py` edits (DEC-12, DEC-16) minimal, one-line-scoped, and
  independently verifiable against the specific check functions they affect.
- Sequence the delete-and-rename so a partial application of this change (e.g. review checkpoint
  mid-task-list) never leaves the repo in a red-`broken_links` or agent-orphaned state for longer
  than one task.

**Non-Goals:**
- Redesigning `orphan_path_mentions` or the exemption mechanism into a config file (explicit rabbit-hole).
- Any content edit inside `dod-quality-gates.md` beyond the one inbound link retarget (epic 3's file).
- Deciding whether `build-lifecycle.md` is later absorbed into epic 5's umbrella doc (left open in the EPIC).

## Decisions

New structuring choices only — every naming/content bet (DEC-1..DEC-18) is settled in the EPIC and
cited, not re-argued, below.

- **Sequencing of rename vs. link retarget vs. delete (implements DEC-2, DEC-7 without a red window).**
  Order within the task list: (1) `git mv two-tier-methodology.md build-lifecycle.md` and rewrite its
  contents in place; (2) retarget all six inbound links to the new filename; (3) delete the three v1
  files. Rationale: after step (1) the old filename is gone, so doing (3) before (2) would make
  `broken_links` red against the *v1* files' own inbound pointers (each v1 file links to
  `two-tier-methodology.md` too — see the file dump above) for no reason; doing (2) before (1) would
  briefly point six files at a file that doesn't yet carry the rewritten content. Reordering to
  (1)→(2)→(3) means every intermediate git-committable state has zero dangling links and zero
  stale-content links. `broken_links` is the safety net (DEC-2) — this ordering is what makes it stay
  green throughout rather than only at the end.
- **Rewrite before wiring, not after.** The full rewrite (diagram, table, method-spine passage,
  governance paragraph, PROJECT-tier expansion) lands in the same file operation as the rename
  (step 1), not as a follow-up edit — otherwise a reviewer sees an intermediate commit-worthy state
  that is renamed but still narratively wrong (still "two-tier", still missing ADLC/MDLC-lite), which
  is exactly the confusion this EPIC exists to remove.
- **`FROZEN_GLOBS` edit is a deletion of the tuple's only element, not a rewrite of the mechanism.**
  `FROZEN_GLOBS = ("docs/ai-coding/",)` becomes `FROZEN_GLOBS = ()` (empty tuple), with the comment
  above it (`# Files/dirs whose content must never be edited (frozen)...`) updated to note that
  `docs/ai-coding/` was the only entry and is no longer frozen as of this change, and why (DEC-12).
  Keeping it as an empty tuple (rather than deleting the constant) preserves the mechanism for any
  future freeze without speculative re-engineering (YAGNI).
- **`orphan_agent_references` exemption is scoped to the function's own file loop, mirroring the
  existing `_is_frozen(...) or f.name.startswith("EPIC-setup") or f.name == "environment-setup.md"`
  guard clause** — add `or str(f.relative_to(repo)).startswith("openspec/changes/")` to that same
  `if` (line ~265). Rationale: `_ARCHIVE_PREFIX` already fully skips *archived* changes at the
  `_iter_text_files` level; active changes need the narrower, function-local exemption DEC-16
  describes, because `orphan_path_mentions` and other prose checks must keep seeing active-change
  text (the EPIC's rabbit-hole: "don't widen the lint work" — only `orphan_agent_references` gets the
  new clause, not a directory-wide skip).
- **Verification step for the six link retargets is a grep, not a manual read.** After step (2),
  `grep -rn "two-tier-methodology" docs/ README.md` must return zero matches outside archived
  changes — this is the cheap check DEC-18's governance principle asks every gate to offer.

## Algorithm / approach

Worked sequencing for the file-level change (idempotent — re-running any step on an already-updated
repo is a no-op or a clean error, never silent corruption):

1. `git mv docs/ai-coding/two-tier-methodology.md docs/ai-coding/build-lifecycle.md`.
2. Rewrite `build-lifecycle.md` in place: retitle, drop "two-tier" framing (DEC-1), expand PROJECT
   tier into named steps citing owners (DEC-4, DEC-5, DEC-6), add the method-spine passage (DEC-17),
   add the governance paragraph (DEC-18), redraw the Mermaid diagram and responsibility table
   (DEC-8, DEC-9, DEC-10); no ownership-table row edit (DEC-11, superseded — epic 3's to correct).
   Carry forward verbatim in
   substance (not necessarily wording) §2 (labelled Shape-Up divergence), §3 (guardrails pointer), §4
   (model tiering), §6 (no-double-spec layering), §7 (agent roster), §8 (SEED/AgOCQs++) from the
   current file (DEC-15).
3. Retarget the six inbound links (mechanical `s/two-tier-methodology/build-lifecycle/` at each of the
   six call sites listed in Context — no other text in those files changes, per the EPIC's No-gos).
4. `git rm docs/ai-coding/ai-coding-methodology.md docs/ai-coding/ai-coding-runbook.md docs/ai-coding/ai-coding-setup-guide.md`.
5. Edit `tools/repo_lint/lint.py`: empty `FROZEN_GLOBS`, add the `openspec/changes/` clause to
   `orphan_agent_references`.
6. Edit `docs/environment-setup.md` §6 (one sentence: drop "predates this change and still names the
   older agents", since the doc it describes no longer does) and root `README.md`'s docs table row
   (filename + one-line description, still "you're learning how we build with agents").
7. Add the spec delta at `specs/build-lifecycle/spec.md`.

### Anti-patterns

- Deleting the three v1 files before the six links are retargeted (temporarily breaks nothing since
  v1 files aren't link *targets* for the six — but do not reorder steps 3/4 below step 2, since step 2
  is what makes the six links point at *correct* content, not just an *existing* file).
- Copy-pasting the v1 diagram/table into the new file and relabelling nodes — DEC-8 requires
  adaptation (new artifact vocabulary, three-wrapper roster, no `MEMORY.md`-as-truth), not a reskin.
  A copy-paste that still says `EPIC.md` or `gherkin-writer` anywhere fails this change.
- Editing `dod-quality-gates.md` beyond its one inbound link — any content fix noticed while
  un-freezing belongs to `define-delivery-release-lifecycle`, not here.
- Turning the `FROZEN_GLOBS` edit into a general "make it a config" refactor — it stays a tuple
  literal, now empty.
- Writing prose for GAP-1 or GAP-2 into `build-lifecycle.md` — they are named in the EPIC only; this
  design and its tasks touch zero files for them.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| `repo_lint.broken_links` fires mid-sequence (a link retargeted before the rename lands, or vice versa) | Follow the fixed order (rename+rewrite → retarget → delete); run `broken_links` after each of steps 1–4, not only at the end, to catch a misordered edit immediately |
| A seventh, previously-unverified inbound link to `two-tier-methodology.md` surfaces after the grep in step 3 | Re-run `grep -rn "two-tier-methodology" docs/ README.md skills/ spine/` before deleting the v1 files (step 4); fix any additional hit the same way (mechanical retarget only) |
| `orphan_agent_references` still red after the lint.py edit | Confirm the new clause matches the active change's actual relative path (`openspec/changes/define-meaningfy-lifecycle/...`, not `openspec/changes/archive/...` which is already exempt); re-run `python -m tools.repo_lint.lint` (or the project's invocation) to confirm green |
| `repo_lint.duplicate_fact_candidates` (advisory) starts flagging the un-frozen `build-lifecycle.md` against `dod-quality-gates.md` or the engagement docs | Expected per the EPIC's Gates table (non-blocking); review the findings but do not treat them as blocking this change — content fixes in sibling-owned files are out of scope |
| `openspec validate --strict` fails on the new `build-lifecycle` capability spec | Check scenario hashtag count (`####` exactly) and that every `### Requirement:` has ≥1 scenario before re-running |
| A reviewer asks for GAP-1/GAP-2 detail | Point to the EPIC's "Known gaps" section — this PLAN designs neither, by the EPIC's own No-gos |

## Risks / Trade-offs

- **[Risk]** The un-freeze (DEC-12) surfaces `duplicate_fact_candidates` findings in
  `dod-quality-gates.md` or `docs/engagement/` that look urgent to fix while already in the file.
  → **Mitigation:** the EPIC's rabbit-hole is explicit — fix broken links only; log any content
  finding for the owning sibling epic instead of expanding this change.
- **[Risk]** Rewriting `build-lifecycle.md` in one large diff makes it hard for a reviewer to check
  DEC-8's "adapted, not ported" requirement against the old file.
  → **Mitigation:** keep the `git mv` as its own step so the diff tool shows a rename+diff rather than
  a delete+add; the task list requires an explicit self-check that no v1 artifact name (`EPIC.md`,
  `gherkin-writer`, `documenter`, `MEMORY.md`-as-truth) appears in the new file.
- **[Trade-off]** Emptying `FROZEN_GLOBS` to `()` rather than deleting the constant keeps a small
  amount of now-unused-but-ready machinery in `lint.py`. Accepted: the alternative (delete the
  constant, re-add it later if another directory needs freezing) is a larger, riskier future diff for
  a one-line-swap now.

## Open Questions

- **GAP-1 — "Improvements Outside Contract" pattern.** Named only, per the EPIC's Known Gaps; no
  design work here. Natural future owner: `epic-planning`.
- **GAP-2 — Redelivery Policy.** Named only, per the EPIC's Known Gaps; no design work here. Natural
  future owners: `epic-planning` (re-shape half) / `spec-stewardship` (close/archive half) — which of
  the two is itself unresolved and belongs to that future EPIC's shaping.
- **Umbrella-doc absorption.** Whether `build-lifecycle.md` later becomes a chapter of epic 5's "How
  We Work" doc or stays standalone is explicitly epic 5's call once its own shape is known (deferred
  in the EPIC's Impact section, not decided here).
