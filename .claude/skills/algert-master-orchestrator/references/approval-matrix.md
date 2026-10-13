# Approval Matrix

**Status: starter defaults, consistent with common DFSA governance
expectations — the owner should confirm or override each row for the
actual Authorised Individuals, committees, and Board composition of each
declared entity.** Until confirmed, treat every row as "ask the named
role" rather than as a standing authorisation to proceed without them.

| Decision/output type | Drafted/prepared by | Approved/decided by | This orchestrator may |
|---|---|---|---|
| STR/SAR filing decision (goAML) | MLRO (with AI drafting support) | MLRO alone — non-delegable | Draft the red-flag analysis and supporting narrative only. Never conclude suspicion or recommend filing. |
| Final suspicion determination | MLRO | MLRO alone | Same as above. |
| DFSA notification / breach report | Compliance/MLRO | Senior Executive Officer and/or Board per the firm's governance manual | Prepare the draft and gap analysis; flag the notification trigger; never submit or represent submission as done. |
| Regulatory Business Plan | Compliance | Board | Prepare drafts and gap analysis against DFSA expectations. |
| AML Business Risk Assessment | MLRO/Compliance | Senior Management/Board per firm's manual | Prepare analysis; flag required escalation. |
| Board/committee memo (e.g. `boardmemo` output) | Compliance | Named paper owner; Board/committee notes or approves per its own agenda | Draft only — never assume the Board must approve every document; state explicitly whether the ask is "to note," "to approve," or "to delegate." |
| Policy/manual amendment (e.g. AML Manual) | Compliance/MLRO | Board or delegated committee per the firm's governance framework | Prepare gap analysis and proposed amendments; never auto-apply or represent a policy as amended/approved. |
| New product/service approval | Compliance input | New Product Committee/Board per firm's manual | Prepare the compliance input only. |
| Client onboarding/EDD decision | Compliance/relevant officer | As delegated in the firm's approval matrix (often MLRO for EDD cases) | Prepare the assessment; never auto-approve/reject a client. |
| External regulatory correspondence | Compliance | Senior Executive Officer/MLRO as applicable | Draft only; never send. |
| Production/system change (e.g. this orchestrator's own routing rules, or a specialist skill's logic) | Whoever proposes the change | Algert Beollari (owner) | Propose via `continuous-improvement` notes (see quality-standards.md); never silently change an approved skill's behaviour. |
| Cross-entity data transfer | n/a — requires a new row in `project-boundaries.md` §3 first | Algert Beollari (owner), entity by entity | Never perform without that row existing. |

## Notes

- "This orchestrator may" column states the AI's authority ceiling, not a
  target to automate away — per the user's own fifth design principle,
  governance comes before automation.
- Where a decision depends on a specific firm's Authorised Individual
  register (e.g. who is the current Senior Executive Officer), this
  orchestrator does not assume a name. It asks, or looks it up in the
  entity's own governance manual if the task has given it access to one.
