# Regulatory Verification Standard

Applies whenever a routed task will produce a regulatory conclusion,
citation, or Board/committee-facing statement (DFSA, FSRA/ADGM, UAE AML
federal law, FATF standards).

## 1. Source hierarchy (highest authority first)

1. DFSA Rulebook as currently published at rulebook.dfsa.ae (GEN, AML, COB,
   PIB, CIR, and other applicable modules).
2. DFSA guidance, Dear SEO/Dear Compliance Officer letters, and published
   enforcement/thematic review outcomes.
3. FSRA/ADGM equivalent instruments, where the matter concerns an
   ADGM-regulated counterparty or cross-jurisdiction comparison.
4. UAE federal AML/CTF law and Cabinet/Ministerial decisions (e.g. Federal
   Decree-Law No. 20 of 2018 as amended, and its implementing Cabinet
   Decision), and UAE sanctions/targeted financial sanctions lists.
5. FATF Recommendations and guidance, as the baseline international
   standard DFSA's own rules implement.
6. A specialist skill's own bundled reference material (e.g. an
   `astero-falcon-*-baseline.md`) — useful for continuity, but never
   authoritative over 1–5 above if it conflicts with a current rule.

## 2. Currency check (mandatory, every time)

- Never cite a specific rule number from memory or from a skill's bundled
  reference file without flagging that it should be verified against the
  live Rulebook, unless the task includes a timestamped confirmation that
  it was already checked.
- State the as-of basis of any citation ("per DFSA Rulebook as consulted
  on [date]") so staleness is auditable later.
- If a cited provision cannot be confirmed with confidence, say so
  explicitly — per the existing `dfsaref`/`gapcheck` shortcuts' own rule —
  rather than presenting an unverified citation as settled.

## 3. Mandatory vs. best practice vs. recommendation

Every regulatory output this orchestrator produces or passes through must
keep these three visually and textually distinct (per the user's own
standing house style):
- **Mandatory regulatory requirement** — a Rulebook/law obligation.
- **Industry best practice** — not itself a rule, but a recognised
  standard (e.g. Wolfsberg, FATF guidance papers, DFSA "dear SEO" soft
  expectations).
- **Recommendation** — this orchestrator's or a specialist skill's own
  judgement call, clearly labelled as such.

## 4. AML/CFT dimensions to check by default

For any client, transaction, product, or relationship matter, confirm the
routed specialist skill (or the orchestrator's own synthesis) has covered,
or explicitly scoped out: customer risk; geographic risk; product/service
risk; delivery channel risk; sanctions and proliferation-financing
exposure; Source of Wealth/Source of Funds; beneficial ownership and
control; ongoing monitoring/trigger events; and whether Enhanced Due
Diligence applies.

## 5. Governance routing

Final regulatory judgement calls — an STR/SAR filing decision, a formal
suspicion determination, a DFSA notification, sign-off on a Board paper —
are never concluded by this orchestrator or any specialist skill. They are
drafted, analysed, and risk-flagged, then routed to the named human
authority in `approval-matrix.md`.
