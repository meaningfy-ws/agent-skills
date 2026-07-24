"""Pure generator + gates for the opencode distribution tree.

Design contract: ``docs/dual-cli/mapping.md`` (source→CLI tables) and the EPIC
``dual-cli-generator`` (DEC-1…DEC-6). Output is deterministic (sorted keys,
fixed field order, no timestamps) so the drift gate's diff is meaningful.
"""
from __future__ import annotations

import json
import re
from collections import namedtuple
from pathlib import Path

import yaml

# ------------------------------------------------------------------ paths
SKILLS_DIR = "skills"
AGENTS_DIR = "agents"
MARKETPLACE = ".claude-plugin/marketplace.json"
VERSION_FILE = "VERSION"
OPENCODE_VERSION_FILE = ".opencode-version"
OPENCODE_DIR = ".opencode"
OPENCODE_CONFIG = "opencode.json"
PACKAGE_JSON = "package.json"
# opencode reads spine /opsx commands via `openspec update --tools opencode`, so
# these command sources are out of scope for the generator (EPIC rabbit-hole).
DELEGATED_COMMAND_DIRS = (".claude/commands/opsx",)

# ----------------------------------------------------------------- mapping
# Pinned model aliases (design "Model-alias"); unknown alias → fail loudly.
MODEL_ALIASES = {
    "opus": "anthropic/claude-opus-4-8",
    "sonnet": "anthropic/claude-sonnet-4-6",
    "haiku": "anthropic/claude-haiku-4-5",
}
# Claude tool name → opencode built-in tool name (design "Tool-name").
TOOL_NAMES = {
    "Read": "read", "Edit": "edit", "Write": "write", "Bash": "bash",
    "Grep": "grep", "Glob": "glob", "WebFetch": "webfetch",
}
# disallowedTools → opencode permission capability (deny). Tools that map to no
# permission capability (e.g. NotebookEdit) become a recorded gap, not a silent drop.
TOOL_PERMISSION = {
    "Edit": "edit", "Write": "edit", "Bash": "bash", "WebFetch": "webfetch",
}

Gap = namedtuple("Gap", "source cli reason")

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)


# ---------------------------------------------------------------- read layer
def read_text(repo: Path, rel: str) -> str:
    return (repo / rel).read_text(encoding="utf-8")


def version(repo: Path) -> str:
    return read_text(repo, VERSION_FILE).strip()


def opencode_version(repo: Path) -> str:
    return read_text(repo, OPENCODE_VERSION_FILE).strip()


def _split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Raises ValueError if absent. Parsing is
    tolerant of unquoted colons (the platform loader is lenient, so we must be):
    fall back to a line scanner when strict YAML fails."""
    m = _FRONTMATTER.match(text)
    if not m:
        raise ValueError("no top-of-file YAML frontmatter")
    block, body = m.group(1), m.group(2)
    try:
        data = yaml.safe_load(block)
        if isinstance(data, dict):
            return data, body
    except yaml.YAMLError:
        pass
    out: dict = {}
    for line in block.splitlines():
        mm = re.match(r"^([A-Za-z][\w-]*):\s?(.*)$", line)
        if mm:
            out.setdefault(mm.group(1), mm.group(2).strip())
    return out, body


def skill_dirs(repo: Path) -> list[str]:
    root = repo / SKILLS_DIR
    if not root.exists():
        return []
    return sorted(p.name for p in root.iterdir()
                  if p.is_dir() and (p / "SKILL.md").exists())


def agent_files(repo: Path) -> list[str]:
    root = repo / AGENTS_DIR
    if not root.exists():
        return []
    return sorted(p.name for p in root.glob("*.md"))


def command_files(repo: Path) -> list[Path]:
    """First-party, non-opsx command sources. opsx is delegated (out of scope)."""
    out: list[Path] = []
    cmds = repo / ".claude" / "commands"
    if not cmds.exists():
        return out
    delegated = {(repo / d).resolve() for d in DELEGATED_COMMAND_DIRS}
    for p in sorted(cmds.rglob("*.md")):
        if any(parent in delegated for parent in p.resolve().parents):
            continue
        out.append(p)
    return out


def bundle_membership(repo: Path) -> dict[str, list[str]]:
    """Bundle name → sorted skill names, read from marketplace.json (the truth)."""
    data = json.loads(read_text(repo, MARKETPLACE))
    out: dict[str, list[str]] = {}
    for plugin in data.get("plugins", []):
        out[plugin["name"]] = sorted(
            s.replace("./skills/", "").strip("/").split("/")[-1]
            for s in plugin.get("skills", [])
        )
    return dict(sorted(out.items()))


# -------------------------------------------------------------- emit helpers
def _json_bytes(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def _frontmatter_block(fields: list[tuple[str, object]], body: str) -> bytes:
    """Build a markdown file with a fixed-order YAML frontmatter block. Field
    order is the list order (deterministic), values dumped via yaml for scalars
    and flow style for containers."""
    lines = ["---"]
    for key, val in fields:
        if val is None:
            continue
        dumped = yaml.safe_dump(val, default_flow_style=True, sort_keys=True,
                                allow_unicode=True).strip()
        lines.append(f"{key}: {dumped}")
    lines.append("---")
    block = "\n".join(lines) + "\n"
    if body:
        block += body if body.startswith("\n") else "\n" + body
    return block.encode("utf-8")


# ------------------------------------------------------------------ mappers
def map_skill(repo: Path, name: str) -> tuple[dict[str, bytes], list[Gap]]:
    """D1 — skills pass through unchanged; only validate opencode-required
    frontmatter (name/description). The whole skill dir is copied so reference
    files travel with SKILL.md."""
    src = repo / SKILLS_DIR / name
    text = (src / "SKILL.md").read_text(encoding="utf-8")
    fm, _ = _split_frontmatter(text)
    for field in ("name", "description"):
        if not fm.get(field):
            raise ValueError(f"skill '{name}': SKILL.md missing '{field}'")
    tree: dict[str, bytes] = {}
    for f in sorted(src.rglob("*")):
        if "__pycache__" in f.parts:
            continue  # a skill may ship importable Python assets; never mirror their bytecode cache
        if f.is_file() and f.suffix not in (".pyc", ".pyo"):
            rel = f.relative_to(src).as_posix()
            tree[f"{OPENCODE_DIR}/skills/{name}/{rel}"] = f.read_bytes()
    return tree, []


def map_agent(repo: Path, filename: str) -> tuple[dict[str, bytes], list[Gap]]:
    """D2 — table-driven agent frontmatter map; unmappable fields → Gap."""
    name = filename[:-3]
    text = (repo / AGENTS_DIR / filename).read_text(encoding="utf-8")
    fm, body = _split_frontmatter(text)
    gaps: list[Gap] = []

    alias = fm.get("model")
    if alias is not None and alias not in MODEL_ALIASES:
        raise ValueError(f"agent '{name}': unknown model alias '{alias}'")
    model = MODEL_ALIASES.get(alias) if alias else None

    tools_map: dict[str, bool] = {}
    for t in fm.get("tools", []) or []:
        if t in TOOL_NAMES:
            tools_map[TOOL_NAMES[t]] = True
        else:
            gaps.append(Gap(f"agents/{filename}", "opencode",
                            f"tool '{t}' has no opencode analogue"))

    permission: dict[str, str] = {}
    for t in fm.get("disallowedTools", []) or []:
        if t in TOOL_PERMISSION:
            permission[TOOL_PERMISSION[t]] = "deny"
        else:
            gaps.append(Gap(f"agents/{filename}", "opencode",
                            f"disallowedTools '{t}' has no opencode permission analogue"))

    fields = [
        ("description", fm.get("description")),
        ("mode", "primary" if fm.get("primary") else "subagent"),
        ("model", model),
        ("tools", tools_map or None),
        ("permission", permission or None),
        ("color", fm.get("color")),
        ("skills", fm.get("skills")),
    ]
    content = _frontmatter_block(fields, body)
    return {f"{OPENCODE_DIR}/agents/{name}.md": content}, gaps


def map_command(repo: Path, path: Path) -> tuple[dict[str, bytes], list[Gap]]:
    """D3 — emit `.opencode/commands/<id>.md` with template/$ARGUMENTS. Currently
    no non-opsx command sources exist; this runs only if one is added."""
    name = path.stem
    text = path.read_text(encoding="utf-8")
    try:
        fm, body = _split_frontmatter(text)
    except ValueError:
        fm, body = {}, text
    fields = [
        ("description", fm.get("description")),
        ("template", body.strip() + "\n$ARGUMENTS"),
    ]
    return {f"{OPENCODE_DIR}/commands/{name}.md": _frontmatter_block(fields, "")}, []


# ----------------------------------------------------------------- assembly
def build_tree(repo: Path) -> tuple[dict[str, bytes], list[Gap], dict]:
    """Build the full in-memory opencode tree + gaps + parity ledger. Pure: no
    writes, no reads of the generated tree. Returns (files, gaps, ledger)."""
    ver = version(repo)
    files: dict[str, bytes] = {}
    gaps: list[Gap] = []
    ledger: dict[str, dict] = {}

    for name in skill_dirs(repo):
        tree, g = map_skill(repo, name)
        files.update(tree)
        gaps.extend(g)
        ledger[f"skill:{name}"] = {"claude": True, "opencode": True, "gaps": [x.reason for x in g]}

    for filename in agent_files(repo):
        tree, g = map_agent(repo, filename)
        files.update(tree)
        gaps.extend(g)
        ledger[f"agent:{filename[:-3]}"] = {"claude": True, "opencode": True,
                                            "gaps": [x.reason for x in g]}

    for path in command_files(repo):
        tree, g = map_command(repo, path)
        files.update(tree)
        gaps.extend(g)
        ledger[f"command:{path.stem}"] = {"claude": True, "opencode": True,
                                          "gaps": [x.reason for x in g]}

    # opencode manifest + bundle manifests, version written from VERSION (D4).
    files[OPENCODE_CONFIG] = _json_bytes({
        "$schema": "https://opencode.ai/config.json",
        "version": ver,
    })
    files[f"{OPENCODE_DIR}/bundles.json"] = _json_bytes({
        "version": ver,
        "bundles": bundle_membership(repo),
    })

    files[f"{OPENCODE_DIR}/PARITY.md"] = _parity_report(ver, ledger)
    files[f"{OPENCODE_DIR}/GAP.md"] = _gap_report(ver, gaps)
    return dict(sorted(files.items())), gaps, dict(sorted(ledger.items()))


def _parity_report(ver: str, ledger: dict) -> bytes:
    lines = ["# Parity report", "",
             f"> Generated from VERSION `{ver}` — do not hand-edit.", "",
             "| Artifact | Claude | opencode | Gaps |", "|---|---|---|---|"]
    for art, row in sorted(ledger.items()):
        lines.append(f"| `{art}` | {'✓' if row['claude'] else '—'} | "
                     f"{'✓' if row['opencode'] else '—'} | {len(row['gaps'])} |")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _gap_report(ver: str, gaps: list[Gap]) -> bytes:
    lines = ["# Gap report", "",
             f"> Generated from VERSION `{ver}` — do not hand-edit.", ""]
    if not gaps:
        lines.append("No gaps — every source artifact has a native opencode equivalent.")
    else:
        lines += ["| Source | CLI | Reason |", "|---|---|---|"]
        lines += [f"| `{g.source}` | {g.cli} | {g.reason} |"
                  for g in sorted(gaps)]
    return ("\n".join(lines) + "\n").encode("utf-8")


# -------------------------------------------------------------------- write
def write_tree(repo: Path) -> list[str]:
    """Emit the tree to disk (idempotent). Also writes VERSION into
    marketplace.json metadata.version. Returns the list of written paths."""
    files, _, _ = build_tree(repo)
    # Remove a stale committed tree so deletions are reflected (hand-edits/orphans).
    import shutil
    target = repo / OPENCODE_DIR
    if target.exists():
        shutil.rmtree(target)
    written: list[str] = []
    for rel, data in files.items():
        dest = repo / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        written.append(rel)
    _sync_marketplace_version(repo)
    _sync_package_version(repo)
    return written


def _sync_marketplace_version(repo: Path) -> None:
    path = repo / MARKETPLACE
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("metadata", {})["version"] = version(repo)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _sync_package_version(repo: Path) -> None:
    path = repo / PACKAGE_JSON
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    data["version"] = version(repo)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# -------------------------------------------------------------------- gates
def drift_errors(repo: Path) -> list[str]:
    """Committed tree must equal a fresh build (D5). Compares the in-memory plan
    against on-disk bytes — no temp dir needed."""
    files, _, _ = build_tree(repo)
    out: list[str] = []
    for rel, data in files.items():
        dest = repo / rel
        if not dest.exists():
            out.append(f"missing generated file: {rel}")
        elif dest.read_bytes() != data:
            out.append(f"drifted: {rel}")
    # Any committed file under .opencode/ not in the plan is an orphan.
    planned = set(files)
    od = repo / OPENCODE_DIR
    if od.exists():
        for f in od.rglob("*"):
            if f.is_file():
                rel = f.relative_to(repo).as_posix()
                if rel not in planned:
                    out.append(f"orphan generated file: {rel}")
    return sorted(out)


def parity_errors(ledger: dict) -> list[str]:
    """Every first-party artifact must have both CLIs covered, or a recorded gap
    where a side is missing (D6)."""
    out: list[str] = []
    for art, row in sorted(ledger.items()):
        if row["claude"] and not row["opencode"] and not row["gaps"]:
            out.append(f"asymmetric artifact (claude only, no gap): {art}")
        if row["opencode"] and not row["claude"] and not row["gaps"]:
            out.append(f"asymmetric artifact (opencode only, no gap): {art}")
    return out


def version_sync_errors(repo: Path) -> list[str]:
    """Every tree's declared version must equal root VERSION (D4)."""
    ver = version(repo)
    out: list[str] = []
    market = json.loads(read_text(repo, MARKETPLACE))
    if market.get("metadata", {}).get("version") != ver:
        out.append(f"marketplace.json metadata.version != VERSION ({ver})")
    cfg = repo / OPENCODE_CONFIG
    if cfg.exists():
        if json.loads(cfg.read_text(encoding="utf-8")).get("version") != ver:
            out.append(f"opencode.json version != VERSION ({ver})")
    bundles = repo / OPENCODE_DIR / "bundles.json"
    if bundles.exists():
        if json.loads(bundles.read_text(encoding="utf-8")).get("version") != ver:
            out.append(f".opencode/bundles.json version != VERSION ({ver})")
    package = repo / PACKAGE_JSON
    if package.exists():
        if json.loads(package.read_text(encoding="utf-8")).get("version") != ver:
            out.append(f"package.json version != VERSION ({ver})")
    return out


def coverage_errors(repo: Path) -> list[str]:
    """Every source skill/agent/command is mapped or gap-recorded — nothing
    silently dropped (DEC-3)."""
    _, _, ledger = build_tree(repo)
    out: list[str] = []
    for name in skill_dirs(repo):
        if f"skill:{name}" not in ledger:
            out.append(f"skill '{name}' unaccounted for")
    for filename in agent_files(repo):
        if f"agent:{filename[:-3]}" not in ledger:
            out.append(f"agent '{filename}' unaccounted for")
    for path in command_files(repo):
        if f"command:{path.stem}" not in ledger:
            out.append(f"command '{path.name}' unaccounted for")
    return out


def all_gate_errors(repo: Path) -> list[str]:
    _, _, ledger = build_tree(repo)
    out: list[str] = []
    out += [f"drift: {e}" for e in drift_errors(repo)]
    out += [f"parity: {e}" for e in parity_errors(ledger)]
    out += [f"version-sync: {e}" for e in version_sync_errors(repo)]
    out += [f"coverage: {e}" for e in coverage_errors(repo)]
    return out
