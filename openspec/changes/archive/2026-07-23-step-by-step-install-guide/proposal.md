# EPIC: Linear, copy-paste install checklist per CLI

## Appetite

Small — a documentation restructuring, no code or schema changes. One to two focused doc edits.

## Why

The current install path (`README.md` → `docs/environment-setup.md` → `docs/dual-cli/setup-*.md`)
is correct in content but organized as reference prose: a reader has to jump between three files,
resolve cross-references, and infer which commands are theirs (Claude vs opencode) and in what
order to run them. A first-time installer wants one file, one CLI's steps, numbered top to bottom,
each step naming the exact command or link and nothing else — no synthesis required.

## Solution outline

Add a single linear walkthrough per CLI that a first-time installer can follow start to finish
without branching or cross-referencing: `docs/dual-cli/setup-claude.md` and
`docs/dual-cli/setup-opencode.md` become the literal step-by-step (Step 1, Step 2, …), each step
carrying the exact runnable command, the external link where relevant (GitHub repo for `openspec`,
`ponytail`, `superpowers`, docs URL for the CLI itself), and a one-line "why". A final verification
step confirms the install worked (a command whose output the reader can check against). `README.md`
and `docs/environment-setup.md` keep their existing role (front door / canon reference) and point
into the walkthrough rather than duplicating its steps.

No new mechanism, no new tooling — this is a rewrite of existing install docs into a stricter,
more literal format, using content and commands that already exist in `README.md` and
`docs/environment-setup.md` today.

## Key decisions

- **DEC-1**: The per-CLI runbooks (`docs/dual-cli/setup-claude.md`, `setup-opencode.md`) are the
  target of the rewrite, not a new file — they already own "per-CLI setup" per the
  `dual-cli-distribution` spec's "Per-CLI documentation split" requirement; adding a competing
  quickstart file would create a second install hub.
- **DEC-2**: Each step names one runnable artifact — a shell command, a slash command, or an
  external link — never a paragraph the reader must interpret into an action.
- **DEC-3**: A verification step ends each runbook (e.g. confirm the bundle/skill is visible,
  confirm `openspec --version` or the equivalent), so "did it work" isn't left to the reader.

## Rabbit-holes

- Don't re-derive the dependency list or version pins — reuse the existing table in
  `docs/environment-setup.md` (superpowers, stream-coding, ponytail, `@fission-ai/openspec`,
  optional commit-commands/code-review/gitnexus/context7); only the *presentation* changes.
- Don't fork content between `README.md` and the runbooks — the runbooks own the step sequence,
  `README.md` keeps its short pointer table.

## No-gos

- No change to which bundles/dependencies exist, their versions, or the marketplace/plugin
  mechanics themselves.
- No new install script, Makefile target, or automation — this is documentation only.
- No changes to `docs/dual-cli/mapping.md` or `compatibility.md` content (may be linked from the
  new steps, not rewritten).
- Not touching the `project-setup` skill's brownfield/scaffolding behavior — only how a human is
  walked through *installing the catalogue itself*.

---

## What Changes

- Rewrite `docs/dual-cli/setup-claude.md` as a strict numbered checklist: prerequisites →
  marketplace + bundle install commands → mandatory external deps (with GitHub links) → root
  binding confirmation → spine command registration → optional hooks/MCP → a verification step.
- Rewrite `docs/dual-cli/setup-opencode.md` in the same linear shape, opencode-native at each step.
- Update `README.md`'s Installation section and `docs/environment-setup.md` to point at the
  runbooks as *the* step-by-step, instead of restating overlapping steps.

## Capabilities

### New Capabilities
(none — this modifies how the existing dual-cli documentation capability presents its install path)

### Modified Capabilities
- `dual-cli-distribution`: the "Per-CLI documentation split" requirement gains a scenario requiring
  the per-CLI runbook to be a literal numbered sequence (one action per step, command or link,
  ending in a verification step) rather than narrative reference prose.

## Impact

- Affected files: `docs/dual-cli/setup-claude.md`, `docs/dual-cli/setup-opencode.md`,
  `README.md` (Installation section), `docs/environment-setup.md` (pointer wording only).
- No code, schema, or CI changes. No effect on `make validate` beyond existing doc-link checks.
