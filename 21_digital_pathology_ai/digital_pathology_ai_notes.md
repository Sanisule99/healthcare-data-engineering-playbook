# Digital Pathology AI Notes

## Common Workflow

1. Obtain whole slide images
2. Perform quality control
3. Tile slides into smaller patches
4. Extract features or train tile classifiers
5. Aggregate tile predictions to slide level
6. Interpret model outputs using Grad-CAM or SHAP
7. Validate results with pathologist review

## Key Concepts

- WSI: Whole Slide Image
- Tile: Small image patch extracted from a WSI
- Slide-level label: Diagnosis or outcome assigned to entire slide
- Tile-level prediction: Model prediction for each patch
- Aggregation: Combining tile predictions into slide-level prediction
- Explainability: Visual or statistical interpretation of model behavior

## Responsible Use

Digital pathology AI should support, not replace, expert review.

Models should be evaluated for:

- staining variation
- scanner differences
- site-level bias
- tissue artifacts
- generalizability
