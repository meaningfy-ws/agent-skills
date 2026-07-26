# Seed — BLC/SDLC redefinition brainstorm (excerpt for `define-delivery-release-lifecycle`)

**Status: SECONDARY input. Never groomed, never deleted.** The shaped EPIC
([`../proposal.md`](../proposal.md)) supersedes this as the primary truth but does not replace it.

**Provenance:** a long `/opsx:explore` session between Claude Code and Eugeniu Costetchi
(2026-07-25), auditing `docs/ai-coding/`, `docs/engagement/`, `docs/engineering-standards/`,
`docs/philosophy/`, and the 23-skill catalogue. The full synthesis covers five epics; this file
archives **verbatim** the sections that feed this change: §1 (why the work exists), §4 (the two
bridge ambiguities — the Delivery & Release resolution), §7 (v1/v2 doc findings — the stale
ownership line and the `dod-quality-gates.md` split), and this change's slice of §8 (the five-epic
scope split) plus the scope discipline that applies to all five. Sections 2, 3, 5, and 6 of the
synthesis feed sibling epics (`define-blc-engagement-model`, `define-meaningfy-lifecycle`,
`define-roles-and-raci`, `define-lifecycle-playbooks`) and are deliberately not copied here — cite
those changes, do not restate their content.

**Ground rule carried from the synthesis:** do not ask the user anything. Where a point is OPEN,
make the most reasonable call and record it as a `DEC-` in the proposal with its reasoning.

---

## §1. Why this work exists (verbatim)

Today's SDLC/engagement documentation is fragmented across a v1 (deprecated but still live) and v2
("two-tier") layer, plus a separate P0–P3 engagement model, with real duplication, staleness, and
missing steps. A full audit (see prior artifact, not reproduced here) found the fragmentation is
**80% a narrative/wiring problem** — most needed capabilities already exist as mature skills — and
**20% real new ground** (a genuine capability gap, a business-model correction, and new synthesis
docs that don't exist yet).

**Terminology ground rules, decided by the human:**
- Retire the word **"canon"** — ambiguous, replace with plain wording ("guide", "model", "doc").
- Retire **"two-tier"** as the top-level name — it undercounts the real structure now that business/
  commercial, architecture, modelling, building, and delivery are all distinct concerns.
- **"SDLC" should be scoped specifically to the EPIC-tier build loop** (shape EPIC → PLAN →
  clarity-gate → BDD → TDD implement → review → archive) — not used as a catch-all for the whole
  P2 execution stage the way the old docs did.

---

## §4. The two "bridge" ambiguities — resolved (verbatim)

The human flagged two points as genuinely ambiguous and asked for a definitive split (not just
naming). These are the resolutions reached and confirmed in-session:

### Requirements & Use-Case elicitation
**Not a stage.** It is a **single capability** — `architecture`'s UC White (the contract, black-box)
/ UC Blue (the realisation, white-box) — invoked from **two different entry points at two different
depths**:
- **Shallow (White only)** when it's feeding a **P1 Decision** roadmap — business-case framing, no
  internals.
- **Deep (White + Blue)** when it's feeding **architecture work directly** — either handed off from
  a completed P1, or as the *first* real elicitation when a direct-to-build client skipped P1
  entirely.

One capability, two invocation depths, no dedicated pipeline stage in between.

### Delivery & Release
**Not one stage.** It is **two deliveries that close at the same moment, on two different planes,
owned by two different roles** — stated directly by the human:
- **Builder** is accountable that what shipped matches the **Epic / architecture spec** — the
  SDLC-plane DoD ("builder is responsible to ship properly what was specified in the epic work
  shape, and according to the architecture").
- **Shipper** is accountable that what shipped matches the **contract / client requirement** — the
  BLC-plane DoD ("solution shipper must make sure we shipped properly what was promised in the
  contract and according to client requirements").

Both close together; neither substitutes for the other. Software/model delivery must remain part of
the SDLC process; business delivery sits on a different plane, done by a different role — they are
paired, not sequential.

> *Note (Requirements & Use-Case elicitation, above, is included for context only — it is owned by
> `define-meaningfy-lifecycle`, not by this change.)*

---

## §7. v1 / v2 doc findings (verbatim)

- **v1** = `docs/ai-coding/ai-coding-methodology.md`, `ai-coding-runbook.md`, `ai-coding-setup-guide.md`.
  Marked "retained for reference until the first real engagement closes" (no owner, no date — that
  condition is itself stale/vague and should just be resolved by deleting once the successor content
  exists). v1's **only genuinely good, worth-keeping content**: the lifecycle Mermaid diagram and the
  Developer-vs-Agent responsibility table in `ai-coding-runbook.md` §1 — both better onboarding
  artifacts than anything in v2 today (v2 has zero diagrams — a regression vs. what it superseded).
  **Do not port these verbatim** — the human was explicit: adapt them to current reality (the
  EPIC/PLAN split, the 3-agent roster `epic-planner`/`implementer`/`code-reviewer`, OpenSpec-native
  artifacts, no `MEMORY.md`-as-truth — all of which v1's diagram/table predate).
- **v2** = `docs/ai-coding/two-tier-methodology.md`, `opsx-runbook.md`, `dod-quality-gates.md`,
  `openspec-setup-guide.md`. The EPIC/PLAN split, the single-owner ownership table, and the
  "no double-spec" layering rule are all correct and should be kept. But: `two-tier-methodology.md`
  §1's PROJECT tier is four one-line bullets that don't name ADLC or MDLC-lite at all, even though
  the owning skills (`architecture`, `conceptual-modelling`, `modelling-conventions`, `project-setup`)
  already exist and are mature — they are simply invisible in the narrative.
- **Stale ownership-table line, confirmed against git history**: `two-tier-methodology.md`'s §5 table
  lists `CD / release | ci-cd-delivery (EPIC-10, future)` — but `meaningfy-release` was added to the
  catalogue the **same day** as the "two-tier methodology canon" doc itself (2026-06-18), and
  `ci-cd-delivery` already exists too. This line is simply wrong and should cite the real, existing
  owners (`ci-cd-delivery` for CD, `meaningfy-release` for the release lifecycle,
  `meaningfy-git-workflow` for branch/commit/PR mechanics).
- **`dod-quality-gates.md` currently blends engagement gates and build-tier DoD in one file by an
  explicit past decision** (the file cites "Q8.2=A": "so the hand-off from selling to building is a
  single, legible sequence"). **The human wants this reversed** — engagement gates and the
  "Commercial layer — TODO" block (today duplicated near-verbatim in both `dod-quality-gates.md` and
  `docs/engagement/README.md`) should move fully into `docs/engagement/`, leaving
  `dod-quality-gates.md` as pure build-tier DoD, extended with the Builder/Shipper dual-DoD at
  Delivery & Release (see §4 above).
- No live file outside `docs/ai-coding/` itself links to the v1 files (checked); only archived
  historical planning docs reference them, which is fine to leave alone. Deleting v1 is a clean,
  same-day change once the diagram/table are adapted and ported into the successor.

---

## §8. This change's slice of the five-epic split (verbatim)

> Ordered by real dependency; each item names its change-id, its bet, and what it explicitly does
> **not** cover (the other four epics own those pieces — cite, don't restate).

3. **`define-delivery-release-lifecycle`** — Restructure `dod-quality-gates.md`: remove engagement
   gates + commercial-TODO (moves to epic 1's output — cite, don't restate), add the Builder/Shipper
   dual-DoD Delivery & Release lane (§4), fix the stale ownership-table line (§7). Depends on epics 1
   and 2 conceptually — shape now anyway, note the dependency rather than blocking.

The four sibling changes, for citation only (their content is **not** reproduced here):
`define-blc-engagement-model` (1), `define-meaningfy-lifecycle` (2), `define-roles-and-raci` (4),
`define-lifecycle-playbooks` (5). Parked and explicitly not shaped now: **MDLC-standalone** — an
ontology/application-profile development methodology skill (synthesis §3), real new skill-authorship
with its own shaping cycle later.

**Scope discipline that applies to all five (verbatim):** this round of work is **shaping only** —
produce `proposal.md` (the Shape-Up bet: Appetite / Why / Solution outline / Key decisions /
Rabbit-holes / No-gos / What Changes / Capabilities / Impact) per
`openspec/schemas/meaningfy/templates/proposal.md`. Do **not** derive `design.md`/`tasks.md` (the
PLAN), do **not** implement, do **not** edit any file outside `openspec/changes/<id>/`. No new skills,
no new agent stubs, in any of the five.
