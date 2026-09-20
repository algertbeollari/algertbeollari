---
name: shortcuts
description: All-in-one command shortcut library (generic productivity + DFSA/AML/MLRO compliance). Use whenever the user's message starts with a recognised shortcut word or a slash-style tag (e.g. "brief:", "/brief", "gapcheck:") from the list below, or explicitly invokes /shortcuts <name> <args>.
---

# Shortcuts — all-in-one command library

This skill replaces having a separate command file per shortcut. Invoke it as
`/shortcuts <name> <the rest of your request>` — or just start a message with
`<name>: <request>` — and apply the matching rule below to everything after
the name. If the name isn't recognised, say so and list the closest matches
instead of guessing.

Never fabricate facts, data, or citations to fill out a shortcut's structure.
Where information is genuinely insufficient, say so and state what's missing
rather than inventing it — this applies especially to the compliance set.

## Generic productivity

| name | rule |
|---|---|
| `brief` | Shortest possible, no-fluff answer. No preamble, no restating the question. Bullets only if they shorten it. Max 5 sentences/bullets. |
| `eli5` (alias `explainlikeim5`) | Explain as to someone with no background. One plain analogy, no unexplained jargon, under 200 words. |
| `critique` (alias `critic`) | Structured honest critique: 1) strengths, 2) weaknesses (cite specifics), 3) what's missing, 4) fixes ranked by impact. No sugar-coating, stay professional. |
| `checklist` | Convert into a numbered, actionable checklist. Each item starts with a verb. Don't invent steps not implied by the source. |
| `summarize` | Condense to a maximum of 3 non-overlapping bullet points. |
| `compare` | Markdown table comparing the items by relevant criteria, then a one-paragraph recommendation. |
| `teacher` | Mentor style: core concept in plain language, why it matters, one worked example, then 2 check-understanding questions for the user to answer (don't answer them yourself). |
| `debug` | 1) restate the symptom in one line, 2) ranked likely root causes, 3) evidence for the top cause, 4) minimal fix (not a rewrite), 5) what to check next if it doesn't resolve. |
| `expert` (alias `persona`) | First word(s) of the request name a persona/expert; the rest is the question. Adopt that persona's vocabulary/priorities but never invent credentials, cases, or citations. |
| `ghost` (alias `human`) | Rewrite to sound human-written: cut hedging and AI-style filler ("in today's world", "it's important to note"). Keep facts/meaning exactly intact. |
| `10x` | Rewrite sharper and tighter: cut unnecessary words, lead with the strongest point, remove hedging. Show only the rewrite, not commentary. |
| `godmode` | Give the single strongest, most direct answer — no listing every option, no disclaimers — but still flag a genuinely material risk/caveat in one closing line if one exists. |
| `devil` | Steelman the strongest opposing view to the stated position (a real critic's argument, not a strawman). Note in one line whether it changes the original assessment. |
| `pitch` | 30-second spoken pitch (~75-90 words): hook/problem, what it is in one line, why it matters/why now, clear ask or next step. |
| `scout` | Find risks and blind spots: 1) stated/obvious risks, 2) likely UNSTATED blind spots (the important part), 3) the single missing fact that would most change the picture, 4) one mitigation per material risk. |
| `artifacts` | Build a working demo/mini-app for the request (Claude Code: use the Artifact tool and load artifact-design first; ChatGPT: use Canvas/code interpreter if available). Nothing non-functional. |
| `ooda` | Work the problem through Observe → Orient → Decide → Act. Only for genuinely complex, multi-factor problems — don't pad a simple question into four sections. |
| `roast` | Brutally honest feedback, no sugar-coating — but factual, not insulting. Say what's weak/mediocre plainly, then what to fix first. |
| `ceo` | Outcome-focused, decisive: state the decision, the 1-2 driving facts, what to tell the team to do next. Skip theory. |
| `viral` | Rewrite as a short, hook-first, shareable social post. Strong first line, one clear point, a closing line inviting reaction. Stay truthful to the source — no exaggerated claims. |
| `seo` | Target keyword(s)/intent, suggested title tag + meta description, 3-5 headings, gaps vs. a top-ranking page. Flag any assumed search-volume/ranking data rather than inventing it. |
| `strategy` | Goal restated to confirm, key constraints/assumptions, 2-4 viable options each with the main tradeoff, recommended option and why, first concrete move. |
| `copywriter` | Persuasive marketing rewrite: lead with benefit not feature, address the likely objection, clear CTA. No invented claims, stats, or guarantees. |
| `research` | Overview, key facts/figures, major viewpoints/debates if any, open questions. Clearly separate confident fact from inference — never present speculation as fact. Use a search tool if available and the topic needs current info. |
| `brainstorm` | At least 10 ideas grouped by distinct approach (not 10 variations of one idea). Mark the top 2-3 with a one-line reason why. Favour originality but keep every idea actionable. |
| `promptengineer` | Identify ambiguity, missing context/constraints, missing output format in the given prompt. Show the rewritten prompt in full, then what changed and why. |
| `translate` | Translate preserving tone, register, and technical/legal precision. If no target language is given, ask before translating. |
| `improve` | Tighten wording/structure, strengthen weak verbs and vague claims, lead with the most important point. Preserve original meaning/facts/voice. Show result + a short list of key changes. |
| `simplify` | Shorter sentences, plainer words, one idea per sentence, jargon defined inline. Never drop a material fact or nuance. |
| `expand` | Add real supporting detail, examples, and reasoning to each point. No padding or repetition — if there's nothing real to add to a point, leave it as is. |
| `list` | Convert into a clean, well-organised bulleted list; group under sub-headings if more than ~8 items. Don't invent items. |
| `table` | Convert into a markdown table with sensible headers based on the content's natural dimensions. If it doesn't fit tabular form, say so and suggest a better format. |
| `outline` | Hierarchical outline (headings/sub-points, short phrases not sentences) with a logical flow. |
| `code` | Write clean, idiomatic code matching surrounding project conventions if any. No unnecessary comments, no unrequested abstractions, no speculative error handling. State any assumption made about requirements. |
| `explaincode` | Overall purpose first, then walk the logic in execution order, flagging only non-obvious behaviour/edge cases/side effects. |
| `email` | Professional, concise email: recommendation/ask first, then rationale, then action/owner/timeline. British English unless another convention is implied. |
| `coverletter` | Specific non-generic hook tied to the role/company, 2-3 concrete achievements from the given background tied to what the role needs, confident CTA, one page max. Only use facts given. |
| `interview` | 5-8 likely interview questions (behavioural + role/technical) with a one- or two-line pointer on what a strong answer should cover for each — not a full scripted answer. Tailor to given background if provided. |
| `motivate` | Direct, substantive encouragement grounded in the actual situation given (not platitudes). Name what's genuinely hard, why it's worth it, one concrete next step. |

## Compliance / MLRO / Risk (DFSA-DIFC lens)

These route final regulatory judgement calls (e.g. STR/SAR filing decisions,
final suspicion determinations) to the user acting as MLRO rather than
answering them outright — they are drafting/analysis aids only.

| name | rule |
|---|---|
| `gapcheck` | Compliance gap analysis against a named DFSA module/framework (ask which module/framework if none is given — don't guess). Structure: Executive Summary → Applicable Regulations and Regulatory Basis (cite specific DFSA Rulebook modules where identifiable — GEN, AML, COB, PIB, CIR, etc.) → Risk Assessment → Compliance Gaps or Issues Identified (mark each as mandatory-requirement breach / best-practice deviation / discretionary improvement) → Recommendations → Practical Next Steps and Ownership. Flag where information is insufficient. |
| `redflag` | AML/CFT red-flag screen of a client/transaction/activity description across: customer risk, geographic risk, product/service risk, delivery channel risk, sanctions/PF exposure, Source of Wealth/Source of Funds plausibility, beneficial ownership/control transparency, trigger events. For each: red flag Y/N, specific indicator, severity (Low/Medium/High). Conclude with an overall risk view and whether MLRO escalation/EDD/hold should be considered — never conclude suspicion or recommend a goAML filing outright. |
| `dfsaref` | Identify relevant DFSA Rulebook module(s)/provisions for the topic (GEN, AML, COB, PIB, CIR, etc.), each with a one/two-sentence summary of the requirement and whether it's mandatory or guidance/best practice. Never fabricate a rule number — say "verify against the current DFSA Rulebook" if not confident. This is a starting reference, not a substitute for checking rulebook.dfsa.ae. |
| `boardmemo` | Draft a Board/committee memo in professional, concise British English: Purpose (one sentence) → Background → Analysis/Key Considerations (regulatory, risk, governance, operational, financial as relevant) → Options (if a decision is sought) → Recommendation → Action Required of the Board (approve/note/delegate, explicit) → Owner and Timeline. State clearly where facts are assumed. Don't invent figures, dates, or names. |
| `riskassess` | Inherent/control/residual risk assessment: Risk Statement (cause → risk event → consequence) → Inherent Risk Rating with rationale → Existing Controls and effectiveness → Residual Risk Rating with rationale → Risk Appetite Assessment (within/near/outside; state assumption if appetite isn't given) → Escalation Required? (Board/Risk Committee/MLRO/none, why) → Recommended Actions/KRIs. Distinguish mandatory requirements, best practice, and discretionary recommendations. |
| `sowcheck` | Source of Wealth/Source of Funds plausibility test: Claimed SoW/SoF → Plausibility Test (does it match age/career/business scale/known profile?) → Evidence Held vs Required (bank statements prove movement, not origin) → Chain Completeness (any unexplained links, e.g. a "gift"/"loan" needing its own SoW) → Conclusion (plausible / needs more evidence / not plausible, with reasoning) → Next Steps. Never conclude a filing decision — flag to MLRO if red flags emerge. |

## Notes

- This single skill supersedes needing one file per command in
  `.claude/commands/` — those individual files still work as direct slash
  commands, but you generally don't need to add a new file per shortcut going
  forward; add a new row to the appropriate table above instead.
- A ChatGPT-compatible export of this same table lives in
  `.claude/chatgpt-sync/` — regenerate it from this file if the table above
  changes, since ChatGPT has no equivalent skill mechanism and needs the
  content pasted manually.
