# Setup — opencode

Install the Skillery catalogue on OpenCode. Follow this page end to end — you do **not** need the
Claude setup page. The source-to-CLI contract is in [`mapping.md`](mapping.md).

> Pinned OpenCode version: `.opencode-version`.
> Catalogue version: `VERSION`.
> These instructions target OpenCode's documented `.opencode/skills`, `.opencode/agents`,
> `.opencode/commands`, and `opencode.json` conventions. Re-confirm them on each OpenCode version
> bump.

## 1. Install bundles

### Prerequisites

- OpenCode
- Node.js 18 or newer
- Git, because npm fetches the package directly from the Git repository

### Recommended: bundle installer

The repository ships a small installer that reads the generated `.opencode/bundles.json` manifest
and copies only the selected skills into an OpenCode discovery directory. It records ownership in
`.skillery-manifest.json`, refuses to replace unrelated local skills unless `--force` is supplied,
and can uninstall a bundle later.

List available bundles:

```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode list
```

Install a bundle globally:

```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode install meaningfy-core --global
```

Install one or more bundles into the current project:

```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode install meaningfy-core meaningfy-building --project
```

Rerun the install command to update the selected bundles. Uninstall with:

```bash
npm exec --yes \
  --package='git+https://github.com/meaningfy-ws/skillery.git#develop' \
  -- skillery-opencode uninstall meaningfy-core --global
```

Restart OpenCode after installing, updating, or removing skills so it refreshes skill discovery.

### OpenCode plugin alias

The repository is also an installable OpenCode plugin. The package alias selects the bundle, so this
syntax registers only `meaningfy-core`:

```bash
opencode plugin --global \
  'meaningfy-core@git+https://github.com/meaningfy-ws/skillery.git#develop'
```

The plugin can alternatively be configured under its canonical package name and passed one or more
bundle names through plugin options or `MEANINGFY_SKILLERY_BUNDLES`.

This route uses OpenCode's plugin `config()` hook to add generated skill directories to
`skills.paths`. Some OpenCode versions have initialized or cached skill discovery before that hook
became visible. Use the bundle installer above as the compatibility-safe path for the pinned version;
the plugin package is retained for versions where plugin-provided skill paths are discovered
correctly.

### Direct checkout

For repository development, point `OPENCODE_CONFIG_DIR` at the generated tree to expose the whole
catalogue:

```bash
git clone --branch develop https://github.com/meaningfy-ws/skillery.git
OPENCODE_CONFIG_DIR="$PWD/skillery/.opencode" opencode
```

This loads every generated skill and agent. It does not select a bundle because OpenCode does not
interpret `.opencode/bundles.json` itself.

| Bundle | For | Skills |
|---|---|---:|
| `meaningfy-core` | everyone | 4 |
| `meaningfy-consulting` | consulting | 5 |
| `meaningfy-architecture` | architecture / modelling | 4 |
| `meaningfy-building` | building / spine / review | 9 |

Bundle membership and the package version are generated or checked against the root `VERSION`.

## 2. Scope global skills per project

opencode has no per-project UI control for enabling or disabling globally installed skills. Configure skill permissions in the project's `opencode.json` instead. Restricting irrelevant skills reduces agent selection noise and prevents unrelated instructions from being loaded into a project.

Two approaches:

* **Blacklist — allow all except selected skills.** Use when most global skills are relevant:

  ```
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

* **Allowlist — deny all except selected skills.** Use when the project needs only a small, known subset:

  ```
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

Rules are evaluated in order and the last matching rule wins, so place the catch-all `*` rule before specific skill names. These settings affect only the current project; the global skills remain installed and available to other projects.


## 3. Root binding

OpenCode reads **`AGENTS.md`** natively — it is the canonical, CLI-agnostic operating manual. No
pointer file is required.

## 4. MCP servers

Install each server into `opencode.json` under `mcp`; keep secrets in environment variables. The
per-tool OpenCode shapes are in [`mcp-setup.md`](mcp-setup.md). Every referenced MCP server's
transport maps to OpenCode; see [`compatibility.md`](compatibility.md). No MCP config is committed.

## 5. Spine commands

```bash
openspec update --tools opencode    # registers opsx-propose, opsx-apply, … for OpenCode
```

The spine commands are delegated to this step — they are not part of the generated tree. The
`/opsx:<id>` form on Claude is `opsx-<id>` here.

## 6. Hooks (optional, via project-setup)

`project-setup` writes the shared Git/CI hooks once and the OpenCode agent-hook bindings as plugins
under `.opencode/plugin/`. Intent inventory and binding shapes:
[`../../hooks/README.md`](../../hooks/README.md), [`../../hooks/bindings.md`](../../hooks/bindings.md).

## Pinned versions and gaps

- Catalogue version: root `VERSION`; OpenCode version: `.opencode-version`.
- Recorded gaps on OpenCode:
  - `persist-before-compaction` — no `PreCompact` event; degrades to a `session.idle` binding.
  - Slash-command registration differs by design (`opsx-<id>`) — tool-native, not a gap.
- Full matrix: [`compatibility.md`](compatibility.md).
