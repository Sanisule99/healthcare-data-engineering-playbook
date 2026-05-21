# Validation Rules

## Required Fields

The following fields should not be missing:

- patient_id
- encounter_id
- age
- sex
- encounter_type
- diagnosis_code

## Plausibility Rules

| Field | Rule |
|---|---|
| age | Must be between 0 and 120 |
| length_of_stay_days | Must be >= 0 |
| sex | Must be F, M, Other, or Unknown |
| discharge_date | Should not be before admission_date |

## Duplicate Rules

Duplicate encounter IDs may indicate repeated records.

## Use Case

These checks are useful before:

- dashboard development
- predictive modeling
- public health reporting
- clinical quality analysis
- ETL loading
