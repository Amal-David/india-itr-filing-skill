# Document-led discovery and lawful optimization

Use this workflow when the taxpayer wants the skill to find what applies from documents instead of choosing tax categories.

## 1. Establish the minimum scope

Confirm the financial year, assessment year, filing status, and residential status. Ask whether the document set is believed complete. Do not infer these controlling facts from documents unless an authoritative record directly establishes them and the taxpayer confirms them.

## 2. Create a private file inventory

Work locally where possible. Replace filenames with neutral IDs such as `DOC-001`. For each file record only:

- period and document type;
- issuer category, not private identifiers;
- income, transaction, tax-credit, asset, or disclosure signals;
- whether the record is primary evidence, a reconciliation lead, or incomplete;
- questions and missing companion records.

Never copy passwords, OTPs, Aadhaar, full PAN, account numbers, addresses, folio numbers, signatures, or personal filenames into notes, prompts, tests, issues, commits, or public artifacts.

## 3. Detect provisional route signals

| Evidence signal | Likely route or modifier | Required corroboration |
|---|---|---|
| Form 16 or salary TDS | Salary; possibly multiple employers | Every Form 16, Form 26AS, AIS/TIS |
| Invoice ledger, remittance, FIRC, or consulting receipts | Professional or business; 44ADA candidate only if current conditions pass | Receipt reconciliation, profession, payment modes, bank evidence |
| Broker capital-gains report or CAS | Investor and capital gains | Lot-level cost, classification, AIS/26AS |
| Intraday or derivatives tax P&L | Trader, intraday, or F&O | Segment ledger, contract notes, turnover method, expenses |
| AMC/CAMS/KFintech/MF Central report | Mutual-fund capital gains | Purchase lots, scheme classification, redemption records |
| Interest, dividend, TDS, TCS, or challan record | Other sources or tax credit | Related income and Form 26AS/AIS reconciliation |
| Property agreement, lender certificate, rent, or property TDS | Property modifier | Ownership, completion/possession/use, co-ownership, final interest record |
| Exchange VDA ledger or section 194S entry | VDA | Transaction-level acquisition, transfer, consideration, and cost |
| Foreign account, share, valuation, ODI/LRS, or tax record | Foreign/cross-border and specialist review | Ownership dates, calendar-year values, income, FX, tax, regulatory status |
| Prior ITR acknowledgement or loss schedule | Brought-forward loss or regime history | Filed return, filing date, loss type, carry-forward balance, Form 10-IEA history |

AIS, TIS, Form 26AS, screenshots, bank narrations, and portal prefill are leads. Never treat them as complete proof of the economic transaction or tax classification.

## 4. Build the coverage matrix

Create one row per material category:

```text
Category:
Evidence found:
Provisional route/modifier:
Confidence: high / medium / low
Missing record:
Possible form or schedule effect:
Optimization check:
Status: confirmed / prefilled-only / derived / unresolved / unknown / blocked
```

Never treat an absent document as proof that a category is absent. Ask whether the taxpayer has additional employers, banks, brokers, AMCs, exchanges, properties, countries, businesses, or prior returns.

## 5. Run a lawful optimization review

Optimization means finding supported elections, claims, credits, set-offs, and classification corrections. It never means targeting the largest refund.

Check, where applicable:

- old-versus-new regime comparison using the same complete income set and current rules;
- salary standard deduction and supported salary exemptions;
- eligible professional treatment, including whether every 44ADA condition passes;
- lot-level capital-gain accuracy and proper separation of investment, intraday, F&O, and VDA activity;
- current and brought-forward loss set-off using filed-return evidence;
- house-property treatment based on ownership, completion, possession, use, and regime;
- supported Chapter VI-A or other claims allowed in the selected regime;
- TDS, TCS, advance tax, self-assessment tax, and refund-interest reconciliation;
- foreign-tax credit, treaty, or FEMA issues only with specialist review and required records;
- missed income, duplicate prefill, mismatched gross receipts, or credits claimed without related income.

Label every candidate:

- `supported` — evidence and current rule support it;
- `needs evidence` — plausible but not claimable yet;
- `not available` — current facts or regime fail a condition;
- `professional review required` — law, valuation, audit, notice, residency, treaty, or FEMA risk exists.

Do not use estimated dates, fabricated costs, unsupported deductions, false turnover, or omitted income to improve the result.

## 6. Produce the navigation handoff

Before portal entry, give the taxpayer:

```text
Inferred primary route and modifiers:
Confidence and controlling assumptions:
Documents used:
Documents missing:
Optimization candidates by status:
Form and regime hypothesis:
Schedules likely required:
Portal entry order:
Specialist-review triggers:
Next exact action:
```

If a controlling fact is unresolved, state `do not submit yet`. Keep payment, declaration, submission, and verification under taxpayer control.
