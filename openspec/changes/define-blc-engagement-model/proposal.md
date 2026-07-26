# EPIC: The corrected engagement model — presale is the only free stage

**Golden-thread parents:** the brainstorm seed
[`inputs/2026-07-25-brainstorm-seed.md`](inputs/2026-07-25-brainstorm-seed.md) §1–§2 (the human's
direct commercial correction), the round-2 seed
[`inputs/2026-07-26-handbook-and-advisory-findings.md`](inputs/2026-07-26-handbook-and-advisory-findings.md)
(the Decision-Phase advisory and Employee Handbook excerpts, plus the human's inline review
directives on round 1), and the spine's traceability convention
[`spine/golden-thread.md`](../../../spine/golden-thread.md). This is a business/commercial-layer
change with no requirement or architecture parent — the seeds *are* the root. The two round-2 source
documents are archived in full at
[`define-lifecycle-playbooks/inputs/`](../define-lifecycle-playbooks/inputs/) and cited, not copied.

**Siblings shaped in the same round** (cited, never restated): `define-meaningfy-lifecycle`,
`define-delivery-release-lifecycle`, `define-roles-and-raci`, `define-lifecycle-playbooks`. This
epic is first in the dependency order: the other four cite the commercial layer this one fixes.

## Appetite

**Small, with one bounded increase over round 1.** The core pass is unchanged: two docs rewritten,
one skill reference rewritten, five cited consistency edits, one new spec capability. Round 2 adds
three small, explicitly-scoped items, each justified by new source material the human supplied:

| Addition | Size | Why it is in scope | Decision |
|---|---|---|---|
| `docs/engagement/services-and-packages.md` — a **skeleton** stub, placeholders only | one new short doc, no content beyond known package names | the human asked for it directly, twice ("*prepare the placeholders*") | DEC-18 |
| `semantic-consulting-coach/references/decision-phase-posture.md` — condensed posture/discipline material | one new short reference file | new source material exists and the coach skill is its natural owner | DEC-17 |
| A short contract-conformance subsection in `phases.md` naming the Shipper's document trail | ~10 lines | `define-delivery-release-lifecycle` relocates this content here | DEC-19 |

The appetite is still exceeded the moment the pass starts inventing commercial mechanics (pricing
tables, qualification scoring, CRM, marketing) or a playbook for how to *run* P0-advisory — see
Rabbit-holes. **Naming a gap is in scope; closing one is not** — see Known gaps.

## Why

`docs/engagement/phases.md` states a free→paid boundary that is commercially wrong — "**orientation
is free**", with `P0 Orientation` billed as "unpaid, deliberately shallow" — and a strictly
sequential four-phase funnel in which "P2 [is] valid only once P1 is complete" and `P3 Partnership`
is a fourth stage awaiting an owner. The human's correction is blunt: *nothing is free, only presale
work is free*. Everything with a deliverable is sold, short paid advisory is a product Meaningfy
wants to sell, a client who knows what they want must be able to buy a build contract directly, and
buying twice makes a client a repeat client — not a stage anyone graduates into.

Now, because four sibling epics are being shaped on top of this model in the same round, and because
the wrong rule has already propagated: `decision-package`, `proposal-writing`, the coach skill, and
the root `README.md` all restate "orientation is free" or the four-phase sequence. Every additional
doc built on the old model makes the correction more expensive.

Round 2 adds a second reason: real, working practice exists that no repo file carries. The
Decision-Phase advisory documents a **6–8 week calendar-boxed** engagement, an explicit
**safeguards mechanism** for when agreed outcomes cannot be reached, and a substantial body of
**internal posture and discipline** for holding the boundary under client pressure. The Employee
Handbook names the **written document trail** (request for offer → offer → contract → meeting
minutes) that any contract-conformance check runs against. This material predates LLM-agent working
and is written for a human-only team; the substance carries forward, the mechanics (Jira, timesheets,
career levels) do not. Alongside it sits a set of genuinely missing capabilities in the presale
motion — the human named them precisely and asked that they be *marked*, not built.

## Solution outline

Rewrite the commercial model so that a reader of `docs/engagement/` can answer six questions
without asking anyone: **what is free** (presale, and only presale), **what can a client buy first**
(three alternative paid entry points, not one path), **what can a build contract be** (three service
lines, independently sellable), **what protects a fixed-frame engagement when reality intervenes**
(the safeguards mechanism), **what a repeat client is and who leads that relationship**, and **who
holds the boundary** (which skill to invoke at each step). The outcome to move: nobody reading any
Meaningfy doc concludes that a scoping conversation, a roadmap, or an orientation workshop is free.

Three structural moves make that stick rather than decay:

**Split ownership by fact type.** `docs/engagement/` becomes the single source for the commercial
model as *company fact* (stages, the free/paid line, entry points, service lines, the repeat-client
rule). The coach's `references/engagement-model.md` keeps what is genuinely reusable *coaching
knowledge* — the three client cognitive states, the state-2 signals, how to hold a boundary under
pressure, the design questions that pressure-test an engagement — and cites the doc for Meaningfy's
instantiated model instead of restating it. This follows the precedent already in the repo:
[`docs/ai-coding/dod-quality-gates.md`](../../../docs/ai-coding/dod-quality-gates.md) owns the DoD
standard and the `project-setup` skill cites it. It also fixes today's inversion, where
`docs/engagement/README.md` declares the coach's reference canonical while that reference calls its
own specifics "a working draft to pressure-test, not doctrine" — leaving the model owned by nobody.

**Capture the corrected rules as a spec capability.** The rules become RFC-2119 requirements under
`openspec/specs/engagement-model/`, so the correction is gated by `openspec validate` and citeable
by the four sibling epics — rather than being prose that the next rewrite can quietly undo.

**Name what is missing instead of building it.** The presale motion has real capability gaps
(demo preparation, CRM/lead communication, strategic negotiation) and the services inventory is a
skeleton, not a catalogue. These land in a single, findable **Known gaps** section with owners left
open, so the next shaping round starts from a list rather than from rediscovery. The surviving
"commercial layer — TODO" list in `README.md` keeps its placeholder status, minus the one item this
change actually closes (service packaging, answered for P0-advisory and given a home in DEC-18).

## Key decisions

- **DEC-1**: **Presale is the only free stage.** The spine rule in `phases.md` changes from
  "orientation is free / deciding is paid" to "presale is free; everything with a deliverable is
  sold". Rationale: the human's direct correction. The old rule was not merely imprecise — it gave
  away as "orientation" exactly the short advisory that is now a product (DEC-14), and the coach
  skill's own defection table already treats "a quick free steer on where to start" as leakage.
- **DEC-2**: **Keep the `P` labels; redefine their referents rather than renumbering. BREAKING
  vocabulary change:** `P0` now means **P0-advisory** (paid, 1–2 day, named product), *not* free
  orientation. The free stage is called **Presale** and is deliberately **un-numbered**. Rationale:
  renumbering (presale=P0, advisory=P1, decision=P2…) would churn every existing citation in
  `decision-package`, `proposal-writing`, and the client-facing proposal/SoW templates that already
  say "P1 Decision Phase" — including documents already sent to prospects. And numbering the free
  stage is part of what made it read as a stage every client must traverse. Cost accepted: any
  reader of an old document must be told `P0` changed meaning, which is why every live restatement
  is fixed in the same change (DEC-11). The human granted permission to renumber if a simpler naming
  fell out of round 2; none did, so the decision stands unchanged.
- **DEC-3**: **Three paid entry points after presale, modelled as alternatives rather than a
  sequence** — P0-advisory, P1 Decision, and direct-to-build. They are alternative *first paid
  purchases* (mutually exclusive as an entry) and remain freely composable afterwards in any order:
  P0-advisory may lead to P1, P1 to a build contract, a build contract back to P1 for the next
  initiative. The constraint "P2 [is] valid only once P1 is complete" (`phases.md`) and "Only valid
  once P1 is complete" (the coach reference) are removed, not softened. Rationale: the constraint
  prohibits a sale Meaningfy wants to make; stating entry-exclusivity and post-entry composability
  separately stops "not a sequence" being misread as "never sequential".
- **DEC-4**: **Two different elicitations, and the business layer only does the first one.**
  Direct-to-build's precondition is stated as an input condition, not a phase gate: the
  requirements/use-case elicitation a P1 would have supplied must instead be done, at depth, at the
  start of the build contract. What the business layer does before that is a *different activity
  with a different object*:
  - **Sales-strategy elicitation** (presale, P0-advisory, and the framing half of P1) surfaces pain
    points, fears, aspirations, and the values a client decides by. It is psychological and
    goal-oriented — its goal is a closed deal — and it is the input to a proposal, not to a design.
  - **Use-case elicitation** (`architecture`'s UC White / UC Blue) produces contract-level and
    realisation-level behaviour specifications. At the business level expect **at most a sketchy UC
    White, and often not even that**; real use-case work waits for the build engagement.

  Rationale: conflating them either turns a sales conversation into unpaid analysis (the exact
  leakage DEC-1 fixes) or lets a proposal claim requirements coverage it does not have. The *depth
  mechanism* for the build side (shallow White-only vs. deep White+Blue) is owned by
  `define-meaningfy-lifecycle` — cite it, do not restate it here. The methodology for the sales side
  is a named gap, not a decision (see Known gaps, G-5).
- **DEC-5**: **P2 is a family of three named service-line contracts, not a monolith:** software
  development, ontology/model development, and training & capability building. Named by service
  line, **not sub-numbered** (`P2a/P2b/P2c`). Rationale: sub-numbers imply order and hierarchy;
  these are independently sellable and freely combinable. One or more may be bought as its own
  engagement. The three service lines are the P2 rows of the inventory skeleton (DEC-18).
- **DEC-6**: **Repeat business is a plain fact, not a labelled status and not a phase.** The `P3`
  label is retired entirely — not renamed, not reserved — and round 1's capitalised **"Partner"**
  label is dropped with it. The corrected model states the fact in plain prose: *a client who has
  closed two or more contracts is a repeat client, and `executive-communication` leads that
  relationship*. Rationale: the human, reviewing round 1: *"partner is only a recurring client,
  better to even drop this label, not really helpful here."* A capitalised label invites exactly the
  mechanics this epic refuses to design (who awards it, where it is recorded, whether it expires),
  and a numbered slot would re-invite the sequential reading. Revises round 1's DEC-6, which minted
  the label.
- **DEC-7**: **The former P3 content is re-homed as relationship work, not phase work.** Governance
  support, semantic operations, and capability building are described as the work an
  `executive-communication`-led relationship does with a repeat client. `phases.md`'s
  "**Owner:** *to be shaped* — no skill yet" placeholder is **deleted**, not reassigned to a future
  skill. Rationale: the seed names `executive-communication` as the natural owner; a placeholder for
  a skill nobody intends to write is a permanent stale TODO. The Employee Handbook's *Customer
  Success Manager* role is the pre-LLM-agent precedent for this work — cited in the round-2 seed,
  folded in here rather than resurrected as a role (roles belong to `define-roles-and-raci`).
- **DEC-8**: **Ownership split by fact type** (see Solution outline): `docs/engagement/` owns the
  commercial model as company fact; the coach's `references/engagement-model.md` owns the reusable
  coaching frame and cites the doc. Rationale: this respects
  [`AGENTS.md`](../../../AGENTS.md)'s single-source-of-authority rule in both directions — a skill
  holds reusable knowledge, a doc holds company canon — and matches the `dod-quality-gates.md` ↔
  `project-setup` precedent. It also aligns with `define-delivery-release-lifecycle`, which moves
  engagement gates *into* `docs/engagement/`.
- **DEC-9**: **The three cognitive states survive; the free/paid line moves off the State-1/State-2
  seam.** State 1 (orientation) now spans *both* free presale *and* paid P0-advisory, so the
  commercial column of the coach's cognitive-states table can no longer read "Free" for State 1.
  Rationale: the states describe the *client's* head, the stages describe *what is sold* — they were
  conflated because the boundary happened to coincide. It no longer does, and saying so prevents the
  free/paid rule being silently reintroduced through the states table.
- **DEC-10**: **The coach reference's "working draft to pressure-test, not doctrine" framing is kept
  for the coaching method and withdrawn for Meaningfy's own commercial model**, which is now decided.
  The rewritten file says this explicitly. Rationale: without the explicit withdrawal, the file's
  own preamble invites a future reader to re-open a settled decision.
- **DEC-11**: **Every live file that restates the now-wrong rule is corrected in this change**, with
  minimal, pointer-shaped edits: `semantic-consulting-coach/SKILL.md`,
  `decision-package/SKILL.md`, `proposal-writing/SKILL.md`,
  `semantic-consulting-coach/references/semantic-consulting-domain.md`, and the root `README.md`.
  Rationale: shipping the corrected model while four skill files still assert "orientation is free"
  or tabulate "P0 Orientation | Free, shallow" would leave the catalogue self-contradicting and
  violate single-source-of-authority. These are label and pointer fixes only — no skill redesign
  (see No-gos).
- **DEC-12**: **Add a new spec capability `engagement-model`** carrying the normative rules (only
  presale is free; three paid entry points; the P1 fixed frame and its safeguards; the P2
  service-line family; the repeat-client rule; where the model is owned). Rationale: no spec in
  `openspec/specs/` covers the engagement model today (checked), so nothing mechanically prevents the
  next doc pass from reintroducing "orientation is free". A spec makes the correction enforceable and
  gives the sibling epics a stable citation.
- **DEC-13**: **Retire "canon" in the rewritten files** (seed §1) — `README.md`'s "the human canon
  for the four-phase engagement model" becomes plain wording. Rationale: the word is being retired
  repo-wide, and these two files are already being rewritten; deferring it to
  `define-lifecycle-playbooks` would mean touching them twice.
- **DEC-14**: **P0-advisory is defined commercially, not procedurally.** In scope: it is paid,
  1–2 days, named, sellable, distinct from presale, and its output is explicitly **not** the
  Decision Package. Out of scope: what its output artefact looks like — no template, no reference
  file, no new skill. Rationale: the seed names the product but not its deliverable; naming a
  product Meaningfy has not yet sold is a decision, designing its artefact is speculation. The
  boundary that matters commercially (it is not, and does not substitute for, the Decision Package)
  is stated; the format waits for the first sale.
- **DEC-15**: **P1 runs 6–8 weeks, calendar-boxed, at fixed price and fixed duration, with variable
  depth handled explicitly.** Rationale: the Decision-Phase advisory states *"Typically 6–8 weeks ·
  Calendar-based, not effort-based"* and *"we do not anchor the Decision Phase to a predefined number
  of man-days or a rate card"*. This supersedes the round-1 brainstorm seed's "4–6wk", which was
  never written into any repo file — no live text is being corrected, a missing fact is being added.
  "Calendar-based, not effort-based" is stated alongside the number, because the number alone would
  be read as an effort estimate and re-open the man-day anchoring the model rejects.
- **DEC-16**: **The safeguards mechanism is documented as existing practice, in three sentences, and
  no further.** If agreed outcomes cannot reasonably be reached within the agreed duration for
  reasons outside Meaningfy's control (stakeholder availability, information access, late
  decision-makers, reorganisations), Meaningfy signals it explicitly and proposes one of: **a scope
  reduction, a short extension, or a formal stop with partial delivery** — never a silent overrun.
  Rationale: this is capture, not invention — the advisory doc already states it, and the coach's
  `engagement-model.md` already carries it as a principle without the commercial doc carrying it as
  a rule. It brushes the "do not design commercial mechanics" rabbit-hole, and the human explicitly
  bounded the attempt: *"despite this being a risk you could give it a short, limited attempt only,
  but mark it as a point to work on further and extend."* Contractual mechanics (how an extension is
  priced, what partial delivery entitles either party to, notice periods) are **out** — Known gaps,
  G-6.
- **DEC-17**: **The Decision-Phase posture material gets its own coach reference file,
  `skills/semantic-consulting-coach/references/decision-phase-posture.md` — condensed, not
  verbatim.** It carries: ambiguity-is-a-signal; helpfulness vs. usefulness; "we do not guess"; calm
  under pressure; no need to prove expertise; protective-not-defensive formulations ("*we can, but
  that would be guesswork at this stage*"); redirect-don't-block; yes / not-yet; ending cleanly; and
  the internal red-flags list. Rationale: this is coaching knowledge, so DEC-8 puts it in the skill,
  not in `docs/engagement/`. It does not fit inside `engagement-model.md` without doubling that
  file's length and blurring its job (that file states *what each stage is for*; this one states
  *how a consultant behaves inside it*). This **relaxes round 1's own No-go against new reference
  files** — the justification is the new source material, which did not exist when that No-go was
  written. Bound: one file, condensed from one source, no new skill, no sales-script content.
- **DEC-18**: **Add `docs/engagement/services-and-packages.md` as a skeleton, not a catalogue.** It
  lists what Meaningfy sells today — Presale (free), P0-advisory, P1 Decision, and the three P2
  service lines — one row each, with `Scope`, `Duration`, `Price`, `Deliverable`, and `Owning skill`
  fields left as explicit `TODO` placeholders except where this epic already decides them (P1's
  6–8 weeks and fixed frame, P0-advisory's 1–2 days). Rationale: the human asked twice, directly:
  *"we must have a services we sell inventory and a set of packages we sell. so that the client can
  easely buy from us, like from a shop, pick from a shelf and know what is in the box and how much
  it costs. this is a TODO now, and must be extended in the future, prepare the placeholders."* This
  is the appetite increase named in Appetite, and it is deliberately the cheapest form of it: a table
  with named rows and empty cells is editable by anyone, citeable by future skills, and impossible to
  mistake for a priced catalogue. Populating it is Known gaps G-7.
- **DEC-19**: **`docs/engagement/` hosts the contract-conformance (Shipper) side of Delivery &
  Release; `docs/ai-coding/dod-quality-gates.md` keeps the Builder side.** `phases.md` gains a short
  subsection naming what a contract-conformance check runs against — the written trail of **request
  for offer, offer, contract, and meeting minutes / documented exchanges** — adapted from the
  Employee Handbook's *Contractual Validation* step and stated for light human sign-off with
  agent-assisted document review. Rationale: the human's framing is that *"this shipping/business
  delivery is clearly a document part of the commercial bulk of the documentation not SDLC"*, and
  `define-delivery-release-lifecycle` is relocating it here in the same round. **Coordination is by
  content, not by merge order:** this epic states the document trail and the ownership fact; the
  sibling epic owns the DoD's exact wording, the Builder/Shipper pairing, and the disagreement /
  re-shape rule, and leaves a pointer in `dod-quality-gates.md`. If the sibling lands first, this
  subsection cites it instead of restating it. What this epic will **not** do is invent the DoD's
  checklist items — that would duplicate the sibling's authored text.

  **Cross-checked against the sibling's content contract (`define-delivery-release-lifecycle`
  DEC-12) and completed to match it.** That contract requires six elements of whatever this epic
  writes; the paragraph above committed to the document trail, the accountability, and the
  light-touch framing, but not to the remaining two, which this subsection **also carries**: a
  **one-line pointer back** to the Builder's DoD in `dod-quality-gates.md`, stating that the two
  close together on two planes and neither substitutes for the other; and a **one-line citation** of
  the disagreement/re-shape rule the sibling states once, in its own file, scoped to both DoDs (never
  restated here). Both are one sentence each — this does not grow the subsection's ~10-line size
  estimate in Appetite, it closes a gap between two already-shaped proposals rather than adding new
  content.

## Rabbit-holes

- **Do not design the commercial mechanics.** The `README.md` TODO block (qualification criteria,
  pre-sale cadence, closing mechanics, marketing, CRM, fit-for-market) stays a TODO. Two items come
  off the list and no more: *service packaging* (for P0-advisory, and as the DEC-18 skeleton) and
  the *safeguards mechanism* (DEC-16, three sentences, capture-only). Everything else the safeguards
  imply — extension pricing, partial-delivery entitlements, notice periods — is Known gaps G-6, not
  work.
- **Do not write the P0-advisory playbook or its deliverable template** (DEC-14). Name it, bound it,
  stop. The coach's existing design questions already cover *how to design* it.
- **Do not populate the services skeleton** (DEC-18). Rows and empty fields only. The moment a price,
  a rate card, or a package bundle appears, the appetite is gone.
- **Do not renumber the phases** (DEC-2) and do not invent `P2a/P2b/P2c` or a fourth service line
  (DEC-5). Permission to renumber was granted in review and deliberately not exercised: the
  citation churn cost is unchanged and round 2 produced no simpler naming.
- **Do not mint a replacement label for "Partner"** (DEC-6). "Repeat client" is a description, not a
  status; if it starts acquiring criteria beyond *≥2 closed contracts*, stop.
- **Do not resolve elicitation depth for direct-to-build** (DEC-4) — that is
  `define-meaningfy-lifecycle`'s. Cite it; a cross-reference is cheaper than a duplicated rule.
- **Do not turn the posture file into a sales script** (DEC-17). The source is explicit that it is
  *"written for senior consultants and leadership, not as a sales script and not as a junior
  playbook"*. Condense the principles and the example formulations; do not expand them into
  objection-handling trees.
- **Do not extend the consistency edits into skill redesign.** `decision-package` and
  `proposal-writing` remain correct about P1 — the Decision Package's structure, the fixed-frame
  pricing, the scope-boundary checklist are all untouched. Only their *phase labels and the free/paid
  sentence* move.
- **Beware the ownership split becoming a rewrite of the whole coach skill** (DEC-8). The coach's
  modes, defection table, worked examples, and question bank are out of scope; only the passages
  that assert the commercial model change, plus the new posture file.
- **Do not restate the sibling epics.** The Builder/Shipper dual DoD, the SDLC/MDLC/CBLC planes, the
  roles, and the RACI matrix all belong elsewhere and are one-line pointers at most. Note in passing
  that `define-roles-and-raci` now defines **six** roles (a Work Shaper was added in round 2 from the
  Employee Handbook) — this epic names no roles, but any role name it cites must match that model.

## Known gaps

Named, not closed. Each is a real missing capability or unwritten process surfaced by the human or by
the round-2 source material. **Nothing in this section is built by this epic.** Owners are left open
deliberately: a gap with a speculative owner is harder to re-shape than a gap with none.

| # | Gap | What exists today | Shape |
|---|---|---|---|
| **G-1** | **The presale-to-contract process itself** — how a lead becomes a signed contract, step by step | `semantic-consulting-coach/references/presales-discovery.md` covers discovery *questions*; nothing covers the *process* | New doc under `docs/engagement/`, or a skill; not decided |
| **G-2** | **Demo preparation** — how a demo is scoped, built, rehearsed, and what it may and may not promise | nothing | Likely a skill |
| **G-3** | **CRM and lead communication** — grooming meeting minutes into follow-ups, keeping the CRM current, lead email cadence | nothing | Likely a skill |
| **G-4** | **Strategic negotiation / strategic thinking for the client relationship** | nothing | Likely a skill, possibly with an agent |
| **G-5** | **External sales & closing methodology** as a source input for DEC-4's sales-strategy elicitation | nothing; the repo has no sales-methodology material at all | An input to G-1/G-4, not a deliverable itself |
| **G-6** | **Commercial mechanics behind the safeguards** (DEC-16): how an extension is priced, what partial delivery entitles either side to, notice and escalation | the three-option mechanism only (DEC-16) | Contractual/legal, probably not a skill |
| **G-7** | **Populating the services & packages inventory** (DEC-18): scope, duration, price, deliverable per row | the skeleton this epic adds | Ongoing edit of the DEC-18 doc |
| **G-8** | **MDLC-standalone ontology/application-profile methodology** | `conceptual-modelling` covers modelling *inside* a software project only, and says so | Parked by the round-1 seed for its own shaping cycle |

Detail where the human was specific:

- **G-4** was named precisely: *"strategic planning according to Chriss Voss, Robert Greene and
  SunZhi… a strategic thinking agent/skill that can think of the relationship like a chess game,
  cold calculated, deeply psychological."* Recorded as named; **not** designed here — what such a
  skill contains, whether the influence material belongs in a skill at all, and how it interacts
  with `executive-communication` are all open.
- **Not a gap: pitch and presentation material.** [`executive-communication`](../../../skills/executive-communication/SKILL.md)
  already owns preparing pitches, decks, and executive narrative, including the Governing Thought.
  G-2 (demos) is adjacent but distinct — a demo is a working artefact, not a communication artefact —
  and G-3/G-4 are distinct again. Do not fold any of them into `executive-communication` by default.
- **G-1 and G-5 are the same missing input seen from two sides** — the process and the methodology
  behind it. Whoever shapes one should shape both.

## No-gos

- **No new skills and no new agents** — including no partnership/governance phase-owner skill to
  replace the deleted "to be shaped" placeholder (DEC-7), no skill for any Known gap, and no agent
  stub for any commercial role. Gaps are named in the Known gaps section and nowhere else.
- **No edits anywhere under `docs/ai-coding/`.** Retiring v1, rewriting `two-tier-methodology.md`,
  and restructuring `dod-quality-gates.md` (including *removing* its duplicated commercial-TODO
  block, and reducing the Shipper's DoD to a pointer per DEC-19) belong to
  `define-meaningfy-lifecycle` and `define-delivery-release-lifecycle`. This epic owns only the
  content that lives in `docs/engagement/`.
- **No roles, no RACI, no playbooks** — `define-roles-and-raci` and `define-lifecycle-playbooks`.
  Where the corrected model needs to name a doer, it names the *owning skill*, not a role; the one
  exception is DEC-19's contract-conformance subsection, which names the Shipper because the
  sibling epic's relocation requires it, and which defines nothing about the role.
- **No commercial-process invention:** no pricing model, no rate card, no qualification scoring, no
  CRM or marketing design, no B2B/B2G motion split. DEC-16 and DEC-18 are the two bounded, decided
  exceptions and neither adds a number.
- **No MDLC-standalone ontology-methodology skill** — parked by the seed for its own shaping cycle
  (G-8).
- **No client-facing artefact rewrites.** The proposal template, SoW template, and Decision Package
  template keep saying "P1 Decision Phase"; DEC-2 exists specifically to preserve that.
- **No change to what the Decision Package contains** or to P1's substance. P1 gains a stated
  duration and a stated safeguards mechanism (DEC-15, DEC-16) — both facts that were true and
  unwritten — and changes position (one of three entry points). Its activities, deliverable, and
  boundary are untouched.
- **No new reference files under `skills/semantic-consulting-coach/references/` beyond the one named
  in DEC-17.** `engagement-model.md` is still rewritten in place; `question-bank.md`,
  `presales-discovery.md`, and `semantic-consulting-domain.md` are untouched except for the one cited
  passage in the last (DEC-11).
- **No bundle or marketplace membership changes** — no skill is added, moved, or removed.

---

## What Changes

- **Rewrite `docs/engagement/README.md`** (path later retired by a follow-up restructure into
  `docs/how-we-work/business/`; unlinked here for historical accuracy): presale-only-free
  funnel replacing the four-phase table; three paid entry points (DEC-3); P2 service-line family
  (DEC-5); the repeat-client rule (DEC-6); ownership statement making this directory the source for
  the commercial model (DEC-8); "canon" removed (DEC-13); a link to the new services skeleton
  (DEC-18); the TODO block retained minus the service-packaging and safeguards items
  (Rabbit-holes), with a pointer to Known gaps for what is missing rather than merely undecided.
- **Rewrite `docs/engagement/phases.md`** (path later retired by the same follow-up restructure;
  unlinked here for historical accuracy) — **BREAKING**
  vocabulary: `P0` redefined from free orientation to paid advisory (DEC-2); the "orientation is
  free" spine rule replaced (DEC-1); the "P2 valid only once P1 is complete" gate removed (DEC-3)
  with the input condition and the two-elicitations distinction stated instead (DEC-4); P1 gains its
  6–8-week calendar-boxed fixed frame (DEC-15) and the safeguards mechanism (DEC-16); the
  `P3 — Partnership & Evolution` section replaced by the repeat-client rule and its relationship work
  (DEC-6, DEC-7), including deletion of the "**Owner:** *to be shaped*" placeholder; a short
  contract-conformance subsection naming the RfO/offer/contract/minutes trail (DEC-19).
- **Add `docs/engagement/services-and-packages.md`** (DEC-18) — six rows, placeholder fields, no
  prices.
- **Substantively rewrite
  [`skills/semantic-consulting-coach/references/engagement-model.md`](../../../skills/semantic-consulting-coach/references/engagement-model.md)**:
  keeps the coaching frame (what is being sold, the three cognitive states, state-2 signals, the
  boundary safeguard, the P1 intent, the design questions); the commercial-model definitions become
  a citation to `docs/engagement/` (DEC-8); the cognitive-states table's commercial column re-mapped
  (DEC-9); the "working draft, not doctrine" caveat scoped to the method only (DEC-10); the P0–P3
  intentions table replaced; the "duration and shape" design question resolved rather than left open
  (DEC-15); a pointer to the new posture file.
- **Add `skills/semantic-consulting-coach/references/decision-phase-posture.md`** (DEC-17) —
  condensed posture and discipline material, cited from the coach's SKILL.md reference list.
- **Cited consistency edits** (DEC-11), minimal and pointer-shaped:
  - `skills/semantic-consulting-coach/SKILL.md` — the "core insight" free→paid sentence, the
    "When to use" engagement-process bullet, the client-orchestration cell of the three-layers table,
    the "Modes are not Phases" note, the `references/` bullets under Reference material (one edited,
    one added), and the `Owns:` line in Boundary & Related Skills (it currently claims to own the
    engagement model outright).
  - `skills/decision-package/SKILL.md` — the two-row phase table asserting "P0 Orientation | Free,
    shallow" and the sentence "Orientation is free, shallow, and never deeply customised" become a
    pointer to the owning doc.
  - `skills/proposal-writing/SKILL.md` — "**Inputs:** P0 orientation notes" and "this is still P0"
    re-labelled to presale / P0-advisory.
  - `skills/semantic-consulting-coach/references/semantic-consulting-domain.md` — the public-funnel
    vs. internal-`P0–P3`-axis note re-labelled.
  - root [`README.md`](../../../README.md) — the docs-table row "the P0–P3 engagement model".
- **Add `openspec/specs/engagement-model/spec.md`** via this change's spec delta (DEC-12).
- **Regenerate** the `.opencode/` mirror (`make generate-opencode`) and
  `docs/skill-inventory.md` (`make skill-inventory`) after the skill edits.

## Capabilities

### New Capabilities

- `engagement-model`: the normative commercial model — presale as the only free stage; the three
  paid entry points and their preconditions; P1's fixed calendar frame and its scope-reduce /
  extend / stop safeguards; the P2 service-line family; the repeat-client rule and who leads that
  relationship; and the ownership rule that `docs/engagement/` holds the commercial fact while the
  coach skill holds the coaching frame and the consulting posture.

### Modified Capabilities

None. No spec under `openspec/specs/` currently states any requirement about the engagement model,
the free/paid boundary, or the P0–P3 phases (checked across all ten existing specs). The only
existing spec that so much as names `semantic-consulting-coach` is `writing-antipatterns`, in a
cross-reference list this change does not alter.

## Impact

- **Docs:** `docs/engagement/README.md`, `docs/engagement/phases.md` (both rewritten),
  `docs/engagement/services-and-packages.md` (new, skeleton), root `README.md` (one row).
- **Skills:** one reference substantively rewritten
  (`semantic-consulting-coach/references/engagement-model.md`), one reference added
  (`semantic-consulting-coach/references/decision-phase-posture.md`), and four files edited at cited
  passages (`semantic-consulting-coach/SKILL.md`, `decision-package/SKILL.md`,
  `proposal-writing/SKILL.md`, `semantic-consulting-coach/references/semantic-consulting-domain.md`).
  No skill is added, renamed, or removed.
- **Generated artifacts:** the committed `.opencode/` tree mirrors every edited and added skill file
  and must be regenerated; `docs/skill-inventory.md` regenerates because the coach's
  `Owns:`/`Related:` lines change. Both are gated inside `make lint`.
- **Gates:** `repo_lint`'s `broken_links` check covers the new cross-links between `skills/` and
  `docs/engagement/` (the `docs/ai-coding/` ↔ `project-setup` links prove the pattern passes);
  `openspec validate --strict` covers the new spec.
- **Downstream (documentation only, no code):** `define-delivery-release-lifecycle` depends on this
  epic owning the surviving commercial-TODO block before it deletes the copy in
  `dod-quality-gates.md`, and hands this epic the contract-conformance content per DEC-19;
  `define-roles-and-raci` and `define-lifecycle-playbooks` cite the corrected stages, the
  repeat-client rule, and this epic's Known gaps rather than re-deriving them. Shaping order is this
  epic first, but none of them is blocked from being shaped in parallel.
- **No code, runtime, API, dependency, or CI impact.** No bundle or `marketplace.json` change.
- **Commercial risk accepted:** `P0` changes meaning (DEC-2), so any prospect-facing material that
  used "P0" for free orientation is now inconsistent with the internal model. Client-facing
  templates are unaffected because they reference only "P1 Decision Phase" (verified across the
  proposal, SoW, and Decision Package templates). The 6–8-week figure (DEC-15) becomes a stated
  commitment where none was written before; it is documented as *typical* and calendar-boxed, with
  the safeguards mechanism (DEC-16) as its release valve.
- **Known gaps are recorded, not owned.** Eight named gaps (G-1…G-8) leave this change with no
  assignee and no schedule. That is deliberate — but it means the Known gaps section is the single
  place a future shaping round must read, and it will go stale silently if a gap is closed elsewhere
  without updating it.
