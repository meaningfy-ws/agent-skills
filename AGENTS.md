# Skillery — Repo Operating Manual

This file is the **canonical, CLI-agnostic Binding** for this repo: it mandates and routes.
It carries no reusable knowledge — every substantive topic lives in the skill or doc it points to.
It is consumed natively by **opencode** (`AGENTS.md`) and pointed to by **Claude Code** (`CLAUDE.md`).
CLI-specific guidance lives in that CLI's binding, never here.

## What this repo is

A company-wide skills/agents/docs catalogue for **Claude Code and opencode**. Every artifact is
exactly one of four types (defined in [`spec/skill-repo-governance.md`](spec/skill-repo-governance.md)):

| Type | Home | Rule |
|------|------|------|
| **Skill** | `skills/` | Reusable knowledge; single source of authority per fact |
| **Agent** | `agents/` | Thin wrapper — role + model + tools + skill list; no inlined knowledge |
| **Doc** | `docs/` | Human canon; narrates and points, never restates skill rules |
| **Binding** | `prompts/` + root agentic files (`AGENTS.md`, `CLAUDE.md`) | Mandates and routes; never carries the standard |

**Single-source-of-authority rule:** if a fact belongs to a skill, it lives there and nowhere else.
See [`spec/skill-repo-governance.md`](spec/skill-repo-governance.md) for placement rules.

## Dual-CLI distribution

This catalogue runs on both Claude Code and opencode from one set of sources, with verified parity.
See the durable capability spec [`openspec/specs/dual-cli-distribution`](openspec/specs/dual-cli-distribution/spec.md)
and [`docs/dual-cli/`](docs/dual-cli/README.md) (per-CLI setup + the source→CLI mapping + the
external-dependency compatibility matrix). `AGENTS.md` is canonical; `CLAUDE.md` is a thin pointer
that adds only Claude-specific guidance.

## How to maintain / extend the catalogue

- **Adding a new skill** — follow [`spec/CREATING_SKILLS.md`](spec/CREATING_SKILLS.md).
- **Assigning to a bundle** — bundles are declared in [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).
- **Boundary / related-skills** — every skill's frontmatter must declare its `boundary` and list
  any `related_skills`. This keeps triggers crisp and prevents collisions with external neighbours.
- **Versioning** — the root [`VERSION`](VERSION) file is the single source of version truth; both
  CLI distributions derive their version from it.
- **Dual-CLI parity** — anything you add or change must work on **both** CLIs; the rules are below.

### Dual-CLI authoring rules

The catalogue ships to Claude Code **and** opencode from one set of sources (the
[`dual-cli-distribution`](openspec/specs/dual-cli-distribution/spec.md) contract). When you add or
update an artifact, keep both CLIs working — the gates in `make validate` enforce it:

- **Skills, agents, bundles** — author the Claude source (`skills/`, `agents/`,
  `.claude-plugin/marketplace.json`); the opencode tree is *generated*. After any change run
  `make generate-opencode` and commit the regenerated `.opencode/`. **Never hand-edit `.opencode/`** —
  the drift gate will fail. The frontmatter map is the contract in
  [`docs/dual-cli/mapping.md`](docs/dual-cli/mapping.md); an unmappable field becomes a recorded gap,
  not a silent drop.
- **Skill/agent bodies stay CLI-agnostic** — no `/opsx:`-style command forms or `.claude/` paths in a
  body unless it is on the recorded allow-list (the `body_agnosticism` check fails otherwise). Phrase
  operationally-neutral; record an unavoidable CLI-ism as a cosmetic gap in
  [`docs/dual-cli/body-agnosticism-audit.md`](docs/dual-cli/body-agnosticism-audit.md).
- **Commands** — only *content/templates* are shared; registration is **tool-native** (`/opsx:<id>`
  on Claude, `opsx-<id>` on opencode). Don't try to generate one registration form for both.
- **Specs & versions** — the root `VERSION` flows into `marketplace.json`, `opencode.json`, and the
  bundle manifest; the version-sync gate fails on any mismatch. Hook *intent* is single-sourced in
  [`hooks/inventory.yaml`](hooks/inventory.yaml) and rendered per CLI (see
  [`hooks/bindings.md`](hooks/bindings.md)).

Full per-CLI setup and the compatibility matrix: [`docs/dual-cli/`](docs/dual-cli/README.md).

## How to validate

`make validate` is the guardrail. Run it before every PR; CI runs it too. See
[`spec/skill-repo-governance.md`](spec/skill-repo-governance.md) for what the validator enforces.

## Common Meaningfy practices

- **Architecture** — align on cosmic-python layering (see the
  [`skills/cosmic-python`](skills/cosmic-python) skill when designing non-trivial additions).
- **Commits** — conventional commits are mandatory; see the
  [`skills/meaningfy-git-workflow`](skills/meaningfy-git-workflow) skill for the full standard.
- **Spine / OpenSpec conventions** — the durable spec spine lives in [`spine/`](spine/) (docs) and [`openspec/`](openspec/) (the live OpenSpec instance + the forked `meaningfy` schema). See [`spine/README.md`](spine/README.md).
- **External method skills land in the spine (binding).** `superpowers` (brainstorming, writing-plans, executing-plans, TDD, …) provides *disciplines*, not a parallel spec system. In a spine-wired repo, their artifacts MUST land in the spine, never in a `docs/superpowers/` tree: a **brainstorming** design feeds the **EPIC** (`openspec/changes/<id>/proposal.md`); **writing-plans is SUPERSEDED** by the **PLAN** (`design.md` + `tasks.md`, gated by `clarity-gate`); execution uses `superpowers:test-driven-development` / `subagent-driven-development`, tracked via the opsx apply command (`/opsx:apply` on Claude, `opsx-apply` on opencode). The verb↔artifact map is in [`spine/workflows.md`](spine/workflows.md#superpowers--spine). skillery **dogfoods this**: its own non-trivial changes are `openspec/changes/` EPICs.
- **Hooks** — hook *intent* is single-sourced in [`hooks/inventory.yaml`](hooks/inventory.yaml) (see [`hooks/README.md`](hooks/README.md)); git-mechanism hooks are shared across CLIs, agent-mechanism hooks are rendered per CLI.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **skillery** (3307 symbols, 3960 relationships, 37 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> Index stale? Run `node .gitnexus/run.cjs analyze` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? `npx gitnexus analyze` (npm 11 crash → `npm i -g gitnexus`; #1939).

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows. For regression review, compare against the default branch: `detect_changes({scope: "compare", base_ref: "main"})`.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `context({name: "symbolName"})`.

## Never Do

- NEVER edit a function, class, or method without first running `impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit changes without running `detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/skillery/context` | Codebase overview, check index freshness |
| `gitnexus://repo/skillery/clusters` | All functional areas |
| `gitnexus://repo/skillery/processes` | All execution flows |
| `gitnexus://repo/skillery/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
