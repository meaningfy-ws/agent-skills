# dual-cli-distribution Specification

## Purpose
The foundation and contract for running the skillery catalogue identically on Claude Code and
opencode from one set of sources: the single-`VERSION` rule, the canonical `AGENTS.md` /
pointer-`CLAUDE.md` root binding, the hook intent inventory, MCP documented per-tool setup, the
external-dependency and baseline-pack compatibility matrix, the tool-native registration boundary,
skill-body CLI-agnosticism, and the per-CLI documentation split. The generation/parity engine that
emits and gates the opencode tree against this contract is the `dual-cli-generation` capability.

## Requirements
### Requirement: Single version source
The repository SHALL contain a root `VERSION` file as the only source of version truth; the Claude `marketplace.json` `metadata.version` and the opencode distribution version SHALL both be derived from it. (Enforcement of agreement is the version-sync gate owned by `dual-cli-generator`.)

#### Scenario: Versions derive from VERSION
- **WHEN** `VERSION` is set to a value
- **THEN** the Claude and opencode distribution versions are both expected to equal that value

### Requirement: AGENTS.md canonical, CLAUDE.md pointer, no symlink
`AGENTS.md` SHALL be the canonical, CLI-agnostic root binding. `CLAUDE.md` SHALL be a thin Binding that instructs the agent to read `AGENTS.md` and carries only Claude-specific addenda. There SHALL be no symlink between them, and `AGENTS.md` SHALL NOT contain Claude-only paths, tool names, or invocation forms.

#### Scenario: opencode reads a CLI-agnostic canonical file
- **WHEN** opencode reads `AGENTS.md`
- **THEN** its referenced paths, tool names, and command forms are valid on opencode

#### Scenario: Claude is pointed to the canonical file
- **WHEN** the agent reads `CLAUDE.md`
- **THEN** it is instructed to read `AGENTS.md`, and `CLAUDE.md` adds only Claude-specific guidance

#### Scenario: No symlink couples the two
- **WHEN** the repository is inspected
- **THEN** `AGENTS.md` and `CLAUDE.md` are distinct regular files, neither a symlink to the other

### Requirement: MCP documented per-tool setup with templates
The repository SHALL document MCP server setup as an install-one-by-one section with per-tool reference templates for both CLIs (Claude `.mcp.json` and opencode `opencode.json` shapes), and SHALL NOT commit or generate any MCP configuration. Templates SHALL use environment-variable placeholders for all credentials.

#### Scenario: Each referenced tool has a per-CLI template
- **WHEN** the catalogue references an MCP-backed tool
- **THEN** the MCP setup docs show its Claude and opencode config shape as a reference template

#### Scenario: No MCP config committed or generated
- **WHEN** the repository is inspected
- **THEN** no committed or generated MCP configuration file exists, and the templates carry env-var placeholders, not literal secrets

### Requirement: External-dependency and baseline-pack compatibility matrix
The change SHALL provide a committed compatibility matrix recording, for each external plugin, skill, and MCP server the catalogue references, its opencode support status (native, `.claude/`-compatible, or unsupported) and a per-CLI install path or a gap entry. The matrix SHALL also identify each CLI's baseline pack (e.g. Claude Code's default/marketplace skills; an opencode community pack such as opencode-power-pack) and, where the catalogue or workflow assumes a baseline capability, name the equivalent per CLI or record a gap. External dependencies and baseline packs SHALL NOT be generated.

#### Scenario: Every external reference is classified
- **WHEN** the catalogue references an external plugin, skill, or MCP server
- **THEN** the compatibility matrix records its opencode support status and a per-CLI install path or gap

#### Scenario: Baseline packs are identified per CLI
- **WHEN** the catalogue or its workflow assumes a capability provided by a CLI's baseline pack
- **THEN** the matrix names the equivalent baseline capability on each CLI or records a gap

### Requirement: Per-CLI documentation split
Documentation under `docs/` SHALL clearly distinguish opencode setup and configuration from Claude setup and configuration, over a shared source→CLI mapping reference, and SHALL cover the pinned opencode version and recorded gaps. Each role bundle SHALL have a documented install path on each CLI. Each per-CLI runbook (`docs/environment/dual-cli/setup-claude.md`, `docs/environment/dual-cli/setup-opencode.md`) SHALL present its install path as a literal numbered sequence of steps, where each step names exactly one runnable action — a copy-paste command block or a single external link — plus at most one line of rationale, and the sequence SHALL end with a verification step naming a command and its expected output. Version numbers and dependency pins SHALL be linked to their single source (`docs/environment/setup.md`) rather than restated in the runbook.

#### Scenario: A team member can set up either CLI
- **WHEN** a team member follows the documentation for their chosen CLI
- **THEN** they can install and configure the catalogue for that CLI without following the other CLI's instructions

#### Scenario: Each bundle is installable on each CLI
- **WHEN** a team member follows the documented install path for a bundle on either CLI
- **THEN** they obtain that bundle's mapped skills and agents

#### Scenario: Each step is a single runnable action
- **WHEN** a reader is on a numbered step in a per-CLI runbook
- **THEN** that step contains exactly one command block or external link to act on, not a paragraph requiring interpretation or a forward reference to another document for the action itself

#### Scenario: A reader can verify their install succeeded
- **WHEN** a reader completes the last numbered step of a per-CLI runbook
- **THEN** that step is a verification step naming a command to run and the output that confirms success

#### Scenario: Version pins are not duplicated in the runbook
- **WHEN** a runbook step installs a versioned external dependency
- **THEN** the step links to `docs/environment/setup.md` for the pinned version rather than restating the version number inline

### Requirement: Tool-native registration stays separate
Slash-command registration/invocation SHALL be tool-native: its registration form SHALL NOT be generated identically across CLIs. The shared surface is limited to standards/context (the root binding), behaviour (skill bodies), command *content/templates*, and the hook *intent inventory* — not native command registration or native hook bindings.

#### Scenario: Native command registration is per CLI
- **WHEN** a command is exposed on both CLIs
- **THEN** its registration/invocation form is the CLI-native one (e.g. `/opsx:<id>` on Claude, `opsx-<id>` on opencode), while only its content/template derives from a shared source

### Requirement: Hook intent inventory and per-CLI adoption
The repository SHALL contain a committed `hooks/` inventory as the single source of hook intent, with both a machine-readable form and a human-readable table visible in the repo structure. Each entry SHALL record intent, trigger, mechanism, phase, per-CLI binding, and provenance, and a single intent MAY carry several bindings. Provenance SHALL be either a source skill or an imperative rule in a binding (a MUST/NEVER rule in `CLAUDE.md`/`AGENTS.md`) — imperative binding rules are inventory provenance, not only skills. Each binding SHALL be classified on two axes — **mechanism**: `git` (CLI-agnostic, single shared implementation), `ci` (shared PR/Actions check), or `agent` (same intent rendered into each CLI's native binding); and **phase**: `quality` (commit/push-time) or `phase-gate` (workflow-transition-time). Setup SHALL be able to project the inventory into a repository — the shared git-hook config once, and the agent-hook bindings for each targeted CLI.

#### Scenario: Inventory is the single source of hook intent
- **WHEN** a hook intent exists
- **THEN** it appears once in the committed `hooks/` inventory with its mechanism, phase, and provenance, and the human-readable table is visible in the repo structure

#### Scenario: git hooks share one implementation
- **WHEN** a hook is classified as git-mechanism
- **THEN** a single shared implementation serves both CLIs and is not duplicated per CLI

#### Scenario: agent hooks share intent, not binding
- **WHEN** a hook is classified as agent-mechanism
- **THEN** the same intent is rendered into each targeted CLI's native binding, and the two bindings are not required to be byte-identical

#### Scenario: Setup projects hooks per CLI
- **WHEN** setup projects the inventory into a repository targeting one or more CLIs
- **THEN** the shared git-hook configuration is written once and the agent-hook bindings are written for each targeted CLI

### Requirement: Skill bodies are CLI-agnostic
Skill bodies SHALL be CLI-agnostic, or any residual CLI-specific operational reference (e.g. a `/opsx:`-style command form or a `.claude/` path) SHALL be neutralised to CLI-agnostic phrasing or recorded as a known cosmetic gap. The body-agnosticism audit SHALL cover every first-party skill.

#### Scenario: A behavioural skill references a CLI-specific command form
- **WHEN** a skill body names a command or path in a CLI-specific form
- **THEN** it is either rephrased CLI-agnostically or recorded as a cosmetic gap

#### Scenario: Audit covers all skills
- **WHEN** the body-agnosticism audit completes
- **THEN** every first-party skill is either confirmed agnostic or has its CLI-specific references neutralised or gap-recorded

### Requirement: Single-home dual-CLI authoring rule
The repository SHALL document, in exactly one canonical location (the root `AGENTS.md`), the rule that
any added or updated skill, agent, command, or spec must work on both CLIs — covering opencode-tree
regeneration, CLI-agnostic bodies, and per-CLI command registration. Other documents SHALL link this
rule rather than restate it. Installation documentation SHALL form a single hierarchy — `README.md`
(front door) → `docs/environment/setup.md` (canon) → the per-CLI runbooks — with `docs/environment/dual-cli/` as a
reference annex, not a competing install hub.

#### Scenario: Authoring rule has one home
- **WHEN** a contributor looks up how to keep a change working on both CLIs
- **THEN** the canonical rule is in `AGENTS.md`, and other docs (`CREATING_SKILLS.md`,
  `docs/environment/setup.md`, `README.md`) link to it without restating it

#### Scenario: Install entry is the canon, the dual-CLI folder is the annex
- **WHEN** a reader sets out to install the catalogue on either CLI
- **THEN** the documented install path starts at `docs/environment/setup.md` (front door `README.md`),
  and `docs/environment/dual-cli/` is presented as the reference annex rather than a parallel install entry

