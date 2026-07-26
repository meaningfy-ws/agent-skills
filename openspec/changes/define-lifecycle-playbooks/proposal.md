# EPIC: How We Work — the end-to-end flow doc plus one playbook per role

> **Golden-thread parents.** This EPIC derives from:
>
> - the archived brainstorming synthesis
>   [`inputs/2026-07-25-brainstorm-seed.md`](inputs/2026-07-25-brainstorm-seed.md) (§2 commercial
>   model, §3 planes, §4 bridge resolutions, §5 roles, §7 doc findings, §8 epic 5);
> - the *Employee Handbook — Second Edition (2026)* PDF in this change's `inputs/` folder (not
>   linked directly — its filename's parentheses break this repo's markdown-link checker),
>   §*Role structure* / §*Brief: what are the project roles?* / §*Allegory: what are the project
>   roles?* (pp. 65-70) — the primary source that Meaningfy already names **six** project roles,
>   including *Project Owner — the Work Shaper*, and the source of that role's mandate (`DEC-9`);
> - [`inputs/decission-phase-advisory.md`](inputs/decission-phase-advisory.md) — the P1 Decision-Phase
>   operational definition, internal posture, and client-facing narrative (relevant here only as the
>   evidence that a P0-advisory/presales description is a real, currently-missing document —
>   *Known gaps*, owned by epic 1);
> - [`inputs/presales-material.md`](inputs/presales-material.md) — the pre-LLM-agent phase sheet and
>   discovery checklist, same status: evidence of a gap epic 1 owns, not content this EPIC ports;
> - the four sibling EPICs it synthesises: `define-blc-engagement-model` (1),
>   `define-meaningfy-lifecycle` (2), `define-delivery-release-lifecycle` (3),
>   `define-roles-and-raci` (4).
>
> It **owns no lifecycle content of its own** — it is the map over theirs. Seed §8 names it the
> last-consumed of the five; `DEC-10` makes that a sequencing constraint, not a preference.
>
> **Re-shape note (2026-07-26).** This is round 2 of shaping. New source material (the Employee
> Handbook) invalidated part of the round-1 bet: `DEC-9` and `DEC-13` are **reversed**, logged in
> place rather than silently rewritten. Everything else stands.

## Appetite

**Small.** Seven short documents (one flow doc, six one-page playbooks), one capability spec, and a
handful of additive link lines. No new skills, no new agents, no tooling, no generation pipeline.
The budget is deliberately tight because every fact these docs state must already exist in an epic
1-4 output — writing them is composition and link-work, not authorship. If a playbook cannot be
written without inventing a rule, that is a defect in epic 1-4's output, not a reason to spend more
here.

The sixth playbook (`DEC-9`) does not move the appetite: it is one more file on the fixed template
of `DEC-5`, against a role epic 4 defines. What *would* have broken Small is the per-plane diagram
set — deliberately deferred, see *Known gaps*.

## Why

The corrected model (seed §2-§5) is legible only to someone who reads four separate documents and
holds the whole thing in their head: the commercial funnel lives in `docs/engagement/`, the build
loop in `docs/ai-coding/two-tier-methodology.md`, the dual delivery DoD in
`docs/ai-coding/dod-quality-gates.md`, and the roles/RACI in a fifth new place. Nobody joining
Meaningfy — and no agent orienting itself — has an entry point that shows presale → P0-advisory →
P1 → P2 service-line contract → Delivery & Release → repeat-client relationship as one continuous
flow, and nobody has a view filtered to *their own* role: which stages they touch, which skills they
invoke, who hands work to them and to whom they hand it on. The v1 documentation had exactly one
artifact that did this job well (a lifecycle diagram plus a responsibility table, seed §7); v2
dropped it and replaced it with nothing. This EPIC restores that entry point against the corrected
model.

The Employee Handbook is the second half of the same problem. It carries real, good operating
wisdom — six named project roles with concrete mandates — written for a pre-LLM-agent, human-only
team. Nothing in today's `docs/` reflects it, and nothing in the handbook reflects today's way of
working (people govern, steer, and check lightly; agents do the heavy work). This EPIC is where the
role-level half of that wisdom lands, as playbooks; epic 4 is where the role definitions themselves
land.

## Solution outline

One folder, `docs/how-we-work/`, containing a **map** and six **filtered views** of it.

The map (`README.md`) tells the whole story once, in Explanation register, in one screen plus one
diagram: the funnel with its free/paid boundary, the three entry points into a build contract
(from P1, from P0-advisory, or direct-to-build), the three planes a P2 contract can pick (SDLC,
MDLC, CBLC), the Work Shaper authoring the Epic-shaping step, the paired Builder/Shipper close at
Delivery & Release, and the repeat-client relationship as a property of the relationship rather than
a stage anyone passes through. Every normative claim in it is a deep link to the epic 1-4 output
that owns that claim; the map's own prose carries only sequence, transitions, and the shape of the
whole. It closes with a short, honest **Known gaps** section (`DEC-16`) so a reader can tell what is
missing on purpose from what is missing by oversight.

The six playbooks are the same flow read from one seat. Each answers four questions in a fixed
order — the stages you touch, the skills you invoke at each, who hands off to you, who you hand off
to — and ends at the role's own definition of done. They are How-to register, one page, no
narrative.

The outcome to judge this against: a new Solution Shipper can read one page and know what they are
accountable for and where to look next, without reading the engagement model, the build methodology,
or the RACI matrix end to end first. And the reader who *does* want the whole picture reaches it
from the repository README in one hop.

## Key decisions

- **DEC-1**: The umbrella name is **"How We Work"**. Rejected: *"canon"* in any form — the human
  retired the word as ambiguous (seed §1). Rejected *"Meaningfy Delivery Model"* — the doc's span
  starts at free presale relationship-building, which is not delivery; naming the whole after its
  last third would mislead exactly the newcomer it is written for. Rejected *"Meaningfy Lifecycle
  Guide"* — "lifecycle" is already carrying five distinct referents in this vocabulary (BLC, SDLC,
  MDLC, CBLC, ADLC) and epic 2's change id `define-meaningfy-lifecycle` already claims that phrase
  for the build-tier methodology; reusing it at the umbrella level re-creates the naming collision
  this whole round is fixing. "How We Work" is plain, contains no term of art, reads as an entry
  point rather than a specification, and works as both a title and a directory name.
- **DEC-2**: Paths are `docs/how-we-work/README.md` (the map) and
  `docs/how-we-work/playbooks/<role>.md` — six files: `sales-presales.md`,
  `technical-consultant.md`, `work-shaper.md`, `solution-architect.md`, `solution-builder.md`,
  `solution-shipper.md`. One folder, sibling to `docs/engagement/` and `docs/ai-coding/`, because
  the map spans both and belongs to neither. Playbooks sit with the flow they filter, **not** with
  epic 4's role definitions — a playbook is a view of the lifecycle, the role definition is a view
  of the organisation, and co-locating them would invite the two to merge.
- **DEC-3**: **Map, not source.** Zero normative statements originate in this folder. Every rule,
  gate, threshold, phase duration, price boundary, role definition, and RACI cell is a deep link to
  the epic 1-4 output that owns it. This is the repo's standing single-source-of-authority rule
  (`AGENTS.md`) applied to a synthesis doc, and it is the only thing that keeps seven new files from
  becoming seven new places to go stale. Operationally: if a sentence here would still be true after
  deleting the target it links to, it is a duplication and must be cut or replaced by the link.
- **DEC-4**: **One diagram, Mermaid, in the map only.** It renders the funnel, the three P2 entry
  paths, the three planes, the Epic-shaping step **with the Work Shaper named on it as its author**
  (`DEC-9` — the step is owned, not floating), and the paired delivery close. Seed §7 records that
  v2 regressed to zero diagrams from a v1 that had a good one; this restores the capability without
  porting v1's content (which predates the EPIC/PLAN split and the current agent roster). Mermaid
  because it renders on GitHub with no build step. Playbooks get no diagrams — a one-page filtered
  view that needs a diagram is too long. Per-plane diagrams are out of scope this round — see
  *Known gaps*.
- **DEC-5**: **Fixed playbook template**, identical headings in all six: *Your stages* → *Skills
  you invoke* → *Handed to you by* → *You hand off to* → *Your done*. Identical structure is what
  makes six documents comparable at a glance and what makes a coverage gap visible (an empty
  section is a real finding about the role, not a formatting lapse). Hard cap: one screen of prose
  plus tables, roughly 120 lines — a playbook that outgrows the cap is duplicating its targets,
  which DEC-3 forbids.
- **DEC-6**: The **repeat-client relationship is drawn as an annotation on the client, not a node in
  the sequence** (seed §2). The diagram has no P3 box and no arrow leading into partnership. The
  ≥2-closed-contracts fact is stated once, as a link to epic 1's output; the map's own text says
  only that it can hold concurrently with any live engagement. Whether epic 1 keeps a capitalised
  "Partner" label or states the plain fact is epic 1's call — the map links to whatever it lands on
  and mints no vocabulary of its own.
- **DEC-7**: **Delivery & Release renders as two parallel lanes converging on one gate** (seed §4) —
  Builder on the SDLC plane (conformance to EPIC + architecture), Shipper on the BLC plane
  (conformance to contract + client requirement) — never as two sequential steps, and never with one
  lane subordinate to the other. The gate criteria themselves are epic 3's (Builder DoD) and epic
  1's (Shipper DoD, relocated to `docs/engagement/` this round); the map shows the shape and links
  to each where it actually lives.
- **DEC-8**: **Requirements & UC renders as one capability invoked at two depths, not a stage box**
  (seed §4): shallow (UC White) when feeding a P1 Decision, deep (White + Blue) when feeding
  architecture — whether handed over from a completed P1 or performed for the first time on a
  direct-to-build entry. The diagram attaches depth to the arrow, not to a box, so no reader infers
  a pipeline stage that does not exist.
- **DEC-9** *(reverses the round-1 DEC-9, "the Work-Shaper conflation stays visible and unowned")*:
  **Work Shaper is a real role and gets its own playbook**, `docs/how-we-work/playbooks/work-shaper.md`.
  The reversal is evidence-driven: the Employee Handbook (2nd ed. 2026, p. 66, *"Project Owner — the
  Work Shaper"*) shows the role already exists in Meaningfy's own operating documentation with a
  concrete mandate — develop the Work Breakdown Structure from the request-for-offer, the offer and
  the client meeting notes; establish the project roadmap; **write the Epic Pitches on Shape-Up
  methodology**; identify risks and mitigations; guide the project from inception to delivery;
  discover work with the Builders as it emerges and map Epic scope into User Stories. Round 1 read
  the absence of a named owner as an ambiguity worth preserving; it was simply a source we had not
  read. Consequences here:
  - The role's *definition* is epic 4's to write (it adds Work Shaper as a sixth role this round);
    this EPIC adds the matching playbook because `DEC-15`'s coverage invariant is bidirectional —
    six roles means six playbooks, and no playbook may exist without a role.
  - The playbook's content seed is the handbook mandate above, adapted to today's way of working:
    the Work Shaper is the human who owns and steers `epic-planning` (and its `epic-planner` agent
    counterpart, which already does most of the mechanical work), governing and checking rather than
    hand-writing every artifact.
  - Positioning: `define-roles-and-raci`'s DEC-13 is the authoritative source for how Work Shaper
    relates to Solution Architect and Solution Builder — including the human's own "skill-wise
    between Architect and Builder, leaning Builder" framing — and this playbook **cites that
    boundary rather than restating it** (DEC-3's pointer discipline applies to role positioning the
    same way it applies to gates and thresholds). The playbook itself states only the operational
    consequence: the Work Shaper thinks the work through ahead of building, plans it, and makes the
    consequential scoping decisions before the Builder starts.
  - The artifacts differ by plane — an Epic pitch for a software build, for an ontology/model
    project, or for a training/materials engagement — same role, different plane, exactly as Builder
    varies by plane. The playbook states this in one line and links to epic 4 for the rule.
  - The Solution Architect and Solution Builder playbooks each keep **one short line** noting they
    consult during Epic shaping (`C`, per epic 4's RACI). That is documented collaboration, not the
    unresolved conflation round 1 described; the conflation is resolved.
- **DEC-10**: **This EPIC is implemented last of the five.** Its readiness condition is that the
  four sibling changes' documents have landed on `develop` — because DEC-3 leaves this folder with
  nothing to say on its own, and links written against unmerged siblings would break the repo's
  `broken_links` lint gate. Shaping happens now (this proposal); implementation waits. The
  dependency is on the siblings' **content existing on `develop`**, not on which epic is shaped
  first — epic 4 being re-shaped in the same round as this one changes nothing about the constraint.
  If a sibling epic is descoped, this EPIC is re-shaped rather than patched around it.
- **DEC-11**: **Named gaps stay named, not filled.** The plane diagram marks the MDLC-standalone
  plane as having no owning methodology skill today (seed §3, parked as a separate future EPIC), in
  one line, with no attempt at guidance. CBLC-standalone is drawn as a real, sellable plane — the
  writing skills that serve it already exist; only the service-line framing was missing.
- **DEC-12**: **Register is fixed per document type**, per the genre map in `writing-antipatterns`:
  the map is Explanation (it exists to make a reader understand a shape), the playbooks are How-to
  (they exist to let a reader act). This is decided up front because the failure mode for a
  synthesis doc is drifting into aspirational prose, and for a playbook is drifting into narrative.
  All three writing skills apply and are cited in the PLAN, not `writing-antipatterns` alone:
  `explanatory-writing` governs the map's Explanation prose, `technical-writing` governs the
  playbooks' How-to prose and the tables in both, and `writing-antipatterns` is the genre/smell
  check run over the result.
- **DEC-13** *(reverses the round-1 DEC-13, "exactly five playbooks")*: **Six playbooks, one per
  role in epic 4's corrected role set** — Sales/Presales, Technical Consultant, Work Shaper,
  Solution Architect, Solution Builder, Solution Shipper. Still no client-facing counterpart and no
  per-agent playbook. Two handbook roles deliberately get **no** playbook here because epic 4
  deliberately does not carry them as roles: *Reviewer — the Quality Overseer* (its four-eyes review
  is now largely done by `meaningfy-code-review`, with light human sign-off) and *Customer Success
  Manager* (its aftercare mandate is Sales/Presales' account-nurture activity). Both are named in
  the relevant playbooks as inherited responsibilities, never as absent roles — the adaptation
  rationale itself lives in epic 4 and is linked, not restated. Role-set completeness stays epic 4's
  call; this EPIC tracks it rather than extending it.
- **DEC-14**: **Discoverability edits outside the folder are limited to link lines**: one row in the
  root `README.md` documentation table, and one "start here" link line in each of the four sibling
  outputs. Additive lines only, no content edits, no restructuring. This is safe precisely because
  DEC-10 sequences this EPIC last — the four targets already exist and are stable by then.
- **DEC-15**: The change carries **one capability spec, `lifecycle-playbooks`**, whose requirements
  are the two invariants that can actually rot: every role defined by epic 4's output has exactly one
  playbook (bidirectional — no orphan playbook, no unplaybooked role), and no normative statement
  appears in this folder without the link to its owner (DEC-3). A docs-only change earns a spec only
  when it has enforceable invariants; these two are it. The count of playbooks is **not** written
  into the spec — the invariant is the bidirectional match, so a future seventh role changes the
  folder without changing the spec. (Round 1 hard-coding "five" is precisely what `DEC-13` had to
  reverse.)
- **DEC-16**: **The map carries a short, first-class "Known gaps" section** — one line per gap,
  each saying what is missing and who owns closing it, with no attempt at guidance. This exists so a
  reader can distinguish "deliberately not written yet" from "we forgot", which is the single most
  useful thing a synthesis doc can say about its own edges. It duplicates nothing: each line links
  to the owning epic or names the parked EPIC. The gaps listed are those in this proposal's *Known
  gaps* section below.

## Known gaps

Named here, not closed here. Each one is either owned by a sibling epic, parked as its own EPIC, or
a deliberate deferral of this EPIC's own scope. `DEC-16` mirrors this list, one line each, into the
map itself.

| Gap | Status | Owner |
|---|---|---|
| **Per-plane diagrams** — rich, colourful, self-explanatory diagrams for BLC, SDLC, MDLC, ADLC, CBLC individually, alongside the overview | Deferred, near-term extension | This EPIC's successor |
| **Presales-process description** — a written description of how presale actually runs (and possibly supporting skills) | Named, not authored here | Epic 1 (`define-blc-engagement-model`) |
| **P0-advisory package description** — what that initial paid commercial package contains and how the advisory/consulting is done | Named, not authored here | Epic 1 (`define-blc-engagement-model`) |
| **MDLC-standalone methodology skill** — no owning skill exists for standalone ontology/application-profile development | Parked as a separate future EPIC | Future EPIC (seed §3) |
| **Missing sales/presales skills** — demo preparation, CRM/lead communication, strategic-negotiation practice | Named, not authored here | Epic 1 (its instruction set enumerates them) |
| **Agent wrappers for non-Builder roles** — open fork; Work Shaper is the highest-priority-if-ever case, since `epic-planner` already does most of the work | Open fork, unresolved by design | Epic 4 (`define-roles-and-raci`) |
| **Single-source generation of the playbook set** — if the set outgrows hand-maintenance, a generation decision is needed | Not needed at six files | This EPIC's successor, if triggered |

Notes on the first three, which are the ones most likely to be misread as oversights:

- **Per-plane diagrams.** Requested directly, in the human's own "*I would like to see **eventually**
  somewhere diagrams of the business LC, SDLC, MDLC, ADLC, CBLC*". "Eventually" is why this is a
  near-term extension rather than in-scope now: `DEC-4`'s single overview diagram is the deliverable
  that keeps the appetite Small, and five richly-illustrated plane diagrams is a second piece of work
  of comparable size to this whole EPIC. Shaping it as its own bet keeps both honest.
- **Presales-process and P0-advisory-package descriptions.** The two documents newly archived in
  `inputs/` (the Decision-Phase advisory and the presales sheet) are real, good pre-LLM-agent
  material that deserves a modern successor. That successor is commercial content, which this EPIC's
  own No-gos exclude and epic 1 owns; epic 1 is being revised in the same round and names these gaps
  in more detail. One cross-reference is the whole treatment here — this EPIC maps to those documents
  once they exist, and its links will resolve or the lint gate will say so.

## Rabbit-holes

- **Restating the lifecycle instead of pointing at it.** This folder orients; it does not define.
  The pull is real: while writing, a rule almost always reads slightly better restated in place than
  linked. Restating it creates a second copy, and the second copy is the one that quietly goes stale
  when the first changes. The practical test while writing: *if this sentence would still read as
  true after the document it links to was deleted, it is a copy* — cut it, keep the link. Orientation
  sentences (what comes next, who hands to whom, why this stage exists) are exactly what this folder
  *should* carry; rules, numbers, gates and definitions are exactly what it should not. When epic
  1-4's own wording is too weak to link to, fix it there and link to the fixed version.
- **Redefining roles or re-litigating the RACI.** The playbooks are role-*shaped*, which makes it
  feel natural to sharpen a role definition or a RACI cell while writing one. Epic 4 owns refining
  it — including the Work-Shaper addition (`DEC-9`), which this EPIC consumes rather than decides.
  Disagreements surfaced while writing a playbook go back to epic 4 as findings, not into this
  folder as corrections.
- **Generating the playbooks from a single source table.** Tempting (six files, one shape), and
  wrong at this size — no tooling exists for it, and the repo already keeps comparable
  hand-maintained cross-reference tables in every SKILL.md. Six short files kept in sync by hand;
  the trigger for revisiting that is in *Known gaps*.
- **One mega-diagram.** Funnel + planes + roles + handoffs + dual DoD in a single figure is
  unreadable. One overview diagram covering the flow (DEC-4); handoffs live as text in the
  playbooks; per-plane diagrams are a named, deferred extension (*Known gaps*), not a reason to
  overload the overview.
- **Closing the MDLC-standalone gap.** Explicitly parked (seed §3); one line naming it is the whole
  treatment (DEC-11).
- **Porting the Employee Handbook.** The handbook is 104 pages and much of it is HR and tooling
  mechanics written for a human-only team (Jira conventions, templates, career levels). Only the
  role mandates in pp. 65-70 are in scope, and only as content seeds for playbooks. Everything else
  in it is either out of scope entirely or a finding for another epic.
- **Publishing.** The root README already announces a future AsciiDoc/Antora publication of the
  durable documentation set. Not this EPIC — plain Markdown in `docs/`, same as its neighbours.
- **Deciding how long a "stage" takes or what it costs.** Durations and the free/paid boundary are
  epic 1's; the map links.

## No-gos

- **No new skills and no new agents or agent stubs.** The agent-wrapper question stays an open fork
  (seed §5) — this EPIC neither answers it nor prepares for it. Where a missing skill or agent is
  genuinely needed, it is **named in *Known gaps* and nowhere else**: naming is in scope, building
  and designing are not.
- **No edits to lifecycle content owned elsewhere**: `docs/engagement/**`,
  `docs/ai-coding/build-lifecycle.md` (`define-meaningfy-lifecycle` renames this from
  `two-tier-methodology.md` in the same round — follow the content, not the pre-rename path),
  `docs/ai-coding/dod-quality-gates.md`,
  `skills/semantic-consulting-coach/references/engagement-model.md`, or epic 4's roles/RACI doc.
  Link lines only, per DEC-14. If one of those documents is wrong, that is a finding for its owning
  epic.
- **No RACI matrix in this folder** — not a copy, not a filtered per-role slice, not a "simplified"
  version. Playbooks link to epic 4's matrix.
- **No role definitions in this folder** — including Work Shaper's. `DEC-9` adds a *playbook*; the
  role, its boundary against Solution Architect, and its RACI cells are epic 4's output, linked.
- **No retiring or deleting of v1 docs here** — epic 2 owns that (seed §7).
- **No P0-advisory product, pricing, or service-packaging definition, and no presales-process
  description** — epic 1 owns both; named in *Known gaps*, not written here.
- **No client-facing derivative** (pitch deck, one-pager, capability statement). These are internal
  orientation docs; client-facing artifacts belong to `proposal-writing` and
  `executive-communication`.
- **The word "canon" appears in no title, heading, or body text** of either deliverable (seed §1).
- **No `design.md` / `tasks.md` in this change round** — shaping only, per seed §8.

---

## What Changes

- Add `docs/how-we-work/README.md` — the integrative map: the funnel (presale free → P0-advisory →
  P1 Decision → direct-to-build), the three entry paths into a P2 service-line contract, the three
  planes (SDLC / MDLC / CBLC, with MDLC-standalone marked as a known gap), Requirements & UC as one
  capability at two depths, Epic shaping with the Work Shaper named as its author, the paired
  Builder/Shipper close at Delivery & Release, and the repeat-client relationship as an annotation.
  One Mermaid diagram. Pointer tables to every owning document. A closing **Known gaps** section
  (DEC-16).
- Add `docs/how-we-work/playbooks/sales-presales.md`, `technical-consultant.md`, `work-shaper.md`,
  `solution-architect.md`, `solution-builder.md`, `solution-shipper.md` — six one-page filtered
  views on the fixed template of DEC-5. `work-shaper.md` is seeded from the Employee Handbook's
  *Project Owner — the Work Shaper* mandate (DEC-9); `solution-architect.md` and
  `solution-builder.md` each carry one line noting they consult during Epic shaping.
- Add one row to the `## Documentation` table in the root `README.md`, pointing at
  `docs/how-we-work/README.md` as the entry point.
- Add one "start here" link line to each of the four epic 1-4 outputs (additive only, DEC-14).
- Add `openspec/specs/lifecycle-playbooks/spec.md` via this change's spec delta (DEC-15).

No breaking changes: every edit is additive, and no existing document's content is altered.

## Capabilities

### New Capabilities

- ~~`lifecycle-playbooks`: the end-to-end lifecycle map and its per-role filtered views —
  role/playbook coverage completeness (one playbook per defined role, no orphans in either
  direction) and the pointer-discipline rule that no normative lifecycle statement originates in
  `docs/how-we-work/`.~~ **(superseded)** This conflicted with `define-ai-domains`'s own DEC-3/DEC-12,
  which retires `docs/how-we-work/` entirely and redistributes its content across three named
  `ai-*` domains (`docs/ai-coding/`, `docs/ai-sales/`, `docs/ai-consulting/`), each carrying its own
  runbook, DoD, and role-filtered playbooks. This capability's requirements assert properties of a
  tree (`docs/how-we-work/`) that no longer exists once that EPIC lands — this change was still
  in-progress and unarchived at the time, so the capability was never merged into
  `openspec/specs/` and there is nothing there to amend with a delta. **Resolution:** the
  role/playbook bidirectional-coverage and pointer-discipline *principles* survive, restated and
  scoped to the new structure as `ai-domain-model` (see
  `openspec/changes/define-ai-domains/specs/ai-domain-model/spec.md`). This capability's own spec
  (`openspec/changes/define-lifecycle-playbooks/specs/lifecycle-playbooks/spec.md`) is not deleted,
  only marked superseded here, per this repo's established reversal-logging convention (matching
  `define-meaningfy-lifecycle`'s DEC-11 annotation of a sibling capability).

### Modified Capabilities

None. No existing capability in `openspec/specs/` covers engagement or lifecycle documentation;
the four sibling epics may introduce such capabilities, and if they do, this change's spec delta
cites them rather than modifying them.

## Impact

- **Documentation only.** No code, no runtime, no public API, no dependency changes.
- **Untouched build machinery**: `.claude-plugin/marketplace.json` (no new skills or bundles),
  `.opencode/` (no regeneration needed — `docs/` is not a generated tree),
  `docs/skill-inventory.md` and `tools/skill_inventory.py` (no new skills to inventory).
- **`tools.repo_lint` `broken_links` gate is the main mechanical risk.** These documents are
  overwhelmingly links, several of them to files created by the sibling epics; DEC-10's sequencing
  exists to keep every target resolvable at merge time. `make lint` must pass with no new findings.
- **Sequencing dependency**: implementation is gated on epics 1-4's documents landing on `develop`
  (DEC-10) — a content dependency, not a shaping-order one. This proposal can be reviewed and bet on
  immediately; the change cannot be implemented in parallel with its siblings.
- **Coupling to epic 4's role set is now load-bearing.** DEC-9 and DEC-13 make the playbook set a
  direct function of epic 4's roles. If epic 4 lands a role set other than the six named in DEC-2,
  this EPIC's file list changes with it — which is what DEC-15's bidirectional invariant is for.
- **Standing maintenance obligation created**: six playbooks plus a map that must be revisited
  whenever the role set (epic 4), the funnel (epic 1), the build loop (epic 2), or the delivery DoD
  (epic 3) changes. The `lifecycle-playbooks` spec (DEC-15) exists to make that obligation
  checkable rather than remembered.
- **Reader-facing surface change**: the root README gains a new recommended first stop for
  "how does Meaningfy actually work", which shifts the default onboarding path away from
  `docs/ai-coding/` for non-Builder roles.
