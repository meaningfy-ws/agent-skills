# Setup — Claude Code

Install the skillery catalogue on Claude Code, one step at a time. Follow every step in order —
you do **not** need the opencode page. Each step is one command or one link; run it, then move on.
The source→CLI contract behind these steps is in [`mapping.md`](mapping.md).

## Step 1 — Check your prerequisites

- [Claude Code](https://docs.claude.com/claude-code) (CLI, desktop, or IDE) installed.
- Node ≥ 18, for OpenSpec (Step 4c):
  ```bash
  node -v
  ```

## Step 2 — Add the skillery marketplace

```bash
/plugin marketplace add meaningfy-ws/skillery
```

## Step 3 — Install the bundle(s) for your role

Pick your role(s) from the table, then run the matching install command(s). Everyone installs
`meaningfy-core`; add the rest only if that role is yours.

| Bundle | Install if you… |
|---|---|
| `meaningfy-core` | …do anything (cross-cutting basics) — **always install this one** |
| `meaningfy-building` | …build software with the spine |
| `meaningfy-architecture` | …design systems or model a domain |
| `meaningfy-consulting` | …do advisory / front-of-funnel work |

```bash
/plugin install meaningfy-core@meaningfy-skillery
/plugin install meaningfy-building@meaningfy-skillery   # repeat with the other bundles you need
```

## Step 4 — Install the mandatory external dependencies

These are referenced by skillery's skills but are separate installs. Pinned versions and the
full optional-dependency list live in
[`environment-setup.md`](../environment-setup.md#2-external-dependencies) — this step only covers
what's mandatory.

**4a. superpowers** — TDD, systematic debugging, verification-before-completion, brainstorming.
```bash
/plugin install superpowers@claude-plugins-official
```

**4b. ponytail** — YAGNI / minimal-code discipline. Upstream: https://github.com/DietrichGebert/ponytail
```bash
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

**4c. OpenSpec** — the spine engine (`/opsx:*` commands). Upstream: https://github.com/Fission-AI/OpenSpec.
Pinned version: [`../../spine/openspec-version.txt`](../../spine/openspec-version.txt).
```bash
npm i -g @fission-ai/openspec
```

**4d. stream-coding** — the documentation-first build method. Upstream:
https://github.com/frmoretto/stream-coding (a single `SKILL.md`, not a plugin package):
```bash
git clone https://github.com/frmoretto/stream-coding /tmp/stream-coding
mkdir -p ~/.claude/skills/stream-coding
cp /tmp/stream-coding/SKILL.md ~/.claude/skills/stream-coding/SKILL.md   # adjust the source path if the repo's layout differs
```

## Step 5 — Confirm the root binding

Nothing to install — both files already ship in the repo you're working in. Just confirm:
- `CLAUDE.md` exists and points to `AGENTS.md` (the canonical, CLI-agnostic operating manual).
- `AGENTS.md` exists alongside it.

## Step 6 — Register the spine commands

Run this once per repo that uses the spine:
```bash
openspec update --tools claude    # registers /opsx:propose, /opsx:apply, …
```

## Step 7 — Project the `meaningfy` schema into a repo

Step 6 only registers the `/opsx:*` *commands* — it does not give you skillery's forked `meaningfy`
OpenSpec schema (the templates and rules behind `openspec/config.yaml`'s `schema: meaningfy`).
That's a **separate action**: in the target repo, ask Claude Code to run the **`project-setup`**
skill — e.g. say *"scaffold this repo with project-setup"* or *"project the spine / set up
openspec here"* (it's a conversational skill invocation, not a shell command, so there is no
`/plugin`-style command for it). It then copies `openspec/schemas/meaningfy/` into the repo as a
frozen, per-repo **pinned copy** and writes `openspec/config.yaml` to point at it. What exactly
gets projected, and how to refresh the pinned copy later (re-run `project-setup`, review the diff,
never silently overwritten):
[`../../skills/project-setup/references/spine-projection.md`](../../skills/project-setup/references/spine-projection.md).

## Step 8 — Optional: hooks, MCP servers, extra plugins

- **Hooks** — written for you by `project-setup` when you scaffold a repo. Reference:
  [`../../hooks/README.md`](../../hooks/README.md).
- **MCP servers** (GitNexus, Atlassian, Google Workspace, Odoo, Neo4j, MongoDB, context7, …) —
  install one by one, per-tool packages/links and config templates in
  [`mcp-setup.md`](mcp-setup.md).
- **Optional plugins** (`commit-commands`, `code-review`) — see the table in
  [`environment-setup.md`](../environment-setup.md#2-external-dependencies).

## Step 9 — Verify

Run:
```bash
/plugin
```
Confirm `meaningfy-core` (and any other bundle you installed in Step 3) shows as **enabled**. Then
confirm the spine registered by running `/opsx:propose` — it should prompt you for a change
description rather than say the command is unknown.

There are no recorded Claude-side capability gaps; if you're curious what differs on opencode, see
[`compatibility.md`](compatibility.md).
