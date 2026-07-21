# Portal troubleshooting

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

## Foreign asset validation

- Complete Schedule FA before answering “Yes” to the foreign-asset question in Part B-TTI.
- Reconcile opening, acquired, transferred, and closing quantities.
- Do not enter foreign shares in Schedule VDA.

## Trading validation

If “income cannot exceed turnover” appears, recheck whether the field expects gross profit, net profit, or an absolute-turnover figure. Use the broker report and the schedule definitions. Do not increase turnover arbitrarily.

## Missing schedule in the summary

Use “Add More Schedules” when a required schedule was not selected. Common omissions include Schedule CG, Schedule 112A, Schedule FA, Schedule VDA, Schedule BP, and loss schedules.

## Portal state problems

- Save each schedule and return to the summary before validation.
- Reopen the schedule after changing a dependency because computed fields may be stale.
- Regenerate the preview after every material correction.
- If the online utility behaves inconsistently, download the JSON, preserve the draft, and compare with the current offline utility rather than repeatedly changing correct figures.
