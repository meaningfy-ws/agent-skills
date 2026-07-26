<!-- PLAN (design half). PLAN = this file + tasks.md. The clarity gate scores the pair (≥9/10). -->

> Parent: [`openspec/changes/define-ai-domains/proposal.md`](proposal.md)

## Context

Three domains — `ai-coding` (exists), `ai-sales` (missing), `ai-consulting` (missing, the named
gap) — share one template (proposal DEC-1: lifecycle/methodology + runbook + DoD + `playbooks/`).
`docs/how-we-work/` retires; its content redistributes. This is the fourth reshaping of the
reader-facing shape in three days (proposal Impact) and the closest prior sibling,
`define-lifecycle-playbooks`, already solved an adjacent problem (bidirectional role↔playbook
coverage, pointer-discipline) for the tree this EPIC now retires — its `design.md` and
`specs/lifecycle-playbooks/spec.md` are the direct precedent this PLAN reuses rather than
re-deriving.

Current file inventory verified by direct read (paths, exact line counts/anchors that matter for
the moves):

| File | Lines | Notable anchors cited from elsewhere |
|---|---|---|
| `docs/how-we-work/overview.md` | 134 | `#two-kinds-of-work-one-client-relationship` |
| `docs/how-we-work/business/discovery-and-onboarding.md` | 151 | `#presale-free-no-deliverable`, `#discovery--onboarding-paid-two-depths`, `#direct-to-build`, `#the-outcome-semantic-layer-adoption`, `#known-gaps` |
| `docs/how-we-work/business/repeat-clients.md` | 27 | (cited as whole-file link, no sub-anchor) |
| `docs/how-we-work/business/semantic-layer-services.md` | 12 | — |
| `docs/how-we-work/business/playbooks/sales-presales.md` | 57 | — |
| `docs/how-we-work/business/playbooks/technical-consultant.md` | 48 | — |
| `docs/how-we-work/build/playbooks/{solution-architect,solution-builder,solution-shipper}.md` | 49/51/49 | — |
| `docs/how-we-work/playbooks/work-shaper.md` | 59 | — |
| `docs/how-we-work/roles-and-raci.md` | 213 | `#work-shaper`, `#raci-matrix`, `#solution-builder`, `#solution-shipper`, `#technical-consultant`, `#salespresales`, `#solution-architect`, `#open-question--agent-wrappers` |
| `docs/services/index.md` + 6 pages | — | `docs/services/agentic-framework-development.md` etc. already use the exact **"No skill in this catalogue owns X"** phrasing this EPIC needs for the four `methods/` stubs (see Decisions) |
| `docs/ai-coding/dod-quality-gates.md` | 106 | lines 54-64 (Shipper's DoD definition, to relocate), lines 69-72 (Disagreement rule, canonical, stays) |
| `docs/ai-coding/openspec-setup-guide.md` | 81 | already `../../`-depth (under `docs/ai-coding/`) |
| `docs/environment-setup.md` | 145 | currently `../`-depth (directly under `docs/`) |
| `docs/dual-cli/` | 6 files | moves wholesale, contents untouched (proposal, Rabbit-holes) |
| `skills/decision-package/references/discovery-flow.md` §3 | — | the gap-analysis owner `methods/gap-analysis.md` points to |

Verified live inbound markdown-link sites (actual `[text]` + `(path)` syntax, the only thing
`repo_lint.broken_links` scans — plain-text path mentions, e.g. in the five sibling
`openspec/changes/*/proposal.md` files, are **not** link syntax and are therefore historical prose
per the repo's existing convention, needing no edit):

- `README.md` (lines 6, 55, 133-135, 152 — repo-structure block too)
- `AGENTS.md` (lines 27, 58, 63, 71 — all `docs/dual-cli/...`)
- `THIRD_PARTY_NOTICES.md` (line 10 — `docs/environment-setup.md`)
- `hooks/bindings.md` (line 86 — `docs/dual-cli/compatibility.md`)
- `skills/project-setup/SKILL.md` (line 40 — `docs/ai-coding/openspec-setup-guide.md`)
- `skills/decision-package/SKILL.md` (line 87 — `docs/how-we-work/business/`)
- `skills/semantic-consulting-coach/SKILL.md` (7 sites) and its 3 `references/*.md` files (12 sites
  total) — all `docs/how-we-work/business/...`
- `docs/ai-coding/dod-quality-gates.md` (4 sites) and `docs/ai-coding/build-lifecycle.md` (4 sites) —
  internal cross-links into `../how-we-work/...` and same-dir `openspec-setup-guide.md`
- `docs/ai-coding/opsx-runbook.md` (1 site — same-dir `openspec-setup-guide.md`)
- `.opencode/**` mirrors every `skills/**` hit above — **regenerated, never hand-edited** (README.md
  Repository-structure block: `make generate-opencode`)

## Goals / Non-Goals

**Goals:**
- Every file move preserves content and fixes its own outbound relative links (the mover's
  responsibility, not a separate pass).
- Every live inbound markdown link across the repo is retargeted in the same change that moves its
  target, so no intermediate commit ships a broken link.
- The two genuinely new-content files (`sales-runbook.md`, `advisory-runbook.md`) and the five
  `methods/`+DoD scaffolds have one fixed, comparable internal template each, decided here so the
  implementer fills a mould rather than improvising structure per file.
- The cross-change supersession mechanics question (proposal DEC-12 / Capabilities) is resolved
  concretely, not left for implementation to guess.

**Non-Goals:**
- No content authoring for Wardley mapping, enterprise/process modelling, or maturity assessment
  (proposal Rabbit-holes — named, not designed).
- No re-litigation of `roles-and-raci.md`'s role definitions, RACI cells, or the Employee-Handbook
  adaptation notes (proposal No-gos).
- No CI/lint logic changes beyond what keeps `broken_links` green (proposal No-gos).

## Decisions

Settled in the EPIC — cited, not re-argued: DEC-1 (domain template) · DEC-2 (runbook/playbook
definitions) · DEC-3 (how-we-work retires, roles-and-raci stays top-level) · DEC-4 (work-shaper into
ai-coding/playbooks/) · DEC-5 (services → ai-sales/services/) · DEC-6 (technical-consultant
consulting-only) · DEC-7 (DoD-per-domain, Disagreement rule stays canonical) · DEC-8
(maturity-assessment correction) · DEC-9 (method-doc ownership/gap naming) · DEC-10
(advisory-runbook written for real) · DEC-11 (environment/ cluster) · DEC-12 (`ai-domain-model`
capability + `lifecycle-playbooks` superseded).

New planning-level choices made while deriving this PLAN:

- **The cross-change supersession mechanics (resolves the proposal's own flagged uncertainty).**
  Verified by direct inspection: `lifecycle-playbooks`'s capability spec lives at
  `openspec/changes/define-lifecycle-playbooks/specs/lifecycle-playbooks/spec.md` — that change is
  **not archived** (it sits under `openspec/changes/`, not `openspec/changes/archive/`), so the
  capability has **never been merged into `openspec/specs/`**. OpenSpec's delta mechanism
  (`## MODIFIED Requirements` / `## REMOVED Requirements` in a *different* change's `specs/` folder)
  exists to amend an entry in the durable `openspec/specs/<cap>/spec.md` store — there is nothing
  there to amend, because `lifecycle-playbooks` was never archived into it. Writing a delta against
  it from `define-ai-domains/specs/` would target a capability that doesn't exist in the place
  deltas resolve against. This is exactly the situation `define-meaningfy-lifecycle`'s own **DEC-11**
  already handled, for the same reason (a sibling capability, not yet archived, whose ownership a
  later-written epic needs to override) — that precedent's mechanism is a **direct annotation in the
  sibling change's own still-open `proposal.md`**: the conflicting decision is struck through
  (`~~...~~`), a one-paragraph "this conflicted with / resolution" note is added inline, and the
  Capabilities section's own capability line is suffixed `**(superseded)**` with a pointer to the
  successor. **Resolution:** this EPIC's `tasks.md` (group i) instructs the implementer to make that
  same annotation directly in `openspec/changes/define-lifecycle-playbooks/proposal.md`'s
  Capabilities section — not a spec delta in `define-ai-domains/specs/`. `define-ai-domains/specs/`
  therefore carries **only** `ai-domain-model` as an `## ADDED Requirements` delta (no `## MODIFIED
  Requirements` block for `lifecycle-playbooks` — there is nothing in the durable store to modify).
  `openspec validate --strict` must still pass on **both** changes afterward — `define-lifecycle-
  playbooks`'s own capability spec is not deleted, only annotated, so it stays structurally valid.

- **Exact write order** (drives `tasks.md`'s group sequence a-j, dependency-ordered, not
  alphabetical): moves and new content first (a-f), then the cross-repo link sweep (g) — deferred
  until every destination path is final, so the sweep is a single pass with no rework — then
  retiring `docs/how-we-work/` (h), which is **the one hard dependency**: the source tree must not
  be deleted before every one of its files has been confirmed moved, because deleting first would
  leave nothing to move *from* if a task is interrupted mid-sequence. The spec delta and the
  sibling-supersession annotation (i) land after the structure exists, so they describe what was
  actually built. Validation (j) is strictly last.

- **`ai-consulting/consulting-dod.md`'s exact scaffold wording** (DEC-7/DEC-9, "reads as an honest
  gap-statement, not a stub apology"). Fixed four-heading structure, each heading itself a checkable
  claim rather than a vague placeholder:
  ```
  # Consulting DoD — Definition of Done for advisory work

  ## What "done" would need to answer
  <!-- the 2-3 concrete questions a real DoD would have to settle, e.g. "when is a gap analysis
       complete enough to hand to option framing?" -->

  ## Why this isn't decided yet
  <!-- one paragraph: no advisory engagement has closed yet against a maturity-assessment or
       gap-analysis deliverable specifically (cite the DEC-8 finding), so there's no lived
       experience to generalise from — same discipline dod-quality-gates.md itself models for the
       build tier: it doesn't invent gates it hasn't verified either. -->

  ## What it depends on
  <!-- links to the five methods/ files: gap-analysis.md (owned, could inform a real DoD sooner),
       and the four extension-point stubs (blocked on the technique existing at all) -->

  ## Until then
  <!-- one line: what an engagement should do in the absence of a formal DoD — fall back to the
       Decision Package's own five-part completeness check (decision-package SKILL.md R1), cited,
       not restated -->
  ```
  This mirrors the exact discipline `docs/services/*.md`'s four "no owning skill" pages already use
  (`agentic-framework-development.md` et al.: **"No skill in this catalogue owns X"** as a direct,
  bolded, first-sentence claim) — reused here as the repo's established idiom for "this is a real,
  checked gap," not invented fresh.

- **`methods/` stub template — one shape for all four extension points**, adapted directly from the
  `docs/services/*.md` "no owning skill" template already proven at four sites in this repo
  (verified: `agentic-framework-development.md`, `analytics-bi-connections.md`,
  `data-mappings-integration.md`, `training-capability-building.md` all share this shape):
  ```
  # <Technique name>

  ## What it is
  <!-- one paragraph, plain language, no jargon left unexplained -->

  ## Why it matters in a Deep-tier engagement
  <!-- one paragraph: what decision or option this technique would sharpen, tying back to
       decision-package's discovery-flow steps 2-4 (landscape reading / gap analysis / option
       framing) -->

  ## Current status
  **No skill in this repo owns <technique> today.** <!-- + one sentence naming what search was run
       to confirm this (mirrors docs/services/*.md's "confirmed by X search" discipline) -->

  ## Where it would fit
  <!-- pointer to advisory-runbook.md (which stage would invoke it) and consulting-dod.md (why its
       absence is named there too) -->
  ```
  `methods/gap-analysis.md` does **not** use this template — it is the one *pointer*, not a stub
  (DEC-9). Its shape is shorter: `## What it is` (one line) + `## Owning flow` (a direct citation of
  `skills/decision-package/references/discovery-flow.md` §3's gap-class table, reproduced as a link
  and a one-line paraphrase, never the table's content copied) + `## Where it fits`. The difference
  in shape between the pointer and the four stubs is itself the signal a reader needs — a stub that
  looked like a pointer would misrepresent an owned capability as an unowned one and vice versa.

- **`advisory-runbook.md` and `sales-runbook.md` share `opsx-runbook.md`'s narrative shape** (a
  numbered sequence of stages, each one pointing to the skill or doc that owns its content, never
  restating it — the same "runbook points, doesn't duplicate" discipline `opsx-runbook.md` states
  explicitly in its own opening line). Concretely:
  - `sales-runbook.md`: `1. Presale` → `2. Discovery & Onboarding (Light/Deep)` → `3. Contracting /
    hand-off` → `4. Repeat-client relationship` — each stage citing `engagement-lifecycle.md`'s
    matching section and `roles-and-raci.md`'s RACI cells, never restating either.
  - `advisory-runbook.md`: `1. Intake` (deciding persona, problem, outcome — cites discovery-flow §1)
    → `2. Landscape reading` (cites discovery-flow §2) → `3. Method selection` (cites `methods/`:
    which techniques apply, explicitly noting where a step 3 method is an unowned extension point)
    → `4. Gap analysis → option framing → sequencing → buy/build/defer` (cites discovery-flow §3-6 as
    one block — DEC-10 says the *sequencing* is fully knowable today, so this block is the runbook's
    substantive content, not a pointer) → `5. Decision Package production` (cites `decision-
    package` SKILL.md's five parts) → `6. Hand-off` (cites discovery-flow §7 execution brief).
    Step 4 is where DEC-10's "written for real" commitment actually shows up in the file; steps 1, 2,
    5, 6 are thin pointers by design, matching the source material's own depth.

- **`sales-dod.md`'s relocated content is a verbatim move of `dod-quality-gates.md` lines 54-64**
  (the Shipper's-DoD definition), followed by one new sentence citing the Disagreement rule
  (`dod-quality-gates.md#delivery--release`) rather than copying it — matching the proposal's DEC-7
  instruction exactly ("cites it, does not copy it").

- **`repeat-clients.md`'s content folds into `engagement-lifecycle.md`** as a same-named `## Repeat
  clients` section (heading text preserved verbatim from the source file's own `# Repeat clients`
  H1, demoted one level) — this was already decided by the EPIC's own Solution outline and What
  Changes (single destination file named once, `engagement-lifecycle.md`), not reopened here; the
  only planning-level addition is fixing the exact anchor (`#repeat-clients`) so the two live inbound
  links (`skills/semantic-consulting-coach/references/engagement-model.md` line 80,
  `docs/ai-coding/dod-quality-gates.md`'s sibling `solution-shipper.md`-style citations once moved)
  resolve to that section rather than a whole-file link.

- **Heading-anchor preservation rule.** Every moved file's internal heading text stays byte-identical
  unless DEC-8 specifically requires a wording change (the maturity-assessment correction in
  `engagement-lifecycle.md`) — because `discovery-and-onboarding.md`'s headings are cited by anchor
  from 9+ external sites (table above), a silent heading reword would break those anchors invisibly
  (no lint catches anchor drift, only whole-file 404s — see Error matrix). Where DEC-8 does change
  wording, the specific heading that changes is named in `tasks.md` so every anchor citing it is
  found and updated in the same task.

- **`docs/environment/` relative-link depth arithmetic**, verified by direct inspection: moving
  `docs/environment-setup.md` (currently depth-1 under `docs/`, using single `../` links to
  `README.md`, `AGENTS.md`, `spine/`, `openspec/specs/`, `prompts/`, `skills/`) into
  `docs/environment/setup.md` (depth-2) requires every one of those single-`../` links to become
  `../../`. Moving `docs/ai-coding/openspec-setup-guide.md` (already depth-2, using `../../` links)
  into `docs/environment/openspec-setup-guide.md` (also depth-2) requires **no change** to its
  outbound links — same depth, different depth-2 parent. `docs/dual-cli/` moves wholesale alongside
  `setup.md` into the same `docs/environment/` parent, so `setup.md`'s same-directory links to
  `dual-cli/setup-claude.md` etc. stay valid unchanged (both files move together, relative
  relationship preserved). This asymmetry — one file's links all shift, the other's don't move at
  all — is easy to get backwards; `tasks.md` calls it out explicitly per file rather than as one
  generic "fix relative links" instruction.

## Algorithm / approach

Structural moves in dependency order (see Decisions' write-order rationale), each move bundling
"copy content + fix the mover's own outbound links + note every known inbound site to fix in
group (g)":

1. `ai-coding/playbooks/` (4 files in, `dod-quality-gates.md` and `build-lifecycle.md`'s
   `../how-we-work/`-rooted internal links become same-domain links).
2. `ai-sales/` (`engagement-lifecycle.md` merge, `services/` move, `sales-presales.md` move, two new
   runbook/DoD files).
3. `ai-consulting/` (new runbook, new DoD scaffold, five `methods/` files, `technical-consultant.md`
   move).
4. `roles-and-raci.md` un-move to top-level `docs/`.
5. `dod-quality-gates.md` edit (remove Shipper's-DoD prose, add `sales-dod.md` citation).
6. `environment/` cluster (three items, per the depth-arithmetic decision above).
7. Cross-repo link sweep (the enumerated site list in Context) — done once, last, against final
   paths, to avoid re-touching a file twice.
8. Retire `docs/how-we-work/` (`git rm -r`) — only once 1-7 are confirmed.
9. Spec delta + sibling-supersession annotation.
10. Validation.

Idempotency: every step is a file move/create/edit against a fixed, named destination — re-running
an already-applied step is a no-op check ("does the destination already have this content?"), the
same standard `define-lifecycle-playbooks` used for its own docs-only change. Step 8 (the delete) is
the one step that is **not** safely re-runnable if run out of order — it is gated behind explicit
confirmation of 1-6 in `tasks.md`, mirroring `define-lifecycle-playbooks` task 1.1's sequencing gate
pattern.

### Anti-patterns

- ❌ **Writing real methodology content into `methods/data-maturity-assessment.md`,
  `wardley-mapping.md`, `enterprise-process-modelling.md`, or `semantic-maturity-assessment.md`.**
  The moment a stub grows past What-it-is / Why-it-matters / Current-status / Where-it-would-fit, the
  bet is overrun (proposal Rabbit-holes, Appetite). This is the highest-risk anti-pattern in this
  EPIC because it is the most tempting — a capable writer *can* draft a Wardley-mapping methodology,
  which is exactly why the template above fixes the ceiling structurally, not just by instruction.
- ❌ **Inventing acceptance criteria for `consulting-dod.md`.** The owner's own instruction ("mark it
  so I know what can be extended") is violated by any sentence that reads like a checklist item
  rather than a named unknown.
- ❌ **Deleting `docs/how-we-work/` before every destination is verified.** See the write-order
  dependency above — this is the one step where "move fast" directly causes data loss.
- ❌ **Hand-editing `.opencode/**` to fix a link.** It is a generated mirror
  (`make generate-opencode`); a hand-edit there drifts from `skills/**` and both CLIs' parity breaks
  silently until the next generation run overwrites it.
- ❌ **Retargeting a plain-text path mention in a sibling `openspec/changes/*/proposal.md` as if it
  were a live link.** Verified: none of the five sibling proposals contain actual markdown-link
  syntax to a moved path — they are historical prose describing what was true when written, per this
  repo's existing convention (matches `define-delivery-release-lifecycle`'s own "unlinked here for
  historical accuracy" precedent). Touching that prose is out of scope and risks silently rewriting a
  settled, already-shaped EPIC's own narrative.
- ❌ **A combined "map" file replacing `docs/how-we-work/overview.md`.** The proposal explicitly
  rejects this (What Changes: "no replacement 'map' file is created") — each domain's own
  lifecycle/methodology doc is the entry point now; resist the urge to rebuild the one-screen
  overview out of habit.
- ❌ **Renaming `docs/dual-cli/README.md`'s own file while relocating the folder.** Explicitly
  deferred (Rabbit-holes) — move the folder, leave every filename inside it untouched.
- ❌ **A fourth `ai-*` domain, or a fourth DoD file, invented to "complete the pattern."** Only three
  domains exist by direct observation (Rabbit-holes) — do not extrapolate.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| A link-retarget in group (g) misses a file | `repo_lint.broken_links` (blocking, `make validate`) catches every missed **markdown-link-syntax** site immediately — but it does **not** scan plain-text path mentions (verified: `_MD_LINK` regex only). A prose reference that names a moved path without `[text]` + `(path)` syntax will not be caught mechanically; task 10's validation step includes one manual `grep -rn` sweep for the literal strings `how-we-work`, `docs/services/`, `docs/environment-setup`, `ai-coding/openspec-setup-guide`, `docs/dual-cli` across the whole repo (outside `openspec/changes/*` and `.opencode/`) as the human-verified backstop for exactly this gap. |
| `dod-quality-gates.md`'s edit lands before `sales-dod.md` exists (mid-implementation ordering slip) | Task group (e) is sequenced strictly after (b) in `tasks.md`, and both are part of one change — never committed separately. If an implementer nonetheless commits (e) alone, the Disagreement-rule citation in `dod-quality-gates.md` would point at a file that doesn't exist yet; `broken_links` catches this the same way as any other dangling link, so the failure is mechanically caught even if the sequencing discipline slips. |
| A moved file's heading text changes incidentally (not per DEC-8) and an external anchor citing it silently 404s | Anchors are not scanned by `broken_links` (it only checks the pre-`#` file path, per the tool's own `target.split("#")[0]` logic) — a heading rename inside a moved file is **invisible to CI**. The heading-anchor-preservation rule (Decisions) is the only guard; task 10 adds a manual check of every anchor listed in this design's Context table against the moved file's final headings. |
| `.opencode/**` is hand-edited instead of regenerated | Drifts from `skills/**`; the next `make generate-opencode` run silently overwrites the hand-edit, and until then the two CLIs' catalogues disagree. Task 7 ends with `make generate-opencode`, not a manual `.opencode/` edit. |
| `define-lifecycle-playbooks` is archived by someone else mid-implementation of this EPIC | Its capability would then live in `openspec/specs/lifecycle-playbooks/spec.md` instead of its own change dir — the annotation target in Decisions' supersession resolution moves from that change's `proposal.md` to a proper `## REMOVED`/`## MODIFIED` delta in `define-ai-domains/specs/lifecycle-playbooks/spec.md` against the now-archived durable spec. Task 9 checks `openspec/specs/lifecycle-playbooks/` for existence immediately before writing the annotation, and switches mechanism if it now exists. |
| The `docs/environment/` depth-arithmetic (Decisions) is applied backwards — `openspec-setup-guide.md`'s already-correct `../../` links get an erroneous extra `../` added "for consistency" with `setup.md`'s fix | Every `../../`-prefixed link in the moved `openspec-setup-guide.md` would then 404 (resolving one level above the repo root). Task 6 states the two files' link-depth deltas separately and explicitly (zero change vs. one extra `../`), not as one shared instruction, specifically to prevent this. |

## Risks / Trade-offs

- **[Risk]** Relocation churn across ~25 link sites is mechanically large for a "documentation-only"
  Medium-appetite EPIC. → **Mitigated**: every site was enumerated by direct `grep` against actual
  markdown-link syntax during this design (Context, above) rather than left for implementation to
  discover — the count is now known and bounded, not a source of surprise mid-task.
- **[Risk]** Folding `repeat-clients.md` into `engagement-lifecycle.md` reduces that content's
  standalone addressability (one whole-file link becomes one section-anchor link). →
  **Accepted, not mitigated further**: this was the EPIC's own Solution-outline decision, not a new
  choice; the mitigation available (preserve the heading verbatim as an anchor) is already applied.
- **[Trade-off]** The root `README.md`'s Documentation table grows from one `how-we-work` row + one
  `services` row to three domain rows (`ai-coding`, `ai-sales`, `ai-consulting`) + a `roles-and-raci`
  row + an `environment` row — net +3 rows. → **Accepted**: this is the direct, intended consequence
  of naming three domains instead of one umbrella; a shorter table would misrepresent the new
  structure.
- **[Trade-off]** `advisory-runbook.md` step 4 (gap analysis → buy/build/defer) is written with real
  depth while steps 1, 2, 5, 6 stay thin pointers — an asymmetric file. → **Accepted**: matches DEC-10
  exactly (the gap is in the *techniques*, not the *sequencing script*); a uniformly-thin or
  uniformly-deep runbook would misrepresent where this EPIC's actual knowledge boundary sits.

## Content-recovery check (resolved, not open)

Before implementation, this PLAN was checked against the repo's state at git tag
`pre-lifecycle-redefinition-2026-07-25` (the point before any of this multi-round rewrite began), to
catch anything genuinely good that got silently dropped across the rounds. Verdict: the direction is
sound — only two small items had no successor anywhere and are now folded into tasks.md 1.4/1.5: the
old `ai-coding-methodology.md` §7 practitioner-experience notes (roadmap-driven development, planning
mode first, stating project structure upfront, a "needs manual attention" list) and one `/context`
token-monitoring tip from the old `ai-coding-setup-guide.md` §8 troubleshooting table. Both land in
`docs/ai-coding/opsx-runbook.md`, adapted to the current three-wrapper agent model. Everything else
checked (v1's other content, `two-tier-methodology.md`→`build-lifecycle.md`, the engagement docs'
two rewrites, `dod-quality-gates.md`, `opsx-runbook.md`, `openspec-setup-guide.md`,
`environment-setup.md`, `dual-cli/`) carried forward cleanly with no loss.

## Open Questions

Parked, per the proposal's own Rabbit-holes / Known-gaps — not guessed at here:

- **Wardley mapping / enterprise-process-modelling / maturity-assessment real technique content** —
  a future EPIC's appetite (Rabbit-holes item 1); this PLAN only fixes the stub template's ceiling.
- **`docs/dual-cli/README.md`'s own file-naming exception** — explicitly deferred (Rabbit-holes item
  4); the folder move happens, the internal rename does not.
- **Agent wrappers for any non-Builder role** (including the Work-Shaper-highest-priority note) —
  owned by `define-roles-and-raci`'s own Open Question / Known-gaps, reopens only once a role has
  been exercised on a real engagement; this EPIC neither answers nor advances it, and the
  `roles-and-raci.md` un-move carries that section forward unchanged.
- **Where do `docs/how-we-work/overview.md`'s two Known-gaps rows whose named owner was "this doc's
  successor" land**, now that no single successor "map" file exists (per this EPIC's own explicit
  rejection of a combined map)? Specifically: *per-plane diagrams* (business/software/model/
  architecture/training, individually) and *single-source generation of the playbook set*. The other
  four rows in that table already have a named owner that is a surviving file (`discovery-and-
  onboarding.md`'s own Known-gaps, `build-lifecycle.md`, `roles-and-raci.md`) and relocate
  automatically with their owning file; these two do not. Not designed here — flagged for the
  implementer to either re-home (most likely candidate: a short "Known gaps" note in each domain's
  own runbook, or `ai-coding/build-lifecycle.md` for the per-plane-diagram one specifically, since it
  already carries the SDLC diagram) or explicitly re-park with a named next owner, rather than
  silently dropped.
