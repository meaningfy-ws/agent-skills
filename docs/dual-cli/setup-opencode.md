# Setup — opencode

Install the skillery catalogue on opencode, one step at a time. Follow every step in order — you
do **not** need the Claude Code page. Each step is one command or one link; run it, then move on.
The source→CLI contract behind these steps is in [`mapping.md`](mapping.md).

## Step 1 — Check your prerequisites

- opencode installed: https://opencode.ai
- Node ≥ 18:
  ```bash
  node -v
  ```
- Git (npm fetches the skillery package directly from the Git repository).

## Step 2 — List available bundles

```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode list
```

## Step 3 — Install the bundle(s) for your role

Pick your role(s) from the table, then install. Everyone installs `meaningfy-core`; add the rest
only if that role is yours.

| Bundle | Install if you… |
|---|---|
| `meaningfy-core` | …do anything (cross-cutting basics) — **always install this one** |
| `meaningfy-building` | …build software with the spine |
| `meaningfy-architecture` | …design systems or model a domain |
| `meaningfy-consulting` | …do advisory / front-of-funnel work |

Install one or more bundles into the current project:
```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode install meaningfy-core meaningfy-building --project
```
Or globally, for every project:
```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode install meaningfy-core --global
```
Restart opencode afterwards so it refreshes skill discovery. Want to preview first? Add `--dry-run`
to either command — it prints what it *would* copy without touching disk. Other install routes (the
opencode plugin alias, a direct-checkout dev mode) are documented in this file's
[Alternate install routes](#alternate-install-routes) section — use the installer above unless you
have a specific reason to use one of those.

## Step 4 — Install the mandatory external dependencies

These are referenced by skillery's skills but are separate installs. `superpowers` and `ponytail`
each ship a native opencode plugin (add one line to `opencode.json`); `stream-coding` is a plain
skill file (opencode reads `.claude/skills/` natively, so the install is: put the file there);
`openspec` is a global npm package, identical to Claude Code. Pinned versions and the full
optional-dependency list live in
[`environment-setup.md`](../environment-setup.md#2-external-dependencies) — this step only covers
what's mandatory.

**4a. superpowers** — TDD, systematic debugging, verification-before-completion, brainstorming.
Upstream: https://github.com/obra/superpowers. Add to `opencode.json` (global or project-level):
```json
{ "plugin": ["superpowers@git+https://github.com/obra/superpowers.git"] }
```
Restart opencode; verify by asking it "tell me about your superpowers". Full opencode install
notes (updating, troubleshooting): https://github.com/obra/superpowers/blob/main/docs/README.opencode.md.

**4b. ponytail** — YAGNI / minimal-code discipline. Upstream: https://github.com/DietrichGebert/ponytail.
Add to `opencode.json`:
```json
{ "plugin": ["@dietrichgebert/ponytail"] }
```

**4c. stream-coding** — the documentation-first build method. Upstream:
https://github.com/frmoretto/stream-coding (a single `SKILL.md`, not a package):
```bash
git clone https://github.com/frmoretto/stream-coding /tmp/stream-coding
mkdir -p ~/.claude/skills/stream-coding
cp /tmp/stream-coding/SKILL.md ~/.claude/skills/stream-coding/SKILL.md   # adjust the source path if the repo's layout differs
```

**4d. OpenSpec** — the spine engine (`opsx-*` commands). Upstream: https://github.com/Fission-AI/OpenSpec.
Pinned version: [`../../spine/openspec-version.txt`](../../spine/openspec-version.txt).
```bash
npm i -g @fission-ai/openspec
```

## Step 5 — Scope global skills per project (optional)

opencode has no per-project UI toggle for globally installed skills — configure
`permission.skill` in the project's `opencode.json` instead, to reduce agent selection noise. Two
patterns (allow-all-except vs deny-all-except) are shown in
[Scoping skill permissions](#scoping-skill-permissions) below.

## Step 6 — Confirm the root binding

Nothing to install. opencode reads `AGENTS.md` natively — no pointer file is required. Just
confirm `AGENTS.md` exists at the repo root.

## Step 7 — Register the spine commands

Run this once per repo that uses the spine:
```bash
openspec update --tools opencode    # registers opsx-propose, opsx-apply, …
```
(The `/opsx:<id>` form on Claude Code is `opsx-<id>` here.)

## Step 8 — Project the `meaningfy` schema into a repo

Step 7 only registers the `opsx-*` *commands* — it does not give you skillery's forked `meaningfy`
OpenSpec schema (the templates and rules behind `openspec/config.yaml`'s `schema: meaningfy`).
That's a **separate action**: in the target repo, ask your agent to run the **`project-setup`**
skill — e.g. say *"scaffold this repo with project-setup"* or *"project the spine / set up
openspec here"* (it's a conversational skill invocation, not a shell command). It then copies
`openspec/schemas/meaningfy/` into the repo as a frozen, per-repo **pinned copy** and writes
`openspec/config.yaml` to point at it. What exactly gets projected, and how to refresh the pinned
copy later (re-run `project-setup`, review the diff, never silently overwritten):
[`../../skills/project-setup/references/spine-projection.md`](../../skills/project-setup/references/spine-projection.md).

## Step 9 — Optional: hooks, MCP servers

- **Hooks** — written for you by `project-setup` as `.opencode/plugin/` bindings. Reference:
  [`../../hooks/README.md`](../../hooks/README.md).
- **MCP servers** (GitNexus, Atlassian, Google Workspace, Odoo, Neo4j, MongoDB, context7, …) —
  install one by one into `opencode.json` under `mcp`; per-tool packages/links and config
  templates in [`mcp-setup.md`](mcp-setup.md).

## Step 10 — Verify

Restart opencode, then check the installer's own record of what's there — use the **same**
`--project`/`--global`/`--target` flag you installed with in Step 3:
```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode status --project
```
Expected output: `Installed bundles:` followed by each bundle you installed and the catalogue
version it's pinned to (not `Installed bundles: none`). Then confirm the spine registered by
running `opsx-propose` — it should prompt you for a change description rather than say the command
is unknown.

One recorded gap worth knowing before you rely on it: `persist-before-compaction` has no `PreCompact`
event on opencode and degrades to a `session.idle` binding. Full matrix (every other dependency's
status): [`compatibility.md`](compatibility.md).

---

## Reference

### Alternate install routes

**opencode plugin alias** — the repository is also an installable opencode plugin; the package
alias selects the bundle:
```bash
opencode plugin --global \
  'meaningfy-core@git+https://github.com/meaningfy-ws/skillery.git#develop'
```
The plugin can alternatively be configured under its canonical package name and passed one or more
bundle names through plugin options or `MEANINGFY_SKILLERY_BUNDLES`. This route uses opencode's
plugin `config()` hook to add generated skill directories to `skills.paths`; some opencode versions
have initialized or cached skill discovery before that hook became visible, so the Step 3 installer
is the compatibility-safe default — this route is retained for versions where plugin-provided skill
paths are discovered correctly.

**Direct checkout** (repository development) — point `OPENCODE_CONFIG_DIR` at the generated tree to
expose the whole catalogue, unfiltered by bundle:
```bash
git clone --branch develop https://github.com/meaningfy-ws/skillery.git
OPENCODE_CONFIG_DIR="$PWD/skillery/.opencode" opencode
```

**Uninstall / update a bundle** — rerun the Step 3 install command to update; uninstall with:
```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode uninstall meaningfy-core --global
```

The installer records ownership in `.skillery-manifest.json` and refuses to replace unrelated local
skills unless `--force` is supplied.

### Scoping skill permissions

* **Blacklist — allow all except selected skills.** Use when most global skills are relevant:
  ```json
  {
    "$schema": "https://opencode.ai/config.json",
    "permission": {
      "skill": {
        "*": "allow",
        "explanatory-writing": "deny",
        "technical-writing": "deny"
      }
    }
  }
  ```

* **Allowlist — deny all except selected skills.** Use when the project needs only a small, known
  subset:
  ```json
  {
    "$schema": "https://opencode.ai/config.json",
    "permission": {
      "skill": {
        "*": "deny",
        "guardrails": "allow",
        "meaningfy-git-workflow": "allow"
      }
    }
  }
  ```

Rules are evaluated in order and the last matching rule wins, so place the catch-all `*` rule
before specific skill names. These settings affect only the current project; the global skills
remain installed and available to other projects.
