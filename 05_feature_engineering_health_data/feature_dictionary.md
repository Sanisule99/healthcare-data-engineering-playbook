# Feature Dictionary

## age_group

Categorizes patients into age bands:
- 18-39
- 40-64
- 65+

## high_utilization_flag

1 if encounter_count >= 5, otherwise 0.

## multiple_chronic_conditions_flag

1 if chronic_condition_count >= 3, otherwise 0.

## long_stay_flag

1 if length_of_stay_days >= 5, otherwise 0.

## bp_screening_status

Classifies whether a participant was screened for blood pressure.

## followup_gap_flag

1 if high_bp_identified = 1 and followup_completed = 0.

## simple_risk_score

Sum of:
- high utilization
- multiple chronic conditions
- long stay
- follow-up gap
