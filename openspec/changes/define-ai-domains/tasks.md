> Derived from EPIC: define-ai-domains (openspec/changes/define-ai-domains/proposal.md)

## 1. `ai-coding/playbooks/` (DEC-4)

- [ ] 1.1 Create `docs/ai-coding/playbooks/`; move
      `docs/how-we-work/build/playbooks/{solution-architect,solution-builder,solution-shipper}.md`
      and `docs/how-we-work/playbooks/work-shaper.md` into it, content unchanged.
- [ ] 1.2 In each of the four moved files, fix outbound relative links that pointed at
      `../../overview.md`, `../../roles-and-raci.md`, `../../business/...` — retarget to the new
      top-level `../../roles-and-raci.md` (now correct, unchanged depth) and drop the "Start here:
      How We Work" pointer line (no successor map file exists — design.md Anti-patterns).
- [ ] 1.3 In `docs/ai-coding/dod-quality-gates.md` and `docs/ai-coding/build-lifecycle.md`, retarget
      every `../how-we-work/roles-and-raci.md` link to `../roles-and-raci.md` and every
      `../how-we-work/overview.md` link per design.md (drop or retarget per what replaces it).
- [ ] 1.4 (content recovery, per the pre-session content-comparison pass) Add a short "Practitioner
      notes" section to `docs/ai-coding/opsx-runbook.md`, recovered from the deleted v1
      `ai-coding-methodology.md` §7 (confirmed to have no successor anywhere in current docs or
      skills): roadmap-driven development (a dedicated file per phase that the agent reads/writes
      makes it easy to build on prior work), planning mode first (reasoning-heavy work is cheaper and
      faster when planned before files are touched), and stating project structure upfront (naming
      ports/entrypoints/layers in the prompt lets the agent generate correct boilerplate) — plus a
      short "what still needs manual attention" list (dependency-file edits, docker-compose tweaks,
      import-path corrections: the overhead of agent interaction can exceed the fix itself). Adapt
      the wording to the current three-wrapper agent model; do not reintroduce v1's five-agent
      framing.
- [ ] 1.5 (content recovery) Add the `/context` token-monitoring tip from the deleted v1
      `ai-coding-setup-guide.md` §8 troubleshooting table (confirmed to have no successor) to
      `docs/ai-coding/opsx-runbook.md`'s practitioner notes (task 1.4) or wherever it names heavy/
      long-running operations: "context window filling up → run `/context` to check usage; use
      subagents to isolate heavy operations rather than doing them in the main thread."

## 2. `ai-sales/` (DEC-5, DEC-6, DEC-7, DEC-8)

- [ ] 2.1 Create `docs/ai-sales/engagement-lifecycle.md` by merging
      `docs/how-we-work/business/discovery-and-onboarding.md` and
      `docs/how-we-work/business/repeat-clients.md` into one file (design.md Decisions: the
      `repeat-clients.md` content becomes a `## Repeat clients` section, heading preserved
      verbatim). Apply the DEC-8 correction: state the Deep tier's actual deliverable is the
      Decision Package via gap analysis, drop the "semantic & data maturity assessment" framing from
      this commercial promise.
- [ ] 2.2 Preserve every heading anchor from `discovery-and-onboarding.md` used by external citations
      (`#presale-free-no-deliverable`, `#discovery--onboarding-paid-two-depths`, `#direct-to-build`,
      `#the-outcome-semantic-layer-adoption`, `#known-gaps`) — per design.md's heading-anchor rule,
      only the DEC-8 sentence itself changes wording, not the headings.
- [ ] 2.3 Move `docs/how-we-work/business/semantic-layer-services.md` →
      `docs/ai-sales/semantic-layer-services.md`, fixing its one outbound link to
      `discovery-and-onboarding.md` (now `engagement-lifecycle.md`, same directory).
- [ ] 2.4 Move `docs/services/` (7 files) → `docs/ai-sales/services/` wholesale; fix each page's
      outbound links to `../how-we-work/business/discovery-and-onboarding.md` →
      `../engagement-lifecycle.md` and to `../how-we-work/roles-and-raci.md` → `../../roles-and-raci.md`.
- [ ] 2.5 Create `docs/ai-sales/playbooks/`; move
      `docs/how-we-work/business/playbooks/sales-presales.md` into it (DEC-6: technical-consultant.md
      does NOT move here). Fix its outbound links (`../discovery-and-onboarding.md` →
      `../engagement-lifecycle.md`, `../repeat-clients.md` → `../engagement-lifecycle.md#repeat-clients`,
      `../../roles-and-raci.md` → `../../../roles-and-raci.md`).
- [ ] 2.6 Write `docs/ai-sales/sales-runbook.md` — new — per design.md's fixed shape (Presale →
      Discovery & Onboarding → Contracting/hand-off → Repeat-client relationship), each stage citing
      `engagement-lifecycle.md` and `roles-and-raci.md`, never restating either (spec requirement:
      playbooks/runbooks cite, not restate).
- [ ] 2.7 Write `docs/ai-sales/sales-dod.md` — new — verbatim-moved content from
      `docs/ai-coding/dod-quality-gates.md` lines 54-64 (the Shipper's-DoD definition), plus one new
      sentence citing (not copying) the Disagreement rule at
      `docs/ai-coding/dod-quality-gates.md#delivery--release` (design.md Decisions; spec requirement:
      cross-domain rules stay single-sourced).

## 3. `ai-consulting/` (DEC-7, DEC-9, DEC-10)

- [ ] 3.1 Write `docs/ai-consulting/advisory-runbook.md` — new, written for real per DEC-10 — using
      design.md's six-step shape (Intake → Landscape reading → Method selection → Gap analysis/
      option framing/sequencing/buy-build-defer → Decision Package production → Hand-off), citing
      `skills/decision-package/references/discovery-flow.md`'s matching numbered sections concretely
      by section number, and `skills/decision-package/SKILL.md`'s five-part deliverable list for step
      5, never restating either.
- [ ] 3.2 Write `docs/ai-consulting/consulting-dod.md` — new, scaffold — using design.md's exact
      four-heading structure (What "done" would need to answer / Why this isn't decided yet / What it
      depends on / Until then), citing all five `methods/` files and
      `skills/decision-package/SKILL.md`'s R1 five-part check as the interim fallback.
- [ ] 3.3 Write `docs/ai-consulting/methods/gap-analysis.md` — the one pointer (not a stub) — citing
      `skills/decision-package/references/discovery-flow.md` §3's gap-class table by link, per
      design.md's pointer-vs-stub shape distinction.
- [ ] 3.4 Write `docs/ai-consulting/methods/data-maturity-assessment.md` — extension-point stub, per
      design.md's four-heading stub template (What it is / Why it matters / Current status /
      Where it would fit), including the direct "No skill in this repo owns..." sentence.
- [ ] 3.5 Write `docs/ai-consulting/methods/semantic-maturity-assessment.md` — same stub template.
- [ ] 3.6 Write `docs/ai-consulting/methods/wardley-mapping.md` — same stub template.
- [ ] 3.7 Write `docs/ai-consulting/methods/enterprise-process-modelling.md` — same stub template.
- [ ] 3.8 Create `docs/ai-consulting/playbooks/`; move
      `docs/how-we-work/business/playbooks/technical-consultant.md` into it wholly (DEC-6 — straight
      relocation, no split). Fix its outbound links: `../discovery-and-onboarding.md` →
      `../../ai-sales/engagement-lifecycle.md`, `../../roles-and-raci.md` → `../../../roles-and-raci.md`.

## 4. `roles-and-raci.md` un-move (DEC-3)

- [ ] 4.1 Move `docs/how-we-work/roles-and-raci.md` → `docs/roles-and-raci.md` (back to top-level),
      content unchanged except the one outbound link to `overview.md` (drop — no successor map file,
      per design.md Anti-patterns) and the "Start here" line at the top (drop for the same reason;
      the RACI matrix is now reached via each domain's own docs, not a single map).
- [ ] 4.2 Confirm every anchor this file exposes (`#work-shaper`, `#raci-matrix`, `#solution-builder`,
      `#solution-shipper`, `#technical-consultant`, `#salespresales`, `#solution-architect`,
      `#open-question--agent-wrappers`) is unchanged — every citing file across sections 1-3 above
      already assumes this.

## 5. `dod-quality-gates.md` edit (DEC-7)

- [ ] 5.1 Remove lines 54-64 (the Shipper's-DoD definition, now relocated to `sales-dod.md`) from
      `docs/ai-coding/dod-quality-gates.md`. Keep lines 69-72 (the Disagreement rule) and the
      Builder's DoD content untouched (proposal Rabbit-holes: no redesign of Builder's-DoD content).
- [ ] 5.2 Add one citation line pointing to `docs/ai-sales/sales-dod.md` where the removed prose
      used to sit, and update the file's Purpose header to state it is now Builder's-DoD-only.

## 6. `environment/` relocation (DEC-11)

- [ ] 6.1 Create `docs/environment/`; move `docs/environment-setup.md` →
      `docs/environment/setup.md`. Per design.md's depth-arithmetic decision: every existing
      single-`../` link in this file (to `README.md`, `AGENTS.md`, `spine/*`, `openspec/specs/*`,
      `prompts/`, `skills/*`) becomes `../../`. Same-directory links to `dual-cli/*` stay unchanged
      (dual-cli moves alongside it in task 6.3).
- [ ] 6.2 Move `docs/ai-coding/openspec-setup-guide.md` → `docs/environment/openspec-setup-guide.md`.
      Per design.md: this file's existing `../../` links need **no change** (same depth, different
      depth-2 parent) — do not add an extra `../` "for consistency" with task 6.1 (Error matrix).
- [ ] 6.3 Move `docs/dual-cli/` (6 files, contents untouched — Rabbit-holes) →
      `docs/environment/dual-cli/`.
- [ ] 6.4 In `docs/ai-coding/opsx-runbook.md` and `docs/ai-coding/build-lifecycle.md`, retarget the
      same-directory `openspec-setup-guide.md` links to `../environment/openspec-setup-guide.md`.

## 7. Cross-repo link sweep (mechanical, per design.md's Context site list)

- [ ] 7.1 `README.md`: retarget lines 6, 55, 133-135 (Documentation table: replace the single
      `how-we-work` row and `services` row with rows for `ai-coding`, `ai-sales`, `ai-consulting`,
      `roles-and-raci.md`, and `environment/`); update the Repository-structure block (line 152).
- [ ] 7.2 `AGENTS.md`: retarget lines 27, 58, 63, 71 (`docs/dual-cli/...` →
      `docs/environment/dual-cli/...`).
- [ ] 7.3 `THIRD_PARTY_NOTICES.md`: retarget line 10 (`docs/environment-setup.md` →
      `docs/environment/setup.md`).
- [ ] 7.4 `hooks/bindings.md`: retarget line 86 (`../docs/dual-cli/compatibility.md` →
      `../docs/environment/dual-cli/compatibility.md`).
- [ ] 7.5 `skills/project-setup/SKILL.md`: retarget line 40 (`../../docs/ai-coding/openspec-setup-guide.md`
      → `../../docs/environment/openspec-setup-guide.md`).
- [ ] 7.6 `skills/decision-package/SKILL.md`: retarget line 87
      (`../../docs/how-we-work/business/discovery-and-onboarding.md` →
      `../../docs/ai-sales/engagement-lifecycle.md`).
- [ ] 7.7 `skills/semantic-consulting-coach/SKILL.md` (7 sites) and its `references/engagement-model.md`
      (9 sites), `references/decision-phase-posture.md` (1 site), `references/semantic-consulting-domain.md`
      (1 site): retarget every `docs/how-we-work/business/discovery-and-onboarding.md` and
      `.../repeat-clients.md` link to the corresponding `docs/ai-sales/engagement-lifecycle.md`
      (with `#repeat-clients` anchor where the target was `repeat-clients.md`).
- [ ] 7.8 Run `make generate-opencode` to regenerate `.opencode/**`'s mirror of every `skills/**` edit
      above — do not hand-edit `.opencode/` (design.md Anti-patterns).

## 8. Retire `docs/how-we-work/` (only after 1-7 confirmed)

- [ ] 8.1 Confirm, file by file, that every file under `docs/how-we-work/` has a corresponding moved
      destination created in sections 1-4 above (checklist: overview.md content redistributed with
      no replacement map — confirmed intentional per proposal; discovery-and-onboarding.md,
      repeat-clients.md, semantic-layer-services.md, both playbooks/ subtrees, roles-and-raci.md all
      have a destination).
- [ ] 8.2 `git rm -r docs/how-we-work/`.

## 9. Spec delta + sibling supersession annotation (DEC-12)

- [ ] 9.1 Confirm `openspec/changes/define-ai-domains/specs/ai-domain-model/spec.md` exists (already
      written as part of this PLAN) — no further action; it is `## ADDED Requirements` only, per
      design.md's resolved supersession mechanics (no `## MODIFIED Requirements` block is written
      against `lifecycle-playbooks`, because that capability was never archived into
      `openspec/specs/`).
- [ ] 9.2 Before editing, check whether `openspec/specs/lifecycle-playbooks/` now exists (i.e.
      whether `define-lifecycle-playbooks` was archived by someone else in the meantime — design.md
      Error matrix). If it does NOT exist (the expected case): edit
      `openspec/changes/define-lifecycle-playbooks/proposal.md`'s Capabilities section directly —
      strike through the `lifecycle-playbooks` capability line, add a one-paragraph "this conflicted
      with / resolution" note pointing to `ai-domain-model`, matching the exact annotation pattern
      used in `define-meaningfy-lifecycle/proposal.md` DEC-11. If it DOES exist: write a
      `## REMOVED Requirements` (with Reason + Migration) delta in
      `openspec/changes/define-ai-domains/specs/lifecycle-playbooks/spec.md` instead, and skip the
      `proposal.md` annotation.

## 10. Validation

- [ ] 10.1 Run `make validate` (`repo_lint`'s `broken_links` gate) — zero broken links across every
      moved, created, and edited file.
- [ ] 10.2 Run the manual grep backstop (design.md Error matrix) for plain-text (non-link) mentions
      of `how-we-work`, `docs/services/`, `docs/environment-setup`, `ai-coding/openspec-setup-guide`,
      `docs/dual-cli` outside `openspec/changes/*` and `.opencode/` — confirm none remain stale.
- [ ] 10.3 Manually verify every anchor listed in design.md's Context table still resolves against
      the moved files' final headings (anchors are invisible to `broken_links` — design.md Error
      matrix).
- [ ] 10.4 Run `python -m tools.repo_lint` (or the repo's equivalent invocation) directly to confirm
      the same result outside `make validate`'s wrapper.
- [ ] 10.5 Run `openspec validate --strict` on both `define-ai-domains` and
      `define-lifecycle-playbooks` — confirm both remain structurally valid after the section 9
      annotation.
- [ ] 10.6 Note for the implementer (not run here): re-run the explanatory-writing /
      writing-antipatterns check on every new or substantively rewritten prose file from sections 2-3
      (`engagement-lifecycle.md`, `sales-runbook.md`, `sales-dod.md`, `advisory-runbook.md`,
      `consulting-dod.md`, the five `methods/` files) — same discipline as the prior writing-
      antipatterns round, per the assignment's own closing instruction.

## Roadmap

- [ ] 1.1 · [ ] 1.2 · [ ] 1.3 · [ ] 1.4 · [ ] 1.5 · [ ] 2.1 · [ ] 2.2 · [ ] 2.3 · [ ] 2.4 · [ ] 2.5 · [ ] 2.6 · [ ] 2.7 ·
  [ ] 3.1 · [ ] 3.2 · [ ] 3.3 · [ ] 3.4 · [ ] 3.5 · [ ] 3.6 · [ ] 3.7 · [ ] 3.8 · [ ] 4.1 · [ ] 4.2 ·
  [ ] 5.1 · [ ] 5.2 · [ ] 6.1 · [ ] 6.2 · [ ] 6.3 · [ ] 6.4 · [ ] 7.1 · [ ] 7.2 · [ ] 7.3 · [ ] 7.4 ·
  [ ] 7.5 · [ ] 7.6 · [ ] 7.7 · [ ] 7.8 · [ ] 8.1 · [ ] 8.2 · [ ] 9.1 · [ ] 9.2 · [ ] 10.1 · [ ] 10.2 ·
  [ ] 10.3 · [ ] 10.4 · [ ] 10.5 · [ ] 10.6

**Ordering note:** sections 1-6 (moves, new content, edits) must all land before section 7 (the
cross-repo link sweep, which targets final paths only), which must land before section 8 (the
delete — see design.md's write-order rationale: deleting first would destroy the source before
every destination is confirmed). Section 9 can run any time after 1-6 but is placed after 8 so its
annotation describes the structure as actually built. Section 10 is strictly last.

## Verification

`make validate` passes with zero broken links, both changes pass `openspec validate --strict`, the
manual anchor and plain-text-mention backstops in section 10 find nothing stale, and the
`ai-domain-model` spec's six requirements are each checkable by inspection against the final
`docs/ai-coding/`, `docs/ai-sales/`, `docs/ai-consulting/`, and `docs/roles-and-raci.md` structure.
