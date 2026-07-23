"""Generator + gate tests for the opencode distribution tree.

Mappers, gap paths, the error matrix, determinism, coverage, and the
parity/version-sync gates — one covering test per spec scenario.
"""
from pathlib import Path

import pytest

from tools.opencode_gen import gen

REPO = Path(__file__).resolve().parents[1]


# --------------------------------------------------------------- fixtures
def _make_repo(tmp_path: Path, *, version="1.0.0", marketplace=None,
               skills=None, agents=None) -> Path:
    """Build a minimal fixture repo with the four sources."""
    (tmp_path / "VERSION").write_text(version + "\n", encoding="utf-8")
    (tmp_path / ".opencode-version").write_text("1.17.11\n", encoding="utf-8")
    market = marketplace if marketplace is not None else {
        "name": "x", "metadata": {"version": version}, "plugins": [],
    }
    import json
    (tmp_path / ".claude-plugin").mkdir()
    (tmp_path / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps(market), encoding="utf-8")
    for name, body in (skills or {}).items():
        d = tmp_path / "skills" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(body, encoding="utf-8")
    if agents:
        (tmp_path / "agents").mkdir()
        for filename, body in agents.items():
            (tmp_path / "agents" / filename).write_text(body, encoding="utf-8")
    return tmp_path


# ----------------------------------------------------- 6.1 mappers + matrix
def test_skill_passthrough_copies_body(tmp_path):
    repo = _make_repo(tmp_path, skills={"foo": "---\nname: foo\ndescription: d\n---\nbody\n"})
    tree, gaps = gen.map_skill(repo, "foo")
    assert gaps == []
    assert tree[".opencode/skills/foo/SKILL.md"] == b"---\nname: foo\ndescription: d\n---\nbody\n"


def test_skill_pycache_excluded(tmp_path):
    """A skill may ship importable Python assets; its bytecode cache must never
    be mirrored — it's a local build artifact, not a source file (found via
    linkml-engineering's vendored generators tripping this for the first time:
    no prior skill shipped executable Python, so this exclusion never mattered
    before)."""
    repo = _make_repo(tmp_path, skills={"foo": "---\nname: foo\ndescription: d\n---\nbody\n"})
    pycache = repo / "skills" / "foo" / "__pycache__"
    pycache.mkdir()
    (pycache / "mod.cpython-314.pyc").write_bytes(b"\x00")
    (repo / "skills" / "foo" / "mod.py").write_text("x = 1\n", encoding="utf-8")
    tree, gaps = gen.map_skill(repo, "foo")
    assert gaps == []
    assert ".opencode/skills/foo/mod.py" in tree
    assert not any("__pycache__" in path or path.endswith(".pyc") for path in tree)


def test_skill_missing_frontmatter_field_fails(tmp_path):
    repo = _make_repo(tmp_path, skills={"foo": "---\nname: foo\n---\nbody\n"})
    with pytest.raises(ValueError, match="missing 'description'"):
        gen.map_skill(repo, "foo")


def test_agent_model_alias_resolved(tmp_path):
    repo = _make_repo(tmp_path, agents={"a.md": "---\nname: a\ndescription: d\nmodel: opus\n---\nx\n"})
    tree, gaps = gen.map_agent(repo, "a.md")
    out = tree[".opencode/agents/a.md"].decode()
    assert "model: anthropic/claude-opus-4-8" in out
    assert gaps == []


def test_agent_unknown_alias_fails_loudly(tmp_path):
    repo = _make_repo(tmp_path, agents={"a.md": "---\nname: a\ndescription: d\nmodel: zzz\n---\nx\n"})
    with pytest.raises(ValueError, match="unknown model alias 'zzz'"):
        gen.map_agent(repo, "a.md")


def test_agent_tool_mapping_and_gap(tmp_path):
    body = "---\nname: a\ndescription: d\ntools: [Read, Bash, Skill]\ndisallowedTools: [Write, NotebookEdit]\n---\nx\n"
    repo = _make_repo(tmp_path, agents={"a.md": body})
    tree, gaps = gen.map_agent(repo, "a.md")
    out = tree[".opencode/agents/a.md"].decode()
    assert "read: true" in out and "bash: true" in out
    assert "edit: deny" in out
    reasons = {g.reason for g in gaps}
    assert any("Skill" in r for r in reasons)            # tool with no analogue → gap
    assert any("NotebookEdit" in r for r in reasons)     # disallowedTool no analogue → gap


# --------------------------------------------------------- 6.2 determinism
def test_two_runs_byte_identical(tmp_path):
    repo = _make_repo(tmp_path, skills={"foo": "---\nname: foo\ndescription: d\n---\nbody\n"},
                      agents={"a.md": "---\nname: a\ndescription: d\nmodel: opus\n---\nx\n"})
    first, _, _ = gen.build_tree(repo)
    second, _, _ = gen.build_tree(repo)
    assert first == second


def test_real_repo_regeneration_is_noop():
    """The committed tree equals a fresh build — drift gate green on the live repo."""
    assert gen.drift_errors(REPO) == []


# ------------------------------------------------------------- 6.3 coverage
def test_every_source_mapped_or_gapped():
    assert gen.coverage_errors(REPO) == []


def test_coverage_ledger_has_every_skill_and_agent(tmp_path):
    repo = _make_repo(tmp_path, skills={"foo": "---\nname: foo\ndescription: d\n---\nb\n"},
                      agents={"a.md": "---\nname: a\ndescription: d\nmodel: opus\n---\nx\n"})
    _, _, ledger = gen.build_tree(repo)
    assert "skill:foo" in ledger and "agent:a" in ledger


# -------------------------------------------------- 6.4 parity + version-sync
def test_asymmetric_artifact_fails_parity():
    ledger = {"skill:x": {"claude": True, "opencode": False, "gaps": []}}
    assert gen.parity_errors(ledger) != []


def test_symmetric_or_gapped_passes_parity():
    ledger = {
        "skill:x": {"claude": True, "opencode": True, "gaps": []},
        "skill:y": {"claude": True, "opencode": False, "gaps": ["no analogue"]},
    }
    assert gen.parity_errors(ledger) == []


def test_version_mismatch_fails_version_sync(tmp_path):
    repo = _make_repo(tmp_path, version="1.0.0",
                      marketplace={"name": "x", "metadata": {"version": "9.9.9"}, "plugins": []})
    errors = gen.version_sync_errors(repo)
    assert any("marketplace" in e for e in errors)


def test_live_repo_version_sync_clean():
    assert gen.version_sync_errors(REPO) == []
