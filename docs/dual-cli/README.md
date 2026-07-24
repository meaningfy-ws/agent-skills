# Dual-CLI reference annex

**Audience: skillery contributors/maintainers** extending or auditing dual-CLI parity (adding a
skill, keeping the generated `.opencode/` tree honest, checking an external dependency's opencode
support). **Not** for installing the catalogue — if that's you, go to
[`docs/environment-setup.md`](../environment-setup.md) (front door: [`README.md`](../../README.md))
instead; nothing here restates its content.

This folder also physically holds the per-CLI install runbooks
([`setup-claude.md`](setup-claude.md), [`setup-opencode.md`](setup-opencode.md)) and
[`mcp-setup.md`](mcp-setup.md) — but those belong to the install path above and are reached from
there, not from this page.

The contributor-facing contract docs this page indexes:

| If you want to… | Read |
|---|---|
| Understand source → CLI translation (what generates what) | [`mapping.md`](mapping.md) |
| Regenerate the committed `.opencode/` tree | run `make generate-opencode` (gated by `make validate`) |
| Check an external plugin/skill/MCP server's opencode support | [`compatibility.md`](compatibility.md) |
| See the skill-body CLI-agnosticism audit | [`body-agnosticism-audit.md`](body-agnosticism-audit.md) |
| Understand hook intent → per-CLI binding | [`../../hooks/README.md`](../../hooks/README.md) |

The authoring rule that ties these together lives in
[`AGENTS.md` → How to maintain / extend](../../AGENTS.md#how-to-maintain--extend-the-catalogue) —
read that first. The canonical operating manual is the root [`AGENTS.md`](../../AGENTS.md)
(CLI-agnostic); `CLAUDE.md` is a thin pointer to it. Versions on both CLIs derive from the root
`VERSION` file.
