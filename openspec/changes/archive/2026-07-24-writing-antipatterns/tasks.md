> Derived from EPIC `writing-antipatterns` (DEC-1 through DEC-13)

## 1. Skill scaffold

- [x] 1.1 Create `skills/writing-antipatterns/SKILL.md` — frontmatter, overview, the genre map
      table, the DEC-13 domain-vs-genre note, U1–U6 stated in full, a pointer table (genre →
      reference file), self-check, `Owns:`/`Does NOT own:`/`Related:` boundary section.
- [x] 1.2 Create `skills/writing-antipatterns/references/inversion-matrix.md` — the compact
      cross-genre table plus the 13 canonical A1–A13 entries in full (smell, fails-in,
      required-in, guard, cue, fix), each as an anchored heading per-genre files can link to.

## 2. Per-genre reference files

- [x] 2.1 `references/tutorial.md`, `references/how-to.md`, `references/reference.md`,
      `references/explanation.md` — register signature, owning skill link, pointer table only
      (move | status | link to `inversion-matrix.md` anchor).
- [x] 2.2 `references/decision.md`, `references/decision-record.md`, `references/contract.md`,
      `references/coaching.md` — same format.
- [x] 2.3 Verify no per-genre file restates smell/fix/cue prose — confirmed by construction (each
      file is a pointer table only, authored directly from the design, never copy-pasted from
      `inversion-matrix.md`).

## 3. Human explainer

- [x] 3.1 Create `references/explainer.md` from `inputs/session-handout.md` §2, §6, Appendix C,
      and a generalised (no Hulubul specifics) version of Appendix A, per design.md's content
      boundary. Dropped session/meta sections (§0, §1, §3–4, §7–9).

## 4. Cross-links (no restatement)

- [x] 4.1 Added one `Related:` line to `technical-writing`, `explanatory-writing`,
      `executive-communication`, `proposal-writing`, `decision-package`, `architecture`,
      `semantic-consulting-coach`, pointing at `writing-antipatterns`.
- [x] 4.2 The `explanatory-writing` spec delta (`specs/explanatory-writing/spec.md`) is the
      complete change — the "single home for writing knowledge" family list is a spec-only
      governance requirement, never restated in any skill's prose (confirmed by grep), so no
      additional skill-file edit was needed.

## 5. Catalogue registration

- [x] 5.1 Added `writing-antipatterns` to `meaningfy-core` in `.claude-plugin/marketplace.json`.
- [~] 5.2 **Deferred.** `tools/skill_inventory.py` and `docs/skill-inventory.md` do not exist on
      `develop` — they were built on the still-unmerged `feature/linkml-neo4j-generators-and-
      skill-inventory` branch (PR #49). Pulling that tooling into this branch would improperly
      couple two independent PRs. Once PR #49 merges, `writing-antipatterns` needs one
      `PURPOSE_OF` entry and a `make skill-inventory` regeneration as a follow-up (one line +
      one command, not tracked further here).
- [x] 5.3 Regenerated `.opencode/` (`make generate-opencode` → 175 files). `docs/skill-inventory.md`
      regeneration deferred with 5.2 (same reason).
- [x] 5.4 Updated `README.md`'s skill count (20 → 21) and the `meaningfy-core` bundle row.

## 6. Validation

- [x] 6.1 `make validate` → "OK — repository self-consistent." (advisory-only notes: this skill has
      no trigger probe yet, same pre-existing gap as `linkml-engineering`/`modelling-conventions`;
      17 pre-existing non-reciprocal `Related:` notes, unrelated to this change.)
- [x] 6.2 `python -m tools.repo_lint` — passes as part of `make validate`'s lint step; 63 tests pass.
- [x] 6.3 Verified every cross-skill claim against actual current text: `architecture`'s per-C4-level
      ADR counts (2–3/3–5/2–4/1–2, confirmed the flat "5–8 typical, 14+ signals conflation" claim in
      the source drafts was an overreach — corrected in A1); `technical-writing`'s "prefer tables and
      lists over long prose" (confirmed verbatim); `proposal-writing`'s "precise, enumerated, no
      marketing prose" (confirmed verbatim, SKILL.md:105); `semantic-consulting-coach`'s defection
      table quote "They called me the expert and asked me to design it, so I should produce it."
      (confirmed verbatim, SKILL.md:157).

## Roadmap

- [x] 1.1 · [x] 1.2 · [x] 2.1 · [x] 2.2 · [x] 2.3 · [x] 3.1 · [x] 4.1 · [x] 4.2 · [x] 5.1 · [~] 5.2 · [x] 5.3 · [x] 5.4 · [x] 6.1 · [x] 6.2 · [x] 6.3

## Verification

`make validate` passes (repository self-consistent, 63 tests pass). `make skill-inventory` and its
`PURPOSE_OF` entry are deferred to a follow-up once PR #49 merges (5.2). Every cross-skill claim
cited in the new skill is confirmed against that skill's actual current text (6.3).
