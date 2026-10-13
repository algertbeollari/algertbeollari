# Quality Standards — Acceptance Criteria

Every output this orchestrator produces or hands back from a specialist
skill must pass this checklist before being presented as final. Failing an
item does not block delivery — it means the gap must be stated, not hidden.

## 1. Citation and evidence
- [ ] Every regulatory citation is attributed to a source and dated
      ("verify against current Rulebook" if not independently confirmed).
- [ ] No fact, figure, name, date, or quote has been invented to fill a
      template's structure. If information is missing, the output says so.
- [ ] Assumptions are listed explicitly, not buried in prose.

## 2. Classification distinction
- [ ] Mandatory requirement / best practice / recommendation are visually
      and textually distinguishable throughout.

## 3. Document control (for Board/committee/regulatory-facing drafts)
- [ ] Version marked as DRAFT unless the approval-matrix row for this
      output type has actually been satisfied.
- [ ] Author/preparer and date stated.
- [ ] Clear statement of what decision (if any) is being sought and from
      whom (ties to `approval-matrix.md`).

## 4. Consistency
- [ ] No contradiction between this output and another recent output for
      the same entity (e.g. two risk ratings for the same client that
      don't reconcile). If a prior conflicting output exists and is known,
      flag the discrepancy rather than silently using the newer one.
- [ ] Terminology matches the entity's own register/manual where one is
      available, rather than introducing a new term for the same concept.

## 5. Segregation compliance
- [ ] Confirms no cross-entity data was used without an approved row in
      `project-boundaries.md` §3.

## 6. Routing transparency
- [ ] States which specialist skill(s) were used and why, so the choice
      is auditable and a wrong routing decision can be corrected at the
      rule level (via `routing-rules.md`), not just patched once.

## 7. Continuous improvement (without silent drift)
- A pattern that should change an approved skill or rule (e.g. "this
  collision should route the other way," "this entity's status is now
  confirmed") is written up as a proposed change and put to the owner
  (`approval-matrix.md` — "production/system change" row). The
  orchestrator never edits an approved skill's `SKILL.md` or another
  specialist skill's logic on its own initiative.
