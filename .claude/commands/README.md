# Custom slash commands

These are real Claude Code slash commands (not the "secret prompt code" gimmicks
circulating on social media — those are just user-typed text with no special
backend behaviour). Each `.md` file here defines a `/name` command: Claude Code
loads the file's instructions and substitutes `$ARGUMENTS` with whatever text
you type after the command.

Usage: `/brief explain DFSA GEN 5.5` or `/gapcheck <paste document> against AML module`.

## Generic productivity

| Command | Purpose |
|---|---|
| `/brief` | Shortest possible, no-fluff answer |
| `/eli5` | Explain simply, one analogy |
| `/critique` | Structured, brutally honest critique |
| `/checklist` | Convert text/task into an actionable checklist |
| `/summarize` | Condense to max 3 bullets |
| `/compare` | Side-by-side comparison table + recommendation |
| `/teacher` | Mentor-style explanation with check-understanding questions |
| `/debug` | Step-by-step root-cause debugging |
| `/expert` | Answer as a named persona/expert |

## Compliance / MLRO / Risk (DFSA-DIFC lens)

| Command | Purpose |
|---|---|
| `/gapcheck` | Compliance gap analysis against a named DFSA module/framework |
| `/redflag` | AML/CFT red-flag screen across customer/geo/product/channel/SoW/PF risk |
| `/dfsaref` | Point to relevant DFSA Rulebook module(s) for a topic |
| `/boardmemo` | Draft a Board/committee memo skeleton |
| `/riskassess` | Inherent/control/residual risk assessment |
| `/sowcheck` | Source of Wealth / Source of Funds plausibility test |

These are drafting aids, not a substitute for verifying current DFSA Rulebook
text or reaching a final regulatory/filing conclusion — each command is
written to flag assumptions and route final judgement calls (e.g. STR/SAR
filing decisions) to the MLRO rather than answering them itself.

Add new commands by dropping another `<name>.md` file in this folder with a
`description` frontmatter field and a body using `$ARGUMENTS` for the
user-supplied text.
