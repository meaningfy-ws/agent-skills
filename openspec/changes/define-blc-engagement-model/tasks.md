<!-- PLAN (tasks half). PLAN = design.md + this file. The apply phase parses `- [ ]` checkboxes. -->

> Derived from EPIC: define-blc-engagement-model (openspec/changes/define-blc-engagement-model/proposal.md)

## 1. Spec delta — DEC-12

- [ ] 1.1 Confirm `specs/engagement-model/spec.md` (already written) covers: presale-only-free
      (DEC-1), the three paid entry points and P0-advisory's commercial-only definition (DEC-2,
      DEC-3, DEC-14), P1's 6–8-week frame and three safeguards (DEC-15, DEC-16), the P2 service-line
      family (DEC-5), the repeat-client fact (DEC-6), and the docs/coach ownership split (DEC-8) —
      seven requirements, each with ≥1 four-hashtag `#### Scenario:`

## 2. docs/engagement/README.md — DEC-1, DEC-3, DEC-5, DEC-6, DEC-8, DEC-13, DEC-18

- [ ] 2.1 Replace the four-phase table with the presale-only-free funnel and the three paid entry
      points (DEC-3), stated as alternatives, not a sequence
- [ ] 2.2 Add the P2 service-line family (DEC-5) and the repeat-client rule (DEC-6)
- [ ] 2.3 Add the ownership statement: this directory is the source for the commercial model
      (DEC-8); remove "canon" wording (DEC-13)
- [ ] 2.4 Add a link to `services-and-packages.md`; reduce the TODO block per Rabbit-holes (drop
      service-packaging and safeguards items, since this change answers them) and add one pointer
      line to the EPIC's Known-gaps table (PLAN-D5) instead of re-listing G-1..G-8 in prose

## 3. docs/engagement/phases.md — DEC-1, DEC-2, DEC-3, DEC-4, DEC-6, DEC-7, DEC-15, DEC-16, DEC-19

- [ ] 3.1 Redefine `P0` from free orientation to paid advisory (DEC-2); replace the "orientation is
      free" spine rule (DEC-1)
- [ ] 3.2 Remove the "P2 valid only once P1 is complete" gate; state the direct-to-build input
      condition and the two-elicitations distinction instead (DEC-3, DEC-4)
- [ ] 3.3 Add P1's 6–8-week calendar-boxed frame and the three-option safeguards mechanism
      (DEC-15, DEC-16)
- [ ] 3.4 Replace the `P3 — Partnership & Evolution` section with the repeat-client rule and its
      relationship work, deleting the "Owner: to be shaped" placeholder (DEC-6, DEC-7)
- [ ] 3.5 Add the contract-conformance subsection per PLAN-D4: document trail (RfO/offer/contract/
      minutes), Shipper accountability, human-sign-off verdict status, one-line pointer to
      `dod-quality-gates.md`'s Builder DoD, one-line citation of the disagreement/re-shape rule
      (cited, not restated), and the light-touch/agent-assisted framing — satisfies
      `define-delivery-release-lifecycle` DEC-12's six-element content contract independent of
      merge order (DEC-13 of that change)

## 4. docs/engagement/services-and-packages.md — DEC-18, PLAN-D3

- [ ] 4.1 Add the new file: six rows (Presale, P0-advisory, P1 Decision, and the three DEC-5
      service lines), columns `Scope` / `Duration` / `Price` / `Deliverable` / `Owning skill`
- [ ] 4.2 Fill only the cells this EPIC already decided (Presale Price = Free; P0-advisory
      Duration = 1–2 days; P1 Duration = 6–8 weeks, calendar-boxed); everything else `TODO`
- [ ] 4.3 Add a one-line header note stating this is a skeleton (DEC-18) with a pointer to Known gap
      G-7 for who populates it next

## 5. skills/semantic-consulting-coach/references/engagement-model.md — DEC-8, DEC-9, DEC-10, DEC-15

- [ ] 5.1 Keep the coaching frame (three cognitive states, state-2 signals, boundary safeguard,
      design questions); replace commercial-model definitions with citations to `docs/engagement/`
      (DEC-8)
- [ ] 5.2 Re-map the cognitive-states table's commercial column: State 1 now spans both free
      presale and paid P0-advisory (DEC-9)
- [ ] 5.3 Scope the "working draft, not doctrine" caveat to the coaching method only, and state the
      commercial model is decided (DEC-10)
- [ ] 5.4 Replace the P0–P3 intentions table; resolve the "duration and shape" design question using
      P1's stated frame (DEC-15); add a pointer to the new posture file

## 6. skills/semantic-consulting-coach/references/decision-phase-posture.md — DEC-17

- [ ] 6.1 Add the new file, condensed (not verbatim) from the round-2 source: ambiguity-is-a-signal,
      helpfulness vs. usefulness, "we do not guess", calm under pressure, no need to prove
      expertise, protective-not-defensive formulations, redirect-don't-block, yes/not-yet, ending
      cleanly, and the internal red-flags list
- [ ] 6.2 Cite the new file from the coach's `SKILL.md` reference list

## 7. Cited consistency edits — DEC-11

- [ ] 7.1 `skills/semantic-consulting-coach/SKILL.md`: fix the "core insight" free→paid sentence, the
      "When to use" engagement-process bullet, the client-orchestration cell of the three-layers
      table, the "Modes are not Phases" note, the `references/` bullets (edit one, add the posture
      file), and the `Owns:` line in Boundary & Related Skills (stop claiming outright ownership of
      the engagement model)
- [ ] 7.2 `skills/decision-package/SKILL.md`: replace the "P0 Orientation | Free, shallow" row and
      the "Orientation is free, shallow, and never deeply customised" sentence with a pointer to the
      owning doc
- [ ] 7.3 `skills/proposal-writing/SKILL.md`: relabel "P0 orientation notes" and "this is still P0"
      to presale / P0-advisory
- [ ] 7.4 `skills/semantic-consulting-coach/references/semantic-consulting-domain.md`: relabel the
      public-funnel vs. internal-P0–P3-axis note
- [ ] 7.5 Root `README.md`: fix the docs-table row referencing "the P0–P3 engagement model"

## 8. Regeneration and verification

- [ ] 8.1 Run `make generate-opencode`; commit the regenerated `.opencode/` mirror
- [ ] 8.2 Run `make skill-inventory`; commit the regenerated `docs/skill-inventory.md`
- [ ] 8.3 Run `openspec validate --strict` for this change; fix any scenario/hashtag/format errors
- [ ] 8.4 Run `make lint`; confirm `broken_links` and any SSOT/reciprocal-link checks pass on the
      new cross-links between `skills/` and `docs/engagement/`

## Roadmap

- [ ] 1.1 → [ ] 2.1 · 2.2 · 2.3 · 2.4 → [ ] 3.1 · 3.2 · 3.3 · 3.4 · 3.5 → [ ] 4.1 · 4.2 · 4.3 →
  [ ] 5.1 · 5.2 · 5.3 · 5.4 → [ ] 6.1 · 6.2 → [ ] 7.1 · 7.2 · 7.3 · 7.4 · 7.5 →
  [ ] 8.1 · 8.2 · 8.3 · 8.4

## Verification

`openspec validate --strict` green for the spec delta, `make lint` green (regenerated `.opencode/`
and `skill-inventory.md` match their sources, no broken links), and no file in the catalogue still
states "orientation is free" or a P1-before-P2 gate — checked by grep across `docs/` and `skills/`
before this change is marked done.
