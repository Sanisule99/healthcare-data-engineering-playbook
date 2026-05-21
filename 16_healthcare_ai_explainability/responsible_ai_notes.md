# Responsible AI Notes for Healthcare Explainability

## Why explainability matters

Healthcare AI tools may influence clinical, operational, or public health decisions. Therefore, models should be interpretable and auditable.

## Key Questions

1. What features drive the prediction?
2. Are the features clinically reasonable?
3. Is the model over-relying on proxy variables?
4. Does performance differ by subgroup?
5. Has the model been validated externally?
6. Is there a human-in-the-loop review process?

## Feature Importance Interpretation

Feature importance can help identify which variables contribute most to model prediction.

However, feature importance does not prove causality.

## Limitations

This example uses synthetic data and should not be used for clinical decision-making.

## Future Enhancements

- Add SHAP values
- Add calibration curves
- Add subgroup fairness evaluation
- Add model cards
- Add human review workflow
