# Document intake and privacy

## Framing

This skill assists from documents the taxpayer chooses to provide. Original records remain under taxpayer control. Collect the minimum evidence needed for the selected routes; do not build a reusable identity profile.

## Intake modes

- **Minimal disclosure:** taxpayer supplies redacted figures and source locators.
- **Local evidence review:** files remain in a case-scoped local folder excluded from source control and cloud sync.
- **Professional handoff:** produce a redacted question and evidence manifest for a CA, lawyer, or RBI/FEMA adviser.

Never request passwords, OTPs, Aadhaar, full PAN, full bank or card numbers, complete residential addresses, signatures, biometrics, or login sessions.

## Evidence manifest

Rename references in working notes to neutral IDs such as `DOC-001`. Do not reproduce the original filename.

Record:

- neutral document ID;
- document type and covered period;
- route/modifier served;
- local-only source locator;
- tax fields extracted;
- status: confirmed, prefilled-only, derived, unresolved, unknown, or blocked;
- unresolved question;
- deletion or retention action.

## Minimum evidence by route

- Salary: Form 16 Parts A/B from every employer, AIS/TIS, Form 26AS, interest/dividend records.
- Professional: invoices, gross-receipt ledger, bank/remittance records, cash/electronic split, GST/FIRC evidence where applicable.
- Investor: broker/AMC capital-gains report, CAS, lot-level transactions, AIS/26AS.
- Trader: segment-wise tax P&L, turnover working, contract notes/ledger, charges, prior ITR loss schedules.
- Property: ownership and share, possession/completion, use, rent, municipal tax, final annual lender certificate, sale/purchase and property-TDS records.
- VDA: exchange/deductor identity, asset identity, acquisition and transfer dates, cost, consideration, ledger and TDS.
- Foreign: legal/beneficial interest, entity/account details, acquisition, opening/peak/closing values, income/proceeds, FX evidence, foreign tax, and relevant AD-bank/ODI/LRS records.
- Tax credits: Form 16/16A/16B/16C/16D as applicable, Form 26AS, TCS records, and challans.

## Retention and publishing

- Keep raw financial files outside the skill repository.
- Never commit or publish taxpayer screenshots, PDFs, spreadsheets, exports, emails, JSON, or copied filenames.
- Delete case-scoped working copies after the handoff when the taxpayer no longer needs them; state what was deleted.
- Retain a redacted evidence register only when the taxpayer requests it.
- A passing privacy scan is necessary but not sufficient. Manually review tracked files and Git history before publication.
- Do not add binary fixtures to this public repository. Use synthetic text fixtures only.
