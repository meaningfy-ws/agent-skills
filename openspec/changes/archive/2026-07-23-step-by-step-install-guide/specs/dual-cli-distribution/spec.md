## MODIFIED Requirements

### Requirement: Per-CLI documentation split
Documentation under `docs/` SHALL clearly distinguish opencode setup and configuration from Claude setup and configuration, over a shared source→CLI mapping reference, and SHALL cover the pinned opencode version and recorded gaps. Each role bundle SHALL have a documented install path on each CLI. Each per-CLI runbook (`docs/dual-cli/setup-claude.md`, `docs/dual-cli/setup-opencode.md`) SHALL present its install path as a literal numbered sequence of steps, where each step names exactly one runnable action — a copy-paste command block or a single external link — plus at most one line of rationale, and the sequence SHALL end with a verification step naming a command and its expected output. Version numbers and dependency pins SHALL be linked to their single source (`docs/environment-setup.md`) rather than restated in the runbook.

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
- **THEN** the step links to `docs/environment-setup.md` for the pinned version rather than restating the version number inline
