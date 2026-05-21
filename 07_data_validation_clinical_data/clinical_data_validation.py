import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "clinical_validation_sample.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

results = []

def add_result(rule_name, issue_count, severity, description):
    results.append({
        "rule_name": rule_name,
        "issue_count": int(issue_count),
        "severity": severity,
        "description": description
    })

required_cols = [
    "patient_id",
    "encounter_id",
    "age",
    "sex",
    "encounter_type",
    "diagnosis_code"
]

for col in required_cols:
    add_result(
        f"missing_{col}",
        df[col].isna().sum(),
        "high",
        f"Missing values in {col}"
    )

add_result(
    "duplicate_encounter_id",
    df["encounter_id"].duplicated().sum(),
    "high",
    "Duplicate encounter IDs detected"
)

invalid_age = df[(df["age"] < 0) | (df["age"] > 120)]
add_result(
    "invalid_age",
    len(invalid_age),
    "high",
    "Age outside expected range 0-120"
)

negative_los = df[df["length_of_stay_days"] < 0]
add_result(
    "negative_length_of_stay",
    len(negative_los),
    "high",
    "Length of stay cannot be negative"
)

valid_sex = ["F", "M", "Other", "Unknown"]
invalid_sex = df[~df["sex"].isin(valid_sex)]
add_result(
    "invalid_sex_category",
    len(invalid_sex),
    "medium",
    "Sex category outside accepted values"
)

df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce")
df["discharge_date"] = pd.to_datetime(df["discharge_date"], errors="coerce")

invalid_dates = df[df["discharge_date"] < df["admission_date"]]
add_result(
    "discharge_before_admission",
    len(invalid_dates),
    "high",
    "Discharge date occurs before admission date"
)

report = pd.DataFrame(results)
report.to_csv(OUTPUT_DIR / "validation_report.csv", index=False)

print("Clinical data validation complete.")
print(report)
print("Saved report to:", OUTPUT_DIR / "validation_report.csv")
