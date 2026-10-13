---
name: algert-master-orchestrator
description: Pointer to the canonical Algert Master Orchestrator (discovery/classification/routing/governance layer across all skills). This folder (Algert-AI) is entity ID `algert-ai` in the canonical project-boundaries.md — currently UNCONFIRMED, treat as a distinct, undefined entity until the owner completes its row. Use whenever a task in this project could be served by more than one skill, or needs entity-boundary/approval checks before proceeding.
---

# Algert Master Orchestrator — entry point for Algert-AI

This is **not a second copy** of the orchestrator — it is a pointer, kept
so the skill is discoverable while working inside this folder. The
authoritative files live at:

```
../../../.claude/skills/algert-master-orchestrator/SKILL.md
../../../.claude/skills/algert-master-orchestrator/references/
../../../.claude/skills/algert-master-orchestrator/scripts/
```

Read the canonical `SKILL.md` there and follow it. Do not duplicate its
reference files into this folder — a second copy would drift and break the
"single source of truth" principle the orchestrator itself enforces.

## Entity identity of this folder

Per `project-boundaries.md` §2, this folder is entity ID **`algert-ai`**,
status **unconfirmed**. Until the owner (Algert Beollari) fills in what
this entity actually represents (Astero Falcon? the separate "Algert AI
project" repository described by the `brain` skill? something else?), any
work done here must be treated as its own, undefined, mutually
non-trusting context — do not pull in content from `Algert-Tech-AI/`, the
repo root, or any other entity without an approved row in
`project-boundaries.md` §3.

## Before doing anything non-trivial in this folder

1. Open the canonical `project-boundaries.md` and re-read §0 and the
   `algert-ai` row in §2.
2. If the task depends on knowing what this entity actually is, ask the
   owner rather than inferring it from the folder name.
