# Seed: BLC/SDLC redefinition brainstorm — the slice that feeds this change

**Type:** secondary seed input (per `epic-planning` §Seed intake — **preserved, never groomed**).
**Provenance:** distilled record of a long `/opsx:explore` session between Claude Code and Eugeniu
Costetchi (2026-07-25) auditing `docs/ai-coding/`, `docs/engagement/`, `docs/engineering-standards/`,
`docs/philosophy/` and the 23-skill catalogue. The full synthesis seeded five parallel EPICs; this
file archives the sections that feed **`define-meaningfy-lifecycle`** — §1 (why the work exists +
terminology ground rules), §3 (the planes model, for context on where MDLC-lite sits), §4 (the two
bridge ambiguities, resolved), §7 (the v1/v2 doc audit — the direct input), and the §8 slice that
fixes this epic's boundaries against its four siblings.

**Deliberately excluded** (owned by sibling epics — cite, do not restate here):
synthesis §2 (the corrected commercial model) → `define-blc-engagement-model`;
§5 (the five roles) and §6 (the draft RACI) → `define-roles-and-raci`;
the Delivery & Release DoD restructuring → `define-delivery-release-lifecycle`;
the integrative big-picture doc and per-role playbooks → `define-lifecycle-playbooks`.

**Sibling seed in this folder:** [`handover-analysis.md`](handover-analysis.md) — the earlier
cross-repo audit that first asked "where is the Meaningfy SDLC actually defined?". Both seeds stand;
neither is groomed.

**Ground rule carried over from the synthesis:** whoever shapes from this seed does **not** ask the
human anything. Every open point is flagged "OPEN"; where one is hit, make the most reasonable
well-reasoned call and record it as a `DEC-` decision or in Rabbit-holes/No-gos.

---

## §1. Why this work exists (verbatim from the synthesis)

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

## §3. The "planes" model — SDLC / MDLC / CBLC (verbatim; context for MDLC-lite)

A build contract (P2) doesn't traverse one fixed path; it **picks one or more of three planes**,
depending on which service line was sold:

```
        ┌───────────────────────┬───────────────────────┬───────────────────────┐
        ▼                       ▼                       ▼
   SDLC plane              MDLC plane              CBLC plane
   software build      ontology/model dev,      training, docs,
                        standalone methodology    handbooks, teaching
   Req&UC(deep)          Req&UC(deep)             scoped like any
   → ADLC → MDLC-lite    → ontology                other engagement;
   → setup → Epic loop     methodology              reuses technical-writing /
   (all skills exist       ⚠ NO OWNING SKILL         explanatory-writing /
    today)                  TODAY — real gap          writing-antipatterns
```

- **SDLC plane** — software build. This is the plane that today's `two-tier-methodology.md` mostly
  describes, but under-illustrates. Everything it needs already exists as skills.
- **MDLC — two very different scales, do not conflate them:**
  - **MDLC-lite** (inside a software contract): domain + technical modelling using LinkML/UML at
    software-project scope, generating typed artefacts. Already fully covered by
    `conceptual-modelling` + `linkml-engineering`, cross-checked by `modelling-conventions`
    ("review this model for smells" — vocabulary consistency, missing/conflated/redundant/YAGNI
    concepts). This is legitimately **part of SDLC**, sold inside software-development contracts,
    not ontology contracts.
  - **MDLC-standalone** (its own contract): developing models, application profiles, and ontologies
    as a project in its own right, using a proper ontology-development methodology (e.g.
    METHONTOLOGY/NeOn/DILIGENT-style). **The human states plainly: "skills are still missing to
    support this."** This is a genuine capability gap, not a doc-wiring problem.
    **`conceptual-modelling`'s own SKILL.md already says it is "provisional pending the first-engagement
    gate"** and is explicitly scoped to "product-development (programming) projects" — it
    deliberately does not claim to own the standalone-ontology-methodology case.
    **This gap is explicitly OUT OF SCOPE for the five epics being shaped now** — it is parked as a
    future, separately-shaped EPIC ("MDLC-standalone: ontology/application-profile development
    methodology skill" — large, its own shaping cycle). Do not attempt to close it in any of the five
    epics below; only *name* it as a known gap where relevant (e.g. in the ownership-table fix).
- **CBLC (Capacity Building Life Cycle)** — same two-scale shape as MDLC:
  - **CBLC-lite** (reused inside any plane): producing documentation, handbooks, explanatory
    material for whatever was built. Already fully covered by `technical-writing`,
    `explanatory-writing`, `writing-antipatterns` (all in the `meaningfy-core` bundle — usable by
    anyone already).
  - **CBLC-standalone** (its own contract): training/teaching/documentation sold as the entire
    engagement. This is **new framing, not new skill-building** — the writing skills already exist;
    what's missing is naming it as a recognised, sellable service line (a service-packaging /
    `proposal-writing` concern, not a new skill).

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

> **Boundary for this change:** the Requirements & UC resolution is *this* epic's to land in the
> build-plane doc. The Delivery & Release dual-DoD is `define-delivery-release-lifecycle`'s to land
> in `dod-quality-gates.md`; it is reproduced above only as context so the build-plane doc can point
> at it correctly instead of restating it.

---

## §7. v1 / v2 doc findings (verbatim — the direct input to this change)

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

## §8 slice — this epic's place among the five (verbatim entry + sibling boundaries)

> 2. **`define-meaningfy-lifecycle`** *(existing change folder — already has
>    `inputs/handover-analysis.md` from an earlier audit; preserve it, add this seed alongside it, do
>    not delete or groom it)* — Retire v1, rewrite `two-tier-methodology.md` with the ADLC/MDLC-lite
>    steps named and cited, resolve Requirements & UC (§4). Does not touch delivery/release content
>    (that's epic 3) or engagement/commercial content (that's epic 1) — note the split explicitly,
>    cite rather than restate.

The four siblings, for citation (their content is theirs, not restated here):

1. **`define-blc-engagement-model`** — `docs/engagement/README.md` + `phases.md` +
   `semantic-consulting-coach/references/engagement-model.md`, for the corrected commercial model
   (synthesis §2). Does not touch `docs/ai-coding/`.
3. **`define-delivery-release-lifecycle`** — restructures `dod-quality-gates.md`: engagement gates +
   commercial TODO out, Builder/Shipper dual-DoD lane in, stale ownership-table line fixed.
   Conceptually depends on epics 1 and 2.
4. **`define-roles-and-raci`** — the five roles (synthesis §5) + the RACI matrix (§6), including the
   Work-Shaper ambiguity and the agent-wrapper fork, both left deliberately open.
5. **`define-lifecycle-playbooks`** — the integrative big-picture flow doc plus one short per-role
   playbook, each a filtered view. Avoids "canon" in any title; picks its own umbrella name.

**Parked, explicitly not one of the five:** MDLC-standalone — an ontology/application-profile
development methodology skill (§3). Real new skill-authorship, its own shaping cycle later.

**Scope discipline that applies to all five:** this round is **shaping only** — produce
`proposal.md` per `openspec/schemas/meaningfy/templates/proposal.md`. Do **not** derive
`design.md`/`tasks.md`, do **not** implement, do **not** edit any file outside
`openspec/changes/<id>/`. No new skills, no new agent stubs, in any of the five.
