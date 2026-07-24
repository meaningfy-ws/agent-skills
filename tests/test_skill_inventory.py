"""Codegen-freshness gate for docs/skill-inventory.md — same pattern as
tools/opencode_gen's drift check: regenerate and diff against the committed
file, so a skill/bundle change without regeneration fails the build."""

from pathlib import Path

from tools import skill_inventory

REPO = Path(__file__).resolve().parents[1]


def test_real_repo_generation_is_noop():
    assert skill_inventory.drift_errors(REPO) == []


def test_first_sentence_trims_dense_description():
    description = 'Use to do X. Trigger on "a", "b", "c". Not a greenfield skill.'
    assert skill_inventory._first_sentence(description) == "Use to do X."


def test_related_extracts_backticked_names_across_lines():
    body = (
        "## Boundary & Related Skills\n\n"
        "**Owns:** something.\n\n"
        "**Related:** `foo`, `bar`,\n`baz` (aside).\n\n"
        "## Next Section\n"
    )
    assert skill_inventory._related(body) == ["foo", "bar", "baz"]


def test_tolerant_frontmatter_survives_unquoted_colon():
    text = '---\nname: x\ndescription: A: b, C: d\n---\nbody\n'
    fm = skill_inventory._frontmatter(text)
    assert fm["name"] == "x"
    assert "description" in fm
