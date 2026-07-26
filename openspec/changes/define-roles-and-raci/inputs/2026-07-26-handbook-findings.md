# Seed — Employee Handbook role findings (excerpt for `define-roles-and-raci`)

**Status:** SECONDARY input. Preserved verbatim, **never groomed, never deleted**. The shaped EPIC
(`../proposal.md`) supersedes this as the primary truth but does not replace it. This file sits
alongside, and does not supersede, [`2026-07-25-brainstorm-seed.md`](2026-07-25-brainstorm-seed.md).

**Provenance:** *Employee Handbook — Second Edition (2026)*, 103 pages, released 28.01.2026, supplied
by Eugeniu Costetchi on 2026-07-26. Sections quoted below: **"Role structure — On Roles, Profiles and
Levels"** (p. 65) and **"Brief: what are the project roles?"** (pp. 66–68), cross-checked against
**"Allegory: what are the project roles?"** (pp. 69–72), which repeats the same six roles in
storybook register with no additional normative content.

**Full text location.** The canonical copy of the PDF for this shaping round is
[`../../define-lifecycle-playbooks/inputs/Employee Handbook - Second Edition (2026) (1).pdf`](../../define-lifecycle-playbooks/inputs/Employee%20Handbook%20-%20Second%20Edition%20(2026)%20(1).pdf).
A working copy also sits in this change's own `inputs/` folder, placed there directly by the human.
Neither is groomed; this file quotes only the role-bearing excerpt, in more depth than the sibling
epics need, because the six-role table is **this** change's core correction.

**Why this seed exists.** It reverses a decision. Round-1 shaping concluded from the brainstorm seed
(§5) that Meaningfy has exactly five delivery roles and that "Work Shaper" was a conflation to be
documented rather than a role to be named. The handbook proves otherwise: Meaningfy already had a
named Work Shaper role, with a written mandate, before this shaping round began. The EPIC's DEC-2 is
reversed on the strength of this document.

**Reading instruction from the human (verbatim, applies to all material in this round):**

> "work autonomously towards the completion of this task just up to the moment you are ready to
> implement, ask nothing, assume the provided materials are outdated, but of good quality and need to
> be carried forward to a modern way of working where people govern, and steer and check lightly the
> heavy work of LLM agents"

So: port the *substance* (roles, responsibilities, the process shape), not the *mechanics* written
for a human-only team. Where a practice is ported, state how it adapts to light human steering over
heavy LLM-agent execution.

---

## 1. Roles vs. Profiles (p. 65, verbatim)

> **On Roles, Profiles and Levels**
>
> At Meaningfy we distinguish between Roles and Profiles. Each Profile can have five levels described
> in the section on making a career.
>
> Profiles are defined in terms of skills, competencies and academic background that a person has. We
> hire the following profiles:
>
> - Semantic Engineer
> - Software Engineer
> - DevOps Engineer
> - QA Engineer
>
> Roles are defined in terms of responsibilities in the company or a project. Most often we refer to
> project roles (real-world equivalents in parentheses):
>
> - Mastermind Wizard (Business Developer)
> - Shaper (Project Owner)
> - Builder (Engineering or Implementation Lead)
> - Shipper (Delivery Manager)
> - Quality Overseer (QA Lead)
> - Customer Success Manager (Client Relationship Manager)
>
> The company roles are:
>
> - CEO
> - Operations Officer
> - Finance Officer
> - Communications and Marketing Officer
> - Business Development and Sales Officer

**Load-bearing line for this EPIC:** *"Roles are defined in terms of responsibilities in the company
or a project"*, against *"Profiles are defined in terms of skills, competencies and academic
background"*. This is the handbook's own statement of what the EPIC's DEC-4 asserts — role is a slot
in a process, profile is what a person knows. The Builder role spanning both the Semantic-Engineer
and Software-Engineer profiles (see §2 below) is the handbook's own worked example.

**Note on the company-roles list:** company roles (CEO, Operations Officer, …) are org-chart
positions, deliberately **out of scope** for this EPIC, which covers project roles only.

## 2. The six project roles (pp. 66–68, verbatim substance)

Below, each handbook role, its stated mandate, and how it maps onto the EPIC's model.

| # | Handbook role (allegorical) | Real-world equivalent | Maps to |
|---|---|---|---|
| 1 | Mastermind Wizard | Business Developer | **Sales/Presales** — direct match |
| 2 | **Work Shaper** | **Project Owner** | **Work Shaper** — added as the sixth role by this EPIC |
| 3 | Builder — the Craftsman | Engineering or Implementation Lead | **Solution Builder** — direct match |
| 4 | Reviewer — the Quality Overseer | QA Lead | **no role** — adapted, see §4 |
| 5 | Shipper | Delivery Manager | **Solution Shipper** — direct match |
| 6 | Customer Success Manager — the Wizard of Client Satisfaction | Client Relationship Manager | **no role** — folded into Sales/Presales, see §4 |

The handbook has no equivalent of the EPIC's **Technical Consultant** and no equivalent of the
**Solution Architect**; both are additions from the 2026-07-25 brainstorm and are not contradicted by
the handbook.

### 2.1 Project Owner — the Work Shaper (p. 66, verbatim)

> **Project Owner - the Work Shaper**
>
> The Project Owner is responsible for shaping and guiding the project from its initial concept to
> successful completion. This role involves converting abstract ideas into practical, executable
> project plans, ensuring alignment with the client's vision and project objectives.
>
> **Key Responsibilities and Deliverables:**
>
> - Developing the Work Breakdown Structure based on the request for offer, the offer and adjacent
>   meeting notes with the client.
> - Establishing a project roadmap outlining key milestones, deliverables, and timelines.
> - Writing down the Epic Pitches based on the Shape Up methodology, encompassing important aspects
>   of planning and execution and detailing the scope, challenges, and resources needs.
> - Identifying potential risks and formulating strategies to mitigate them.
> - Overseeing and providing clear guidance and direction from project inception to delivery,
>   ensuring all phases are well-defined and executed.
> - Discover work (as more work is getting done) with the project Builders and map the Epic scope
>   with User Stories (or Tasks).
>
> **Duration of Role:** Although not full-time, this role is pivotal throughout the project
> lifecycle, from initial concept development to the final delivery of the project.
>
> **Reporting Structure:** The Project Owner will report directly to the CEO, ensuring alignment with
> strategic goals and client requirements.

**Observation carried into the EPIC (DEC-2R):** this mandate is, near-verbatim, what the
[`epic-planning`](../../../../skills/epic-planning/SKILL.md) skill already does — "Shape an EPIC from
human seeds, then derive its clarity-gated PLAN". "Writing down the Epic Pitches based on the Shape
Up methodology" *is* authoring `proposal.md`; "map the Epic scope with User Stories" *is* deriving
`tasks.md`. Work Shaper is therefore the human role that owns and steers that skill, and the closest
of all six roles to already having a mature agent counterpart (`epic-planner`).

### 2.2 Builder — the Craftsman (pp. 66–67, verbatim excerpt)

> The project Builder is responsible for the practical execution of project tasks, translating shaped
> conceptual designs into tangible, demonstrable and deliverable outcomes.
>
> **Key Responsibilities and Deliverables:** […]
> - Establishing, prior to starting a task, who will be the reviewer of the work done, and when that
>   review will take place.
> - Discovering work to be done as the work is progressively executed and reporting it to the Project
>   Owner so that he/she can place it in the Epic scope as User Stories (or Tasks).
> - Documenting the development process, the technical decisions, architecture diagrams. […]
>
> **For Software Engineers**
> - Developing and refining software, meticulously crafting each feature and functionality.
>   - Apply TDD, DDD and Onion Architecture.
>
> **For Semantic Engineers**
> - Constructing and evolving knowledge frameworks, ensuring they are comprehensive and accurate.
>   - Apply LOT Methodology.
>
> **Reporting Structure:** Reports to the Project Owner and Delivery Manager, depending on the
> project's nature.

**Load-bearing for the EPIC:** one Builder *role*, two engineering *profiles* under it, differing
only in the methodology applied to the plane being built. This is the handbook's own evidence for the
EPIC's DEC-4 formulation — "a Builder is a Builder for a modelling/ontology project, or for a
software-development process, or for a teaching-and-preparing-materials process". It also shows the
**Builder ↔ Work Shaper work-discovery loop** running in both directions: the Shaper discovers work
*with* Builders, the Builder reports discovered work *to* the Shaper.

### 2.3 Reviewer — the Quality Overseer (p. 67, verbatim)

> The Reviewer is primarily focused on evaluating the work outcomes of colleagues during the Building
> phase. Their responsibility is to ensure that these outcomes align with the project specifications,
> methodologies, and best practices.
>
> **Key Responsibilities and Deliverables**
>
> - Aligning with the Builder on what work needs to be reviewed by when.
> - Actively engaging in the 'four eyes principle', where each piece of work is reviewed by another
>   qualified team member to ensure compliance with Epic Pitch project specifications, quality
>   standards, methodologies and best practices.
> - Providing constructive feedback to colleagues to enhance quality and adherence to project
>   guidelines.
> - Documenting the review process and outcomes, and recommending improvements as necessary.
>
> **Duration of Role:** This role is non-permanent but contextual based on the work done by the team.
> It is crucial throughout the Building phase of the project.
>
> **Reporting Structure:** The Reviewer reports to the Project Owner and Delivery owner.

### 2.4 Delivery Manager — the Shipper (p. 68, verbatim excerpt)

> The Delivery Manager is responsible for overseeing the final phase of the project, ensuring the
> timely and accurate delivery of project outputs to the client. This role involves ensuring that all
> deliverables meet the highest quality standards and are in complete accordance with the contractual
> agreements. […]
> - Conducting comprehensive inspections of the deliverables to guarantee quality and adherence to
>   contract specifications.
> - Facilitating a seamless handover process, achieving full client satisfaction and contractual
>   compliance.

Confirms the EPIC's Solution Shipper: accountable for **contract**-conformance, not Epic-conformance.

### 2.5 Customer Success Manager — the Wizard of Client Satisfaction (p. 68, verbatim excerpt)

> The Customer Success Manager is dedicated to maintaining and enhancing customer relationships. This
> role is pivotal in ensuring clients are not only satisfied with the deliverables, but also engaged
> and content with the overall service experience.
>
> **Key Responsibilities and Deliverables:**
>
> - Managing client relationships and the expectations, and ensuring high levels of customer
>   satisfaction.
> - Leading client meetings for project status updates or delivery demonstrations, with a focus on
>   informing the client and building lasting goodwill engagement.
> - Overseeing the client aftercare process, ensuring a smooth and satisfactory client journey
>   post-delivery.
> - Conducting thorough reviews and feedback sessions with clients to gauge satisfaction and gather
>   insights for improvement.
> - Facilitating the transition of project deliverables to clients, ensuring a ceremonial and
>   satisfactory handover.
>
> **Duration of Role:** This role is intermittent and continuous, with a focus on long-term customer
> relationship management and success.

### 2.6 Business Developer — the Mastermind Wizard (p. 66, verbatim excerpt)

> The primary objective of this role is to identify and create business opportunities, utilising
> strategic insight and innovative approaches to drive commercial growth and expansion. […]
> - Develop a clear, and comprehensive project offer for the client that delimits clearly the scope,
>   deadlines, and the approach.
>
> **Duration of Role:** In a project, this role is exercised in the conception phase. In the company,
> this role is ongoing, with a focus on long-term strategic development within the business.

Confirms the EPIC's Sales/Presales role, and (via the offer deliverable) the document trail the
Shipper later validates against.

## 3. Human directives attached to this material

Inline `EC:` annotations left on `../proposal.md` (round 2), resolved by the revised EPIC and removed
from its text:

1. > "well work shaper is a role. and I can provide you later with some old definitions, make this as
   > a todo to strenghten this section, but for now carry on your understanding. In fact I just did
   > it, I have addedd the employee handbook 2026 to the inputs folder of this epic, and I expect you
   > to consider what s written there about how we work, only adjusted to the realities of having a
   > very potent senior llm agent on the side."
   → resolved by **DEC-2R** (Work Shaper is the sixth role) and the RACI reassignment.
2. > "and roles are not tied to competences but to a set of responsabilities in a process, that is a
   > builder is a builder for modelling ontology project, or for software develoopment process or for
   > teaching and preparing materals process, and a shaper is an architect that either architects the
   > ontology or software of the course .... keep it in mind."
   → resolved by the sharpened **DEC-4**; grounded in §1's Roles-vs-Profiles distinction above.
3. > "I already sommented on roles being more related to a set of responsabilities ain a phase of a
   > workflow, not specific qualifications as those will depend on the type of the project."
   → same, restated by the human; folded into **DEC-4**.
4. > "do not rederive but a proper adjustment and alignment is desirable to avoid vocabulary drift or
   > conflations or ambiguity."
   → resolved by softening the "do not re-derive the lifecycle" rabbit-hole into a rule against
   re-deriving *content* plus a **required consistency pass** once siblings 1–3 land (**DEC-14**).
5. > "if any are needed flag them and mark that need somewhere easy to indentify."
   → resolved by the EPIC's **Known gaps** section.
6. > "adjust to the roles in teh handbook, so there is a work shapr in fact."
   → same as (1); the "No sixth role" no-go is deleted.

## 4. Adaptation decisions taken on this material (summary; full rationale in `../proposal.md`)

- **Quality Overseer is not added as a role.** The four-eyes review it performed is now largely
  carried out by LLM agents ([`meaningfy-code-review`](../../../../skills/meaningfy-code-review/SKILL.md)),
  with the Builder doing the work and the Shipper — or the Work Shaper on non-software planes —
  giving light human sign-off. No dedicated review headcount. The handbook role is cited in the EPIC
  as the pre-LLM-agent precedent this replaces, not silently dropped.
- **Customer Success Manager is not added as a role.** Its aftercare/satisfaction/long-term-
  relationship mandate is exactly the partnership and account-nurture activity already assigned to
  Sales/Presales. Cited as precedent, folded in, not duplicated.
- **Company roles are out of scope.** Project roles only.
- **Handbook mechanics are not ported**: JIRA keys, Confluence spaces, Google-Drive template folders,
  document header/footer rules, career levels. Substance only.
