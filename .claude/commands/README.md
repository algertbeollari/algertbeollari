# Custom slash commands

These are real Claude Code slash commands (not the "secret prompt code" gimmicks
circulating on social media — those are just user-typed text with no special
backend behaviour). Each `.md` file here defines a `/name` command: Claude Code
loads the file's instructions and substitutes `$ARGUMENTS` with whatever text
you type after the command.

Usage: `/brief explain DFSA GEN 5.5` or `/gapcheck <paste document> against AML module`.

## From the "Claude Command secret codes" list

| Command | Purpose |
|---|---|
| `/ghost` | Human-sounding rewrite (no AI-style hedging/filler) |
| `/10x` | Rewrite sharper and tighter |
| `/godmode` | Direct, assertive, single-best-answer mode |
| `/devil` | Steelman the strongest opposing view |
| `/pitch` | 30-second investor/client pitch |
| `/compare` | Side-by-side comparison table + recommendation |
| `/scout` | Find risks and blind spots |
| `/artifacts` | Build a live working mini-app/page |
| `/ooda` | Observe-Orient-Decide-Act problem-solving |
| `/critique` | Structured, brutally honest critique |
| `/explainlikeim5` | Alias of `/eli5` |
| `/brief` | Shortest possible, no-fluff answer |
| `/teacher` | Mentor-style explanation with check questions |
| `/roast` | Brutally honest feedback, no sugar-coating |
| `/debug` | Step-by-step root-cause debugging |
| `/checklist` | Convert into an actionable checklist |
| `/persona` | Alias of `/expert` — respond as a named expert |
| `/summarize` | Condense to max 3 bullets |

## From the "30 skills" list

| Command | Purpose |
|---|---|
| `/human` | Alias of `/ghost` |
| `/expert` | Answer as a named persona/expert |
| `/ceo` | Outcome-focused, decisive answer |
| `/viral` | Hook-first, shareable social rewrite |
| `/seo` | SEO assessment and suggestions |
| `/critic` | Alias of `/critique` |
| `/teacher` | (see above) |
| `/eli5` | Explain simply, one analogy |
| `/brief` | (see above) |
| `/strategy` | Strategic options analysis |
| `/copywriter` | Persuasive marketing/sales rewrite |
| `/research` | Structured research summary with sourcing caveats |
| `/brainstorm` | Wide, diverse idea generation |
| `/promptengineer` | Improve a prompt for better model output |
| `/summarize` | (see above) |
| `/translate` | Translate, preserving tone/meaning |
| `/improve` | Tighten clarity, structure, impact |
| `/simplify` | Simplify for a general audience |
| `/expand` | Add depth/detail to text or an outline |
| `/compare` | (see above) |
| `/list` | Convert into a clean bulleted list |
| `/table` | Convert into a markdown table |
| `/outline` | Structured heading/sub-point outline |
| `/code` | Write code for a request |
| `/debug` | (see above) |
| `/explaincode` | Explain what code does |
| `/email` | Draft a professional, concise email |
| `/coverletter` | Draft a tailored cover letter |
| `/interview` | Likely interview questions + answer angles |
| `/motivate` | Grounded, substantive encouragement |

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
text or reaching a final regulatory/filing conclusion — the compliance
commands are written to flag assumptions and route final judgement calls
(e.g. STR/SAR filing decisions) to the MLRO rather than answering them
themselves.

Add new commands by dropping another `<name>.md` file in this folder with a
`description` frontmatter field and a body using `$ARGUMENTS` for the
user-supplied text.
