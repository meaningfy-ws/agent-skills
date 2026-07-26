# Seed (secondary, never groomed) — BLC/SDLC redefinition brainstorming synthesis

**Archived:** 2026-07-25 · **Change:** `define-lifecycle-playbooks` (epic 5 of 5) ·
**Status:** secondary input — preserved verbatim, never deleted or groomed. The shaped EPIC
(`../proposal.md`) supersedes it as the primary truth but does not replace it.

**Why the full document is archived here** (and not just the excerpt): this epic is the synthesis
layer over the other four — its deliverables are an end-to-end "big picture" doc and one filtered
per-role playbook, so every section below (§2 commercial funnel, §3 planes, §4 bridge resolutions,
§5 roles, §6 RACI, §7 doc findings, §8 epic split) is directly load-bearing for it.

The verbatim synthesis follows.

---

# Meaningfy BLC/SDLC redefinition — brainstorming synthesis

**Source:** a long `/opsx:explore` session between Claude Code and Eugeniu Costetchi (2026-07-25),
auditing `docs/ai-coding/`, `docs/engagement/`, `docs/engineering-standards/`, `docs/philosophy/`,
and the 23-skill catalogue. This document is the distilled record of every decision made in that
session. It is a **seed**, not a shaped EPIC — archive it verbatim (or the relevant excerpt) into
each change's `inputs/`, then shape the EPIC from it. Do not silently drop any decision below; if
you disagree with one, flag it in the proposal's Key Decisions / Rabbit-holes rather than overriding
it unilaterally — the human already made these calls across five conversational rounds.

**Ground rule for whoever shapes from this seed: do not ask the user anything.** Every open point
below is explicitly flagged as "OPEN" — where you hit one, make the most reasonable, well-reasoned
call and record it as a `DEC-` decision or in Rabbit-holes/No-gos, with your reasoning. Never block
on human input; the human has explicitly asked for autonomous shaping this round.

---

## 1. Why this work exists

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

## 2. The corrected commercial model (free/paid boundary)

**Correction, stated directly by the human: "nothing is free, only presale work is free, which is
mainly business and relationship building."** This revises `docs/engagement/phases.md`'s stated
"orientation is free" spine rule — that rule was wrong as previously written.

The corrected funnel:

```
PRESALE (free)              →  P0-advisory (paid, 1-2d)  →  P1 Decision (paid, 4-6wk)  →  direct-to-build
relationship/qualification     short orientation product     roadmap + Decision Package    (skip hand-holding
only — "is this relevant?"                                                                   entirely — precise
no deliverable                                                                                ask, straight to
                                                                                                a build contract)
```

- **Presale** — free, bounded, relationship-building and qualification only. No deliverable. This is
  the *only* free thing in the model.
- **P0-advisory** — a **new, paid, short (1-2 day) product** — a named, sellable orientation package.
  Distinct from presale. (This directly answers the existing "Service packaging — how P0–P3 bundle
  into named, sellable offers" TODO already flagged in `docs/engagement/README.md`.)
- **P1 Decision** — unchanged in spirit from today's docs: paid, 4-6 weeks, produces a strategic
  roadmap, data-governance recommendations, semantic-layer architecture sketch, etc. — assessments
  and documents, no building yet. Deliverable: the Decision Package.
- **Direct-to-build** — a client who already knows exactly what they want can skip all hand-holding
  and go straight to a build contract. Today's docs don't allow this path at all ("P2 valid only
  once P1 is complete") — that constraint is now wrong and should be relaxed.
- **P2 — a separate, later contract** for actual delivery. Not monolithic "software build" — it is a
  **family of possible service-line contracts**: (a) ontology/model development, (b) software
  development, (c) teaching/training. A client buys one (or more) of these as its own engagement.
- **Partnership is NOT a phase/stage.** It is a **status label** that attaches to a client relationship
  once they have closed **≥2 contracts** with Meaningfy. It can be true concurrently with any future
  P0/P1/P2 engagement — it does not come "after" P2 in sequence. The existing `docs/engagement/`
  framing of P3 as a fourth sequential phase is wrong; the *content* that was going to live in "P3"
  (governance support, semantic-ops, capability building) is still real, but it's better understood
  as **the kind of work an executive-communication-led relationship does with a Partner-labelled
  client**, not a lifecycle stage everyone passes through.
- Owner of the partnership/account-nurture work: the human explicitly named `executive-communication`
  as its natural owner ("partnership is still part of the business/commercial layer, and is for the
  executive communicators").

---

## 3. The "planes" model — SDLC / MDLC / CBLC

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

## 4. The two "bridge" ambiguities — resolved

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

---

## 5. The five roles

Defined and refined across the session; treat these as decided, not draft:

1. **Sales / Presales** — owns presale relationship-building and qualification (free), leads P0-advisory
   and P1 Decision commercially, and leads partnership/account nurture once a client is Partner-labelled.
2. **Technical Consultant** — involved in **assessment and Decision-Package development and strategic
   advisory on data governance and management** (this is the human's own, narrower, corrected
   description — not primarily a "requirements bridge" role as first guessed; it is P0/P1-centric).
3. **Solution Architect** — leads ADLC (architecture: ADRs, C4, UC White/Blue) and MDLC-lite
   (domain/technical modelling within a software contract).
4. **Solution Builder** — leads Project/repo setup and the SDLC Epic loop (shape → PLAN → clarity-gate
   → BDD → TDD → review → archive); accountable for Epic/architecture-spec conformance at delivery.
5. **Solution Shipper** — **"like a PM, but adapted to Shape-Up methodology, responsible for delivering
   to the client what the client requested (ideally a bit more, to make the client happy)."**
   Accountable for contract/client-requirement conformance at delivery — the BLC-plane delivery role.

**"Work Shaper" is deliberately NOT a sixth role.** The human flagged this ambiguity explicitly and
it should stay an acknowledged, documented ambiguity rather than be forced into a fixed owner:
turning a decided scope into Epics/changes is sometimes the Architect's work (shaping architecture),
sometimes the Builder's (turning architecture into work shapes), and — depending on the type of
contract — could equally be led by a future modelling-lead (MDLC-standalone) or training-lead (CBLC).
Document the conflation as real and useful to keep visible, not as a gap to close.

**Open fork, explicitly unresolved, flag but do not decide:** whether any of these roles beyond
Solution Builder ever gets a dedicated Claude Code **agent** wrapper (today only `epic-planner`,
`implementer`, `code-reviewer` exist, all Builder/Architect-adjacent). Default recommendation from
the session: **documentation-only for now** — describe the role and the skills it draws on; treat
"does this role need its own agent" as a separate, later decision once the role has actually been
exercised. Do not create new agent stubs in any of these five epics.

---

## 6. Draft RACI (from the session — treat as a strong draft, not gospel; refine when shaping)

| Activity | Sales/Presales | Tech Consultant | Solution Architect | Solution Builder | Solution Shipper |
|---|---|---|---|---|---|
| Presale / P0-advisory / P1 sales & advisory | A/R | R | C | – | – |
| Requirements & UC (via P1, shallow) | C | R | I | – | – |
| Requirements & UC (via P2, deep) | I | C | A/R | C | – |
| ADLC — architecture | I | C | A/R | C | – |
| MDLC-lite (within SDLC) | – | – | A | R | – |
| MDLC standalone (ontology methodology) | C | C | A *(no skill yet — gap)* | – | – |
| Project/repo setup | – | – | C | A/R | – |
| Epic / work shaping | – | – | C¹ | A/R¹ | C |
| Epic build (TDD/BDD) | – | – | C | A/R | I |
| Review | – | – | C | R | A |
| Release & deploy | – | – | – | R | A |
| Contract-conformance check | I | C | – | C | A/R |
| CBLC (training/docs) | C *(if sold standalone)* | C | C | R | I |
| Partnership / account nurture | A/R | C | – | – | I |

¹ deliberately role-fluid — see the Work-Shaper note in §5.

---

## 7. v1 / v2 doc findings (from the earlier audit — still valid, feed Epic B directly)

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

## 8. The five epics being shaped now (do not exceed this scope)

Ordered by real dependency; each item names its change-id, its bet, and what it explicitly does
**not** cover (the other four epics own those pieces — cite, don't restate).

1. **`define-blc-engagement-model`** — Rewrite `docs/engagement/README.md` + `phases.md` and
   `semantic-consulting-coach/references/engagement-model.md` for the corrected commercial model
   (§2). Does not touch `docs/ai-coding/`.
2. **`define-meaningfy-lifecycle`** *(existing change folder — already has
   `inputs/handover-analysis.md` from an earlier audit; preserve it, add this seed alongside it, do
   not delete or groom it)* — Retire v1, rewrite `two-tier-methodology.md` with the ADLC/MDLC-lite
   steps named and cited, resolve Requirements & UC (§4). Does not touch delivery/release content
   (that's epic 3) or engagement/commercial content (that's epic 1) — note the split explicitly,
   cite rather than restate.
3. **`define-delivery-release-lifecycle`** — Restructure `dod-quality-gates.md`: remove engagement
   gates + commercial-TODO (moves to epic 1's output — cite, don't restate), add the Builder/Shipper
   dual-DoD Delivery & Release lane (§4), fix the stale ownership-table line (§7). Depends on epics 1
   and 2 conceptually — shape now anyway, note the dependency rather than blocking.
4. **`define-roles-and-raci`** — New doc(s) defining the five roles (§5) and the RACI matrix (§6),
   including the Work-Shaper ambiguity and the agent-wrapper fork, both documented as deliberate
   open points, not resolved. Cross-cutting; depends on 1-3 conceptually but shape now from this seed.
5. **`define-lifecycle-playbooks`** — New synthesis doc(s): one integrative "big picture" flow doc
   plus one short playbook per role (§5), each a filtered view. Naturally the last-consumed epic;
   shape its proposal now from this seed regardless. Avoid "canon" in any title (§1); candidate
   umbrella names surfaced in-session: "How We Work", "Meaningfy Delivery Model", "Meaningfy
   Lifecycle Guide" — pick one, record it as a `DEC-`, don't leave it a placeholder.

**Parked, explicitly not one of the five, do not shape it now:**
6. MDLC-standalone — an ontology/application-profile development methodology skill (§3). Real new
   skill-authorship, its own shaping cycle later.

**Scope discipline that applies to all five:** this round of work is **shaping only** — produce
`proposal.md` (the Shape-Up bet: Appetite / Why / Solution outline / Key decisions / Rabbit-holes /
No-gos / What Changes / Capabilities / Impact) per
`openspec/schemas/meaningfy/templates/proposal.md`. Do **not** derive `design.md`/`tasks.md` (the
PLAN), do **not** implement, do **not** edit any file outside `openspec/changes/<id>/`. No new skills,
no new agent stubs, in any of the five.

---

## Q&A record for this change (epic 5)

No live Q&A round was held for this epic: the shaping instruction was explicitly **autonomous — do
not ask the user anything**. Every ambiguity encountered while shaping was resolved from the seed
above and recorded as a `DEC-` in `../proposal.md`, or parked in its Rabbit-holes / No-gos. The
points the seed left open and how this epic disposed of them:

| Seed open point | Disposition in `../proposal.md` |
|---|---|
| Umbrella name (three candidates, §8) | Decided — `DEC-1` |
| Document paths ("paths are your call") | Decided — `DEC-2` |
| Work-Shaper ownership ambiguity (§5) | Kept visible, not closed — `DEC-9` |
| Agent-wrapper fork (§5) | Left open by design — No-gos |
| MDLC-standalone gap (§3) | Named in one line, not closed — `DEC-11`, Rabbit-holes |
| RACI is "a strong draft, not gospel" (§6) | Not re-litigated here; epic 4 owns it — `DEC-3`, No-gos |
