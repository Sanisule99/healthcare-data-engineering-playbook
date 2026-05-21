import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "clinical_missing_data_sample.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Missingness profile
missing_report = pd.DataFrame({
    "column": df.columns,
    "missing_count": df.isna().sum().values,
    "missing_percent": (df.isna().mean().values * 100).round(2)
})

missing_report.to_csv(OUTPUT_DIR / "missingness_report.csv", index=False)

# Create missingness flags for important fields
for col in ["bp_systolic", "bp_diastolic", "followup_completed", "risk_score"]:
    df[f"{col}_missing_flag"] = df[col].isna().astype(int)

# Simple imputation strategy for demonstration only
df["age_imputed"] = df["age"].fillna(df["age"].median())
df["bp_systolic_imputed"] = df["bp_systolic"].fillna(df["bp_systolic"].median())
df["bp_diastolic_imputed"] = df["bp_diastolic"].fillna(df["bp_diastolic"].median())
df["risk_score_imputed"] = df["risk_score"].fillna(df["risk_score"].median())

# Categorical/binary simple fill
df["screening_completed_imputed"] = df["screening_completed"].fillna(0)
df["followup_completed_imputed"] = df["followup_completed"].fillna(0)

df.to_csv(OUTPUT_DIR / "clinical_missing_data_cleaned.csv", index=False)

print("Missing data analysis complete.")
print(missing_report)
print("Outputs saved to:", OUTPUT_DIR)
