import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "multimodal_dataset_example.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# Basic summary
summary = df.describe()
summary.to_csv(OUTPUT_DIR / "multimodal_summary_statistics.csv")

# Correlation analysis
correlation = df.select_dtypes(include="number").corr()
correlation.to_csv(OUTPUT_DIR / "multimodal_correlations.csv")

# High-risk stratification example
df["high_risk"] = (
    (df["tumor_grade"] >= 3)
    & (df["mutation_burden"] > 8)
).astype(int)

risk_summary = (
    df.groupby("high_risk")
    .agg(
        patient_count=("patient_id", "count"),
        avg_survival=("survival_months", "mean"),
        avg_pd_l1=("pd_l1_expression", "mean"),
        avg_tumor_fraction=("wsi_tumor_fraction", "mean")
    )
    .reset_index()
)

risk_summary.to_csv(
    OUTPUT_DIR / "multimodal_risk_summary.csv",
    index=False
)

print("\nRisk Summary:")
print(risk_summary)

print("\nOutputs saved to:", OUTPUT_DIR)
