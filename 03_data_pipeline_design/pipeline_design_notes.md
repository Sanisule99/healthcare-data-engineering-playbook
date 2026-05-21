# Healthcare Data Pipeline Design Notes

## Basic Pipeline

Source data
? extraction
? validation
? transformation
? curated table
? dashboard or model

## Key Design Questions

- What is the source system?
- What fields are required?
- What validation rules are needed?
- What transformations are applied?
- Where are outputs stored?
- How is the pipeline monitored?

## Common Pipeline Layers

### Raw Layer

Original source extract.

### Validated Layer

Data after quality checks.

### Curated Layer

Analytics-ready dataset.

### Reporting Layer

Dashboards, reports, and model inputs.
