> Derived from EPIC `step-by-step-install-guide`

## 1. Claude Code runbook

- [x] 1.1 Rewrite `docs/dual-cli/setup-claude.md` into the literal numbered sequence from
      design.md's Algorithm/approach: prerequisites → add marketplace → install bundles → install
      mandatory external deps (superpowers, ponytail, stream-coding, OpenSpec — each with its
      upstream link inline) → root-binding confirmation → spine command registration
      (`openspec update --tools claude`) → optional hooks/MCP → verification.
- [x] 1.2 Each step contains exactly one command block or link plus ≤1 line of rationale — no
      forward references the reader must resolve to act.
- [x] 1.3 Version numbers/pins link to `docs/environment-setup.md` instead of being restated.
- [x] 1.4 Add the closing verification step (e.g. list installed plugins/bundles, or the
      equivalent Claude-native check) with the expected output described.

## 2. opencode runbook

- [x] 2.1 Rewrite `docs/dual-cli/setup-opencode.md` into the same linear shape, opencode-native
      commands only (no `/plugin` forms).
- [x] 2.2 Mirror steps 1.2–1.4 for the opencode runbook (single-action steps, linked version pins,
      closing verification step with expected output).

## 3. Pointer docs

- [x] 3.1 Update `README.md`'s Installation section to point at the two runbooks as *the*
      step-by-step, trimming any restated steps to a one-line pointer.
- [x] 3.2 Update `docs/environment-setup.md` wording (not its dependency table) to reference the
      runbooks as the step sequence, keeping itself as the canonical version-pin source per
      design.md's Decisions.

## 4. Validate

- [x] 4.1 Confirm all internal links in the rewritten files resolve (`make validate` doc-link
      check, or manual link check if not covered). `make validate` itself can't run in this
      environment (no `.venv`); ran a manual link/anchor resolution check instead — all resolve.
- [x] 4.2 Manually walk both runbooks top to bottom on a clean read to confirm no step requires
      information from a step that comes later.

## 5. Follow-up refinements (from live review)

- [x] 5.1 Drop the trailing "Pinned versions & gaps" section from both runbooks — non-actionable
      filler on Claude (no gaps), redundant with Step 6 on opencode; kept the one real opencode
      gap (`persist-before-compaction`) folded into the Step 9 verify text instead.
- [x] 5.2 Add a step in both runbooks linking to
      `skills/project-setup/references/spine-projection.md` — registering `/opsx:*`/`opsx-*`
      commands (Step 6) is not the same as getting the pinned `meaningfy` schema into a repo
      (a separate `project-setup` projection), and this wasn't previously called out.
- [x] 5.3 Rewrite `docs/dual-cli/mcp-setup.md` into the same literal-step format (decide what you
      need → open your config file → install package + add block, per server → verify), and add
      the missing local-package install commands (GitNexus `npm install -g gitnexus`, Odoo
      `pip install odoo-mcp-multi`) that the original version omitted (it only showed JSON config,
      assuming the package already existed).
- [x] 5.4 Link `docs/dual-cli/mcp-setup.md` from `README.md`'s Installation section — it had no
      direct link before (only an indirect mention via the `docs/dual-cli/` pointer row).

## 6. IA cleanup — audience separation (from live review)

- [x] 6.1 Fix `docs/environment-setup.md` §2 (External dependencies): it had Claude-only `/plugin`
      commands baked into a table presented as CLI-agnostic canon — the actual cause of "this file
      only offers Claude instructions". Dropped the per-CLI install-command column; the table now
      states what/why/source-version only, and each runbook's Step 4 owns the per-CLI command.
- [x] 6.2 Fix `stream-coding`'s install everywhere it's mentioned (`environment-setup.md`,
      `setup-claude.md` 4d, `setup-opencode.md` 4c): it was "install as an external skill" with no
      command. Found its real upstream (`frmoretto/stream-coding`, a single `SKILL.md`) and gave
      the actual clone + copy-into-`.claude/skills/` commands.
- [x] 6.3 Clarify "Step 7 — Project the meaningfy schema" in both runbooks: it reads as a shell
      step but the action is invoking the `project-setup` *skill* conversationally. Spelled out
      that it has no CLI command and gave an example trigger phrase to say to the agent.
- [x] 6.4 Corrected two stale compatibility claims found while fixing 6.2: `superpowers` and
      `ponytail` were documented as opencode-installed via a `.claude/skills/` copy
      (`compatibility.md`); both actually ship their own native opencode plugin
      (`{"plugin": [...]}` in `opencode.json`) per their own current upstream docs. Fixed
      `compatibility.md`'s two rows and `setup-opencode.md`'s Step 4a/4b to the real commands.
      `stream-coding` (plain `SKILL.md`, no plugin) was the only one where the `.claude/skills/`
      copy claim was actually correct — left as-is.
- [x] 6.5 Added a full "Step 4 — Install the mandatory external dependencies" to
      `setup-opencode.md` — it didn't have one at all (superpowers/ponytail/stream-coding/OpenSpec
      were only covered on the Claude side); renumbered opencode Steps 4-9 → 5-10.
- [x] 6.6 Trim `README.md`'s Installation section to a single pointer at
      `docs/environment-setup.md` — it previously duplicated the runbook table directly, which let
      a reader bypass the documented install hierarchy (README → environment-setup.md → runbooks)
      that `dual-cli-distribution`'s "Single-home dual-CLI authoring rule" requirement already
      mandates.
- [x] 6.7 Reframe `docs/dual-cli/README.md` as a contributor-only annex (audience line added);
      removed the setup-claude/setup-opencode/mcp-setup rows from its table (they're install-track,
      reached via `environment-setup.md`, not this page) per the same spec requirement's "reference
      annex, not a competing install hub" language.
- [x] 6.8 Add an explicit audience line to `mapping.md`, `compatibility.md`, and
      `body-agnosticism-audit.md` (all: skillery contributors, not installers) — evaluated merging
      `mapping.md` (generation contract for skillery's own artifacts) with `compatibility.md`
      (external-dependency support status) and decided against it: different questions, ~15+
      existing cross-references each from other contributor docs, low benefit for the blast radius.
- [x] 6.9 Restore MCP discoverability from `environment-setup.md` — trimming §2's dependency table
      (6.1) left `mcp-setup.md` reachable only via two of its seven servers' rows (gitnexus,
      context7); Atlassian/Google Workspace/Odoo/Neo4j/MongoDB had no path in from this page at
      all. Added a named "MCP servers (optional)" subsection linking `dual-cli/mcp-setup.md`
      directly. Left `README.md` without a *direct* mcp-setup.md link by design — it already
      mentions MCP in its one-paragraph pointer to `environment-setup.md`; a direct link would
      re-open the same bypass-the-hierarchy problem 6.6 just closed.

## Roadmap

- [x] 1.1 · [x] 1.2 · [x] 1.3 · [x] 1.4 · [x] 2.1 · [x] 2.2 · [x] 3.1 · [x] 3.2 · [x] 4.1 · [x] 4.2 ·
      [x] 5.1 · [x] 5.2 · [x] 5.3 · [x] 5.4 · [x] 6.1 · [x] 6.2 · [x] 6.3 · [x] 6.4 · [x] 6.5 ·
      [x] 6.6 · [x] 6.7 · [x] 6.8 · [x] 6.9

## Verification

Manual top-to-bottom read of each runbook (no forward references, one action per step, ends in a
verification step) plus `make validate` for link/doc integrity.
