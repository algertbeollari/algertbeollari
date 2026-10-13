# Routing Rules

How the orchestrator picks specialist skill(s) for an incoming task. Read
`skill-registry.md` (current inventory) and `dependency-conflicts.md`
(current name collisions) before routing anything non-trivial — both are
generated, so they reflect what is actually installed right now, not what
this file assumes.

## 1. Routing sequence

1. **Classify the entity.** Before anything else, decide which declared
   entity (`project-boundaries.md` §2) this task belongs to. If it is
   ambiguous or spans more than one entity, stop and ask — do not guess and
   do not proceed under "whichever is loaded by default."
2. **Classify the domain.** One or more of: Regulatory Compliance (DFSA/
   FSRA/AML/Risk), Regulatory AI (architecture/requirements/governance),
   Personal Second Brain (memory/productivity/planning), Professional
   Documents (policies/reports/reviews), Development & Automation (Codex/
   Claude/GitHub), Creative & Research (presentations/media/research).
3. **Shortlist candidates** from `skill-registry.md` whose `description`
   matches the task, scoped to namespaces permitted for the classified
   entity (see §3).
4. **Resolve collisions.** If more than one namespace claims the same
   skill `name` (see `dependency-conflicts.md`), apply the precedence
   table in §4. If no rule covers the collision, ask rather than pick
   silently.
5. **Decide single- vs multi-skill.** Most tasks route to exactly one
   specialist skill. Coordinate multiple only when the task genuinely has
   independent sub-parts (e.g. "review the AML manual AND draft the board
   paper" = policy/gap-analysis skill + board-memo skill), and say which
   skills were combined and why.
6. **Apply the regulatory/quality/approval gates** in
   `regulatory-standards.md`, `quality-standards.md`, and
   `approval-matrix.md` before presenting output as final.

## 2. Domain → namespace map (current inventory)

This is a starting map, not exhaustive — re-derive from `skill-registry.md`
whenever a namespace is added. Namespaces not listed here are **out of
scope by default** (see §5) until added deliberately.

| Domain | Primary namespace(s) | Notes |
|---|---|---|
| Regulatory Compliance (DFSA/FSRA/AML/Risk) | `algert-compliance-skills:dfsa-*`, `algert-compliance-skills:uae-*`, `algert-compliance-skills:difc-data-protection` | Canonical source — see §4 for the `anthropic-skills:dfsa-*` shadow. |
| Regulatory AI (governance of AI itself) | `ai-governance-legal:*` | Distinct from "Regulatory Compliance" above — this is about regulating AI systems (EU AI Act etc.), not DFSA financial regulation. Do not conflate the two domains even though both are "regulatory." |
| Legal practice areas (if ever used) | `commercial-legal:*`, `employment-legal:*`, `corporate-legal:*`, `privacy-legal:*`, `regulatory-legal:*`, `legal:*` | General-purpose legal plugin bundles, not DFSA-specific. Treat as out of scope for DFSA/MLRO work unless a task explicitly needs general contract/employment/privacy help. |
| Personal Second Brain | `algert-compliance-skills:brain`, `productivity:*`, local `shortcuts` | `brain` is specifically the "Algert AI project" continuity skill — see `project-boundaries.md` §0 before invoking it; confirm which entity's "brain" is meant. |
| Professional Documents | `algert-compliance-skills:docx/pptx/xlsx/pdf`, `algert-compliance-skills:board-meeting-pack-production`, `algert-compliance-skills:executive-briefing`, `algert-compliance-skills:presentation-*`, local `boardmemo`/`checklist`/`email` | |
| Development & Automation | local repo commands, `engineering:*`, `anthropic-skills:skill-creator`, `anthropic-skills:mcp-builder`, this orchestrator's own `scripts/` | |
| Creative & Research | `algert-compliance-skills:infographic-creator`, `algert-compliance-skills:web-video-presentation`, `algert-compliance-skills:remotion-*`, `anthropic-skills:research`, `anthropic-skills:deep-research` | |
| General business functions (sales/marketing/HR/finance/etc.) | `sales:*`, `marketing:*`, `human-resources:*`, `finance:*`, `small-business:*`, `figma:*`, `wix:*`, `canva:*`, `adobe-for-creativity:*`, `brightdata-plugin:*`, `fastly-agent-toolkit:*`, etc. | Not part of the DFSA/MLRO/Risk remit. Route here only if the user is plainly doing non-compliance work (e.g. drafting a sales email), and never let these namespaces' skills touch entity-classified compliance data. |

## 3. Entity → permitted namespace scoping

Until `project-boundaries.md` §2 placeholders are completed, **every
entity other than `repo-root` is scoped to zero cloud namespaces** except
read-only use of this orchestrator's own discovery scripts. This is
intentionally restrictive: it is easier to safely widen scope once an
entity's regulatory status is confirmed than to discover after the fact
that an unconfirmed entity was given access to live DFSA reporting
baselines.

## 4. Collision precedence rules

Re-run `scripts/check_dependencies.py` to get the current list — treat the
rules below as the only ones pre-resolved; anything else it reports is
**unresolved** and must be asked about, not guessed.

| Collision | Resolution |
|---|---|
| `algert-compliance-skills:dfsa-*` vs `anthropic-skills:dfsa-*` (recorded in `dependency-conflicts.md`, not independently re-verifiable from this filesystem) | **`algert-compliance-skills` wins.** It is the deliberately maintained, owner-curated pack. Treat `anthropic-skills:dfsa-*` as a possibly-stale mirror; if it contains a skill `algert-compliance-skills` lacks (e.g. `dfsa-client-assets-crisis-pack`), flag the gap to the owner rather than silently using the mirror's version. |
| Generic local commands duplicated across `repo-root` / `Algert-AI` / `Algert-Tech-AI` (e.g. `brief`, `debug`, `summarize`, all 49) | **Not a real conflict** — each entity is meant to carry its own copy once they diverge (see `project-boundaries.md` §0). Use the copy that lives inside the active entity's own folder; never reach into another entity's folder to use its copy. |
| `cold-start-interview` / `customize` / `matter-workspace` across six `*-legal:*` plugin bundles | Resolve by which legal practice area the task actually is (commercial vs employment vs corporate vs privacy vs regulatory vs AI-governance) — these are deliberately parallel, not accidental duplicates. Pick by domain match, not by listing order. |
| `account-research` / `call-prep` (`common-room` vs `sales`), `competitive-brief` (`marketing` vs `product-management`), `content-strategy` (`searchfit-seo` vs `small-business`), `build-dashboard` (`algert-compliance-skills` vs `data`) | None of these are in the DFSA/MLRO remit. If ever invoked, ask which the user means — do not infer from skill-name popularity. |

## 5. Out-of-scope by default

A namespace not mapped in §2 is **not** to be auto-selected even if its
`description` text matches keywords in the task. Surface it as "found but
not yet classified" and ask before routing to it. This keeps the
orchestrator's blast radius bounded as the cloud catalogue grows — the
"for the future ones too" requirement is handled by re-running
`inventory_skills.py`, not by silently trusting every newly-synced plugin.

## 6. Conflict detection beyond name collisions

Besides exact-name collisions, watch for:
- **Contradictory instructions** between two candidate skills (e.g. one
  says "never conclude a filing decision," another's generic template
  implies a conclusion). When both could apply, the compliance-specific
  skill's constraint always wins over a generic one.
- **Stale vs current regulatory content** — a skill whose reference file
  predates a rulebook change. `regulatory-standards.md` sets the
  currency-check protocol; run it before trusting any skill's citations.
