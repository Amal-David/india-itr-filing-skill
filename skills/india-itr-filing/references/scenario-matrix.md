# Synthetic scenario matrix

Use these scenarios to test routing and safety. They are synthetic and contain no taxpayer data.

| Scenario | Expected route | Required safeguards |
|---|---|---|
| One employer, bank interest only | Salary essential | ITR-1 eligibility trace; Form 16/AIS/26AS reconciliation; no Form 10-IEA |
| Two employers and investment redemptions | Salary investor + multiple employers + capital gains | Reconcile both Form 16s; lot-level gains; ITR-1 exclusion check |
| Salary and qualifying consulting receipts | Professional 44ADA candidate + salary | ITR-3/limited ITR-4 test; exact profession; gross receipts; cash condition; no expense double claim |
| Independent professional below presumptive floor | Professional regular + audit review | Do not self-resolve books/audit consequence |
| Delivery investments, intraday, and F&O | Trader + capital gains + intraday + F&O | Three separate lanes; explicit turnover method; no sign flipping |
| Mutual-fund redemption screenshot only | Investor + unknown transaction | Request CAS/capital-gains report; proceeds are not taxable gain |
| Unknown AIS VDA/TDS line | VDA + unknown transaction | Identify exchange, asset, dates, cost, and consideration before Schedule VDA |
| Foreign unlisted shares received by gift | Foreign cross-border + unlisted equity | Tax disclosure and FEMA lanes; not VDA; specialist review |
| Property buyer TDS | Property + tax credit | Keep Form 26QB/16B records; do not claim seller's tax credit as buyer's credit |
| Home under construction with EMI | Property | Establish ownership, completion/possession, use, final certificate, and regime before any claim |
| Prior trading loss remembered but no filed ITR | Trader + brought-forward loss | Block carry-forward claim until prior ITR, filing date, and schedule are obtained |
| Portal validation succeeds but evidence differs | Complex composite | Preview reconciliation fails; do not submit |
| Redacted files attached but taxpayer does not know categories | Document-led discovery | Confirm FY/AY, filing status, residency, and completeness; inventory first; infer provisional routes only |
| Form 16 and broker report attached | Document-led discovery -> salary investor | Ask only for missing AIS/26AS and lot-level evidence; do not repeat supported intake questions |
| AIS attached without source records | Document-led discovery + unknown transactions | Treat AIS as leads; produce a missing-document list; no final form or optimization conclusion |
| Documents reveal a foreign holding | Foreign cross-border + document-led discovery | Stop ordinary optimization; obtain calendar-year values and specialist review |

## Cross-schedule invariants

- Professional 44ADA receipts and presumptive income must reconcile to P&L/BP; trading never enters 44ADA receipts.
- Delivery capital gains, speculative intraday, non-speculative eligible F&O, and VDA remain separate.
- Schedule CG period buckets equal the applicable gain total by actual transfer dates.
- Schedule VDA capital-gain total flows to Schedule CG C2; a VDA loss cannot reduce another source.
- Every brought-forward loss has prior-return provenance and the correct loss character.
- Part B-TTI foreign-asset answer, Schedule FA, foreign income, and unlisted disclosures are internally consistent.
- Tax credits match Form 26AS/challans and the related offered income.
- The final preview maps back to every confirmed evidence-register row.
