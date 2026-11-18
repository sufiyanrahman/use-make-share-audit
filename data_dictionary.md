# Data Dictionary for checklist.csv

Each row of checklist.csv is one criterion of the Use–Make–Share self-audit.

| Column | Description | Allowed values |
|---|---|---|
| id | Criterion code. D = Data, C = Code, R = Results | D1–D6, C1–C5, R1–R4 |
| criterion | The requirement, written as a statement that can be checked | Free text |
| stage | The Use–Make–Share stage the criterion mainly tests | Use, Make, Share |
| score | Result of the audit for one project | 1 (met and verified), 0 (applies but not met), N/A (does not apply) |
| evidence_link | Public link that proves the score | A URL, or empty when the score is N/A |

## Notes
- The file is plain CSV (RFC 4180), so any spreadsheet or text editor can open it.
- The criteria are derived from the public descriptions of NASA's Open Science 101 curriculum. This project is independent and not affiliated with NASA.
