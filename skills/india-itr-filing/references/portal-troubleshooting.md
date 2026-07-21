# Portal troubleshooting

Read the validation category, exact field name, and exact error text before changing data. Category A errors block upload; other categories may be warnings or claim restrictions. Portal validation is not evidence that the return is complete.

## Part A General says business income is absent

If Schedule BP contains professional, speculative, or non-speculative business income or loss, answer “Yes” to the current-assessment-year business/profession question. Revisit the Form 10-IEA questions that appear after changing it.

## Salary nature errors

- Select the truthful nature of employer.
- For unused zero-value perquisite or profit-in-lieu rows, delete the row if possible.
- If the row is required, select the accurate nature, add a neutral factual description, and keep the amount at the supported value.

## Schedule CG quarterly breakup mismatch

The accrual/receipt table must equal the relevant capital-gain total. Allocate each gain to the bucket containing its transfer date:

- up to 15 June;
- 16 June to 15 September;
- 16 September to 15 December;
- 16 December to 15 March;
- 16 March to 31 March.

Populate only the rows that correspond to the gain type. Do not distribute amounts evenly without transaction dates.

Where Schedule VDA flows to Schedule CG C2, the corresponding Schedule CG Table F period buckets must sum exactly to C2 using actual transfer dates.

## Foreign asset validation

- Complete Schedule FA before answering “Yes” to the foreign-asset question in Part B-TTI.
- Reconcile opening, acquired, transferred, and closing quantities.
- Do not enter foreign shares in Schedule VDA.

## Trading validation

If “income cannot exceed turnover” appears, recheck whether the field expects gross profit, net profit, or an absolute-turnover figure. Use the broker report and the schedule definitions. Do not increase turnover arbitrarily.

For the current ITR-3 schema, separately verify intraday income against intraday turnover and F&O income against F&O turnover. A validation inequality does not authorize using P&L as turnover or converting a loss into positive income.

## Missing schedule in the summary

First pass the form-eligibility and evidence gate. Then use “Add More Schedules” when an evidence-supported required schedule was not selected. Common omissions include Schedule CG, Schedule 112A, Schedule FA, Schedule VDA, Schedule BP, and loss schedules.

## Portal state problems

- Save each schedule and return to the summary before validation.
- Reopen the schedule after changing a dependency because computed fields may be stale.
- Regenerate the preview after every material correction.
- Archive the online Return Summary JSON and redacted error artifacts. Before attempting offline import, verify that the exact AY/form supports online-draft import. Never hand-edit return JSON. If unsupported, start a fresh offline draft from current prefilled data and reconcile it independently.

## Validation repair rule

Never zero, delete, duplicate, reclassify, or fabricate a real item merely to clear validation. Resolve one error family at a time, rerun validation, and keep a redacted change log. If the portal cannot represent the supported result, stop and escalate.
