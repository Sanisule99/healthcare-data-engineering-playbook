# Missing Clinical Data Notes

## Types of Missingness

### MCAR — Missing Completely at Random
Missingness is unrelated to observed or unobserved data.

### MAR — Missing at Random
Missingness is related to observed data.

### MNAR — Missing Not at Random
Missingness is related to the missing value itself.

## Common Healthcare Examples

- Missing follow-up status
- Missing lab values
- Missing screening completion
- Missing demographic fields
- Missing risk scores

## Common Strategies

- Report missingness transparently
- Create missingness flags
- Use simple imputation for demos
- Use multiple imputation for formal research
- Avoid silently dropping records
- Evaluate whether missingness differs by group

## Caution

Imputation can introduce bias if missingness mechanisms are not understood.
