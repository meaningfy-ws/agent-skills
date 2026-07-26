> Derived from EPIC: define-roles-and-raci (openspec/changes/define-roles-and-raci/proposal.md)

## 1. Role definitions

- [ ] 1.1 Create `docs/roles-and-raci.md` with title + one-paragraph framing, and the Sales/Presales
      and Technical Consultant role blocks (mandate / accountable for / skills drawn on / artifacts
      produced), per design.md's fixed four-line shape.
- [ ] 1.2 Add the Solution Architect role block.
- [ ] 1.3 Add the Work Shaper role block: mandate (WBS, roadmap, Epic pitch, risk list, story
      mapping with the Builder, DEC-2R), citing `skills/epic-planning/SKILL.md` as the skill it
      owns and steers, plus the two DEC-13 boundary paragraphs (vs. Solution Architect, vs. Solution
      Shipper) and the "leaning Builder" spectrum line, positioned as the authoritative source other
      docs cite.
- [ ] 1.4 Add the Solution Builder and Solution Shipper role blocks.

## 2. RACI legend and matrix

- [ ] 2.1 Add the RACI legend (R, A, C, I, `–`) plus the two invariant statements (one-A-per-row,
      DEC-5; role = responsibility not competence/headcount, DEC-4) immediately before the matrix.
- [ ] 2.2 Add the 17-row × 6-column RACI matrix in funnel-to-delivery row order (presale through
      partnership/account nurture, per proposal.md's What Changes), with the Epic/work-shaping row
      set to A/R Work Shaper, C Architect, C Builder (DEC-5, DEC-13) and the MDLC-standalone row
      annotated "no owning skill — parked capability gap" (DEC-8).
- [ ] 2.3 Verify by inspection that every row has exactly one `A` mark and no row has zero or two.

## 3. Adaptation notes and open question

- [ ] 3.1 Add the Quality Overseer adaptation note (DEC-14: agent-assisted review, Builder does the
      work, Shipper signs off as A, Work Shaper signs off as R on non-software-plane reviews with no
      client-facing shipment) and the Customer Success Manager adaptation note (DEC-15: folded into
      Sales/Presales' partnership/account-nurture row), each citing the handbook page it replaces.
- [ ] 3.2 Add the agent-wrapper open question subsection: today's default (documentation-only, roster
      stays `epic-planner`/`implementer`/`code-reviewer`), the reopening condition (role exercised on
      a real engagement), and the priority order (Work Shaper highest-priority-if-ever, DEC-3) —
      stated as a priority, not a commitment.

## 4. Known gaps and references

- [ ] 4.1 Add the Known-gaps subsection reproducing proposal.md's five-row gap table verbatim
      (work-shaper agent wrapper; other four agent wrappers; MDLC-standalone owning skill; agent-
      assisted review's non-software equivalent; vocabulary consistency pass pending) (DEC-17).
- [ ] 4.2 Add the references table: deep links to `define-blc-engagement-model`,
      `define-meaningfy-lifecycle`, `define-delivery-release-lifecycle`, `define-lifecycle-playbooks`,
      and the handbook excerpt in `inputs/2026-07-26-handbook-findings.md`.

## 5. Cross-repo wiring

- [ ] 5.1 Add one row to `README.md`'s Documentation table, after the `docs/engagement/` row,
      pointing at `docs/roles-and-raci.md`.
- [ ] 5.2 Extend the `docs/` line in `README.md`'s Repository-structure block to list
      `roles-and-raci.md` alongside `ai-coding/ · engineering-standards/ · philosophy/ · engagement/
      · environment-setup.md`.

## 6. Spec delta and vocabulary check

- [ ] 6.1 Add `openspec/changes/define-roles-and-raci/specs/role-accountability-model/spec.md`
      (already present — verify it stays in sync with the written doc: closed six-role set,
      one-A-per-row invariant, roles-not-competences-or-headcount, Work Shaper mandate + positioning
      citation).
- [ ] 6.2 Once siblings `define-blc-engagement-model`, `define-meaningfy-lifecycle`, and
      `define-delivery-release-lifecycle` publish their activity/plane/gate vocabulary, compare this
      doc's row labels against theirs and rename any row that diverges (DEC-16 — rename-and-check
      only, no new definitions).

## 7. Validation

- [ ] 7.1 Run `make validate` — confirm `broken_links` passes for every relative link in
      `docs/roles-and-raci.md` and the two `README.md` edits (docs-root files get no illustrative
      exemption, `tools/repo_lint/lint.py:230`).

## Roadmap

- [ ] 1.1 · [ ] 1.2 · [ ] 1.3 · [ ] 1.4 · [ ] 2.1 · [ ] 2.2 · [ ] 2.3 · [ ] 3.1 · [ ] 3.2 · [ ] 4.1
- [ ] 4.2 · [ ] 5.1 · [ ] 5.2 · [ ] 6.1 · [ ] 6.2 · [ ] 7.1

## Verification

`make validate` passes (`broken_links` + `repo_lint`), and every RACI matrix row is inspected by eye
to confirm exactly one `A` — no validator is written for this (proposal.md rabbit-holes).
