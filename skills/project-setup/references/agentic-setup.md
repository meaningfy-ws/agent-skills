# Agentic Setup — the CLAUDE-canonical layer

How to stand up the agentic layer of a Meaningfy repo: the canonical **`CLAUDE.md`** (Claude Code
loads it), the optional **`AGENTS.md` symlink → `CLAUDE.md`**, and the regenerable `.claude/` index.
Implements **DEC-4** (CLAUDE-canonical inversion) and **DEC-12** (the global vs repo `CLAUDE.md`
split). The work *memory* now lives in the spine (`openspec/`) — see `spine-projection.md`.

This pillar creates the *containers*. The *content* — EPIC specs, clarity scoring, review
criteria — comes from the installed skillery skills and the spine, not from here. This skill does
**not** vendor those skills.

## Templates this pillar renders

| Template (`assets/templates/agentic/`) | Renders to | Notes |
|----------------------------------------|------------|-------|
| `CLAUDE.md.tmpl` | `CLAUDE.md` (repo root) | **Canonical** agent instructions. `AGENTS.md` symlinks to it. |
| `AGENTS.md.tmpl` | `AGENTS.md` (Windows copy-fallback only) | A thin mirror note; on every other platform `AGENTS.md` is the symlink and this is not rendered. |
| `MEMORY.md.tmpl` | `.claude/memory/MEMORY.md` | Regenerable orientation **index** (≤200 lines). The truth is `openspec/specs/`. |

The `EPIC.md.tmpl`, `PLAN.md.tmpl`, and `task.md.tmpl` templates are **retired** (they survive only
as redirect notes). The EPIC/PLAN/task artifacts are now the spine's native files — see "The artifact
shift" below and `spine-projection.md`.

Placeholders: see the canonical registry in `config-files.md` (chiefly `<<PROJECT_NAME>>`,
`<<PACKAGE>>`, `<<DEFAULT_BRANCH>>`).

## CLAUDE-canonical: `CLAUDE.md` is the source, `AGENTS.md` is a symlink (DEC-4)

`CLAUDE.md` is the single source of truth — Claude Code loads it directly. `AGENTS.md` is an
**optional symlink** to it, so AGENTS.md-aware tools read the same canon. This **inverts** the older
AGENTS-canonical convention: mirrored copies rot, and Claude Code's first-class file is `CLAUDE.md`,
so making it the source removes a layer of indirection while staying tool-neutral.

### Create the symlink

```bash
# from the repo root, after rendering CLAUDE.md
ln -s CLAUDE.md AGENTS.md
git add CLAUDE.md AGENTS.md      # git stores the symlink as a symlink (core.symlinks=true)
```

Verify: `ls -l AGENTS.md` shows `AGENTS.md -> CLAUDE.md`. Edit **only** `CLAUDE.md`; the header
comment in the template says so. Document the symlink in the README so a contributor does not "fix"
it into a copy.

### Windows fallback

Some Windows checkouts cannot materialise symlinks (developer mode off, or
`git config core.symlinks=false`). **The failure is silent and dangerous:** on such a checkout
`AGENTS.md` becomes a literal text file whose entire content is the string `CLAUDE.md` — so a tool
reads the word "CLAUDE.md" as broken instructions. Detect it via the README symlink note (or
`git ls-files -s AGENTS.md` showing mode `120000` upstream but a plain file on disk) and apply the
copy-hook **before first use**.

Fallback: keep two real files and a pre-commit hook that copies `CLAUDE.md → AGENTS.md` so they
never diverge.

```yaml
# .pre-commit-config.yaml — add when symlinks are unavailable
  - repo: local
    hooks:
      - id: sync-agents-md
        name: sync AGENTS.md from CLAUDE.md
        entry: bash -c 'cp CLAUDE.md AGENTS.md && git add AGENTS.md'
        language: system
        files: '^CLAUDE\.md$'
        pass_filenames: false
```

Note the chosen approach (symlink vs copy-hook) in the README either way.

### .gitignore — or not

Commit **both** `CLAUDE.md` and the `AGENTS.md` symlink (or copy). Neither is ignored — they are
project documentation. A fresh clone must get the agent instructions. The only thing to keep out of
git is machine-local agent state, never these files.

## The global vs repo `CLAUDE.md` split (DEC-12)

There are **two** `CLAUDE.md` files with different jobs:

| File | Owns | Loaded |
|------|------|--------|
| **Global** `~/.claude/CLAUDE.md` | the company-wide *standard* — Clean Code, Clean Architecture, testing, tooling, security | every session, every repo |
| **Repo** `./CLAUDE.md` | the *operating manual for this repo* — skill routing, the spine, project specifics | this repo's sessions |

The repo `./CLAUDE.md` **ROUTES to** the global standard and to the installed skills; it **never
restates** the standard. It records only what is specific to this repo (the package(s), the
datastores, the archetype, the spine pointers). This keeps the repo file short and prevents the
single-source-of-authority drift that a restated standard would cause.

## The spine is the work memory (not `.claude/`)

In-flight work and durable truth now live in `openspec/`, not in `.claude/memory/epics/`:

| Meaningfy noun | OpenSpec-native file |
|---|---|
| **EPIC** (work shape) | `openspec/changes/<id>/proposal.md` |
| **PLAN** | `openspec/changes/<id>/design.md` + `tasks.md` (clarity gate scores the pair ≥9/10) |
| normative requirements | `openspec/changes/<id>/specs/<cap>/spec.md` (RFC-2119 SHALL + GWT) |
| durable truth | `openspec/specs/` (deltas merge here on `archive`) |
| seed inputs | `openspec/changes/<id>/inputs/` (preserved, never groomed) |

Drive it with the `/opsx:*` commands (core profile). The full projection mechanics — config,
the pinned schema, the command install — are in `spine-projection.md`.

### The artifact shift (retiring the old templates)

The legacy `.claude/memory/epics/EPIC.md`+`PLAN.md`+`task.md` model is **superseded**. The
scaffolder no longer renders those skeletons; the `.tmpl` files redirect to the spine. Don't
reintroduce parallel epic files under `.claude/` — `proposal.md`/`design.md`/`tasks.md` are the one
home for each fact (no double-spec).

## `.claude/` is a regenerable index (R7)

```
.claude/
├── agents/                 # OPTIONAL thin agent wrappers (or rely on installed skillery agents)
├── skills/                 # PROJECT-SPECIFIC skills only — do NOT vendor the skillery
└── memory/
    └── MEMORY.md           # regenerable orientation INDEX, ≤200 lines, stable patterns only
```

- **`MEMORY.md` is an index, not authority.** It is ≤200 lines (truncated when loaded — curate it):
  stable codebase patterns, key paths, spine pointers. **No** session notes, no unverified
  conclusions, no epic detail (that lives in `openspec/changes/`). If it disagrees with
  `openspec/specs/`, **specs/ wins**.
- **Orientation index of record is `openspec/config.yaml`'s `context:` field** — the native sink.
  `MEMORY.md` is the cheap local echo of it, not a second source.
- `agents/` is optional (the skillery ships thin wrapper agents as plugins); `skills/` holds only
  skills unique to this repo (never copy the shared skillery in).

## How this complements the installed skills (no vendoring)

This skill ships the canonical `CLAUDE.md` (routing + spine pointers) and the `MEMORY.md` index. It
deliberately does **not** restate planning or review knowledge:

- EPIC content, the planning procedure, and the clarity gate → **epic-planning** + **clarity-gate**
  skills, driving the `/opsx:*` workflow.
- BDD features → **bdd-gherkin**; pre-PR review criteria → **meaningfy-code-review**;
  layering rationale → **cosmic-python**; domain model → **conceptual-modelling** (product repos).

`CLAUDE.md`'s "Skill routing" table points the agent at these for every task.

### Installing the spine + skillery (hand-off / DoD)

`CLAUDE.md`'s skill-routing and the `/opsx:*` commands only resolve once the spine and skillery are
installed. This is the single documented place for the install commands; running them is part of
hand-off and the Definition of Done:

```
# the spine (OpenSpec /opsx:* commands, core profile) — the meaningfy schema is already pinned in
npx -y @fission-ai/openspec@<pin> init --tools claude --profile core

# the skillery (the skill routing target set)
/plugin marketplace add meaningfy-ws/skillery
/plugin install meaningfy-core meaningfy-building
/plugin install superpowers@claude-plugins-official
# ponytail — YAGNI / minimal-code discipline (its own marketplace; pairs with cosmic-python)
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

`ponytail` is a third-party plugin (not part of the skillery), so it has its own `marketplace add`.
It is the routing target for "keep the code minimal" in `CLAUDE.md` — the restraint counterpart to
`cosmic-python`'s structure.

## Pointers

- The spine projection (openspec/, schema pin, /opsx:*) → `spine-projection.md`.
- Planning / EPIC content → **epic-planning** skill; spec readiness → **clarity-gate** skill.
- The CLAUDE-canonical + spine target layout → `../../../docs/environment/openspec-setup-guide.md`.
- Architecture guardrails (how `code-anatomy.md` feeds `.importlinter`) → `architecture-guardrails.md`.
