# Body-agnosticism audit

**Audience: skillery contributors** authoring or editing a skill body — check this before adding a
CLI-specific reference to prose, and update the table if the `body_agnosticism` repo-lint check
flags a new one. Not install documentation.

Skill *bodies* should read identically on Claude Code and opencode. The structural mapping
(frontmatter, tool names, command registration) is the generator's job; the **prose** must not
silently assume one CLI.

This audit covers **every first-party skill**. A skill is `agnostic` if its body names no
CLI-specific command form or path; otherwise it is `neutralised` (rephrased) or recorded as a
`cosmetic-gap` (a Claude-flavoured reference that is harmless because the underlying capability is
delegated and renders per-CLI). The no-go "no body rewrites to accommodate opencode" means the
default disposition is **gap-record, not rewrite** — we record the Claude-ism and its trivial
opencode equivalent rather than churn skill prose.

The repo_lint `body_agnosticism` check enforces **no NEW Claude-isms**: a `/opsx:`- or `.claude/`
-style reference appearing in a SKILL.md body that is *not* in the allowlist below fails the build.

## Result

20 skills audited. 16 agnostic; 4 carry recorded cosmetic gaps. No body was rewritten.

| Skill | Disposition | CLI-specific reference | Why it's a cosmetic gap |
|---|---|---|---|
| epic-planning | cosmetic-gap | `/opsx:explore`, `/opsx:propose` (workflow step labels) | The opsx spine commands are **delegated** — `openspec update --tools opencode` emits `opsx-explore`/`opsx-propose`. The form maps trivially (`/opsx:<id>` ↔ `opsx-<id>`). |
| spec-stewardship | cosmetic-gap | `/opsx:apply`, `/opsx:verify`, `/opsx:sync`, `/opsx:archive` (lifecycle diagram) | Same delegated-spine reason. The lifecycle is identical on both CLIs; only the command prefix differs. |
| guardrails | cosmetic-gap | `.claude/settings.json` (permission/decision bounds) | The agent-permission file is genuinely per-CLI: `.claude/settings.json` on Claude, `.opencode/` config/plugin on opencode. Same intent (encode decision bounds in harness settings), different path. |
| project-setup | cosmetic-gap (by design) | `/opsx:*`, `.claude/` throughout | project-setup is a **scaffolder** that *projects* the spine and the Claude agent layer; emitting these strings is its function, not an accidental assumption. Aligning its convention to AGENTS-canonical (DEC-12) is the project-setup reconciliation follow-up. |
| architecture, bdd-gherkin, ci-cd-delivery, clarity-gate, conceptual-modelling, cosmic-python, decision-package, estimation, executive-communication, explanatory-writing, meaningfy-code-review, meaningfy-git-workflow, meaningfy-release, proposal-writing, semantic-consulting-coach, technical-writing | agnostic | — | No CLI-specific command form or path in the body. |

## Allowlist (regression guard)

These four skills are the *only* SKILL.md bodies permitted to contain `/opsx:`- or `.claude/`-style
references. `tools/repo_lint` (`body_agnosticism`) fails if any other skill body introduces one — so
the gap cannot silently spread.

```
epic-planning      # /opsx: workflow-step labels (delegated spine)
spec-stewardship   # /opsx: lifecycle diagram (delegated spine)
guardrails         # .claude/settings.json (per-CLI permission file)
project-setup      # scaffolder emits the spine + Claude agent layer by design
```

## Closing the gaps later

When the project-setup reconciliation lands, `guardrails` and `project-setup` can phrase the
permission/agent-layer references CLI-neutrally (e.g. "the harness permission settings" with a
per-CLI footnote). The `/opsx:` labels in epic-planning/spec-stewardship are best left as-is: they
are the canonical workflow vocabulary, and a reader on either CLI maps the prefix without friction.
