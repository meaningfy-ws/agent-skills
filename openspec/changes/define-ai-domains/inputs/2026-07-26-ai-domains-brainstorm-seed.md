# Seed — the `ai-*` domain reframe (2026-07-26)

Captured from a live conversation with the company owner, immediately after `define-blc-engagement-model`,
`define-meaningfy-lifecycle`, `define-delivery-release-lifecycle`, `define-roles-and-raci`, and
`define-lifecycle-playbooks` had all landed for real, followed by a critical review pass and a
restructure (`docs/engagement/` retired into `docs/how-we-work/`, a `docs/services/` catalogue added,
a writing-antipatterns/explanatory-writing audit and fix pass). This seed is preserved verbatim as
context, never groomed — the EPIC shaped from it does the deciding.

## The reframe, in the owner's words (paraphrased from the live exchange)

> "ai-coding and how we work/build seem to run in parallel rather than side by side. Better to
> eliminate the 'how we work' layer and integrate ai-coding with the building part, and probably all
> the playbooks shall stay in one place together; the list of services are described from the
> business POV so they belong to business framing; I am missing a sort of opsx-runbook for semantic
> web-consulting and advisory part that is more business like."
>
> "What is the difference between playbook and runbook? They seem awfully similar, need a better
> differentiation vocabulary."
>
> "The openspec setup guide seems to be drifted, it must be in one place with dual-cli and
> environment setup."
>
> "I understand now, so the ai-coding is in fact how the engineering standards for building are
> applied to the building process. We need somehow to figure out how the ai-sales apply the
> sales-standards to the business process, and we need ai-consulting to apply the
> advisory/consulting-standards (including data maturity assessment, semantic maturity assessment,
> gap analysis, Wardley map building, or enterprise & process modelling/architecting...) still to
> pre-building-onboarding/advisory/consulting."

Follow-up corrections after a first exploration pass:

- "Technical consultant must focus on consulting, no need for it in sales." — the Technical
  Consultant playbook moves wholly into `ai-consulting`; `ai-sales` keeps only Sales/Presales.
- "Yes each `ai-*` needs a DoD — but where you don't know, mark it so I know what can be extended
  and where." — every domain gets a DoD file; genuine gaps are named, not invented.
- "I like the structure, now perform a deeper analysis on what would be the eventual content, and
  write that into a new epic work shape proposal, so that you can write the new epic and then
  implement." — this is the direct instruction this EPIC executes.

## The pattern named

`ai-coding` is not "the SDLC doc" — it is one instance of a general template: **"[domain]-standards,
applied by AI agents, to the [domain] process."** Three domains exist in how Meaningfy actually
operates, only one of which has documentation today:

1. **`ai-coding`** (exists) — engineering standards applied to the build process.
2. **`ai-sales`** (missing) — sales/commercial standards applied to the business process (presale,
   the Discovery & Onboarding package's *commercial* framing, contracting, repeat clients, the
   services catalogue).
3. **`ai-consulting`** (missing) — advisory/consulting standards applied to the pre-build discovery
   process itself (the *methodology* of the Deep tier: maturity assessment, gap analysis, Wardley
   mapping, enterprise/process modelling).

## Vocabulary proposed and provisionally accepted

- **Runbook** — the one operational script per domain, chronological, cross-role: "here's the whole
  flow, step by step, regardless of who does which step."
- **Playbook** — a role-filtered lens on that same runbook: "you're role X, here's your slice."
  Many playbooks per domain, one runbook.

## Target shape sketched in the exploration turn (not yet a decision — the EPIC decides)

```
docs/
  ai-coding/            (existing, tightened — work-shaper.md joins its playbooks/)
  ai-sales/             (new — commercial process; services/ moves here, business-framed)
  ai-consulting/        (new — the advisory methodology that's missing today)
  roles-and-raci.md     (stays top-level — genuinely cross-domain)
  environment/          (new cluster — openspec-setup-guide.md, environment-setup.md, dual-cli/)
```
`docs/how-we-work/` retires entirely once its content is redistributed.

## Research findings from this seed's own follow-up investigation (evidence, not decisions)

- **Gap analysis** is already real and owned: `decision-package`'s discovery flow (step 3,
  `skills/decision-package/references/discovery-flow.md` lines 39-51) compares current state against
  strategic ambition and produces a ranked gap map (Blocking / Sequenced / Out of scope). Cite it;
  do not duplicate it.
- **Data & semantic maturity assessment is a documented self-contradiction today**:
  `docs/how-we-work/business/discovery-and-onboarding.md` promises a "semantic & data maturity
  assessment" as a Deep-tier deliverable, while `decision-package/SKILL.md` and its
  `discovery-flow.md` state — twice — that the Deep-tier flow is explicitly **not** a maturity
  assessment. The preserved seeds (`decission-phase-advisory.md`, `presales-material.md`) repeat the
  same disclaimer a further three times. No skill anywhere performs a maturity assessment. This EPIC
  must resolve the contradiction, not just relocate the promise.
- **Wardley mapping**: a clean, uncontested gap — zero repo-wide hits.
- **Enterprise & process modelling as a client-facing discovery technique**: missing. `architecture`
  owns BPMN/ArchiMate but scoped to modelling *what Meaningfy builds*, not the client's existing
  AS-IS organisational landscape. `conceptual-modelling` is scoped to product-development projects
  only.
- **The Shipper's DoD in `docs/ai-coding/dod-quality-gates.md` (lines 54-72) is not cleanly
  relocatable in one piece**: the DoD definition itself (lines 54-64) is commercial-plane and could
  move to an `ai-sales` DoD file, but the Disagreement rule (lines 69-72) explicitly states it
  governs **both** DoDs and is stated once, canonically, in that file — moving it would either
  duplicate it or orphan the Builder-side half. The EPIC should keep the Disagreement rule canonical
  in `dod-quality-gates.md`, with any `ai-sales` DoD citing it rather than inheriting a copy.
- **Technical Consultant's current playbook** (`docs/how-we-work/business/playbooks/technical-consultant.md`,
  48 lines) is already entirely consulting/methodology work (Discovery & Onboarding assessment,
  Decision Package production) — it was homed under `business/` only because Discovery & Onboarding
  lived there, not because its content is commercial. A straight relocation, not a split.
- **`docs/dual-cli/`** is a real existing folder (`README.md`, `setup-claude.md`, `setup-opencode.md`,
  `mcp-setup.md`, `mapping.md`, `compatibility.md`, `body-agnosticism-audit.md`) — the environment
  cluster the owner wants `openspec-setup-guide.md` and `environment-setup.md` co-located with
  already exists; the question is exact placement/naming, not creation from nothing.
