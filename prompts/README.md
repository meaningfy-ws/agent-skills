# Binding templates

The thin "always-on" layer that wires skills into a project. Two tiers:

| File | Tier | Goes where | Purpose |
|------|------|-----------|---------|
| `global-prompt.md` | Personal default | `~/.claude/CLAUDE.md` | per-developer routing + non-negotiables |
| `CLAUDE.md.template` | Committed project binding | `<repo>/CLAUDE.md` | company-wide, team-shared binding for a repo |

`CLAUDE.md.template` is the **single canonical binding template**. There is no separate
`AGENTS.md.template`.

## Rules

- A binding **routes and mandates**; it never carries the standard (standards live in skills and `docs/`).
- **Single source of authority**: fill in `CLAUDE.md` and keep it as the one source; do not duplicate
  policy across multiple agentic files.
- Each template carries a `meaningfy-template-version` stamp so a consuming repo can tell when it is
  behind. Refresh with `scripts/init-meaningfy-project.sh` (see `docs/environment/setup.md`).

## Optional AGENTS.md symlink

Some tools (e.g. OpenAI Codex, other AGENTS.md-reading tools) load `AGENTS.md` instead of
`CLAUDE.md`. To serve those tools without duplicating policy, create a symlink:

```bash
ln -s CLAUDE.md AGENTS.md
```

This means both files point to the same content. **Do not maintain a separate `AGENTS.md` with
divergent content** — a symlink is the correct pattern whenever cross-tool support is needed.
