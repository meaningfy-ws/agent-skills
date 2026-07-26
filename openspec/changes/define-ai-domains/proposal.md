# EPIC: The `ai-*` domains — one shared template for coding, sales, and consulting

**Golden-thread parent:** [`inputs/2026-07-26-ai-domains-brainstorm-seed.md`](inputs/2026-07-26-ai-domains-brainstorm-seed.md)
— a live exploration with the company owner, immediately following the `docs/how-we-work/` +
`docs/services/` restructure and its writing-antipatterns audit. No requirement/architecture parent
sits above it; per [`spine/golden-thread.md`](../../../spine/golden-thread.md) the seed is the root.

**Supersedes, in part:** `define-lifecycle-playbooks` (its `docs/how-we-work/` deliverable retires
entirely under this EPIC — that change is still `in-progress`/unarchived, so this is a logged
re-shape of an implemented-but-not-yet-archived bet, not a silent overwrite: see DEC-3). Touches, by
citation only, real paths written by `define-blc-engagement-model`, `define-delivery-release-lifecycle`,
`define-meaningfy-lifecycle`, and `define-roles-and-raci` — none of their content decisions are
re-litigated, only relocated.

## Appetite

**Medium.** This is a restructure of already-written content (move, don't re-invent) plus a bounded
amount of genuinely new material: two new DoD files (one commercial, one advisory, the latter mostly
a named-gaps scaffold), a handful of "extension point" method stubs, and one environment-docs
relocation. If this grows into actually authoring a Wardley-mapping methodology, a maturity-assessment
scoring rubric, or a full advisory runbook with real technique depth, the bet is being overrun — that
content is future work, named here, not written here.

## Why

Two structures currently describe "how Meaningfy builds": `docs/ai-coding/` (standards-flavoured) and
`docs/how-we-work/build/` (role-flavoured) — competing rather than layered, because nobody had named
the pattern they're both instances of. Once named — **"[domain]-standards, applied by AI agents, to
the [domain] process"** — it's obvious `ai-coding` isn't uniquely a build-plane thing; it's a template,
and Meaningfy runs at least three domains against it: building, selling, and advising. Only the first
has documentation. The commercial content currently lives under a generic `docs/how-we-work/business/`
umbrella with no equivalent standards-doc, and the advisory/discovery methodology — the actual *how*
of a Deep-tier maturity assessment or gap analysis — doesn't exist anywhere, which is exactly the
"missing opsx-runbook for consulting" gap the owner named directly.

**Why now:** the ink is barely dry on the `how-we-work`/`services` restructure; redoing the same ground
a third time later, after more content accretes on the wrong shape, is more expensive than fixing the
shape now while the file count is still small.

## Solution outline

Three parallel domains, each with an identical internal template — **lifecycle/methodology doc +
runbook + DoD + playbooks/** — so a reader who learns one domain's shape already knows where to look
in the other two:

```
docs/
  ai-coding/                    existing, tightened
    build-lifecycle.md          (unchanged home)
    opsx-runbook.md             (unchanged home)
    dod-quality-gates.md        (Builder's DoD stays; Shipper's DoD content moves out — DEC-7)
    playbooks/
      solution-architect.md · solution-builder.md · solution-shipper.md · work-shaper.md  (DEC-4)

  ai-sales/                     new
    engagement-lifecycle.md     (commercial half of discovery-and-onboarding.md + repeat-clients.md)
    sales-runbook.md            (new — the operational script: presale → package sale → contract → repeat client)
    sales-dod.md                (new — the Shipper's DoD definition, relocated; the Disagreement rule stays
                                  canonical in dod-quality-gates.md and is cited, not copied — DEC-7)
    services/                   (moved wholesale from docs/services/ — DEC-5)
    playbooks/
      sales-presales.md         (moved; technical-consultant.md does NOT move here — DEC-6)

  ai-consulting/                new — the named gap
    advisory-runbook.md         (new — the operational script for a Deep-tier engagement)
    consulting-dod.md           (new — mostly a named-extension-point scaffold; see DEC-7, DEC-9)
    methods/
      gap-analysis.md           (thin pointer to decision-package's discovery-flow — DEC-9, already owned)
      data-maturity-assessment.md    (extension-point stub — genuine gap, DEC-8)
      semantic-maturity-assessment.md (extension-point stub — genuine gap, DEC-8)
      wardley-mapping.md             (extension-point stub — genuine gap, DEC-9)
      enterprise-process-modelling.md (extension-point stub — genuine gap, DEC-9)
    playbooks/
      technical-consultant.md   (moved wholly from ai-sales's would-be home — DEC-6)

  roles-and-raci.md             stays top-level — genuinely cross-domain (DEC-3)

  environment/                  new cluster (DEC-11)
    setup.md                    (was docs/environment-setup.md)
    openspec-setup-guide.md     (was docs/ai-coding/openspec-setup-guide.md)
    dual-cli/                   (was docs/dual-cli/, relocated wholesale, contents untouched)
```

`docs/how-we-work/` retires entirely; every file above is either moved (content preserved, cross-links
fixed) or a bounded amount of new scaffold/relocated-DoD content — not a rewrite of settled commercial
or build-plane facts.

## Key decisions

- **DEC-1: The `ai-*` domain pattern is adopted as the organising principle.** Every domain gets the
  same four-part shape (lifecycle/methodology, runbook, DoD, playbooks/). Rationale: a reader who
  understands `ai-coding`'s shape already understands `ai-sales` and `ai-consulting`'s shape — this is
  the structural fix, not a naming preference (owner's own diagnosis, seed).
- **DEC-2: Runbook and Playbook are given distinct, binding definitions.** **Runbook** = the one
  chronological, cross-role operational script per domain. **Playbook** = a role-filtered lens on that
  same runbook — many per domain, one per active role. Every existing and new file must fit one of
  these two shapes; a file that tries to be both is mis-scoped. Rationale: the owner named this
  ambiguity directly; a repo-wide rule beats a per-file judgement call.
- **DEC-3: `docs/how-we-work/` retires; `roles-and-raci.md` stays top-level.** Its content
  redistributes into the three domains (build content → `ai-coding`; business content → `ai-sales`;
  the advisory/consulting content it never actually had → `ai-consulting`, freshly scaffolded).
  `roles-and-raci.md` is the one piece that is genuinely cross-domain (every domain's playbooks cite
  it) and stays a lone top-level file rather than being owned by any one domain. This is a **logged
  re-shape** of `define-lifecycle-playbooks`'s implemented-but-unarchived deliverable, not a silent
  edit — that change's own capability spec (`lifecycle-playbooks`) is marked superseded, see
  Capabilities below.
- **DEC-4: `work-shaper.md` moves into `ai-coding/playbooks/`, not left standalone.** It was homed
  outside `business/`/`build/` in the prior round specifically because it straddles both — but "the
  hybrid role gets its own orphan tier" was exactly what made it read as confusing rather than
  deliberate (owner's own complaint: "makes no sense alone"). Resolution: Work Shaping is
  fundamentally a build-plane activity (it produces the EPIC that Building executes against) that
  *consults* the Architect and *coordinates with* Sales/Presales at its boundary — so it lives with
  the build playbooks, and its own boundary-paragraphs (already written, citing `roles-and-raci.md`)
  keep the cross-domain relationship explicit without needing a separate physical tier.
- **DEC-5: The services catalogue moves under `ai-sales/services/`.** The owner's own framing: the
  catalogue is described from the business point of view (what's sold, to whom, at what scope) — it
  belongs with the domain that sells it, not with a retired umbrella layer.
- **DEC-6: Technical Consultant is consulting-only; Sales/Presales is the only `ai-sales` playbook.**
  Confirmed directly by the owner, reversing this EPIC's own first-draft exploration (which had
  proposed splitting Technical Consultant across two thin playbooks). The existing
  `technical-consultant.md` (48 lines) is already entirely assessment/Decision-Package content with
  no sales-specific material in it — this is a straight relocation, not a split, matching what the
  file already says today.
- **DEC-7: Every domain gets a DoD file; genuine unknowns are named extension points, not invented
  criteria.** `ai-coding/dod-quality-gates.md` (exists, tightened to Builder's-DoD-only wording).
  `ai-sales/sales-dod.md` (new): the Shipper's DoD *definition* (today's `dod-quality-gates.md` lines
  54-64 — the document-trail sign-off) relocates here in substance. The **Disagreement rule** (lines
  69-72) does **not** move — it explicitly governs both DoDs and states it is canonical in one place;
  `ai-sales/sales-dod.md` cites it, `ai-coding/dod-quality-gates.md` keeps sole ownership of the
  sentence. `ai-consulting/consulting-dod.md` (new): what "done" means for a maturity assessment or a
  gap analysis is **not yet decided anywhere in this repo** — this file states that plainly as its own
  content (a short, honest scaffold: what a DoD would need to answer, why nobody's answered it yet,
  and which method docs it would depend on), rather than fabricating acceptance criteria this EPIC has
  no basis for. Rationale: the owner's explicit instruction — "where you don't know, mark it so I know
  what can be extended and where."
- **DEC-8: The maturity-assessment promise is corrected, not carried forward as-is.**
  `docs/how-we-work/business/discovery-and-onboarding.md` currently promises a "semantic & data
  maturity assessment" as a Deep-tier deliverable. `decision-package/SKILL.md` and its own
  `discovery-flow.md` state — twice — that the Deep-tier flow is explicitly **not** a maturity
  assessment, and the preserved seeds repeat the same disclaimer three more times. This is a real,
  documented self-contradiction the prior round carried without noticing (evidence: seed's research
  findings). Resolution: `ai-sales/engagement-lifecycle.md` (the relocated commercial doc) states the
  Deep tier's actual deliverable — the Decision Package, produced via gap analysis against strategic
  ambition — and drops the maturity-assessment framing from the *commercial promise*.
  `data-maturity-assessment.md` / `semantic-maturity-assessment.md` under `ai-consulting/methods/`
  are named as real, separately-sellable techniques (per DEC-9's composable building-block model) that
  the Deep tier does **not** currently include — an honest gap, not a silently-dropped promise.
- **DEC-9: Method docs cite existing ownership where it exists; name the gap where it doesn't.**
  Verified by direct investigation (seed's research section): **gap analysis** is real and owned by
  `decision-package`'s discovery flow — `methods/gap-analysis.md` is a thin pointer, not a rewrite.
  **Wardley mapping** and **enterprise/process modelling as a client-facing discovery technique** are
  clean, uncontested gaps (zero existing repo content) — their stub files name the technique, why it
  matters, and state no skill owns it yet. No stub in this EPIC invents technique content it has no
  grounded basis for.
- **DEC-10: `advisory-runbook.md` is written for real, at the process level — not stubbed.** Unlike
  the individual technique docs, the *sequencing* of a Deep-tier engagement (intake → which methods
  apply → Decision Package → hand-off) is fully knowable today from `decision-package`'s existing
  discovery flow and the Deep-tier description already written — this EPIC assembles that into a
  proper runbook, matching `opsx-runbook.md`'s role in `ai-coding`. The gap is in the *techniques*
  (DEC-9), not in the *script that sequences them*.
- **DEC-11: The environment/tooling cluster is consolidated under `docs/environment/`.**
  `openspec-setup-guide.md` was never build-methodology — it's machine/tooling setup, miscategorised
  under `ai-coding/` since the prior round's rename. It relocates alongside `environment-setup.md`
  (renamed `setup.md` to avoid the `environment/environment-setup.md` redundancy) and `docs/dual-cli/`
  (relocated wholesale, contents untouched) under one new top-level folder. This is a pure relocation;
  no tooling-setup content changes.
- **DEC-12: New capability `ai-domain-model` carries the structural contract.** Every domain has
  exactly one runbook and a DoD; playbooks are role-filtered views citing, not duplicating, their
  runbook; `roles-and-raci.md` is cited by every domain's playbooks, owned by none. `Modified
  Capabilities`: `lifecycle-playbooks` (from `define-lifecycle-playbooks`) is marked superseded — its
  requirements assert properties of `docs/how-we-work/`, which no longer exists after this EPIC.

## Rabbit-holes

- **Don't write the missing methodologies.** Wardley mapping, enterprise/process modelling, and
  maturity assessment are named, not designed. Writing a real scoring rubric or mapping technique is
  a future EPIC's appetite, not this one's — the moment a method stub grows past "what it is / why it
  matters / who doesn't own it yet," this bet is being overrun.
- **Don't reopen the Discovery & Onboarding tiers, pricing, or safeguards.** Those are settled
  (`define-blc-engagement-model`'s decisions, carried into the restructure) — this EPIC relocates the
  commercial doc, it does not re-decide its content, except for the one narrow correction in DEC-8.
- **Don't redesign `dod-quality-gates.md`'s Builder's DoD content.** Only its Purpose header and the
  now-absent Shipper's-DoD section change; the build-tier gate table and automation-boundary section
  are untouched.
- **Don't fix `docs/dual-cli/README.md`'s own naming.** The earlier review flagged it as a third
  pre-existing `README.md`-naming exception; relocating the folder is in scope, renaming its internal
  files is not — a separate, smaller cleanup for later.
- **Don't touch `roles-and-raci.md`'s content** beyond fixing cross-links to moved files. Its role
  definitions, RACI matrix, and adaptation notes are unaffected by where the *playbooks* citing it
  live.
- **Don't invent a fourth `ai-*` domain.** Building, selling, and advising are the three domains named
  by direct observation of how Meaningfy operates today (owner's own framing) — do not extrapolate a
  fourth (e.g. "ai-support" or "ai-ops") without the same direct evidence.

## No-gos

- **No new skills, no new agents, no agent-wrapper stubs.** This EPIC is documentation-only —
  relocating and lightly correcting existing content, plus a handful of clearly-labelled scaffolds.
- **No pricing, rate cards, or contract templates** in any new file — same boundary
  `define-blc-engagement-model` already drew for `services-and-packages.md`/the services catalogue.
- **No CI/workflow changes**, no `tools/repo_lint/lint.py` edits beyond what's needed to keep
  `broken_links` green after the moves (mechanical, not policy).
- **No re-litigating `define-roles-and-raci`'s role definitions or RACI cell values.**
- **No building the Wardley-mapping, enterprise-modelling, or maturity-assessment techniques
  themselves** — see Rabbit-holes. Naming the gap is the entire deliverable for those four files.
- **No changes to `skills/decision-package/` or any other skill's content** — `methods/gap-analysis.md`
  cites it, does not edit it.

---

## What Changes

- **BREAKING (path)**: `docs/how-we-work/` retires entirely. Every live inbound link to any file under
  it is retargeted to the new location.
- Move `docs/how-we-work/build/playbooks/{solution-architect,solution-builder,solution-shipper}.md`
  and `docs/how-we-work/playbooks/work-shaper.md` → `docs/ai-coding/playbooks/` (DEC-4).
- Move `docs/how-we-work/overview.md`'s content into a rewritten `docs/ai-coding/build-lifecycle.md`
  cross-reference and a new `ai-sales`/`ai-consulting` equivalent narrative — the single combined map
  retires in favour of each domain owning its own lifecycle doc (no replacement "map" file is created;
  see Rabbit-holes' overrun guard).
- Move `docs/how-we-work/business/discovery-and-onboarding.md` + `repeat-clients.md` →
  `docs/ai-sales/engagement-lifecycle.md`, with the DEC-8 maturity-assessment wording correction.
- Move `docs/how-we-work/business/playbooks/sales-presales.md` → `docs/ai-sales/playbooks/`.
- Move `docs/how-we-work/business/playbooks/technical-consultant.md` → `docs/ai-consulting/playbooks/`
  (DEC-6).
- Move `docs/services/` → `docs/ai-sales/services/` wholesale (DEC-5).
- Move `docs/how-we-work/roles-and-raci.md` → `docs/roles-and-raci.md` (back to top-level; it moved
  into `how-we-work/` in the prior round, now un-moves).
- Add `docs/ai-sales/sales-runbook.md`, `docs/ai-sales/sales-dod.md` (new; DEC-7).
- Add `docs/ai-consulting/advisory-runbook.md` (new, written for real — DEC-10),
  `docs/ai-consulting/consulting-dod.md` (new, extension-point scaffold — DEC-7).
- Add `docs/ai-consulting/methods/{gap-analysis,data-maturity-assessment,semantic-maturity-assessment,wardley-mapping,enterprise-process-modelling}.md`
  (new — one thin pointer, four extension-point stubs; DEC-9).
- Edit `docs/ai-coding/dod-quality-gates.md`: remove the Shipper's-DoD-definition prose (relocated),
  keep the Disagreement rule and Builder's DoD in place, add a citation to `ai-sales/sales-dod.md`.
- Move `docs/ai-coding/openspec-setup-guide.md`, `docs/environment-setup.md` (renamed `setup.md`), and
  `docs/dual-cli/` → `docs/environment/` (DEC-11).
- Fix every live inbound cross-link across the repo (root `README.md`, `skills/**`, other
  `openspec/changes/*/proposal.md` files' *live* citations — historical citations in already-archived
  or superseded prose are left as historical record per this repo's existing convention).
- Add `openspec/changes/define-ai-domains/specs/ai-domain-model/spec.md` (DEC-12).
- Mark `define-lifecycle-playbooks`'s `lifecycle-playbooks` capability superseded (one annotation in
  that change's own `proposal.md`, matching the pattern already used for the earlier DEC-11
  supersession between `define-meaningfy-lifecycle` and `define-delivery-release-lifecycle`).

## Capabilities

### New Capabilities

- `ai-domain-model`: the structural contract that every `ai-*` domain (`ai-coding`, `ai-sales`,
  `ai-consulting`) carries exactly one runbook and one DoD file; that playbooks are role-filtered views
  citing their domain's runbook rather than restating it; that `roles-and-raci.md` is cited by every
  domain's playbooks and owned by none; and that a method/technique with no owning skill is named as
  an explicit extension point rather than given fabricated content.

### Modified Capabilities

- `lifecycle-playbooks` (from `define-lifecycle-playbooks`, not yet archived): **superseded**. Its
  requirements asserted properties of `docs/how-we-work/` (role/playbook bidirectional coverage,
  pointer-discipline within that tree) — that tree no longer exists after this EPIC. The bidirectional
  coverage and pointer-discipline *principles* survive, restated as `ai-domain-model` requirements
  scoped to the new structure; the old capability's spec is not deleted, just marked superseded with a
  pointer to its replacement, per this repo's existing reversal-logging convention.

## Impact

**Files:** ~11 moves (preserving content), 2 new runbooks (one thin, one fully written), 2 new DoD
files (one relocated-content, one scaffold), 5 new method-doc stubs (one pointer, four extension
points), 1 edited file (`dod-quality-gates.md`), 1 relocated environment cluster (3 items), and the
cross-repo link fix-up this always requires (root `README.md`, `skills/**` citations of any moved
path, other changes' live proposal citations).

**Gates:** `repo_lint.broken_links` is the safety net for every relocation, same as the prior two
rounds. `openspec validate --strict` must pass for both this change and `define-lifecycle-playbooks`
(the superseded annotation, not a content deletion, keeps it valid).

**Cross-epic coordination:** this EPIC is the fourth attempt at getting the reader-facing shape right
in three days — the appetite discipline in Rabbit-holes exists specifically to stop this becoming a
fifth. `define-blc-engagement-model`, `define-delivery-release-lifecycle`, `define-meaningfy-lifecycle`,
and `define-roles-and-raci`'s actual **decisions** are untouched; only the **files carrying them**
move.

**Not affected:** no skill content, no agent roster, no runtime code, no CI configuration.
