## ADDED Requirements

### Requirement: Bidirectional role-to-playbook coverage
The `docs/how-we-work/playbooks/` directory SHALL contain exactly one playbook file per role
defined in `docs/roles-and-raci.md` (owned by `define-roles-and-raci`), and every playbook file
SHALL correspond to exactly one role defined there. Neither an orphan role (a defined role with no
playbook) nor an orphan playbook (a playbook file with no corresponding defined role) SHALL exist.

#### Scenario: Every defined role has a matching playbook
- **WHEN** the set of roles enumerated in `docs/roles-and-raci.md`'s role-definition blocks is
  compared against the set of files under `docs/how-we-work/playbooks/`
- **THEN** every role name has exactly one playbook file whose content is that role's filtered view

#### Scenario: Every playbook maps back to a defined role
- **WHEN** a file exists under `docs/how-we-work/playbooks/`
- **THEN** it corresponds to exactly one role defined in `docs/roles-and-raci.md`, and no playbook
  file exists for a role that document does not define

#### Scenario: A role added later gets a matching playbook
- **WHEN** a future change adds a seventh role to `docs/roles-and-raci.md`
- **THEN** the coverage check fails until a matching seventh playbook file is added, and the
  reverse also holds if a playbook is added before its role is defined

### Requirement: Pointer-discipline — no originating normative statement
No normative lifecycle statement (a rule, gate, threshold, phase duration, price boundary, role
definition, or RACI cell) SHALL originate in `docs/how-we-work/`. Every such statement appearing in
`docs/how-we-work/README.md` or any file under `docs/how-we-work/playbooks/` SHALL carry an
adjacent link to the sibling document that owns and states it.

#### Scenario: A normative claim in the map carries its citation
- **WHEN** `docs/how-we-work/README.md` states a fact about a gate, a threshold, a duration, a price
  boundary, a role definition, or a RACI cell
- **THEN** that statement is accompanied by a link to the document (in `docs/engagement/`,
  `docs/ai-coding/`, or `docs/roles-and-raci.md`) that owns the fact

#### Scenario: A normative claim in a playbook carries its citation
- **WHEN** a playbook under `docs/how-we-work/playbooks/` states a role boundary, a RACI cell, or
  any other normative fact (for example the Work Shaper playbook's citation of
  `define-roles-and-raci`'s Architect–Builder-spectrum positioning)
- **THEN** that statement links to its owning sibling document rather than restating the fact in
  full

#### Scenario: A claim that would survive deletion of its link target is a violation
- **WHEN** a sentence in `docs/how-we-work/README.md` or a playbook would still read as true after
  the document it links to is deleted
- **THEN** that sentence is a duplication and fails this requirement — it must be cut or replaced by
  the link alone, per the pointer-discipline test

### Requirement: The map states the funnel, the planes, and per-role views as one integrated structure
`docs/how-we-work/README.md` SHALL narrate the end-to-end flow as a single structure covering the
commercial funnel and its entry points, the three P2 planes, and the existence of six per-role
filtered views, and SHALL link to all six playbooks and to a Known-gaps section.

#### Scenario: The map covers funnel, planes, and role views in one document
- **WHEN** a reader opens `docs/how-we-work/README.md`
- **THEN** it presents the funnel (presale through the three paid entry points), the three P2
  planes (SDLC / MDLC / CBLC), and a link to each of the six role playbooks, all reachable without
  leaving the document

#### Scenario: The map links to every playbook
- **WHEN** the six playbook files exist under `docs/how-we-work/playbooks/`
- **THEN** `docs/how-we-work/README.md` contains a working link to each of the six

#### Scenario: The map carries a Known-gaps section
- **WHEN** a reader reaches the end of `docs/how-we-work/README.md`
- **THEN** they find a labelled Known-gaps section naming what is missing and who owns closing it,
  distinguishing deliberate deferral from oversight
