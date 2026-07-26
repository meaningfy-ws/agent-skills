<!-- PLAN (design half). PLAN = this file + tasks.md. The clarity gate scores the pair (≥9/10).

     ALTITUDE — the reasoning: HOW + why-this-how. Cites the EPIC's DEC-n; never re-explains a settled bet.
     Acceptance criteria live in the spec delta as GWT scenarios (WHEN/THEN), NOT here. -->

> Parent: openspec/changes/define-delivery-release-lifecycle/proposal.md

## Context

`docs/ai-coding/dod-quality-gates.md` currently serves two audiences from one file (`Q8.2=A`): an
**"Engagement gates (human / commercial)"** table + a "Commercial layer — TODO" blockquote, and the
**build-tier DoD** (the gate-set table, the automation boundary, task/Epic DoD checklists, "The two
questions"). The engagement content is a near-verbatim duplicate of
`docs/engagement/README.md` §35 — two homes, no owner (DEC-1).

Separately, `docs/ai-coding/two-tier-methodology.md` §5's single-owner ownership table still carries
`CD / release | ci-cd-delivery (EPIC-10, future)`, though `ci-cd-delivery`, `meaningfy-release`, and
`meaningfy-git-workflow` have all shipped.

The EPIC settles: single-audience `dod-quality-gates.md` (DEC-1, DEC-2); the Shipper's DoD relocates
to `docs/engagement/` as a content contract this change specifies but does not write (DEC-11, DEC-12,
DEC-13); the Builder's DoD stays in full where it is (DEC-3); a reciprocal one-line pointer replaces
co-location as the pairing mechanism (DEC-3 revised); disagreement between the two DoDs routes to a
logged re-shape, stated once, scoped to both regardless of file (DEC-10); and the ownership row splits
by concern into two rows citing the skills that exist (DEC-6), following the content if the host file
moves (DEC-7).

This design covers only new structuring choices needed to execute those settled decisions — exact
wording patterns, section placement, and how the spec delta operationalizes DEC-12's six-element
content contract as requirements on the engagement-side document.

## Goals / Non-Goals

**Goals:**
- `dod-quality-gates.md` reads as build-tier-only DoD: no reader mistakes it for a second home of
  commercial gates.
- The Builder's DoD (existing ladder) is preserved in full and explicitly labelled Builder-side.
- A reciprocal pointer pair exists: `dod-quality-gates.md` → Shipper's DoD location, and (per the
  content contract handed to `define-blc-engagement-model`) Shipper's DoD → Builder's DoD.
- The disagreement/re-shape rule is stated exactly once, worded to cover both DoDs regardless of
  which file each lives in.
- The ownership table's stale `CD / release` row is replaced by two rows citing skills that exist in
  the catalogue today.
- `delivery-release-dod` spec delta carries DEC-12's six content-contract elements as RFC-2119
  requirements enforceable against whichever document `define-blc-engagement-model` produces.

**Non-Goals:**
- Not writing any prose under `docs/engagement/` (No-gos; DEC-12, DEC-13).
- Not defining "Builder" or "Shipper" as roles — referenced only, linking to `define-roles-and-raci`
  (DEC-8).
- Not building a shipping/PM process, a sign-off artifact, or an escalation ladder (Rabbit-holes; G1,
  G3 stay open).
- Not touching `docs/engagement/`, v1 files, `.claude/HARD-QUESTIONS.md`, or any `SKILL.md` (No-gos).
- Not resolving which file ultimately hosts the ownership table — that follows whichever sibling
  change lands first (DEC-7).

## Decisions

Settled in the EPIC — cited, not re-argued: DEC-1 (single-audience reversal of `Q8.2=A`), DEC-2
(delete-not-migrate), DEC-3 (two co-closing DoDs, two planes, reciprocal pointers not co-location),
DEC-4 (Shipper's DoD as a third, named-not-answered question), DEC-5 (non-CI-automatable, no
automation-boundary entry), DEC-6 (two concern-split ownership rows), DEC-7 (follow the content, not
the path), DEC-8 (roles referenced not defined), DEC-9 (the `delivery-release-dod` capability's
scope), DEC-10 (disagreement → logged re-shape, stated once), DEC-11 (Shipper's DoD relocates to
`docs/engagement/`), DEC-12 (the six-element content contract), DEC-13 (directory-level pointer if
epic 1 hasn't landed; the contract lives in the spec, not a hand-off note).

New, made while designing:

- **Pointer wording pattern (both directions).** The `dod-quality-gates.md` → Shipper's DoD pointer
  reads as a single sentence with three fixed parts, in this order: (1) the target (a specific
  section if it exists, else `docs/engagement/` at directory level per DEC-13), (2) the pairing
  claim verbatim-equivalent to *"the two close together, on two planes, and neither substitutes for
  the other"* (DEC-3), (3) nothing else — no restatement of the Shipper's DoD's content. The spec
  delta requires this same three-part shape on the reciprocal (engagement-side) pointer, so the
  content contract is checkable without depending on epic 1's exact prose.
- **Section placement inside `dod-quality-gates.md`.** The new **Delivery & Release** section is
  inserted after "The automation boundary" and before "Definition of Done (a task)" — it is
  conceptually a third gate family (alongside the task/Epic checklists), not a preamble, so it does
  not precede the gate-set table it depends on. "The two questions" (today the file's closing
  section) is re-anchored in place — retitled to make the Builder-side scope explicit and gains a
  third bullet naming (not answering) the contract-conformance question — rather than moved, since it
  already sits after the Epic DoD checklist and the new section slots naturally before it.
- **Ownership-table row wording.** Two rows, mirroring the existing table's `Capability | Owner`
  shape: `CD / deploy` → `ci-cd-delivery`, and `Release lifecycle (versioning, changelog, publish)` →
  `meaningfy-release`. The existing `meaningfy-git-workflow` row is left untouched and cross-referenced
  from the delivery section's release-mechanics citations rather than duplicated (DEC-6). The "CI vs
  CD do not overlap" note stays, amended only to name both new rows instead of the one merged row it
  used to describe.
- **Content-contract-to-requirement mapping.** DEC-12's six elements map one-to-one onto the six
  requirements of the `delivery-release-dod` spec (see spec delta) rather than being folded into
  fewer, broader requirements — each element has an independent failure mode (e.g., the document
  trail could be present while the pairing pointer is missing), so each gets its own SHALL and its
  own scenario to stay independently testable, per DEC-9's framing of the capability as "the contract
  between the two documents."

## Algorithm / approach

Two-file edit sequence, order-independent (no dependency between them), plus one spec delta:

1. **`docs/ai-coding/dod-quality-gates.md`**
   a. Delete the "Engagement gates (human / commercial)" section in full: the four-row table, the
      "Commercial layer — TODO" blockquote, and the `Q8.2=A` paragraph in the intro. Replace with one
      sentence pointing to `docs/engagement/`.
   b. Rewrite the **Purpose** line: drop "both the engagement stage gates... and the build-tier DoD",
      state build-tier-only scope, keep the existing cross-references to
      `two-tier-methodology.md`/`opsx-runbook.md`.
   c. Insert **Delivery & Release** (placement above) with, in order: the Builder's DoD in full
      (verbatim-equivalent to today's "two questions" verification/validation pair, now explicitly
      labelled SDLC-plane/Builder-side, role linked to `define-roles-and-raci`), the one-line pointer
      (wording pattern above), the disagreement rule (DEC-10, stated once, scoped to "both DoDs
      regardless of which file each lives in"), and the three release-mechanics citations
      (`ci-cd-delivery`, `meaningfy-release`, `meaningfy-git-workflow`) as links only.
   d. Re-anchor "The two questions" → retitled to signal Builder-side scope, its two existing bullets
      unchanged, plus a third bullet naming the contract-conformance question and pointing at the
      Shipper's DoD (no new answering content — DEC-4).
   e. Leave "The automation boundary" byte-for-byte unchanged (DEC-5).
2. **`docs/ai-coding/two-tier-methodology.md` §5 (or wherever the table lives if `define-meaningfy-
   lifecycle` relocated it first — DEC-7)**: replace the one stale row with the two rows above; amend
   the "CI vs CD do not overlap" note to name them.
3. **`openspec/changes/define-delivery-release-lifecycle/specs/delivery-release-dod/spec.md`**: one
   `## ADDED Requirements` block (new capability, nothing modified), six requirements mapping DEC-12's
   elements plus the single-audience, reciprocal-pointer, disagreement-routing, and stale-ownership
   requirements named in the EPIC's Capabilities section.

### Anti-patterns

- Do not describe the Shipper's DoD as running **after** the Builder's DoD, or use words like "then"
  / "finally" between them — they close together on two planes; sequencing language re-imports the
  exact framing DEC-3 rejects.
- Do not draft even a placeholder sentence under `docs/engagement/` "for `define-blc-engagement-model`
  to overwrite" — the content contract is the deliverable; a placeholder is the two-agents-one-
  paragraph failure DEC-2/DEC-12 exist to prevent.
- Do not add a Shipper's DoD row to the build-tier gate-set table or "The automation boundary" — it is
  not a build-tier gate (DEC-5).
- Do not merge the two new ownership rows back into one "CD / release" row, and do not add a third row
  duplicating `meaningfy-git-workflow` — cross-reference the existing row instead (DEC-6).
- Do not restate DEC-10's re-shape rule a second time in the ownership-table file or anywhere else —
  it is written once, in `dod-quality-gates.md`, and cited, never repeated.
- Do not touch `docs/engagement/`, v1 files, `.claude/HARD-QUESTIONS.md`, or any `SKILL.md` (No-gos).

## Error matrix

| Failure mode | Expected handling |
|---|---|
| `define-blc-engagement-model` has not landed when this change is implemented | Pointer targets `docs/engagement/` at directory level (DEC-13); still resolves to a real, existing path, so no dangling link. |
| The ownership table's host file was renamed/relocated by `define-meaningfy-lifecycle` before this change lands | Edit the row wherever the table then lives; do not create a second copy under the old path (DEC-7). |
| A reader follows the `dod-quality-gates.md` → Shipper's DoD pointer before the target section exists | Lands on `docs/engagement/`'s directory root, not a 404 — the reader still finds the commercial-content home, just not yet the specific section. |
| `tests/ownership.yaml` candidate tags produce a false-positive claim-pattern match on a legitimate citation | Non-blocking by design; acceptable outcome is adding no tag at all if no sufficiently specific pattern is found (Impact section). |
| A future reader of `two-tier-methodology.md` §5 looks for a single merged "CD / release" owner | Finds two rows instead, each independently correct, plus the untouched "CI vs CD do not overlap" note explaining the split. |
| Someone tries to treat the Shipper's DoD as CI-enforceable because it's now "just another DoD" in a doc | The content contract requires the non-CI-automatable / human-sign-off element (DEC-12 item 3) to travel with the DoD wherever it lands, and it is absent from the automation boundary and gate-set table by construction (DEC-5). |

## Risks / Trade-offs

- **[Risk] This change's pointer target (`docs/engagement/`) may not yet contain the Shipper's DoD at
  implementation time**, since that content is `define-blc-engagement-model`'s to author. →
  **Mitigation:** hand off the content contract regardless of landing order, per DEC-13; the pointer
  degrades gracefully to directory level rather than failing.
- **[Risk] Cross-epic tension on the ownership-table row.** `define-meaningfy-lifecycle`'s own DEC-11
  resolves the same stale row as a single pointer row to `dod-quality-gates.md`, not the two
  concern-split rows this EPIC's DEC-6 mandates. Both are cited as settled in their respective EPICs.
  → **Mitigation:** out of scope to re-decide here; DEC-7's follow-the-content rule means whichever
  change is implemented second reconciles against what it finds — flagged for the implementer, not
  resolved by this PLAN.
- **[Risk] The ownership table's host file path may move** (`two-tier-methodology.md` →
  `build-lifecycle.md`, per `define-meaningfy-lifecycle`'s own DEC-2) before this change is applied. →
  **Mitigation:** DEC-7 — edit wherever the table lives at implementation time.
- **[Risk] Adding `tests/ownership.yaml` tags for CD/release could produce noisy false positives** on
  legitimate cross-skill citations. → **Mitigation:** additive-only, non-blocking validator flags; if
  the PLAN finds no sufficiently specific `claim_patterns`, adding no tag is an acceptable outcome
  (per Impact section of the EPIC).

## Open Questions

Parked — not designed here, per the EPIC's Known gaps:

- **G1** — Steps 2–6 of the Employee Handbook's shipping chain (Documentation and Preparation,
  Delivery Scheduling, Delivery Execution, Client Demonstration, Final Approval and Handover) have no
  home in `docs/` and no owning skill. A future change decides whether they live under
  `docs/engagement/`, a Shipper playbook under `define-lifecycle-playbooks`, or a new skill.
- **G2** — Agent-assisted contract review (DEC-12 item 6 permits it) has no mechanism: the documents
  it would read (email, drive, CRM) live outside the repo and no skill covers ingesting them.
- **G3** — The rework/redelivery path after a failed Shipper's DoD is undefined here; cross-referenced
  to `define-meaningfy-lifecycle`'s Redelivery Policy and "Improvements Outside Contract" gaps, not
  duplicated.
