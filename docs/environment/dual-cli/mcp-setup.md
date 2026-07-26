# MCP server setup (Claude Code & opencode)

The catalogue does **not** ship committed MCP server configs. MCP servers carry credentials and
are environment-specific, so each developer installs the servers they need **one by one**,
locally, following the steps below. This page is reference-only in one sense — copy a template,
fill in your own paths/keys, never commit secrets — but the steps themselves are literal: follow
them top to bottom for each server you add.

## Step 1 — Decide what you need

Install only what you use, from the ones this catalogue's skills/agents reference:

| Server | Why | Local package or hosted? |
|---|---|---|
| **GitNexus** | code intelligence, impact analysis (`implementer`/`code-reviewer` agents) | local (npm) |
| **Atlassian** (Confluence / Jira, Rovo) | ticket/doc lookups | hosted (Atlassian-run endpoint) |
| **Google Workspace** (Gmail / Drive / Calendar) | mail/doc/calendar lookups | hosted (OAuth) or CLI-native connector |
| **Odoo** (odoo-mcp-multi) | ERP data access | local (PyPI) |
| **Neo4j** (per database) | graph queries | local (`uvx`) |
| **MongoDB** | document-store queries | local (`npx`) |
| **Context7** | live library documentation | local (`npx`) |

## Step 2 — Open your CLI's config file

Pick your CLI — the config file, key name, and field shapes differ; the server list and what you
put in each block is the same.

**Claude Code** — project `.mcp.json` (or user `~/.claude.json` / settings):
```json
{
  "mcpServers": {
    "<name>": { "command": "<cmd>", "args": ["..."], "env": { "SOME_TOKEN": "${SOME_TOKEN}" } },
    "<remote-name>": { "type": "http", "url": "https://example/mcp",
                        "headers": { "Authorization": "Bearer ${SOME_TOKEN}" } }
  }
}
```

**opencode** — project or `~/.config/opencode/` `opencode.json`, under `"mcp"`:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "<name>": { "type": "local", "command": ["<cmd>", "..."], "enabled": true,
                "environment": { "SOME_TOKEN": "${SOME_TOKEN}" } },
    "<remote-name>": { "type": "remote", "url": "https://example/mcp", "enabled": true,
                        "headers": { "Authorization": "Bearer ${SOME_TOKEN}" } }
  }
}
```

Secrets: use environment variables (`${VAR}` placeholders) in both — never paste a literal token
into either file. The field-name differences between the two shapes are in
[Field-name mapping](#field-name-mapping) below.

## Step 3 — Install the package (if any) and add its block

One sub-step per server from Step 1 — install first if it needs a local package, then add the
matching block to the file you opened in Step 2.

**3a. GitNexus** — install first:
```bash
npm install -g gitnexus            # or: npx gitnexus analyze  (bootstraps .gitnexus/run.cjs, no global install)
```
See [`../../../AGENTS.md`](../../../AGENTS.md) (GitNexus section) for the index/analyze commands this
project already conventions on. Then add:
- Claude Code (`mcpServers`):
  ```jsonc
  "gitnexus": { "command": "node", "args": [".gitnexus/run.cjs", "mcp"] }
  ```
- opencode (`mcp`):
  ```jsonc
  "gitnexus": { "type": "local", "command": ["node", ".gitnexus/run.cjs", "mcp"], "enabled": true }
  ```

**3b. Atlassian** (Confluence / Jira, Rovo) — no local package; Atlassian hosts this endpoint, you
only need an API/OAuth token (or use the CLI's built-in Atlassian connector instead of
self-configuring MCP):
- Claude Code:
  ```jsonc
  "atlassian": { "type": "http", "url": "https://mcp.atlassian.com/v1/sse",
                 "headers": { "Authorization": "Bearer ${ATLASSIAN_TOKEN}" } }
  ```
- opencode:
  ```jsonc
  "atlassian": { "type": "remote", "url": "https://mcp.atlassian.com/v1/sse", "enabled": true,
                 "headers": { "Authorization": "Bearer ${ATLASSIAN_TOKEN}" } }
  ```

**3c. Google Workspace** (Gmail / Drive / Calendar) — no local package either; same shape as
Atlassian, or use the CLI's built-in Google Workspace connector (Gmail, Drive, Calendar each their
own connector). Only self-configure the raw MCP server if you're pointing at your own gateway —
one server per product, or a combined gateway, following the provider's MCP endpoint + OAuth:
- Claude Code:
  ```jsonc
  "google-workspace": { "type": "http", "url": "https://<google-mcp-endpoint>/mcp",
                        "headers": { "Authorization": "Bearer ${GOOGLE_OAUTH_TOKEN}" } }
  ```
- opencode:
  ```jsonc
  "google-workspace": { "type": "remote", "url": "https://<google-mcp-endpoint>/mcp", "enabled": true,
                        "headers": { "Authorization": "Bearer ${GOOGLE_OAUTH_TOKEN}" } }
  ```

**3d. Odoo** (odoo-mcp-multi) — install first (PyPI:
[`odoo-mcp-multi`](https://pypi.org/project/odoo-mcp-multi/), multi-profile Odoo MCP server):
```bash
pip install odoo-mcp-multi
```
This provides the `odoo-mcp` console command used below:
- Claude Code:
  ```jsonc
  "odoo": { "command": "odoo-mcp", "args": ["serve", "--profile", "${ODOO_PROFILE}"],
            "env": { "ODOO_API_KEY": "${ODOO_API_KEY}" } }
  ```
- opencode:
  ```jsonc
  "odoo": { "type": "local", "command": ["odoo-mcp", "serve", "--profile", "${ODOO_PROFILE}"],
            "enabled": true, "environment": { "ODOO_API_KEY": "${ODOO_API_KEY}" } }
  ```

**3e. Neo4j** (per database — repeat per DB, e.g. LUXSE, budget, cargo):
- Claude Code:
  ```jsonc
  "neo4j-<db>": { "command": "uvx", "args": ["mcp-neo4j-cypher", "--db", "<db>"],
                  "env": { "NEO4J_URI": "${NEO4J_URI}", "NEO4J_PASSWORD": "${NEO4J_PASSWORD}" } }
  ```
- opencode:
  ```jsonc
  "neo4j-<db>": { "type": "local", "command": ["uvx", "mcp-neo4j-cypher", "--db", "<db>"], "enabled": true,
                  "environment": { "NEO4J_URI": "${NEO4J_URI}", "NEO4J_PASSWORD": "${NEO4J_PASSWORD}" } }
  ```

**3f. MongoDB**:
- Claude Code:
  ```jsonc
  "mongodb": { "command": "npx", "args": ["-y", "mongodb-mcp-server"],
               "env": { "MDB_MCP_CONNECTION_STRING": "${MDB_MCP_CONNECTION_STRING}" } }
  ```
- opencode:
  ```jsonc
  "mongodb": { "type": "local", "command": ["npx", "-y", "mongodb-mcp-server"], "enabled": true,
               "environment": { "MDB_MCP_CONNECTION_STRING": "${MDB_MCP_CONNECTION_STRING}" } }
  ```

**3g. Context7** (library docs):
- Claude Code:
  ```jsonc
  "context7": { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] }
  ```
- opencode:
  ```jsonc
  "context7": { "type": "local", "command": ["npx", "-y", "@upstash/context7-mcp"], "enabled": true }
  ```

## Step 4 — Verify

Restart your CLI (both Claude Code and opencode load MCP config at startup), then ask the agent to
list its available tools/servers and confirm each one you added shows up. For a server needing a
token, a failed auth call (rather than "server not found") tells you the config loaded but the
credential is wrong — a useful distinction when troubleshooting.

---

## Reference

### Field-name mapping

The two config shapes are structurally equivalent: `command`+`env` (local/stdio) or `url`+`headers`
(remote) — only the field names and the enable convention differ.

| Concept | Claude `.mcp.json` | opencode `opencode.json` |
|---|---|---|
| server map | `mcpServers` | `mcp` |
| local transport | `command` (string) + `args[]` | `command[]` (argv array) |
| local env | `env` | `environment` |
| remote transport | `type: "http"`, `url` | `type: "remote"`, `url` |
| remote auth | `headers` | `headers` |
| enable toggle | (omit to enable) | `enabled: true` |

> ⚠️ These templates are **illustrative defaults** — confirm the exact command/endpoint/auth against
> each tool's own current docs before use. Endpoints and package names change. Keep all secrets in
> environment variables.
