---
name: algert-master-orchestrator
description: Intelligence and governance layer that discovers, classifies, routes to, coordinates, and quality-checks every other skill available to Algert Beollari — local repo commands, cloud-synced plugin skills, and DFSA/MLRO compliance skills. Use whenever a task could be served by more than one skill, when it's unclear which specialist skill applies, when a task spans multiple regulated entities or domains, when asked "how many skills do I have" or to audit/inventory skills, or when explicitly invoked as /algert or /master-orchestrator. Does not replace specialist skills — it decides which one(s) to use and enforces entity segregation and approval gates around them.
---

# Algert Master Orchestrator

Governance and routing layer, not a specialist skill. It never substitutes
its own judgement for a specialist skill's regulatory content, and it never
lets information cross a declared entity boundary without an explicit
approval on record.

## 0. Before anything else

Read, in this order, only as far as the task requires:
1. `references/project-boundaries.md` — which entity is this task for, and
   is cross-entity use even permitted.
2. `references/skill-registry.md` — what's actually installed right now
   (regenerate first with `scripts/inventory_skills.py` if it looks stale —
   check the file's own freshness against today's date before trusting it).
3. `references/routing-rules.md` — how to pick the specialist skill(s).
4. `references/regulatory-standards.md`, `references/approval-matrix.md`,
   `references/quality-standards.md` — only once a specialist skill has
   been selected and is about to produce regulatory/governance output.

Do not read every specialist skill's full content "just in case." This is
the progressive-disclosure principle: discover what's needed, load only
that.

## 1. The ten capabilities

| Capability | What it does here |
|---|---|
| Skill discovery | `scripts/inventory_skills.py` scans local `.claude/skills` + `.claude/commands` in every project folder, plus every cloud-synced plugin under `~/.claude/plugins/synced/*/*/skills/*/SKILL.md`, and writes `references/skill-registry.md` + `.json`. Re-run it before trusting any count — never recite a remembered number. |
| Skill classification | `routing-rules.md` §2 maps each namespace to a domain (Regulatory Compliance, Regulatory AI, Personal Second Brain, Professional Documents, Development & Automation, Creative & Research, or "general business — out of DFSA/MLRO scope"). |
| Intelligent routing | `routing-rules.md` §1 and §3 — classify entity, classify domain, shortlist, resolve collisions, decide single- vs multi-skill. |
| Multi-skill execution | `routing-rules.md` §1.5 — coordinate only when sub-parts are genuinely independent; state which skills were combined and why. |
| Conflict detection | `scripts/check_dependencies.py` finds exact-name collisions automatically; `routing-rules.md` §4 and §6 record resolved precedence and contradictory-instruction handling. |
| Regulatory verification | `regulatory-standards.md` — source hierarchy, mandatory currency check, mandatory/best-practice/recommendation labelling. |
| Quality assurance | `quality-standards.md` — the acceptance checklist every output passes before being called final. |
| Skill lifecycle | `scripts/validate_skills.py` checks frontmatter validity; `references/skill-registry.md`'s generation date is the version marker; dependency on another skill is recorded in `dependency-conflicts.md` when found. |
| Context management | §0 above — read boundaries and registry first, specialist content only once routed. |
| Continuous improvement | `quality-standards.md` §7 — propose changes to the owner; never silently edit an approved skill or rule. |

## 2. Entity recognition (non-negotiable)

Before routing, decide which declared entity in `project-boundaries.md` §2
this task belongs to. If the active working directory is `Algert-AI/` or
`Algert-Tech-AI/`, that folder's own `SKILL.md` stub states which entity ID
it is — read it. If it is still marked unconfirmed, **say so and ask**
rather than proceeding as if it were generic/personal work. Being
reachable from the same session is not the same as being the same
project — see `project-boundaries.md` §0 for the concrete reason this
matters (the AF / "Algert AI project" finding).

## 3. Worked example

> "Review AF's AML Manual against current DFSA requirements and
> prepare a Board-ready amendment package."

1. Entity classification: AF — per `project-boundaries.md` §2,
   this entity's data is **not visible from this session**; its baseline
   files live inside cloud-synced skill folders this orchestrator has not
   opened. State that plainly, and ask the owner to confirm the entity
   mapping and supply/point to the AML Manual itself before proceeding,
   rather than fabricating or inferring its content.
2. Once supplied: domain = Regulatory Compliance. Candidate skills:
   `algert-compliance-skills:dfsa-aml-business-risk-assessment`,
   `algert-compliance-skills:dfsa-compliance-mlro`, a policy-drafting
   capability, `algert-compliance-skills:board-meeting-pack-production`.
3. Apply `regulatory-standards.md` — verify cited DFSA provisions are
   current, separate mandatory vs. best practice vs. recommendation.
4. Produce: gap analysis, proposed amendments, approval recommendation —
   structured per the user's standing compliance response format
   (Executive Summary → Applicable Regulations → Risk Assessment →
   Compliance Gaps → Recommendations → Next Steps/Ownership → Final
   answer).
5. Run `quality-standards.md` checklist.
6. Route for decision per `approval-matrix.md` — policy amendment goes to
   Board/delegated committee, never auto-approved here.
7. Never distribute anything from this task into `Algert-AI/`,
   `Algert-Tech-AI/`, or any other entity's context.

## 4. What this skill never does

- Auto-approve an amended policy.
- Assume the Board must approve every document (check `approval-matrix.md`
  for what this specific output type actually needs).
- Move information between declared entities absent an approved row in
  `project-boundaries.md` §3.
- Treat a specialist skill's bundled reference file as more authoritative
  than the live DFSA Rulebook.
- Silently resolve an unresolved name collision — see
  `dependency-conflicts.md` and `routing-rules.md` §4.

## 5. Maintenance

Re-run after any skill is added, removed, or a plugin is enabled/disabled:

```
python3 scripts/inventory_skills.py
python3 scripts/check_dependencies.py
python3 scripts/validate_skills.py
```

Commit the regenerated `references/*.md`/`.json` alongside whatever change
prompted the re-run, so the registry's git history is itself the change
log (lifecycle tracking without a separate database).

## 6. Known gaps (do not claim these are solved)

- **Codex / local Windows skills** (`C:\Users\alger\.codex\skills\...`) are
  invisible to this session entirely. `inventory_skills.py` says so in its
  own output rather than silently omitting them. Treat any count given by
  this orchestrator as "what this Claude Code cloud session can see,"
  never as "everything you have."
- **`anthropic-skills:dfsa-*`** cannot be filesystem-verified from here —
  see `dependency-conflicts.md`. Re-check it by hand periodically.
- **AF's actual data** has not been read by this orchestrator —
  see `project-boundaries.md` §0.
