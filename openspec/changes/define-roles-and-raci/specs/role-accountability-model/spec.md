## ADDED Requirements

### Requirement: The role set is closed at six, and each role is named
The catalogue SHALL document a closed set of exactly six project roles — Sales/Presales, Technical
Consultant, Solution Architect, Work Shaper, Solution Builder, Solution Shipper — in a single file,
`docs/roles-and-raci.md`. No project role beyond these six SHALL be added as a named role or as a
matrix column.

#### Scenario: The role set is counted
- **WHEN** the role definitions in `docs/roles-and-raci.md` are counted
- **THEN** exactly six role blocks are present, named Sales/Presales, Technical Consultant, Solution
  Architect, Work Shaper, Solution Builder, Solution Shipper, and no other role block exists

#### Scenario: A seventh role is proposed
- **WHEN** a contributor proposes adding a handbook role (e.g. Quality Overseer, Customer Success
  Manager) as a seventh named role or matrix column
- **THEN** the proposal is rejected in favour of recording it as an adaptation note that cites which
  of the six roles now holds that mandate

### Requirement: Every named lifecycle activity has exactly one accountable role
The RACI matrix SHALL cover every named lifecycle activity as one row, and each row SHALL carry
exactly one role marked Accountable (`A`). A row with zero `A` marks or with more than one `A` mark
SHALL NOT be published.

#### Scenario: Every row in the matrix is checked
- **WHEN** every row of the RACI matrix is inspected
- **THEN** each row has exactly one cell marked `A` (alone or combined as `A/R`) and no row has zero
  or more than one `A`

#### Scenario: A row is drafted with no accountable role
- **WHEN** a new or edited activity row would otherwise carry zero `A` marks
- **THEN** the row is not published until exactly one role is marked accountable, or the activity is
  instead recorded under Known gaps naming the absent owner

#### Scenario: A row is drafted with two accountable roles
- **WHEN** a draft row marks more than one role `A`
- **THEN** the row is corrected to a single `A` before publication, with the other role(s) marked
  R, C, I, or `–` instead

### Requirement: Roles are documented as responsibilities-in-a-process, not competences or headcount
The catalogue SHALL state, in `docs/roles-and-raci.md`, that a role is a set of responsibilities in
a process rather than a competence/profile or a headcount commitment. This distinction SHALL be
stated explicitly, not left implicit in the role blocks alone.

#### Scenario: A reader conflates a role with a competence
- **WHEN** a reader looks up a role expecting a skills/competency/seniority definition (e.g. "Semantic
  Engineer", "Software Engineer")
- **THEN** the doc states that competences are profiles, distinct from roles, and points out that
  the same role can be executed by different profiles across planes

#### Scenario: A reader infers staffing from the matrix
- **WHEN** a reader tries to infer a required headcount or one-person-per-role staffing model from
  the six-column matrix
- **THEN** the doc states explicitly that the matrix constrains accountability, not staffing, and
  that one person may hold several roles or two people may share one role

### Requirement: The Work Shaper role is documented with its mandate and its positioning citation
The catalogue SHALL document the Work Shaper role with: its mandate (developing the WBS, roadmap,
and Epic pitch, identifying risks, and mapping Epic scope into stories with the Builder), the skill
it owns and steers (`skills/epic-planning/SKILL.md`, cited by path, not restated), and its
positioning on the Architect–Builder spectrum, leaning Builder. `docs/roles-and-raci.md` SHALL be
the authoritative source for this positioning statement; any other document that needs it SHALL
cite this file rather than restate the positioning independently.

#### Scenario: The Work Shaper's mandate is looked up
- **WHEN** a reader looks up what the Work Shaper is accountable for
- **THEN** the role block states the WBS/roadmap/Epic-pitch/risk-list/story-mapping mandate and cites
  `skills/epic-planning/SKILL.md` as the skill it owns and steers, without restating that skill's
  content

#### Scenario: Another document needs the Architect-Builder positioning
- **WHEN** another document (e.g. a per-role playbook) needs to describe where Work Shaper sits
  relative to Solution Architect and Solution Builder
- **THEN** it cites `docs/roles-and-raci.md`'s positioning statement rather than asserting its own
  independent version of that positioning

#### Scenario: The Work Shaper is confused with Solution Architect or Solution Shipper
- **WHEN** a reader is unsure whether an activity belongs to Work Shaper, Solution Architect, or
  Solution Shipper
- **THEN** the doc's boundary paragraphs distinguish Work Shaper's scoping/planning mandate from the
  Architect's technical-design mandate and the Shipper's delivery-close accountability
