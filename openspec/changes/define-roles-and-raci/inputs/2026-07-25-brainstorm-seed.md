# Seed — BLC/SDLC redefinition brainstorm (excerpt for `define-roles-and-raci`)

**Status:** SECONDARY input. Preserved verbatim, **never groomed, never deleted**. The shaped EPIC
(`../proposal.md`) supersedes this as the primary truth but does not replace it.

**Provenance:** a long `/opsx:explore` session between Claude Code and Eugeniu Costetchi
(2026-07-25), auditing `docs/ai-coding/`, `docs/engagement/`, `docs/engineering-standards/`,
`docs/philosophy/` and the 23-skill catalogue. The full synthesis covers five parallel epics; this
file archives the slice that seeds **this** change — §1 (why the work exists), §5 (the five roles),
§6 (the draft RACI), and the relevant part of §8 (epic split). Sections 2, 3, 4 and 7 of the
synthesis seed the sibling epics `define-blc-engagement-model`, `define-meaningfy-lifecycle` and
`define-delivery-release-lifecycle`; they are cited, not restated, here — except for §4's
Builder/Shipper split, quoted below because the two roles it names are defined in this change.

**Ground rule stated in the seed:** whoever shapes from this seed does **not** ask the user
anything. Open points are resolved by the shaper as a reasoned `DEC-` or parked in
Rabbit-holes/No-gos. Decisions below were made by the human across five conversational rounds — do
not silently drop one; disagreement goes in Key Decisions or Rabbit-holes.

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

## §4 (partial) — the Builder/Shipper delivery split (verbatim; needed because it defines two roles)

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

## §5. The five roles (verbatim)

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

## §6. Draft RACI (verbatim — "treat as a strong draft, not gospel; refine when shaping")

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

## §8 (slice). This change's place among the five epics (verbatim entries)

4. **`define-roles-and-raci`** — New doc(s) defining the five roles (§5) and the RACI matrix (§6),
   including the Work-Shaper ambiguity and the agent-wrapper fork, both documented as deliberate
   open points, not resolved. Cross-cutting; depends on 1-3 conceptually but shape now from this seed.

Siblings, cited not restated (each owns its own content):

1. **`define-blc-engagement-model`** — corrected commercial model (§2); rewrites
   `docs/engagement/README.md` + `phases.md` and `semantic-consulting-coach/references/engagement-model.md`.
2. **`define-meaningfy-lifecycle`** — retires v1, rewrites `two-tier-methodology.md` with ADLC/MDLC-lite
   named, resolves Requirements & UC (§4).
3. **`define-delivery-release-lifecycle`** — restructures `dod-quality-gates.md`, adds the
   Builder/Shipper dual-DoD lane (§4), fixes the stale ownership-table line (§7).
5. **`define-lifecycle-playbooks`** — one integrative big-picture flow doc plus one short playbook per
   role (§5), each a filtered view.

**Parked, explicitly not one of the five, do not shape now:** MDLC-standalone — an
ontology/application-profile development methodology skill (§3). The seed states plainly: "skills are
still missing to support this"; it is a real capability gap, out of scope for all five epics, named
only where relevant.

**Scope discipline that applies to all five:** this round is **shaping only** — produce
`proposal.md` per `openspec/schemas/meaningfy/templates/proposal.md`. Do **not** derive
`design.md`/`tasks.md`, do **not** implement, do **not** edit any file outside
`openspec/changes/<id>/`. No new skills, no new agent stubs, in any of the five.
