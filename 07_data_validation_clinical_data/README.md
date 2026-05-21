# 07 — Data Validation for Clinical Data

This module demonstrates common validation checks used in healthcare analytics and informatics workflows.

## Why This Matters

Clinical datasets often contain:

- missing identifiers
- duplicate records
- impossible age values
- negative length of stay
- invalid dates
- missing diagnosis codes
- unexpected categories

Validation helps prevent incorrect analysis, unreliable dashboards, and unsafe model inputs.

## Files

| File | Purpose |
|---|---|
| clinical_data_validation.py | Runs validation checks |
| data/clinical_validation_sample.csv | Synthetic clinical dataset with intentional issues |
| outputs/validation_report.csv | Validation results |
| validation_rules.md | Explanation of rules |

## Skills Demonstrated

- Data quality checks
- Rule-based validation
- Clinical plausibility checks
- Reproducible reporting
- Analytics readiness assessment
