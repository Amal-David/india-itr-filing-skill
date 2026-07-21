---
name: india-itr-filing
description: Assist with preparing, reconciling, reviewing, and troubleshooting Indian individual income-tax returns using an adaptive filer profile. Use for salary-only, salary plus investments, freelance or professional income, section 44ADA, investors, intraday or F&O traders, property, VDA, foreign assets, unlisted shares, tax credits, portal validation, and final preview review. Never conceal income, fabricate evidence, or perform the taxpayer's declaration, payment, submission, or verification.
---

# India ITR Filing

Assist an Indian individual taxpayer in organizing source evidence, deriving the applicable ITR workflow, preparing a reconciled draft, and understanding portal validation errors. This skill is a filing aid, not a Chartered Accountant, advocate, authorized representative, RBI/FEMA adviser, certification, legal opinion, or refund guarantee.

The taxpayer remains responsible for facts, declarations, payment, verification, and submission. Require source files such as Form 16, AIS/TIS, Form 26AS, bank-interest records, invoices or receipt ledgers, broker and AMC reports, tax challans, property records, VDA ledgers, and foreign-asset records when applicable. Do not infer a claim or classification from a screenshot or portal prefill alone.

## Non-negotiable safeguards

1. Verify assessment-year-specific rules, return forms, utilities, schemas, thresholds, and due dates from current official sources.
2. Never request or retain passwords, OTPs, Aadhaar, full PAN, complete bank or card numbers, signatures, biometrics, or unredacted identity documents. Let the taxpayer enter secrets directly.
3. Never manufacture a refund by omitting income, inventing losses or deductions, changing dates, or forcing fields to accept economically false values.
4. Treat portal prefill and AIS as reconciliation leads, not conclusive evidence.
5. Mark every material item `confirmed`, `prefilled-only`, `derived`, `unresolved`, `unknown`, or `blocked`.
6. Do not sign, declare, pay, submit, upload, e-verify, file Form 10-IEA, change a refund account, accept an adjustment, or respond to a notice for the taxpayer.
7. Keep the return in draft until the preview is reconciled to the evidence register and all material uncertainties are resolved.
8. Escalate instead of guessing when facts, source records, law, tax classification, valuation, residency, or FEMA treatment are uncertain.

## Adaptive workflow

### 1. Run the front-door intake

Ask the short multi-select questionnaire in [intake-and-routing.md](references/intake-and-routing.md). Determine:

- filing context: FY/AY, original/revised/belated/updated/notice-response return;
- residential status and uncertainty;
- all income, asset, transaction, and loss categories that occurred;
- records available and records still missing;
- prior regime/Form 10-IEA and loss-carry-forward history;
- whether any mandatory specialist-review trigger exists.

Do not ask the taxpayer to choose a single persona or ITR form. Assign one primary route plus every applicable modifier. A small transaction can still change form eligibility or disclosure obligations.

Primary routes:

- `salary-essential`
- `salary-investor`
- `professional-44ada-candidate`
- `professional-regular`
- `investor`
- `trader`
- `property`
- `foreign-cross-border`
- `complex-composite`

Modifiers include `multiple-employers`, `capital-gains`, `intraday`, `fno`, `vda`, `property`, `foreign-asset-or-income`, `unlisted-equity`, `director-or-partner`, `brought-forward-loss`, `tax-credit`, `notice-or-late-return`, and `unknown-transaction`.

Use the optional local classifier for a deterministic first pass:

```bash
python3 scripts/classify_case.py case-profile.json
```

The classifier is a routing aid, not a tax determination.

### 2. Apply the risk and escalation gate

Use [risk-and-escalation.md](references/risk-and-escalation.md). Continue with ordinary draft assistance only when the evidence and classification are supportable.

Mandatory professional review includes disputed or uncertain residency; audit or books questions; notices; foreign assets, foreign gifts, ODI/LRS or pending AD-bank matters; treaty or foreign-tax credit; missing VDA basis; unsupported prior losses; property ownership or possession disputes; unlisted-share valuation; and irreconcilable AIS, Form 26AS, broker, employer, or bank records.

### 3. Build a minimum evidence pack

Use [document-intake-and-privacy.md](references/document-intake-and-privacy.md). Request only the documents needed for the selected routes and modifiers. Assign neutral document IDs such as `DOC-001`; do not copy original filenames, taxpayer identifiers, or private values into notes, examples, issues, commits, or public artifacts.

Create an evidence register with one row per source: document ID, period, source type, tax fields derived, source locator, status, and unresolved questions.

### 4. Derive form, regime, and schedule map

Use [form-and-regime.md](references/form-and-regime.md). Produce an eligibility trace rather than a bare answer:

- ITR-1 only if every current eligibility restriction passes.
- ITR-2 when no business/profession exists but schedules outside ITR-1 are required.
- ITR-3 when business/professional income exists, including intraday or F&O activity, unless the limited ITR-4 route fully applies.
- ITR-4 only after every current eligibility condition passes; never use it merely because it is shorter.

Run the Form 10-IEA branch only after establishing business/profession status. Compare regimes using the same complete income data and supported claims.

### 5. Reconcile before portal entry

Map each evidence item to its income head, schedule, tax credit, and status. Reconcile:

- salary and salary TDS against Form 16 and Form 26AS;
- professional gross receipts against invoices, receipt ledger, and bank/remittance evidence;
- redemption proceeds against lot-level capital gain;
- intraday, eligible F&O, and delivery activity in separate lanes;
- VDA transfers against transaction-level exchange evidence;
- foreign assets and income against ownership, valuation, income, and conversion records;
- prior losses against filed ITR acknowledgements and schedules;
- TDS/TCS/challans against the related income and tax-credit records.

Use [income-schedules.md](references/income-schedules.md), [securities-and-trading.md](references/securities-and-trading.md), and [tax-and-fema.md](references/tax-and-fema.md).

### 6. Enter in dependency order

Use the current official portal or utility for the exact AY. Enter and validate in clusters:

1. Part A General, filing status, residential status, business/profession status, and regime history.
2. Salary, house property, business/profession, P&L, presumptive income, and trading.
3. Capital gains, VDA, other sources, and foreign disclosures.
4. CYLA, BFLA, CFL, deductions, and tax paid.
5. Unlisted shares, Schedule FA/FSI/TR when applicable, and Part B-TI/TTI.

Save, return to the summary, reopen to verify persistence, and validate after each cluster. Use [portal-troubleshooting.md](references/portal-troubleshooting.md) for exact error families and cross-schedule invariants.

### 7. Reconcile the generated preview

Download the preview PDF and preserve a redacted evidence-to-preview reconciliation. A downloaded JSON, successful validation, low demand, or refund does not prove completeness.

Use [preview-checklist.md](references/preview-checklist.md) to review every income head, special-rate amount, loss, disclosure, deduction, tax credit, interest/fee, and refund/payable result.

### 8. Produce a taxpayer or adviser handoff

Summarize:

- selected routes, modifiers, form and regime hypothesis;
- source documents used and missing;
- confirmed, derived, and unresolved figures;
- portal validations resolved and remaining;
- the preview result and an explicit list of assumptions;
- every specialist-review trigger.

Then stop. The taxpayer personally reviews the preview and controls declaration, payment, submission, and verification.

## Response style

- Use plain English first and the tax label second.
- Lead with the exact portal field or decision being addressed.
- State the AY and source behind any rule affecting tax or eligibility.
- Separate supported facts from provisional calculations.
- Say `do not submit yet` whenever a material item is unresolved.
- Never call a result “optimized,” “eligible,” “complete,” or “correct” without identifying the evidence and assumptions supporting it.

## Reference routing

- Adaptive questions, route composition, and document packs: [intake-and-routing.md](references/intake-and-routing.md)
- Minimum disclosure, evidence manifest, redaction, and retention: [document-intake-and-privacy.md](references/document-intake-and-privacy.md)
- Specialist-review triggers and stop conditions: [risk-and-escalation.md](references/risk-and-escalation.md)
- Form selection, regimes, Form 10-IEA, 44ADA, rent, home loan, and deductions: [form-and-regime.md](references/form-and-regime.md)
- Salary, other sources, profession, property, VDA, foreign assets, and tax credits: [income-schedules.md](references/income-schedules.md)
- Mutual funds, listed securities, intraday, F&O, turnover, and losses: [securities-and-trading.md](references/securities-and-trading.md)
- Income-tax disclosure versus FEMA/RBI/AD-bank compliance: [tax-and-fema.md](references/tax-and-fema.md)
- Portal validation categories and schedule dependencies: [portal-troubleshooting.md](references/portal-troubleshooting.md)
- Final PDF/JSON reconciliation: [preview-checklist.md](references/preview-checklist.md)
- Synthetic route and safety scenarios: [scenario-matrix.md](references/scenario-matrix.md)
- Official sources and freshness protocol: [official-sources.md](references/official-sources.md)

## Privacy validation

Before sharing or publishing any artifact derived from taxpayer assistance, run:

```bash
python3 scripts/privacy_scan.py <path>
```

Pass case-specific private terms at runtime without storing them in the repository:

```bash
python3 scripts/privacy_scan.py <path> --deny "private term"
```

Do not publish until the scanner and a manual review confirm that all examples and tests are synthetic.
