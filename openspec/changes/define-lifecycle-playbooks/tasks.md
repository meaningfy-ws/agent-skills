> Derived from EPIC: define-lifecycle-playbooks (openspec/changes/define-lifecycle-playbooks/proposal.md)

## 1. Sequencing gate

- [ ] 1.1 Confirm the four sibling changes — `define-blc-engagement-model`,
      `define-meaningfy-lifecycle`, `define-delivery-release-lifecycle`, `define-roles-and-raci` —
      have landed their documents on `develop` (DEC-10). **Do not start section 2 or later until
      this is confirmed**; every link written before then targets an unmerged file and fails
      `broken_links`.

## 2. The map

- [ ] 2.1 Create `docs/how-we-work/README.md`: the funnel (presale free → P0-advisory → P1 Decision
      → direct-to-build), the three P2 entry paths, the three planes (SDLC / MDLC / CBLC, MDLC-
      standalone flagged per DEC-11), Requirements & UC as one capability at two depths (DEC-8), the
      Epic-shaping step naming the Work Shaper as its author (DEC-9), the paired Builder/Shipper
      close at Delivery & Release (DEC-7), the repeat-client relationship as an annotation (DEC-6).
- [ ] 2.2 Add the single Mermaid diagram (DEC-4) per design.md's algorithm/approach.
- [ ] 2.3 Add the pointer tables (`Fact | Owning doc`, per design.md's Decisions) under each
      narrated cluster, linking every normative claim to the sibling doc that owns it.
- [ ] 2.4 Add the closing Known-gaps section (DEC-16), mirroring the proposal's Known gaps table
      (`Gap | Status | Owner`).
- [ ] 2.5 Add links from the map to all six playbook files (section 3).

## 3. The playbooks

Each on the fixed DEC-5 template (*Your stages* → *Skills you invoke* → *Handed to you by* → *You
hand off to* → *Your done*), bullet-list format per design.md, one screen (~120 lines) max.

- [ ] 3.1 Create `docs/how-we-work/playbooks/sales-presales.md`.
- [ ] 3.2 Create `docs/how-we-work/playbooks/technical-consultant.md`.
- [ ] 3.3 Create `docs/how-we-work/playbooks/work-shaper.md` — seeded from the Employee Handbook's
      *Project Owner — the Work Shaper* mandate (DEC-9); cite `define-roles-and-raci`'s DEC-13 for
      the Architect–Builder-spectrum positioning claim rather than restating it.
- [ ] 3.4 Create `docs/how-we-work/playbooks/solution-architect.md` — include the one-line note
      that this role consults (`C`) during Epic shaping (DEC-9).
- [ ] 3.5 Create `docs/how-we-work/playbooks/solution-builder.md` — include the one-line note that
      this role consults (`C`) during Epic shaping (DEC-9).
- [ ] 3.6 Create `docs/how-we-work/playbooks/solution-shipper.md`.

## 4. Discoverability links (additive only, DEC-14)

- [ ] 4.1 Add one row to the root `README.md`'s Documentation table pointing at
      `docs/how-we-work/README.md`.
- [ ] 4.2 Add the fixed "start here" link line (design.md's Decisions) to
      `docs/engagement/README.md` (`define-blc-engagement-model`'s output).
- [ ] 4.3 Add the fixed "start here" link line to `docs/ai-coding/build-lifecycle.md`
      (`define-meaningfy-lifecycle`'s output).
- [ ] 4.4 Add the fixed "start here" link line to `docs/ai-coding/dod-quality-gates.md`
      (`define-delivery-release-lifecycle`'s output).
- [ ] 4.5 Add the fixed "start here" link line to `docs/roles-and-raci.md`
      (`define-roles-and-raci`'s output).

## 5. Validation

- [ ] 5.1 Run `make validate` (`repo_lint`'s `broken_links` gate) — zero broken links across the
      seven new files and the four edited sibling outputs.
- [ ] 5.2 Verify bidirectional role/playbook coverage by hand against `docs/roles-and-raci.md`'s six
      role definitions (spec requirement: bidirectional coverage).
- [ ] 5.3 Run the pointer-discipline self-check (design.md's Decisions): confirm every non-
      orientation declarative sentence in `README.md` and each playbook carries an adjacent link to
      its owning sibling doc; confirm none would still read true if its link target were deleted.
- [ ] 5.4 Confirm the four "start here" edits are byte-identical (modulo relative path) and add no
      other content — additive-only per DEC-14.

## Roadmap

- [ ] 1.1 · [ ] 2.1 · [ ] 2.2 · [ ] 2.3 · [ ] 2.4 · [ ] 2.5 · [ ] 3.1 · [ ] 3.2 · [ ] 3.3 · [ ] 3.4 ·
  [ ] 3.5 · [ ] 3.6 · [ ] 4.1 · [ ] 4.2 · [ ] 4.3 · [ ] 4.4 · [ ] 4.5 · [ ] 5.1 · [ ] 5.2 · [ ] 5.3 ·
  [ ] 5.4

**Ordering note:** section 1 is a hard gate — this change's implementation runs *after* the other
four EPICs' documents land on `develop` (DEC-10), because sections 2–4 link into files those changes
create or rewrite. Do not implement this change in parallel with its siblings.

## Verification

`make validate` passes with zero broken links, the bidirectional role/playbook coverage check
(spec `lifecycle-playbooks`) holds, and the pointer-discipline self-check finds no uncited normative
statement.
