# Source → CLI mapping reference

**Audience: skillery contributors** — this is the generation contract for the catalogue's *own*
artifacts (skills, agents, commands, hooks), read by whoever adds a skill/agent or maintains the
`dual-cli-generator`. It is not install documentation; if you're installing the catalogue, see
[`docs/environment/setup.md`](../setup.md) instead.

One set of sources, two CLIs. This is the shared translation table both
[`setup-claude.md`](setup-claude.md) and [`setup-opencode.md`](setup-opencode.md) were *written
against* (it explains why each runbook's steps look the way they do). It records *what derives from
what* — the contract the `dual-cli-generator` implements (it does not generate anything here).

## Artifact mapping

| Source (authored once) | Claude Code | opencode |
|---|---|---|
| `skills/<name>/SKILL.md` | `.claude/skills/<name>/` (or marketplace plugin) | `.opencode/skills/<name>/` — *also* read natively from `.claude/skills/` |
| `agents/<name>.md` | `.claude/agents/<name>.md` | `.opencode/agents/<name>.md` |
| command content | `/opsx:<id>`, `/<name>` (native registration) | `.opencode/commands/<id>.md` (`template` + `$ARGUMENTS`) |
| root binding | `CLAUDE.md` (pointer → `AGENTS.md`) | `AGENTS.md` (read natively) |
| `VERSION` | `marketplace.json` `metadata.version` | opencode manifest version |
| hook *intent* (`hooks/inventory.yaml`) | `settings.json` hooks (agent) + pre-commit/CI (git/ci) | `.opencode/plugin/*` (agent) + the same pre-commit/CI |
| MCP (documented, not generated) | `.mcp.json` `mcpServers` | `opencode.json` `mcp` |

## Frontmatter field mapping (agents)

| Source frontmatter | opencode equivalent |
|---|---|
| `model: opus` | `model: anthropic/claude-opus-4-8` (alias lookup) |
| `tools: [Read, Edit, Bash, …]` (PascalCase) | `tools` / `permission` with lowercased names (`read`, `edit`, `bash`) |
| `disallowedTools: […]` | folded into opencode `permission` (deny) |
| `skills: […]` | opencode agent `skills` list |
| invocation name `meaningfy-<bundle>:<agent>` | opencode agent name |

These tables are the **contract**; the generator (separate change) reads sources and emits the
right-hand columns, then a parity gate asserts every first-party row has both sides at the same
`VERSION`. Anything unmappable becomes an explicit `Gap(source, cli, reason)` — never a silent drop.

## What is NOT mapped (tool-native)

Slash-command *registration* and agent-*hook bindings* are per-CLI by design — see the tool-native
boundary in [`compatibility.md`](compatibility.md). Only their content/intent is shared.
