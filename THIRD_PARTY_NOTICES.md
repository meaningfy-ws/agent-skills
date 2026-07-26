# Third-Party Notices

This repository is licensed under Apache 2.0 (see `LICENSE`). Individual skills may
carry their own `LICENSE.txt`; where present, that license governs the skill.

## Referenced external skills and plugins

The Meaningfy skills and methodology **reference** (and depend on, but do not vendor)
the following external Claude Code skills/plugins. They are installed separately — see
[`docs/environment/setup.md`](docs/environment/setup.md). Each remains under its own
license held by its respective owner:

| Component | Role here | Source |
|-----------|-----------|--------|
| `superpowers` (test-driven-development, systematic-debugging, verification-before-completion, brainstorming) | Mandatory engineering disciplines referenced by Meaningfy skills | claude-plugins-official |
| `stream-coding` | Documentation-first delivery methodology | external skill |
| `commit-commands` | Commit / push / PR mechanics | claude-plugins-official |
| `code-review` | Read-only PR review command | claude-plugins-official |
| `gitnexus-*` | Code intelligence / impact analysis | external plugin |
| `context7` | Up-to-date library documentation (MCP) | external plugin |

No source code from these components is copied into this repository; Meaningfy skills
reference them by name. If attribution requirements change, update this file.
