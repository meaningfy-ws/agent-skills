# Environment Setup — External Dependencies & Projection

**Audience:** anyone installing the Meaningfy skill catalog into their own machine or project.

Meaningfy skills are deliberately small and **reference** external skills rather than copying
them. This page is the single source for what to install and how to wire a project.

> **Install hierarchy.** [`README.md`](../README.md) is the front door — it points here. This page is
> the canon: everything below is CLI-agnostic (what to install, why, which version). The per-CLI
> runbooks carry the literal step-by-step *how*:
> [`docs/dual-cli/setup-claude.md`](dual-cli/setup-claude.md) and
> [`docs/dual-cli/setup-opencode.md`](dual-cli/setup-opencode.md). You should not need to open
> anything else to install the catalogue. (If you're *extending* the catalogue rather than
> installing it — adding a skill, keeping both CLIs generated in parity — that's a different
> audience: start at [`AGENTS.md` → How to maintain / extend](../AGENTS.md#how-to-maintain--extend-the-catalogue),
> which points at the contributor-facing contract docs in [`docs/dual-cli/`](dual-cli/README.md).)

## 1. Install the Meaningfy bundles — choose your CLI

The catalogue runs on **Claude Code** and **opencode** from the same sources, at the same `VERSION`,
with gate-verified parity. There are **four role bundles**; install `meaningfy-core` plus the role(s)
you wear. The step-by-step install sequence (add marketplace/registry → install bundles → mandatory
deps → root binding → spine commands → hooks/MCP → verify) is owned by the per-CLI runbooks — this
page does not restate it:

| Your CLI | Install runbook |
|---|---|
| **Claude Code** | [`dual-cli/setup-claude.md`](dual-cli/setup-claude.md) |
| **opencode** | [`dual-cli/setup-opencode.md`](dual-cli/setup-opencode.md) |

Each bundle pins the same root `VERSION`. The rest of this page is **CLI-agnostic** (external deps
with their pinned versions, the user/project split, projection) — the runbooks link back here for
those pins rather than restating them.

The **spine is a capability, not a bundle**: `meaningfy-building` carries the skills that drive it,
and the durable spine **assets** (`openspec/` + the forked schema, and `spine/` docs) are projected
into a repo by `project-setup`, not installed as a skill — see
[`../spine/meaningfy-spine.md`](../spine/meaningfy-spine.md).

## 2. External dependencies

Meaningfy skills reference these by name. They are **not** vendored here. This table is the
CLI-agnostic canon — **what** each one is, **why** it's needed, and its pinned **source/version**.
The exact install *command*, which differs per CLI, is one sub-step of Step 4 in your runbook
([`setup-claude.md`](dual-cli/setup-claude.md#step-4--install-the-mandatory-external-dependencies) /
[`setup-opencode.md`](dual-cli/setup-opencode.md#step-4--install-the-mandatory-external-dependencies)) —
not restated here, so the version number has exactly one home.

### Mandatory

| Component | Why Meaningfy uses it | Source / pinned version |
|-----------|----------------------|--------------------------|
| `superpowers` | TDD, systematic debugging, verification-before-completion, brainstorming — the universal disciplines our skills point to instead of restating | Claude marketplace `claude-plugins-official`; also `.claude/skills/`-loadable, so opencode reads it natively — no separate port |
| `ponytail` | YAGNI / minimal-code discipline — the routing target for "keep the code minimal, avoid over-engineering" (pairs with `cosmic-python`; wired into `project-setup`'s scaffolded `CLAUDE.md`). Ships `/ponytail`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt` | [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail) — same `.claude/skills/`-compat story as `superpowers` |
| `stream-coding` | The documentation-first delivery method (Work Shape → spec → generate-verify-integrate) | [`frmoretto/stream-coding`](https://github.com/frmoretto/stream-coding) — a single `SKILL.md`, not a plugin package; copied into `.claude/skills/stream-coding/` (both CLIs read it from there) |
| `@fission-ai/openspec` | **The spec-spine engine.** OpenSpec is the artifact-lifecycle engine the Meaningfy spine is built on — it provides the `/opsx:*` slash-commands (`propose`, `explore`, `apply`, `sync`, `archive` on the core profile) and the change → durable-spec store | [`Fission-AI/OpenSpec`](https://github.com/Fission-AI/OpenSpec), npm `@fission-ai/openspec`. Pinned version: [`../spine/openspec-version.txt`](../spine/openspec-version.txt) (currently `1.4.1`). See [`../spine/README.md`](../spine/README.md) and [`../spine/workflows.md`](../spine/workflows.md) |

### Optional / recommended

| Component | Why | Source |
|-----------|-----|--------|
| `commit-commands` | Standardised commit / push / PR mechanics (`meaningfy-git-workflow` delegates here) | Claude marketplace `claude-plugins-official` |
| `code-review` | Read-only PR review *run* (pairs with the `meaningfy-code-review` checklist skill) | Claude marketplace `claude-plugins-official` — **Claude-only**, no opencode equivalent (see [`dual-cli/compatibility.md`](dual-cli/compatibility.md)) |
| `gitnexus-*` | Code intelligence / impact analysis (used by the `implementer` and `code-reviewer` wrappers) | external plugin + MCP server — see **MCP servers** below |
| `context7` | Up-to-date library documentation via MCP | external MCP server — see **MCP servers** below |

> **Drift warning:** the repo validator **cannot detect** when an external skill is renamed
> or removed upstream — Meaningfy skills reference them by name only. If a referenced skill
> stops resolving, check this table against the current upstream names. Treat the *Mandatory*
> set as a release gate when adopting the bundles.

### MCP servers (optional)

Neither table above is the full MCP list — GitNexus and context7 are also MCP servers, but so are
five more this catalogue's skills/agents reference: **Atlassian** (Confluence/Jira), **Google
Workspace** (Gmail/Drive/Calendar), **Odoo**, **Neo4j**, and **MongoDB**. All seven, plus the
literal per-server install steps (split Claude Code / opencode where the config shape differs), are
one place: [`dual-cli/mcp-setup.md`](dual-cli/mcp-setup.md).

## 3. User level vs project level

Installation splits across two scopes. Put each thing where it belongs and avoid duplication.

| | **User / machine level** (install once) | **Project / repo level** (per repo) |
|---|---|---|
| **Skills** | Install the bundles + external skills (superpowers, stream-coding, ponytail, OpenSpec; optional commit-commands / code-review / gitnexus / context7) globally via `/plugin`, so every repo can reach them | Pin the bundles a given project actually uses; wire the `openspec/` instance via `project-setup` |
| **CLAUDE.md** | The global `~/.claude/CLAUDE.md` holds the durable coding prompt — engineering standards, layering rules, the *constitution* that applies everywhere | The repo `./CLAUDE.md` holds the repo operating manual + routing (what this repo is, how to maintain/validate it), complementing — not restating — the global file |

**Why this split.** Skills are machine-wide tooling, so they live once at user level and propagate
through `/plugin update`; per-project pinning only records which of them a repo relies on. The
constitution (durable standards) is the same across all your work, so it belongs in the global
prompt; the repo file carries only what is specific and local, so the two compose without drift.

> **AGENTS.md-canonical.** `AGENTS.md` is the canonical, CLI-agnostic root binding (opencode reads it
> natively); `CLAUDE.md` is a thin pointer that tells Claude Code to read `AGENTS.md` and adds only
> Claude-specific addenda — there is no symlink between them (see
> [`dual-cli-distribution`](../openspec/specs/dual-cli-distribution/spec.md)). Templates live in
> [`../prompts/`](../prompts/) (`CLAUDE.md.template`, `global-prompt.md`).

## 4. Project projection (bootstrap)

Skills propagate through the marketplace (`/plugin update`). To project the agentic files
(`AGENTS.md` canonical + the thin `CLAUDE.md` pointer, no symlink), the `.claude/` layout, and the spine assets
(`openspec/` + the forked schema) into a repo, use the **`project-setup`** skill (in
`meaningfy-building`):

- It is an interview-driven scaffolder that creates the whole Meaningfy-standard repo (layout,
  root tool configs, tests, agentic files, the `openspec/` spine wiring, Antora docs, CI).
- It also runs in **brownfield mode** to gap-check and modernise an existing repo.
- Projection is via this skill **only** — there is no init script.

## 5. CI/CD external boundary (deployable repos)

For **deployable** application repos, delivery is split:

- **CI** (test / lint / guardrail / docs-publish) is owned by **`project-setup`** and scaffolded with
  the repo.
- **CD + release + the delivery contract** is owned by the **`ci-cd-delivery`** skill (app-repo side:
  versioned GHCR image, one reusable deploy mechanism, the deploy-trigger contract).

These are **DevOps-owned and out of the skill's automation scope** — documented as a boundary only:

- **`cloud-infrastructure`** — Terraform + Ansible VM provisioning/config (DevOps-manual; not automated here).
- **`infrastructure-stacks`** — Docker Compose stack deploys (rsync + `.env`-from-Secrets to VMs).
- **Vaultwarden** — secret source-of-truth (GitHub Secrets are the deployment copy); **bastion/SSH**
  is the break-glass path.

The CD building blocks and the DevOps decisions to ratify are in the
[`ci-cd-delivery`](../skills/ci-cd-delivery/SKILL.md) skill.

## 6. Agents → skills migration note

Earlier versions of this repo shipped five sub-agents. The catalog now ships the **knowledge
as skills** plus **three thin wrappers** (`implementer`, `code-reviewer`, `epic-planner`).
The `docs/ai-coding/` runbook predates this change and still names the older agents; map them
as follows when reading it:

| Old agent | Now |
|-----------|-----|
| `gherkin-writer` | the `bdd-gherkin` skill |
| `documenter` | the `technical-writing` skill |
| `code-reviewer` | thin wrapper loading `meaningfy-code-review` (read-only, opus) |
| `epic-planner` | thin wrapper loading `epic-planning` + `clarity-gate` |
| `implementer` | thin wrapper loading `cosmic-python` + external `stream-coding` + `superpowers` TDD |
