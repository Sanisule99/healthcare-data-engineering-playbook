# 18 — Real-World Healthcare ETL

This module demonstrates a simple healthcare ETL workflow.

## ETL Steps

1. Extract raw patient and encounter CSV files
2. Clean column names
3. Remove duplicates
4. Validate required fields
5. Join patients and encounters
6. Save analytics-ready output

## Files

| File | Purpose |
|---|---|
| run_healthcare_etl.py | Main ETL pipeline |
| data/raw/patients_raw.csv | Synthetic raw patient data |
| data/raw/encounters_raw.csv | Synthetic raw encounter data |
| data/processed/ | Clean output files |
| logs/etl_log.txt | ETL run log |

## Skills Demonstrated

- Data ingestion
- Cleaning
- Validation
- Joins
- Logging
- Reproducibility
