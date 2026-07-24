# Meaningfy Agent Skills (Skillery)

The company-wide home for working with LLM agents **consistently**: reusable agent **skills**, thin
**agents**, human **methodology & standards** docs, and the **binding templates** that wire them into
any project. Runs identically on **Claude Code** and **opencode** from one set of sources — see
[`docs/dual-cli/`](docs/dual-cli/README.md).

## What this is

A curated, self-validating catalogue. **Skills** carry reusable knowledge; **agents** are thin
execution wrappers; `docs/` is the human canon (method, engineering standards, philosophy);
`prompts/` holds the agentic-file templates. The root binding is **`AGENTS.md`-canonical**:
`AGENTS.md` is the CLI-agnostic operating manual (read natively by opencode) and `CLAUDE.md` is a
thin pointer that adds only Claude-specific guidance (no symlink between them). It also carries the
**spine** — *the durable, traceable spec backbone*
(an [OpenSpec](https://github.com/Fission-AI/OpenSpec) instance + a forked `meaningfy` schema under
[`openspec/`](openspec) and [`spine/`](spine)) — that threads a requirement all the way to a commit.
External skills (superpowers, stream-coding, …) are **referenced, not copied**.

## Who it's for

Bundles are organised by the **role (hat) you wear** — install `meaningfy-core` plus your role(s):

- **Builders / developers** — clean, layered, well-tested Python driven through an AI build loop.
- **Architects / modellers** — system design and the living conceptual (domain) model.
- **Consultants** — advisory work: semantic-tech coaching, decision packages, proposals, estimation.

## What's inside

22 skills in **4 role bundles** — every skill lives in exactly one bundle (no duplication); the
table below is bundle-level only. For the per-skill picture — purpose, which cross-cutting concern
each one serves, and which skills depend on which — see
[`docs/skill-inventory.md`](docs/skill-inventory.md) (a generated map + tables, not hand-maintained).

| Bundle | Skills | Install if you… |
|--------|--------|-----------------|
| **meaningfy-core** | **technical-writing** · **explanatory-writing** · **meaningfy-git-workflow** · **guardrails** | …do anything (cross-cutting basics) |
| **meaningfy-consulting** | **semantic-consulting-coach** · **decision-package** · **proposal-writing** · **estimation** · **executive-communication** | …do advisory / front-of-funnel work |
| **meaningfy-architecture** | **architecture** · **conceptual-modelling** · **modelling-conventions** · **linkml-engineering** | …design systems or model a domain |
| **meaningfy-building** | **epic-planning** · **spec-stewardship** · **clarity-gate** · **bdd-gherkin** · **meaningfy-code-review** · **cosmic-python** · **project-setup** · **ci-cd-delivery** · **meaningfy-release** | …build software with the spine |

Thin **agent** wrappers live in [`agents/`](agents/) — `epic-planner`, `implementer`,
`code-reviewer` — they pin a model + tools and load the skills above.

> **The spine is a *capability*, not a bundle.** `meaningfy-building` carries the skills that drive
> it; the durable spine **assets** (`openspec/` + the forked schema + `spine/` docs) are *projected*
> into your repo by the `project-setup` skill. A spine repo reuses OpenSpec-native artifacts: an
> **EPIC** is the OpenSpec `proposal.md`; a **PLAN** is `design.md` + `tasks.md`.

## Installation

Runs on **Claude Code** and **opencode**, from the same sources, with gate-verified parity — pick
either, you don't need both.

**Start here:** [`docs/environment-setup.md`](docs/environment-setup.md). It's the canonical,
CLI-agnostic entry point — what to install and why — and links you into your CLI's literal,
copy-paste step-by-step (bundles, mandatory deps, root binding, spine commands, an MCP server if you
want one, and a verify step) from there. You shouldn't need to go looking for any other doc to get
installed.

## Getting started

**Skill or agent? The rule of thumb.**
- A **skill** is *on-demand knowledge / method* loaded into your **current** chat — "guide me through
  X". You keep the wheel.
- An **agent** is a *delegated worker* in its **own fresh context** with a fixed role, model, and
  tools — "go do X and report back". It keeps your main context clean.
- **skill = teach / guide me; agent = delegate a whole task.** The Meaningfy agents
  (`epic-planner`, `implementer`, `code-reviewer`) each just load the relevant skills and run them in
  isolation.

**What do I reach for?**

| I want to… | Reach for (in order) |
|---|---|
| Know the code rules (principles, anti-patterns, naming, exceptions, config, layering) | the **[code-principles catalogue](skills/cosmic-python/references/principles-and-anti-patterns.md)** — owned by `cosmic-python`, the single source; every skill/doc cites its `PR-`/`BP-`/`AP-` ids |
| Stand up a new repo | `project-setup` skill → scaffolds layout, tooling, tests, docs, CI, and the spine |
| Build one epic | the loop below (epic-planner → bdd-gherkin → implementer → code-reviewer) |
| Win / scope a client engagement | `semantic-consulting-coach` (think it through) → `decision-package` (produce it) → `proposal-writing` + `estimation` |
| Model a domain | `conceptual-modelling` (the living model + source decision) · `modelling-conventions` (shared craft) |
| Author LinkML / generate typed artefacts | `linkml-engineering` (LinkML → Pydantic/OWL/SHACL, custom templates, gates) |
| Design a system | `architecture` (C4, ADRs, contracts) |
| Write a board paper / client note | `executive-communication` |
| Write docs / a README | `technical-writing` |
| Write a clear explainer / blog-style explanation | `explanatory-writing` |
| Ship a service | `ci-cd-delivery` (deploy contract) |
| Cut / publish a release | `meaningfy-release` (versioning, release branches, PyPI, release notes) |

**The build loop, step by step** (one epic). Drives the OpenSpec `/opsx` verbs — full map in
[`spine/workflows.md`](spine/workflows.md):

| # | Step | `/opsx` verb | Driven by |
|---|------|-------------|-----------|
| 1 | Gather seeds + elicit (incl. test-scenario interview) | `explore` | **epic-planner** agent ◦ `epic-planning` (+ `superpowers:brainstorming`) |
| 2 | Shape the EPIC (= `proposal.md`) | `propose` | **epic-planner** agent ◦ `epic-planning` |
| 3 | Derive the PLAN (`design.md` + `tasks.md`) **+ author `.feature` scenarios** (design-phase artifact) | — | **epic-planner** agent ◦ `epic-planning` **+ `bdd-gherkin`** |
| 4 | Gate the PLAN (≥9/10, **incl. scenario coverage**) | — | `clarity-gate` skill |
| 5 | Implement: **step definitions + code** (TDD, layered) | `apply` | **implementer** agent ◦ `cosmic-python` + `superpowers:test-driven-development` |
| 6 | Verify / review | `verify` | **code-reviewer** agent ◦ `meaningfy-code-review` |
| 7 | Merge deltas into the living specs | `sync` / `archive` | `spec-stewardship` skill |

> BDD scenario authoring is a **design-phase** activity (the `.feature` files are a PLAN artifact the
> clarity gate scores for coverage); only **step definitions** are written at implement time.

## Uninstall & conflicts

Skillery is additive — it rarely *conflicts*, but it can **overlap** with plugins you already have.

**Check what you have:** on **Claude Code**, open the `/plugin` menu (or inspect `enabledPlugins` in
`~/.claude/settings.json`); on **opencode**, list installed plugins via its plugin manager (or inspect
`opencode.json`). The overlaps below are **Claude-plugin** overlaps (`feature-dev`, `code-review` are
`@claude-plugins-official`); on opencode they simply don't apply — the catalogue's skills are loaded
natively instead.

| Situation | What it is | What to do |
|---|---|---|
| Old `meaningfy-engineering` / `-ai-coding` / `-communication` / `-spine` bundles | the **previous** bundle cut | **Migrate:** uninstall them, install the new `meaningfy-core` + `-building` + `-architecture` + `-consulting`. |
| `feature-dev@claude-plugins-official` | official agents (code-architect/explorer/reviewer) overlapping `epic-planner`/`implementer`/`code-reviewer` | **Redundant, not breaking.** Optionally disable `feature-dev` to avoid two voices on the same task. |
| `code-review@claude-plugins-official` | a read-only review *runner* | **Keep** — complementary: it *runs*, `meaningfy-code-review` is the *checklist*. |
| `commit-commands@claude-plugins-official` | commit/push/PR mechanics | **Keep** — `meaningfy-git-workflow` delegates to it. |
| No `stream-coding` / `ponytail` | mandatory external disciplines | **Install them** (see Installation §2). |

> **Worked example (a real setup).** A machine running the *old* 3 meaningfy bundles +
> `feature-dev` + `code-review` + `commit-commands`, **missing** `stream-coding` and `ponytail`,
> needs: (1) migrate the 3 old bundles → the new 4; (2) install `stream-coding` + `ponytail`;
> (3) optionally disable `feature-dev`; (4) keep `code-review` + `commit-commands`. Nothing needs
> hard-removing — it's mostly *renaming the bundles* and *adding the missing mandatory deps*.

## Documentation

| Where | What | Read it when… |
|---|---|---|
| [`docs/dual-cli/`](docs/dual-cli/README.md) | the **dual-CLI reference annex** — per-CLI setup runbooks, source→CLI mapping, compatibility matrix, MCP shapes (install starts at [`environment-setup.md`](docs/environment-setup.md); authoring rules are in [`AGENTS.md`](AGENTS.md#dual-cli-authoring-rules)) | you're installing on opencode, or adding a skill/agent that must work on both CLIs |
| [`docs/ai-coding/`](docs/ai-coding/) | the two-tier method + the `/opsx` runbook + DoD/quality gates | you're learning how we build with agents |
| [`spine/`](spine/) | the spec-backbone conventions (workflows, golden thread, lifecycle) | you're working with `openspec/` / the spine |
| [`docs/engineering-standards/`](docs/engineering-standards/) | testing standard, project structure, coding prompt — these **narrate**; the operational rules are the [code-principles catalogue](skills/cosmic-python/references/principles-and-anti-patterns.md) | you want the durable engineering canon |
| [`docs/engagement/`](docs/engagement/) | the P0–P3 engagement model | you're scoping/running a client engagement |
| [`docs/philosophy/`](docs/philosophy/) | the mindset behind it all | you want the *why* |
| [`spec/`](spec/) | how to author a skill (governance + template) | you're contributing a skill |

> **Coming:** the durable canon (`engineering-standards/`, `philosophy/`, architecture/ADRs) will be
> published to **GitHub Pages** via AsciiDoc + Antora — skillery applying its own documentation
> standard to itself. Tracked as a follow-up (`.claude/HARD-QUESTIONS.md`).

## Repository structure

```
skillery/
├── skills/        # flat: skills/<skill>/  (bundles group them in marketplace.json)
├── agents/        # three thin wrappers (no knowledge): epic-planner, implementer, code-reviewer
├── docs/          # ai-coding/ · engineering-standards/ · philosophy/ · engagement/ · environment-setup.md
├── prompts/       # CLAUDE.md.template, global-prompt.md (AGENTS.md-canonical; CLAUDE.md is a thin pointer)
├── .opencode/     # GENERATED opencode tree (skills/agents/bundles); make generate-opencode — never hand-edit
├── spec/          # authoring spec, governance, skill-template.md, CREATING_SKILLS.md
├── spine/         # the spec-backbone conventions
├── openspec/      # live OpenSpec instance + forked `meaningfy` schema (skillery runs the spine on itself)
├── tools/ + tests/# the self-consistency validator (make validate)
└── .claude-plugin/# marketplace (4 role bundles)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Creating Skills guide](spec/CREATING_SKILLS.md).
Run `make validate` before opening a PR; CI runs it too. The governance method is in
[`spec/skill-repo-governance.md`](spec/skill-repo-governance.md).

## Licensing

Apache 2.0 (see [LICENSE](LICENSE)); individual skills may carry their own `LICENSE.txt`. External
dependencies are attributed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Support

Open an issue, or contact the maintainers at info@meaningfy.ws.
