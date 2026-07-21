---
name: india-itr-filing
description: Prepare, reconcile, review, and troubleshoot Indian individual income-tax returns on the official e-Filing portal. Use for ITR form and regime selection, AIS/TIS/Form 26AS/Form 16 reconciliation, salary, presumptive professional income under 44ADA, capital gains, trading, VDA, foreign assets, tax credits, portal validation errors, preview review, and lawful refund optimization. Never use it to conceal income, fabricate deductions, or submit without the taxpayer's final review.
---

# India ITR Filing

Guide an Indian individual taxpayer from evidence collection to a reconciled draft return. Optimize only within the law, keep current-year rules source-backed, and preserve a human confirmation boundary before payment, declaration, submission, or e-verification.

## Non-negotiable safeguards

1. Use only official Income Tax Department surfaces for filing and tax-rule verification. Use broker, bank, employer, registrar, or AMC documents only as transaction evidence.
2. Treat tax rates, thresholds, due dates, return schemas, and portal labels as assessment-year-specific. Verify them for the selected assessment year before giving a definitive answer.
3. Never request, read aloud, store, or repeat PAN, Aadhaar, passwords, OTPs, full bank numbers, or complete addresses. Let the taxpayer enter secrets directly.
4. Never manufacture a refund by omitting income, inventing losses, changing dates, or forcing portal fields to accept economically false values.
5. Keep the return as a draft until the generated preview is reconciled against the source documents.
6. Stop before declaration, tax payment, submission, and e-verification. State what will happen and obtain explicit taxpayer approval.
7. When facts are ambiguous or source records conflict, identify the conflict and request the missing record. Do not average or guess.

## Workflow

### 1. Establish scope

Confirm the assessment year, residential status, filing status, age category, income heads, business/profession status, audit exposure, regime history, and whether any foreign asset or income existed during the applicable disclosure period.

Use [form-and-regime.md](references/form-and-regime.md) for the form and regime decision. Do not assume that a low-value transaction is immaterial to form eligibility or disclosure.

### 2. Build the evidence register

Create a checklist with one row per source:

- Identity and bank: masked identifiers, validated refund account, prior acknowledgement.
- Salary: Form 16 Part A and Part B, payslips, termination/arrears details.
- Tax records: AIS, TIS, Form 26AS, TDS/TCS certificates, challans.
- Banking: savings interest, deposit interest, income-tax refund interest.
- Profession/business: invoices, receipt ledger, bank credits, foreign remittance advice, GST/FIRC records where applicable.
- Securities: broker tax P&L, contract notes, mutual-fund capital-gains statement, CAS, transaction ledger.
- Property: ownership, possession/completion, rent, home-loan interest certificate, principal statement, property-purchase TDS records.
- Foreign assets/income: acquisition documents, ownership records, peak/closing values, income, sale proceeds, exchange-rate evidence.
- VDA: exchange ledger with acquisition date, transfer date, cost, consideration, TDS, and asset identity.

Record whether each value is confirmed, prefilled, derived, or unresolved. Prefer exact source records over screenshots of summary totals.

### 3. Reconcile before entering

Reconcile AIS/TIS/Form 26AS with the evidence register. A prefilled figure is a lead, not proof. Resolve differences such as:

- gross salary versus income chargeable under salaries;
- redemption proceeds versus taxable capital gain;
- tax deducted versus income amount;
- refund amount versus taxable refund interest;
- total bank credits versus professional gross receipts;
- trade turnover versus profit or loss;
- foreign-share quantity acquired versus closing quantity.

Use [income-schedules.md](references/income-schedules.md) for schedule routing and [securities-and-trading.md](references/securities-and-trading.md) for investment and trading rules.

### 4. Enter the return schedule by schedule

Enter general information first, then source schedules, loss set-off schedules, deductions, tax paid, foreign assets, and computation schedules. Avoid entering the same item under two heads.

For portal-specific traps and validation messages, use [portal-troubleshooting.md](references/portal-troubleshooting.md).

### 5. Reconcile the generated preview

Download the preview PDF or JSON and independently check:

- filing section, regime, residential status, and return form;
- every income head and special-rate schedule;
- gross receipts and presumptive income;
- capital gains and transaction-date buckets;
- current-year and brought-forward loss treatment;
- foreign asset, unlisted-share, and VDA disclosures;
- TDS, TCS, advance tax, self-assessment tax, and refund account;
- total income, tax, interest, fee, payable amount, or refund.

Use [preview-checklist.md](references/preview-checklist.md). A small refund or a successful portal validation does not prove completeness.

### 6. Hand off the final action

Summarize all entered figures by source, list unresolved assumptions, state the computed payable/refund, and ask the taxpayer to confirm. Leave OTP, declaration, submission, and e-verification to the taxpayer unless they explicitly authorize a final click after reviewing the preview.

## Response style

- Lead with the exact portal choice or correction.
- Give the source and assessment-year context for any rule that affects tax or eligibility.
- Separate confirmed facts from provisional calculations.
- Say “do not submit yet” whenever a material reconciliation item remains open.
- Prefer a short field-by-field answer when the taxpayer shares a portal screen.

## Reference routing

- Form selection, old/new regime, Form 10-IEA, 44ADA, rent, home-loan, and deductions: [form-and-regime.md](references/form-and-regime.md)
- Salary, other sources, profession, property, VDA, foreign assets, and tax credits: [income-schedules.md](references/income-schedules.md)
- Mutual funds, listed securities, intraday, F&O, and losses: [securities-and-trading.md](references/securities-and-trading.md)
- Portal validation errors and schedule dependencies: [portal-troubleshooting.md](references/portal-troubleshooting.md)
- Final PDF/JSON reconciliation: [preview-checklist.md](references/preview-checklist.md)
- Official sources and freshness protocol: [official-sources.md](references/official-sources.md)

## Privacy validation

Before publishing or sharing any artifact derived from a taxpayer interaction, run:

```bash
python3 scripts/privacy_scan.py <path>
```

Pass additional private terms without writing them into the repository:

```bash
python3 scripts/privacy_scan.py <path> --deny "private term" --deny "another term"
```

Do not publish until the scanner passes and a manual review confirms that examples are synthetic.
