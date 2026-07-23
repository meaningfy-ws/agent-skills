## MODIFIED Requirements

### Requirement: Writing knowledge has a single home; consumers reference it

Reusable writing guidance SHALL live only in the writing-skill family — `technical-writing`,
`executive-communication` (incl. the `company-voice.md` profile), `explanatory-writing`, and
`writing-antipatterns`. Any other skill that produces prose SHALL reference the relevant family
skill and SHALL NOT restate its guidance. No writing/communication bundle SHALL be (re)introduced;
the role-bundle taxonomy is unchanged.

#### Scenario: A consumer skill needs writing guidance

- **WHEN** a skill such as `epic-planning`, `proposal-writing`, `decision-package`,
  `spec-stewardship`, or `bdd-gherkin` needs writing guidance
- **THEN** it links to the relevant writing-family skill and does not restate that guidance inline

#### Scenario: A consumer skill needs antipattern guidance

- **WHEN** a skill needs to know how a genre-conditional rule inverts, or which defects apply
  regardless of genre
- **THEN** it links to `writing-antipatterns` and does not restate the guarded/unguarded entries
  inline

#### Scenario: The audit finds restated guidance

- **WHEN** the reference audit finds a consumer that restates writing guidance
- **THEN** the restated guidance is replaced with a link to the family skill, and no other consumer
  content is changed
