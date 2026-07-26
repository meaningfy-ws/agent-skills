# Hook bindings — how each mechanism is implemented

[`inventory.yaml`](inventory.yaml) is the single source of hook *intent*. This page is the
**binding reference**: how an intent's `mechanism` becomes a concrete, projectable artifact, and how
`project-setup` writes those artifacts into a target repo per CLI. It points at templates; it does
not duplicate the inventory.

The rule the whole design turns on: **one intent, mechanism decides duplication.**
`git` and `ci` bindings are CLI-agnostic — a *single* shared implementation serves both Claude Code
and opencode. Only `agent` bindings render per CLI, and even then the *intent* is shared; only the
binding file format differs.

## `git` mechanism — one shared implementation (tasks 2.4)

Every `git`-mechanism intent maps to a hook under a **single git-hook manager config**, committed
once at the repo root. The manager is CLI-agnostic by nature — git runs the hook regardless of which
agent CLI is in use, so there is **no per-CLI copy**.

- **Manager:** `pre-commit` (already the Meaningfy default). The shared config is
  [`../skills/project-setup/assets/templates/root/dot-pre-commit-config.yaml`](../skills/project-setup/assets/templates/root/dot-pre-commit-config.yaml),
  rendered to `.pre-commit-config.yaml` and installed with `pre-commit install`.
- **Trigger → git stage** mapping is read straight from each binding's `trigger`:

  | inventory `trigger` | pre-commit stage |
  |---|---|
  | `commit-msg`, `prepare-commit-msg` | `commit-msg` / `prepare-commit-msg` |
  | `pre-commit` | `pre-commit` (default) |
  | `pre-push` | `pre-push` |
  | `post-merge`, `pre-rebase` | `post-merge` / `pre-rebase` |

- The Meaningfy-specific git intents (`conventional-commits`, `openspec-strict`,
  `validate-precommit`, `spec-link-integrity`, …) are `repo: local` hooks that shell out to the
  existing `make` targets (`make validate`, `openspec validate --all --strict`) — no logic is
  re-implemented in the hook.

**Branch-protection** (`protect-base-branches`) has both a `git` binding (local pre-commit guard)
and a `ci` binding (server-side branch protection); the `ci` half is the authoritative one.

## `ci` mechanism — one shared PR check (tasks 2.4)

`ci`-mechanism intents (`parity-check`, `reference-discipline`, `import-linter-contracts`'s PR half,
the phase-gate reviews) are GitHub Actions jobs that call `make` targets. Shared across CLIs — CI
does not know or care which agent authored the branch. Templates live in
[`../skills/project-setup/assets/templates/ci/`](../skills/project-setup/assets/templates/ci/)
(`ci.yaml.tmpl` calls `make validate`).

## `agent` mechanism — same intent, per-CLI binding (task 2.5)

`agent`-mechanism intents fire inside the agent runtime (PreToolUse, PostToolUse, Stop,
SessionStart, …). The **intent is shared**; the binding is rendered into each targeted CLI's native
format. The two bindings are *not* required to be byte-identical — only behaviourally equivalent.

**Claude Code** — `.claude/settings.json` `hooks` array. One matcher per event:

```jsonc
// agent intent `impact-before-edit` (PreToolUse on Edit) → Claude binding
{ "hooks": { "PreToolUse": [
  { "matcher": "Edit|Write",
    "hooks": [{ "type": "command", "command": "scripts/hooks/impact-before-edit.sh" }] } ] } }
```

**opencode** — a plugin under `.opencode/plugin/` exporting the equivalent event handler:

```js
// .opencode/plugin/impact-before-edit.js — same intent, opencode's plugin-hook shape
export const ImpactBeforeEdit = async ({ project, client }) => ({
  "tool.execute.before": async ({ tool }, output) => {
    if (tool === "edit" || tool === "write") { /* run impact, block on HIGH/CRITICAL */ }
  },
})
```

The shared part is the **script the binding calls** (`scripts/hooks/<intent>.sh`) — written once,
invoked by both bindings. Only the thin event-wiring differs per CLI.

| inventory `trigger` | Claude event | opencode plugin event |
|---|---|---|
| `PreToolUse(Edit)` | `PreToolUse` matcher `Edit\|Write` | `tool.execute.before` |
| `PostToolUse(Edit)` | `PostToolUse` matcher `Edit\|Write` | `tool.execute.after` |
| `Stop` | `Stop` | `session.idle` |
| `SessionStart` | `SessionStart` | `session.start` |
| `UserPromptSubmit` | `UserPromptSubmit` | `chat.message` |
| `PreCompact` | `PreCompact` | (no native equivalent — recorded gap) |

`PreCompact` has no opencode equivalent at the pinned version → recorded as a gap in
[`../docs/environment/dual-cli/compatibility.md`](../docs/environment/dual-cli/compatibility.md); the `persist-before-compaction`
intent degrades to a `Stop`/`session.idle` binding on opencode.

## Projection at setup (task 2.6)

`project-setup` reads `inventory.yaml` and, for a repo targeting one or more CLIs, writes:

1. the **shared** git-hook config (`.pre-commit-config.yaml`) — **once**, regardless of CLI count;
2. the **shared** CI workflow(s) — once;
3. the shared hook **scripts** (`scripts/hooks/<intent>.sh`) — once;
4. the **agent** bindings **per targeted CLI** — Claude `settings.json` hooks for a Claude target,
   `.opencode/plugin/*.js` for an opencode target.

So a Claude-only repo gets (1)+(2)+(3)+Claude bindings; a dual-target repo additionally gets the
opencode plugin bindings — and the git/CI layer is never duplicated.

> Scope note: `project-setup` today renders the Claude agent layer (`settings.json`) and is
> `CLAUDE.md`-canonical. Aligning its root-binding convention with this change's AGENTS-canonical
> model (DEC-12) and adding the opencode agent-binding renderer are tracked as the project-setup
> reconciliation follow-up, not this foundation change.
