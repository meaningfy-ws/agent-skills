> Derived from EPIC: define-delivery-release-lifecycle (openspec/changes/define-delivery-release-lifecycle/proposal.md)

## 1. `docs/ai-coding/dod-quality-gates.md` — split the audiences

- [ ] 1.1 Remove the "Engagement gates (human / commercial)" section in full: the four-row table
      (including its `Build DoD` row), the "Commercial layer — TODO" blockquote, and the `Q8.2=A`
      "one ladder with two clearly-separated halves" paragraph in the intro. Replace with a single
      pointer sentence to `docs/engagement/` (directory-level target unless a specific destination
      section already exists — DEC-13).
- [ ] 1.2 Rewrite the file's **Purpose/Audience** header so its stated scope is build-tier DoD only;
      drop the "single authority for both... engagement stage gates... and build-tier DoD" framing.
- [ ] 1.3 Add the **Delivery & Release** section (placed after "The automation boundary", before
      "Definition of Done (a task)"), containing: the Builder's DoD in full (existing
      verification/validation pair, explicitly labelled SDLC-plane/Builder-side, role link to
      `define-roles-and-raci`); the one-line reciprocal pointer to the Shipper's DoD (pairing wording
      per design.md); the disagreement/re-shape rule (DEC-10), stated once and scoped to both DoDs
      regardless of which file each lives in; and the three release-mechanics citations
      (`ci-cd-delivery`, `meaningfy-release`, `meaningfy-git-workflow`) as links only, no restatement.
- [ ] 1.4 Re-anchor "The two questions" as Builder-side: retitle to signal scope, keep its two
      existing bullets unchanged, and add a third bullet naming (not answering) the third,
      contract-conformance question, pointing at the Shipper's DoD.
- [ ] 1.5 Confirm "The automation boundary" section is left byte-for-byte unchanged (DEC-5) — no new
      row, no new entry.

## 2. Ownership table — correct the stale row

- [ ] 2.1 Locate the single-owner ownership table (today `docs/ai-coding/two-tier-methodology.md`
      §5; if `define-meaningfy-lifecycle` has already renamed/relocated the file, edit it there
      instead — DEC-7, no second copy under any path).
- [ ] 2.2 Replace the stale `CD / release | ci-cd-delivery (EPIC-10, future)` row with two rows:
      `CD / deploy` → `ci-cd-delivery`, and `Release lifecycle (versioning, changelog, publish)` →
      `meaningfy-release`.
- [ ] 2.3 Amend the "CI vs CD do not overlap" note to name both new rows; leave the existing
      `meaningfy-git-workflow` row untouched (no third, duplicate row).

## 3. Spec delta

- [ ] 3.1 Add `openspec/changes/define-delivery-release-lifecycle/specs/delivery-release-dod/spec.md`
      with `## ADDED Requirements` carrying: build-tier-only scope; Builder's DoD present in full;
      the Shipper's DoD six-element content contract (DEC-12); the reciprocal-pointer requirement;
      the disagreement-routes-to-re-shape requirement; and the existing-skills-only ownership
      requirement. Each requirement has ≥1 `#### Scenario:` (exactly 4 hashtags), WHEN/THEN.

## 4. Hand-off (explicitly not this change's edit)

- [ ] 4.1 Confirm no file under `docs/engagement/` is edited by this change. The Shipper's DoD prose
      is `define-blc-engagement-model`'s task (its own DEC-19), already committed in that EPIC; this
      change's sole contribution to it is the content contract carried as spec requirements in
      Task 3.1.
- [ ] 4.2 Confirm no role definitions, no RACI matrix, no new/edited `SKILL.md`, no CI/workflow
      changes, and no edits under `docs/engagement/` or `.claude/` are introduced (No-gos).

## 5. `tests/ownership.yaml` (optional, additive only)

- [ ] 5.1 Evaluate whether a sufficiently specific `claim_patterns` exists for a `CD/deploy`
      (`ci-cd-delivery`) and a `release-lifecycle` (`meaningfy-release`) tag without risking false
      positives on legitimate cross-skill citations. If no such pattern is found, add no tag — that is
      an acceptable outcome (EPIC Impact section).

## Roadmap

- [ ] 1.1 · [ ] 1.2 · [ ] 1.3 · [ ] 1.4 · [ ] 1.5 · [ ] 2.1 · [ ] 2.2 · [ ] 2.3 · [ ] 3.1 · [ ] 4.1 ·
      [ ] 4.2 · [ ] 5.1

## Verification

`openspec validate --strict` on this change's deltas, plus a manual link check that the
`dod-quality-gates.md` → `docs/engagement/` pointer and the ownership-table's two new rows resolve to
real, existing targets.
