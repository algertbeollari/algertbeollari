#!/usr/bin/env python3
"""Discover every skill reachable from this repo and emit a registry.

Scans three source types:
  1. Local, git-tracked skills: <repo>/**/.claude/skills/*/SKILL.md
  2. Local, git-tracked slash-commands: <repo>/**/.claude/commands/*.md
  3. Cloud-synced plugin skills: ~/.claude/plugins/synced/*/*/skills/*/SKILL.md
     (the synced path is session-specific — this machine's Claude Code
     container today, not necessarily the same on Codex or another host —
     so it is globbed, never hardcoded)

Writes:
  - references/skill-registry.json   (machine-readable, for the other scripts)
  - references/skill-registry.md     (human-readable, Phase 0 deliverable)

This script only reads the filesystem. It does not call any model, execute
any skill, or transmit anything off this machine.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
ORCH_DIR = Path(__file__).resolve().parents[1]
HOME = Path.home()

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class SkillEntry:
    name: str
    source_type: str          # local-skill | local-command | cloud-plugin
    namespace: str             # repo-local | <plugin-folder-name>
    path: str                  # path relative to its own root, for portability
    description: str = ""
    has_frontmatter: bool = False
    frontmatter_raw: str = ""


def parse_frontmatter(text: str) -> tuple[dict, bool]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, False
    raw = m.group(1)
    fields: dict[str, str] = {}
    current_key = None
    for line in raw.splitlines():
        if re.match(r"^[A-Za-z_-]+:", line):
            key, _, val = line.partition(":")
            current_key = key.strip()
            fields[current_key] = _strip_quotes(val.strip())
        elif current_key and line.startswith((" ", "\t")):
            fields[current_key] += " " + _strip_quotes(line.strip())
    return fields, True


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def scan_local_skills(project_root: Path, label: str) -> list[SkillEntry]:
    out = []
    skills_dir = project_root / ".claude" / "skills"
    if not skills_dir.is_dir():
        return out
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        fields, has_fm = parse_frontmatter(text)
        out.append(
            SkillEntry(
                name=fields.get("name", skill_md.parent.name),
                source_type="local-skill",
                namespace=label,
                path=str(skill_md.relative_to(project_root)),
                description=fields.get("description", ""),
                has_frontmatter=has_fm,
            )
        )
    return out


def scan_local_commands(project_root: Path, label: str) -> list[SkillEntry]:
    out = []
    commands_dir = project_root / ".claude" / "commands"
    if not commands_dir.is_dir():
        return out
    for cmd_md in sorted(commands_dir.glob("*.md")):
        if cmd_md.name.upper() == "README.MD":
            continue
        text = cmd_md.read_text(encoding="utf-8", errors="replace")
        fields, has_fm = parse_frontmatter(text)
        out.append(
            SkillEntry(
                name=cmd_md.stem,
                source_type="local-command",
                namespace=label,
                path=str(cmd_md.relative_to(project_root)),
                description=fields.get("description", ""),
                has_frontmatter=has_fm,
            )
        )
    return out


def scan_cloud_plugins() -> list[SkillEntry]:
    out = []
    synced_root = HOME / ".claude" / "plugins" / "synced"
    if not synced_root.is_dir():
        return out
    for workspace_dir in sorted(synced_root.iterdir()):
        if not workspace_dir.is_dir():
            continue
        for plugin_dir in sorted(workspace_dir.iterdir()):
            if not plugin_dir.is_dir():
                continue
            namespace = plugin_dir.name
            for skill_md in sorted(plugin_dir.glob("skills/*/SKILL.md")):
                text = skill_md.read_text(encoding="utf-8", errors="replace")
                fields, has_fm = parse_frontmatter(text)
                out.append(
                    SkillEntry(
                        name=fields.get("name", skill_md.parent.name),
                        source_type="cloud-plugin",
                        namespace=namespace,
                        path=f"{namespace}/{skill_md.relative_to(plugin_dir)}",
                        description=fields.get("description", ""),
                        has_frontmatter=has_fm,
                    )
                )
    return out


def project_label_for(project_root: Path) -> str:
    if project_root == REPO_ROOT:
        return "repo-root"
    return project_root.name


def build_registry() -> list[SkillEntry]:
    entries: list[SkillEntry] = []
    project_roots = [REPO_ROOT]
    for child in sorted(REPO_ROOT.iterdir()):
        if child.is_dir() and (child / ".claude").is_dir() and child.name != ".claude":
            project_roots.append(child)

    for root in project_roots:
        label = project_label_for(root)
        entries.extend(scan_local_skills(root, label))
        entries.extend(scan_local_commands(root, label))

    entries.extend(scan_cloud_plugins())
    return entries


def write_json(entries: list[SkillEntry], out_path: Path) -> None:
    payload = [entry.__dict__ for entry in entries]
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_markdown(entries: list[SkillEntry], out_path: Path) -> None:
    by_source: dict[str, list[SkillEntry]] = {}
    for e in entries:
        by_source.setdefault(f"{e.source_type}:{e.namespace}", []).append(e)

    local_count = sum(1 for e in entries if e.source_type != "cloud-plugin")
    cloud_count = sum(1 for e in entries if e.source_type == "cloud-plugin")
    missing_fm = [e for e in entries if not e.has_frontmatter]

    lines = []
    lines.append("# Skill Registry — generated by inventory_skills.py")
    lines.append("")
    lines.append(
        "This file is **generated, not hand-maintained**. Re-run "
        "`python3 scripts/inventory_skills.py` from inside "
        "`algert-master-orchestrator/` after any skill is added, removed, "
        "or moved, then commit the result. Do not edit the tables below by hand."
    )
    lines.append("")
    lines.append(f"- Local skills/commands discovered: **{local_count}**")
    lines.append(f"- Cloud-synced plugin skills discovered: **{cloud_count}**")
    lines.append(f"- Total: **{len(entries)}**")
    lines.append(
        "- Entries missing a parseable `name`/`description` frontmatter block: "
        f"**{len(missing_fm)}**"
    )
    lines.append("")
    lines.append(
        "> **Known blind spot**: this registry only sees what this machine can "
        "see. It cannot see a Codex installation on a different computer "
        "(e.g. a local Windows `.codex/skills/` directory). Treat any such "
        "location as a separate inventory to be merged in manually, not as "
        "covered by this file."
    )
    lines.append("")

    for key in sorted(by_source):
        group = by_source[key]
        lines.append(f"## {key} ({len(group)})")
        lines.append("")
        lines.append("| name | path | description |")
        lines.append("|---|---|---|")
        for e in sorted(group, key=lambda x: x.name):
            desc = (e.description or "—").replace("|", "\\|")
            if len(desc) > 140:
                desc = desc[:137] + "..."
            lines.append(f"| `{e.name}` | `{e.path}` | {desc} |")
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    entries = build_registry()
    write_json(entries, ORCH_DIR / "references" / "skill-registry.json")
    write_markdown(entries, ORCH_DIR / "references" / "skill-registry.md")
    print(f"Discovered {len(entries)} skill/command entries.")
    print(f"Wrote {ORCH_DIR / 'references' / 'skill-registry.md'}")
    print(f"Wrote {ORCH_DIR / 'references' / 'skill-registry.json'}")


if __name__ == "__main__":
    main()
