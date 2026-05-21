# Imbalanced Dataset Notes

## The Problem

In healthcare, the outcome of interest is often rare.

Example:

If only 5% of patients experience an adverse event, a model that predicts "no event" for everyone will be 95% accurate.

But that model is clinically useless.

## Better Metrics

For imbalanced healthcare datasets, review:

- sensitivity / recall
- specificity
- precision
- F1 score
- ROC AUC
- PR AUC
- confusion matrix

## Practical Strategies

- use class weights
- use stratified train/test splits
- evaluate recall for minority class
- avoid relying on accuracy alone
- consider threshold tuning
- validate in external datasets

## Healthcare Interpretation

False negatives may be especially important when missing a high-risk patient has serious consequences.
