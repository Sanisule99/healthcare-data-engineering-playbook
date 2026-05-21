import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "raw_health_features.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Age group feature
def assign_age_group(age):
    if age < 40:
        return "18-39"
    elif age < 65:
        return "40-64"
    else:
        return "65+"

df["age_group"] = df["age"].apply(assign_age_group)

# Utilization features
df["high_utilization_flag"] = (df["encounter_count"] >= 5).astype(int)

# Chronic burden feature
df["multiple_chronic_conditions_flag"] = (
    df["chronic_condition_count"] >= 3
).astype(int)

# Length of stay feature
df["long_stay_flag"] = (df["length_of_stay_days"] >= 5).astype(int)

# Screening features
df["bp_screening_status"] = df["screened_bp"].map({
    1: "screened",
    0: "not_screened"
})

# Follow-up gap feature
df["followup_gap_flag"] = (
    (df["high_bp_identified"] == 1)
    & (df["followup_completed"] == 0)
).astype(int)

# Simple composite risk score
df["simple_risk_score"] = (
    df["high_utilization_flag"]
    + df["multiple_chronic_conditions_flag"]
    + df["long_stay_flag"]
    + df["followup_gap_flag"]
)

# Risk category
def assign_risk_category(score):
    if score >= 3:
        return "high"
    elif score == 2:
        return "moderate"
    else:
        return "low"

df["risk_category"] = df["simple_risk_score"].apply(assign_risk_category)

# Save output
df.to_csv(OUTPUT_DIR / "engineered_features.csv", index=False)

# Summary
summary = (
    df["risk_category"]
    .value_counts()
    .reset_index()
)

summary.columns = ["risk_category", "patient_count"]
summary.to_csv(OUTPUT_DIR / "risk_category_summary.csv", index=False)

print("Feature engineering complete.")
print(df.head())
print("Outputs saved to:", OUTPUT_DIR)
