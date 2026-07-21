# Intake and routing

Use a multi-select intake. Modes are workflow routes, not legal taxpayer categories, and they can be combined.

## Short intake

Ask in plain language:

1. Which financial year and assessment year is this, and is the return original, revised, belated, updated, or responding to a notice?
2. What was the residential status: resident ordinarily resident, resident but not ordinarily resident, non-resident, or unsure?
3. Which occurred during the year? Select all:
   - salary or pension;
   - freelance, consulting, or professional receipts;
   - another business;
   - delivery shares, ETFs, or mutual-fund redemptions;
   - intraday equity;
   - F&O, commodity, or currency derivatives;
   - VDA or crypto transfer;
   - property ownership, purchase, sale, rent, or home loan;
   - interest, dividends, refund interest, TDS, TCS, or tax challans;
   - foreign asset, foreign income, foreign account, or foreign signing authority;
   - unlisted shares, directorship, or partnership interest;
   - prior-year losses, unabsorbed depreciation, MAT, or AMT credit;
   - none or unsure.
4. Are there multiple employers, income sources, brokers, AMCs, exchanges, properties, countries, or prior returns?
5. Which source records are available now, and which figures or transactions remain unknown?
6. Has Form 10-IEA ever been filed, or is the taxpayer unsure?
7. Does any notice, audit question, missed deadline, foreign-tax claim, valuation, gift, or regulatory filing exist?

An `unsure` answer is a request for evidence, not permission to assume `No`.

## Route composition

Choose the narrowest primary route that covers the dominant work, then add every modifier.

| Primary route | Use when | Minimum starting evidence |
|---|---|---|
| Salary essential | Salary/pension with no complexity trigger | Form 16 for every employer, AIS/TIS, Form 26AS, interest/dividend records |
| Salary investor | Salary plus delivery shares, ETFs, or mutual funds | Salary pack, broker/AMC capital-gains reports, CAS, AIS/26AS |
| Professional 44ADA candidate | A qualifying profession may satisfy every current 44ADA condition | Invoice/receipt ledger, gross-receipt reconciliation, payment-mode split, bank/remittance records |
| Professional regular | Professional/business income where 44ADA is unavailable, rejected, or uncertain | Books or income/expense records, bank records, tax records, audit assessment |
| Investor | Delivery securities or mutual-fund activity without business/profession | Capital-gains reports with lots/cost, CAS, AIS/26AS |
| Trader | Intraday, F&O, commodity, or currency activity | Broker tax P&L, segment ledger, contract notes, turnover method, prior classification/loss records |
| Property | Property sale, purchase, rent, loan, co-ownership, or possession questions dominate | Ownership/purchase/sale, possession, rent, tax, and final lender records |
| Foreign cross-border | Foreign asset, account, income, signing authority, unlisted share, or foreign-tax/FEMA issue | Ownership, entity/account, valuation, income, FX, tax and regulatory records |
| Complex composite | Three or more routes, inconsistent records, notice, audit, or blocked classification | Consolidated evidence register and professional handoff pack |

## Mandatory modifiers

Always add modifiers for business/profession, multiple employers, capital gains, intraday, F&O, VDA, property, foreign asset/income, unlisted equity, director/partner status, brought-forward losses, tax credits, notice/late return, and unknown transactions.

Modifiers determine schedules, documents, validation tests, and escalation. They do not disappear because the amount is small.

## Routing output

Before calculating, produce:

```text
Filing context:
Primary route:
Modifiers:
Risk tier:
Form hypothesis and failed eligibility conditions:
Regime/Form 10-IEA status:
Documents received:
Documents missing:
Unknown or blocked facts:
Schedules likely required:
Specialist review required:
```

Do not proceed to portal entry while a fact that controls the form, regime, tax head, disclosure, loss, or regulatory treatment is `unknown` or `blocked`.
