## ADDED Requirements

### Requirement: Every ai-* domain has exactly one runbook and one DoD file
Each of the three `ai-*` domains (`docs/ai-coding/`, `docs/ai-sales/`, `docs/ai-consulting/`) SHALL
contain exactly one runbook file and exactly one Definition-of-Done file at its top level. Neither a
domain missing one of the two, nor a domain with more than one runbook or more than one DoD file,
SHALL exist.

#### Scenario: Every domain has exactly one runbook
- **WHEN** the top level of `docs/ai-coding/`, `docs/ai-sales/`, and `docs/ai-consulting/` is
  inspected
- **THEN** each contains exactly one file matching the domain's runbook (`build-lifecycle.md` +
  `opsx-runbook.md` together serve `ai-coding`'s operational-script role; `sales-runbook.md` for
  `ai-sales`; `advisory-runbook.md` for `ai-consulting`) and exactly one DoD file
  (`dod-quality-gates.md`, `sales-dod.md`, `consulting-dod.md` respectively)

#### Scenario: A domain with a missing DoD fails the check
- **WHEN** a domain directory under `docs/` is named as one of the three `ai-*` domains but has no
  file serving the DoD role
- **THEN** the domain fails this requirement until a DoD file — even a scaffold naming the gap
  rather than inventing criteria — is added

### Requirement: Playbooks cite their domain's runbook rather than restating it
Every file under an `ai-*` domain's `playbooks/` directory SHALL be a role-filtered view that links
to its domain's runbook for the operational sequence, and SHALL NOT restate that sequence's steps,
gates, or ordering in its own prose.

#### Scenario: A playbook's stage list links back to the runbook
- **WHEN** a playbook file (for example `docs/ai-sales/playbooks/sales-presales.md`) describes the
  stages its role touches
- **THEN** each stage links to the section of its domain's runbook (or the pre-existing sibling doc
  that owns that stage's detail) that defines it, rather than re-describing the stage's sequence or
  gate condition in the playbook's own words

#### Scenario: A playbook that duplicates its runbook's sequence fails the check
- **WHEN** a playbook file contains a numbered or chronological restatement of stages that already
  appears, in the same order, in its domain's runbook
- **THEN** that playbook fails this requirement — the duplicated sequence must be replaced by a link

### Requirement: roles-and-raci.md is cited by every domain's playbooks and owned by none
`docs/roles-and-raci.md` SHALL be cited (linked) by at least one playbook in each of the three
`ai-*` domains, and SHALL NOT be located under, or treated as owned by, any single domain's
directory.

#### Scenario: roles-and-raci.md sits outside every domain folder
- **WHEN** the repository's `docs/` top level is inspected
- **THEN** `roles-and-raci.md` exists at `docs/roles-and-raci.md`, not nested under `docs/ai-coding/`,
  `docs/ai-sales/`, or `docs/ai-consulting/`

#### Scenario: Every domain's playbooks link to roles-and-raci.md
- **WHEN** the playbooks under each of the three domains are inspected
- **THEN** at least one playbook per domain contains a working link to `docs/roles-and-raci.md`
  (or a specific anchor within it) for role definition or RACI-cell detail

### Requirement: A method or technique with no owning skill is named as an explicit extension point
Any document under `docs/ai-consulting/methods/` that describes a technique with no skill in this
repository's `skills/` directory owning it SHALL state that absence plainly, in a checkable
sentence, rather than fabricating acceptance criteria, a deliverable definition, or an owning skill
that does not exist.

#### Scenario: An unowned method states its own gap plainly
- **WHEN** a reader opens `docs/ai-consulting/methods/wardley-mapping.md` (or
  `data-maturity-assessment.md`, `semantic-maturity-assessment.md`,
  `enterprise-process-modelling.md`)
- **THEN** the document contains a direct, unambiguous sentence stating that no skill in the
  catalogue owns this technique today, rather than a vague placeholder like "coming soon" or a
  fabricated deliverable description

#### Scenario: An owned method is not mis-stated as an extension point
- **WHEN** a reader opens `docs/ai-consulting/methods/gap-analysis.md`
- **THEN** the document states that gap analysis is owned by `decision-package`'s discovery flow and
  links to it, rather than repeating the "no skill owns this" language used for the genuinely unowned
  techniques

### Requirement: The consulting DoD names its own unknowns rather than inventing done-ness criteria
`docs/ai-consulting/consulting-dod.md` SHALL state that there is no repo-wide agreement on what
"done" means for an advisory/maturity-assessment engagement, name the specific questions a real DoD
would need to answer, and name what a future DoD would depend on — rather than asserting acceptance
criteria not yet decided anywhere in this repository.

#### Scenario: The consulting DoD states the gap rather than inventing criteria
- **WHEN** a reader opens `docs/ai-consulting/consulting-dod.md`
- **THEN** it states there is no repo-wide agreement on Deep-tier advisory done-ness criteria,
  rather than inventing one, and names which `docs/ai-consulting/methods/` files a future DoD would
  depend on

#### Scenario: The consulting DoD names a fallback for today's engagements
- **WHEN** an engagement needs a done-ness check today, before a real consulting DoD exists
- **THEN** `docs/ai-consulting/consulting-dod.md` points to the Decision Package's own five-part
  completeness check (`decision-package` skill) as the fallback, rather than leaving the reader with
  no check at all

### Requirement: Cross-domain rules stay single-sourced across the two DoD files
A rule stated as governing more than one domain's DoD (specifically, the Builder/Shipper
Disagreement rule) SHALL remain defined in exactly one file and SHALL be cited, not copied, by any
other DoD file it also governs.

#### Scenario: sales-dod.md cites the Disagreement rule instead of copying it
- **WHEN** a reader opens `docs/ai-sales/sales-dod.md`
- **THEN** it links to the Disagreement rule in `docs/ai-coding/dod-quality-gates.md` rather than
  restating the rule's text

#### Scenario: The Disagreement rule's text exists in exactly one file
- **WHEN** the full text of the Builder/Shipper Disagreement rule is searched for across
  `docs/ai-coding/dod-quality-gates.md` and `docs/ai-sales/sales-dod.md`
- **THEN** the rule's defining text is found in `docs/ai-coding/dod-quality-gates.md` only
