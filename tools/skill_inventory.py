#!/usr/bin/env python3
"""Generate the skill inventory (docs/skill-inventory.md): a Mermaid map plus
per-bundle tables — not a flat database dump.

Deterministic — a pure function of `skills/*/SKILL.md` frontmatter/body,
`.claude-plugin/marketplace.json`, and two small hand-curated mappings
(`PURPOSE_OF` + `PURPOSE_BLURB`, below — the one piece of judgement this file
can't derive mechanically). DO NOT hand-edit the generated doc; regenerate via
`python -m tools.skill_inventory` (or `make skill-inventory`).
`tests/test_skill_inventory.py` fails the build on drift, the same
codegen-freshness pattern as `tools/opencode_gen`.

The Mermaid map shows three relationships:
  - containment    (bundle -> skill)     one subgraph per bundle, skills inside
  - classification (skill -> purpose)    solid line; a small, curated set of
                                          purpose cards cutting across bundles
  - dependency     (skill -> skill)      dashed line; mechanically parsed from
                                          each skill's own "**Delegates:**" /
                                          "**This skill DELEGATES:**" text —
                                          not hand-curated, not the full
                                          "Related" cross-reference graph
                                          (that stays in the per-bundle tables;
                                          at 20+ cross-bundle pairs alone it's
                                          a hairball at this node count, and
                                          "related" is weaker than "depends on")
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

SKILLS_DIR = "skills"
MARKETPLACE = ".claude-plugin/marketplace.json"
OUTPUT = "docs/skill-inventory.md"

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_RELATED = re.compile(r"\*\*Related:\*\*\s*(.+?)(?:\n\n|\Z)", re.DOTALL)
_DELEGATES = re.compile(
    r"\*\*(?:This skill )?delegates:?\*\*\s*(.+?)(?=\n\*\*|\n\n|\n##|\Z)", re.DOTALL | re.IGNORECASE
)
_BACKTICKED = re.compile(r"`([a-z0-9][a-z0-9-]*)`")

# The one hand-curated judgement call: which small, cross-cutting purpose
# category each skill serves, and a one-line explanation of each category.
# Everything else in this file is mechanically derived. Adding a skill without
# adding it here fails the build (see `category_gaps`) rather than silently
# rendering it uncategorised.
PURPOSE_OF: dict[str, str] = {
    # Writing & Communication
    "technical-writing": "Writing & Communication",
    "explanatory-writing": "Writing & Communication",
    "executive-communication": "Writing & Communication",
    "writing-antipatterns": "Writing & Communication",
    # Modelling & Architecture
    "architecture": "Modelling & Architecture",
    "conceptual-modelling": "Modelling & Architecture",
    "modelling-conventions": "Modelling & Architecture",
    "linkml-engineering": "Modelling & Architecture",
    "cosmic-python": "Modelling & Architecture",
    # Process & Governance (the spine build loop + agentic guardrails)
    "epic-planning": "Process & Governance",
    "spec-stewardship": "Process & Governance",
    "clarity-gate": "Process & Governance",
    "guardrails": "Process & Governance",
    # Quality & Review
    "bdd-gherkin": "Quality & Review",
    "meaningfy-code-review": "Quality & Review",
    # Delivery & Ops
    "project-setup": "Delivery & Ops",
    "ci-cd-delivery": "Delivery & Ops",
    "meaningfy-release": "Delivery & Ops",
    "meaningfy-git-workflow": "Delivery & Ops",
    # Consulting & Business
    "semantic-consulting-coach": "Consulting & Business",
    "decision-package": "Consulting & Business",
    "proposal-writing": "Consulting & Business",
    "estimation": "Consulting & Business",
}

PURPOSE_BLURB: dict[str, str] = {
    "Writing & Communication": "clear prose, persuasion, teaching",
    "Modelling & Architecture": "domain models, system design, LinkML",
    "Process & Governance": "the spine build loop + agentic guardrails",
    "Quality & Review": "tests, BDD, pre-PR review",
    "Delivery & Ops": "scaffolding, CI/CD, releases",
    "Consulting & Business": "front-of-funnel advisory work",
}

# Light-but-distinct fills so each purpose reads as a card, not a container —
# deliberately whiter/less saturated than the bundle fades below.
_PURPOSE_FILLS = {
    "Writing & Communication": "#fdf6e3",
    "Modelling & Architecture": "#eafaf5",
    "Process & Governance": "#eef1fb",
    "Quality & Review": "#fdeef0",
    "Delivery & Ops": "#f6f5ef",
    "Consulting & Business": "#fdeef7",
}

_SKILL_FILL = "#1e1e1e"
_SKILL_TEXT = "#ffffff"

# Dark, hue-paired-with-_PURPOSE_FILLS variants for the Relations diagram's
# skill boxes — same white text, but colour-coded by purpose so a dense
# relation graph is still parseable without tracing every line back to a card.
_SKILL_FILLS_BY_CATEGORY = {
    "Writing & Communication": "#7a5c00",
    "Modelling & Architecture": "#0f5c48",
    "Process & Governance": "#2b3a67",
    "Quality & Review": "#7a2030",
    "Delivery & Ops": "#4a4a3a",
    "Consulting & Business": "#6b1f4d",
}

# Pastel, distinct-enough fills for a fade/contained look — one per bundle, in
# marketplace.json's own order.
_BUNDLE_FILLS = ["#eaf3ff", "#fff2e0", "#eafaf0", "#f5eaff"]

# Tighter than Mermaid's defaults (nodeSpacing 50 / rankSpacing 50) — the
# skill lists read as a compact index, not a spread-out chart.
_INIT_DIRECTIVE = "%%{init: {'flowchart': {'nodeSpacing': 12, 'rankSpacing': 45, 'curve': 'basis'}}}%%"


def _skill_dirs(repo: Path) -> dict[str, Path]:
    root = repo / SKILLS_DIR
    return {
        p.name: p / "SKILL.md"
        for p in sorted(root.iterdir())
        if p.is_dir() and (p / "SKILL.md").exists()
    }


def _frontmatter(text: str) -> dict:
    """Parse the YAML frontmatter tolerantly — some descriptions contain
    unquoted colons that trip a strict YAML parser (the platform's own loader
    is lenient), so fall back to a line-by-line `key: value` read. Mirrors
    `tools/repo_lint/lint.py`'s `_frontmatter` (kept independent rather than
    imported — a few lines, not worth coupling two separately-evolving tools)."""
    m = _FRONTMATTER.match(text)
    if not m:
        return {}
    block = m.group(1)
    try:
        data = yaml.safe_load(block)
        if isinstance(data, dict):
            return data
    except yaml.YAMLError:
        pass
    out: dict = {}
    for line in block.splitlines():
        mm = re.match(r"^([A-Za-z][\w-]*):\s?(.*)$", line)
        if mm:
            out.setdefault(mm.group(1), mm.group(2).strip())
    return out


def _first_sentence(description: str) -> str:
    """Trim a dense, trigger-packed frontmatter description to its first
    sentence — the full text is duplicated triggers/keywords, not prose meant
    to read as a table cell."""
    description = " ".join(description.split())
    m = re.search(r"^(.*?[.!?])(\s|$)", description)
    return m.group(1) if m else description


def _related(body: str) -> list[str]:
    m = _RELATED.search(body)
    if not m:
        return []
    return _BACKTICKED.findall(m.group(1))


def _depends_on(body: str, all_names: set[str], self_name: str) -> list[str]:
    """Skills this one explicitly DELEGATES to (a stronger, narrower claim than
    "Related") — parsed from its own text, filtered to first-party skills."""
    m = _DELEGATES.search(body)
    if not m:
        return []
    found = dict.fromkeys(_BACKTICKED.findall(m.group(1)))  # dedupe, keep order
    return [n for n in found if n in all_names and n != self_name]


def _bundles(repo: Path) -> list[dict]:
    """Bundles in marketplace.json's own order, each with its blurb + skill list."""
    marketplace = json.loads((repo / MARKETPLACE).read_text(encoding="utf-8"))
    out = []
    for plugin in marketplace.get("plugins", []):
        skills = [s.replace("./skills/", "").strip("/").split("/")[-1] for s in plugin.get("skills", [])]
        out.append({"name": plugin["name"], "description": plugin.get("description", ""), "skills": skills})
    return out


def collect(repo: Path) -> tuple[list[dict], dict[str, dict]]:
    """Returns (bundles, skills_by_name) — skills_by_name carries
    purpose/related/depends_on/description."""
    bundles = _bundles(repo)
    paths = _skill_dirs(repo)
    all_names = set(paths)
    skills: dict[str, dict] = {}
    for name, path in paths.items():
        text = path.read_text(encoding="utf-8")
        fm = _frontmatter(text)
        skills[name] = {
            "purpose": _first_sentence(fm.get("description", "")),
            "related": _related(text),
            "depends_on": _depends_on(text, all_names, name),
            "category": PURPOSE_OF.get(name),
        }
    return bundles, skills


def category_gaps(bundles: list[dict], skills: dict[str, dict]) -> list[str]:
    """A skill with no PURPOSE_OF entry — fails generation instead of silently
    rendering uncategorised (the same 'coverage' discipline as opencode_gen's
    every-source-mapped-or-gapped gate)."""
    named = {name for b in bundles for name in b["skills"]}
    return sorted(name for name in named if skills.get(name, {}).get("category") is None)


def _node_id(name: str) -> str:
    return "s_" + name.replace("-", "_")


def _category_id(category: str) -> str:
    return "p_" + re.sub(r"[^a-z0-9]+", "_", category.lower()).strip("_")


def render_map(bundles: list[dict], skills: dict[str, dict]) -> str:
    """Containment + classification only — one edge type, kept clean."""
    lines = ["```mermaid", _INIT_DIRECTIVE, "flowchart LR"]
    for b in bundles:
        bid = "b_" + b["name"].replace("-", "_")
        lines.append(f'  subgraph {bid}["{b["name"]}"]')
        for name in b["skills"]:
            if name in skills:  # external skills (e.g. superpowers) aren't first-party rows
                lines.append(f'    {_node_id(name)}["{name}"]')
        lines.append("  end")
    lines.append("")
    categories = sorted({s["category"] for s in skills.values() if s["category"]})
    for category in categories:
        blurb = PURPOSE_BLURB.get(category, "")
        label = f"{category}<br/><sub>{blurb}</sub>" if blurb else category
        lines.append(f'  {_category_id(category)}("{label}")')
    lines.append("")
    for name, data in skills.items():
        if data["category"]:
            lines.append(f"  {_node_id(name)} --> {_category_id(data['category'])}")
    lines.append("")
    for i, b in enumerate(bundles):
        bid = "b_" + b["name"].replace("-", "_")
        lines.append(f"  style {bid} fill:{_BUNDLE_FILLS[i % len(_BUNDLE_FILLS)]},stroke:#999,stroke-width:1px")
    for category in categories:
        fill = _PURPOSE_FILLS.get(category, "#ffffff")
        lines.append(f"  style {_category_id(category)} fill:{fill},color:#000000,stroke:#333,stroke-width:1.5px")
    for name in skills:
        lines.append(f"  style {_node_id(name)} fill:{_SKILL_FILL},color:{_SKILL_TEXT},stroke:#000")
    lines.append("```")
    return "\n".join(lines)


def _related_only(name: str, data: dict, skills: dict[str, dict]) -> list[str]:
    """Related-but-not-a-hard-dependency targets: the weaker relation, first-
    party only (filters out external names like `stream-coding`/`superpowers`,
    which have no node in this diagram)."""
    return [t for t in data["related"] if t in skills and t != name and t not in data["depends_on"]]


def render_relations(bundles: list[dict], skills: dict[str, dict]) -> str:
    """Both skill<->skill relations in one diagram, grouped by bundle (same
    containers/colours as the Map) and skill boxes colour-coded by purpose
    category — a plain uniform-dark box graph at ~90 edges was unreadable;
    grouping + colour-coding was the fix, confirmed by rendering both ways.
    Two distinct line styles: a **thick solid** arrow is *depends on*
    (stronger — mechanically parsed from "Delegates" text); a **thin dashed**
    arrow is *related* (weaker — everything else in the "Related" list)."""
    lines = ["```mermaid", _INIT_DIRECTIVE, "flowchart LR"]
    for b in bundles:
        bid = "b_" + b["name"].replace("-", "_")
        lines.append(f'  subgraph {bid}["{b["name"]}"]')
        for name in b["skills"]:
            if name in skills:
                lines.append(f'    {_node_id(name)}["{name}"]')
        lines.append("  end")
    lines.append("")
    for name, data in skills.items():
        for target in data["depends_on"]:
            lines.append(f"  {_node_id(name)} ==> {_node_id(target)}")
    lines.append("")
    for name, data in skills.items():
        for target in _related_only(name, data, skills):
            lines.append(f"  {_node_id(name)} -.-> {_node_id(target)}")
    lines.append("")
    for i, b in enumerate(bundles):
        bid = "b_" + b["name"].replace("-", "_")
        lines.append(f"  style {bid} fill:{_BUNDLE_FILLS[i % len(_BUNDLE_FILLS)]},stroke:#999,stroke-width:1px")
    for name, data in skills.items():
        fill = _SKILL_FILLS_BY_CATEGORY.get(data["category"], _SKILL_FILL)
        lines.append(f"  style {_node_id(name)} fill:{fill},color:#ffffff,stroke:#000")
    lines.append("```")
    return "\n".join(lines)


def render(bundles: list[dict], skills: dict[str, dict]) -> str:
    total = sum(len(b["skills"]) for b in bundles)
    dependency_count = sum(len(s["depends_on"]) for s in skills.values())
    related_count = sum(len(_related_only(n, d, skills)) for n, d in skills.items())
    header = [
        "# Skill inventory",
        "",
        "<!-- GENERATED by `python -m tools.skill_inventory` (or `make skill-inventory`) —",
        "     DO NOT hand-edit. Source: each skill's SKILL.md frontmatter/body,",
        "     .claude-plugin/marketplace.json, and this file's own PURPOSE_OF/PURPOSE_BLURB",
        "     mappings. tests/test_skill_inventory.py fails the build if this drifts. -->",
        "",
        f"{total} skills across {len(bundles)} role bundles. Install `meaningfy-core` plus the "
        "bundle(s) matching your role — see the root [`README.md`](../README.md).",
        "",
        "## Map",
        "",
        "**Containers** are bundles. **Dark rectangles** are skills. **Light rounded cards** are "
        "the small set of purposes a skill's description was sorted into, cutting across bundles "
        "— each with a one-line explanation of what it covers. The line is *classified as* "
        "(skill → purpose).",
        "",
        render_map(bundles, skills),
        "",
        "## Relations",
        "",
        "Same bundle containers as the Map, but skill boxes are now colour-coded by **purpose** "
        "(the same six categories, one dark shade each) instead of uniform dark — at this many "
        "edges, colour is what makes the grouping legible without tracing every line. Two line "
        f"types, not one: a **thick solid** arrow is *depends on* ({dependency_count} edges, "
        'mechanically parsed from each skill\'s own "Delegates" text — a skill explicitly handing '
        f"something off to another); a **thin dashed** arrow is *related* ({related_count} edges, "
        'everything else in the "Related" list — weaker, a "see also" rather than a hand-off). '
        f"Kept separate from the Map's classification edges — {dependency_count + related_count} "
        "relation edges plus 22 classification edges in one diagram was tried and was a "
        "long-crossing-line mess, confirmed by actually rendering it.",
        "",
        render_relations(bundles, skills),
        "",
    ]
    body = []
    for b in bundles:
        body.append(f"## {b['name']}")
        body.append("")
        body.append(b["description"] + ".")
        body.append("")
        body.append("| Skill | Purpose | Depends on | Related |")
        body.append("|---|---|---|---|")
        for name in b["skills"]:
            data = skills.get(name)
            if data is None:  # external (e.g. superpowers) — no first-party SKILL.md to describe
                continue
            depends = ", ".join(f"`{x}`" for x in data["depends_on"]) if data["depends_on"] else "—"
            related = ", ".join(f"`{x}`" for x in data["related"]) if data["related"] else "—"
            body.append(
                f"| [`{name}`](../skills/{name}/SKILL.md) | {data['purpose']} | {depends} | {related} |"
            )
        body.append("")
    return "\n".join(header + body)


def generate(repo: Path) -> str:
    bundles, skills = collect(repo)
    gaps = category_gaps(bundles, skills)
    if gaps:
        raise ValueError(f"skill(s) missing from PURPOSE_OF in tools/skill_inventory.py: {gaps}")
    return render(bundles, skills)


def drift_errors(repo: Path) -> list[str]:
    expected = generate(repo)
    actual_path = repo / OUTPUT
    if not actual_path.exists():
        return [f"missing generated file: {OUTPUT}"]
    actual = actual_path.read_text(encoding="utf-8")
    return [] if actual == expected else [f"{OUTPUT} is stale — regenerate with `make skill-inventory`"]


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    out = repo / OUTPUT
    out.write_text(generate(repo), encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
