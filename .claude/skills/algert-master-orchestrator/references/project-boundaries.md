# Project Boundaries — Entity Segregation Register

**Status: DRAFT — default-deny until the owner (Algert Beollari) completes the
placeholders below.** Until every row under "Declared entities" has its
`[OWNER TO COMPLETE]` fields filled in, the orchestrator must treat every
entity as **mutually non-trusting**: no file, fact, conclusion, or draft
produced while working in one entity's context may be carried into another
entity's context, cited in another entity's output, or used to pre-fill
another entity's answer — not even "for efficiency," and not even when the
same regulatory question applies to both. This is the control the Master
Skill proposal calls "environment awareness" and it is enforced here, not
assumed.

## 0. Critical finding from Phase 0 inventory (read this first)

While building this registry, the inventory found that **"Astero Falcon"
already exists as a named, real regulated entity**, with entity-specific
baseline reference files embedded inside several `algert-compliance-skills`
specialist skills on this account (not in this repository):

- `dfsa-quarterly-compliance-reporting/references/astero-falcon-qcr-baseline.md`
- `dfsa-risk-management-reporting/references/astero-falcon-risk-reporting-baseline.md`
- `dfsa-client-assets-reporting/references/astero-falcon-client-assets-reporting-baseline.md`
- `dfsa-regulatory-reporting-calendar/references/astero-falcon-calendar-baseline.md`
- Two dedicated artifact-template skills: `artifact-template-astero-falcon-bcp-testing-report`, `artifact-template-astero-falcon-quarterly-compliance-report`

The inventory also found a `brain` skill (`algert-compliance-skills:brain`)
whose own documentation describes a separate, more mature repository —
referred to as the **"Algert AI project"** — with its own `CLAUDE.md`,
`AGENTS.md`, `project-instructions/`, `wiki/registers/` (including a
decision register and a compliance-actions register), phase/stage
checkpoints, and an explicit information-classification gate (Public /
Internal / Personal / Confidential / Highly Confidential / Restricted,
with an "Algert Restricted Review" approval step).

**That repository is not this one.** This session (`algertbeollari`) has no
`CLAUDE.md`, `AGENTS.md`, `project-instructions/`, or `wiki/registers/` at
all. This orchestrator has **not opened the content of any
`astero-falcon-*-baseline.md` file** — only confirmed the filenames exist —
because reading entity-specific regulatory baseline data was not necessary
to build the architecture and the classification gate described in `brain`
suggests that data may be Confidential/Restricted.

**Consequence for this registry**: do not assume `Algert-AI/` or
`Algert-Tech-AI/` (the two placeholder subfolders in *this* repo) correspond
to Astero Falcon, to each other, or to the "Algert AI project" described
above. They are currently empty except for an identical, generic
`shortcuts` skill and an identical 49-file command set in each — i.e. **no
entity-specific content exists in either folder yet**, so no automatic
inference can be made from this repo's contents alone.

**Action required of the owner before this orchestrator may be used for any
real regulated-entity work**: confirm, in the table below, which declared
entity (if any) each of `Algert-AI/`, `Algert-Tech-AI/`, and "Astero Falcon"
actually refers to, and whether the separate "Algert AI project" repository
should be registered here as a fourth entity/source the orchestrator is
aware of but cannot directly reach from this session.

## 1. Segregation model

- **Default: deny.** No cross-entity data flow is permitted unless an
  explicit row in §3 (Approved cross-references) authorises it.
- **One entity per working context.** When Claude Code (or Codex) is
  invoked inside `Algert-AI/`, `Algert-Tech-AI/`, or the repo root, treat
  that directory as the active entity boundary for the duration of the
  session. Do not read, summarise, or reuse content from another entity's
  directory "for context" unless the task explicitly spans both and a
  human has authorised it for that specific task.
- **The same AI, not the same memory.** Being able to technically access
  multiple entities' skills/files in one session is not authorisation to
  move information between them. This applies to conversation context,
  generated drafts, cached search results, and anything written to a
  shared scratch location.
- **Cloud specialist skills are shared infrastructure, not shared data.**
  `algert-compliance-skills:*` (and the rest of the cloud-synced catalogue)
  may be *invoked* from any entity's context — the skill logic itself is
  generic — but any entity-specific reference file a skill loads (e.g. an
  `astero-falcon-*-baseline.md`) must only be loaded when the active
  working context **is** that entity.

## 2. Declared entities

| Entity ID | Represents | Regulatory status | License/Authorisation ref | Repo location this session can see | Owner/approver | Status |
|---|---|---|---|---|---|---|
| `repo-root` | Personal / shared "second brain" workspace (generic productivity shortcuts, cross-cutting admin) | Not itself a regulated entity | n/a | `algertbeollari/` (this repo's top level) | Algert Beollari | Active, generic content only |
| `algert-ai` | `[OWNER TO COMPLETE — confirm: is this Astero Falcon? the "Algert AI project"? a different entity?]` | `[OWNER TO COMPLETE]` | `[OWNER TO COMPLETE]` | `algertbeollari/Algert-AI/` — currently empty placeholder | Algert Beollari | **Unconfirmed — treat as undefined, do not assume** |
| `algert-tech-ai` | `[OWNER TO COMPLETE — confirm what this entity/product is]` | `[OWNER TO COMPLETE]` | `[OWNER TO COMPLETE]` | `algertbeollari/Algert-Tech-AI/` — currently empty placeholder | Algert Beollari | **Unconfirmed — treat as undefined, do not assume** |
| `astero-falcon` | DFSA-regulated firm referenced throughout `algert-compliance-skills` baseline files | `[OWNER TO COMPLETE — e.g. DFSA Category/license type]` | `[OWNER TO COMPLETE]` | **Not visible from this session** — only its baseline *filenames* are visible, inside cloud-synced skill folders | Algert Beollari (MLRO/Head of Compliance) | Real entity, data location outside this session's reach |
| `algert-ai-project` | The separate, more developed repository described by the `brain` skill (`CLAUDE.md`, `AGENTS.md`, registers, phase checkpoints) — possibly the Regulatory AI product build, possibly something else | `[OWNER TO COMPLETE]` | n/a | **Not visible from this session at all** | Algert Beollari | Known to exist, location/identity to be confirmed |
| `regulatory-ai-product` | The Regulatory AI product mentioned in the user's own architecture note (with existing Phase 0 approvals / Phase 1 entry restrictions) | Product-in-development, not itself DFSA-regulated unless/until stated otherwise | n/a | `[OWNER TO COMPLETE — is this the same as algert-ai-project above?]` | Algert Beollari | **Unconfirmed — may be a duplicate row of `algert-ai-project`, do not merge without owner confirmation** |

Add a row per additional regulated client/firm as they arise. Never infer a
new entity from a skill name or filename without recording it here first.

## 3. Approved cross-references

*(empty by design — this is a default-deny list)*

| From entity | To entity | Scope of what may cross | Approved by | Date | Expiry/review date |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

No row currently exists. Until the owner adds one, the orchestrator must
refuse any task that asks it to compare, merge, or transfer information
between two declared entities, and must say so explicitly rather than
quietly doing a "reasonable-looking" merge.

## 4. What this orchestrator does NOT do

- It does not automatically decide that Algert-AI/ and Algert-Tech-AI/ are
  "probably fine to treat the same" because their current contents are
  identical placeholders — identical *today* is not evidence they will
  stay the same entity.
- It does not read `astero-falcon-*-baseline.md` content on its own
  initiative; a human directs that, in the context of that entity's own
  work.
- It does not merge the "Algert AI project" repository's governance
  artefacts (registers, decision log) into this repository, or vice versa.
