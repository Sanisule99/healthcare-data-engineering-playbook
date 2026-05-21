import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "raw_pipeline_input.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# Validation
required_columns = ["record_id", "patient_id", "source_system", "encounter_type", "value"]
missing_cols = [c for c in required_columns if c not in df.columns]

if missing_cols:
    raise ValueError(f"Missing required columns: {missing_cols}")

# Transform
df.columns = [c.lower().strip() for c in df.columns]
df["high_value_flag"] = (df["value"] >= 20).astype(int)

# Source summary
source_summary = (
    df.groupby("source_system")
    .agg(
        record_count=("record_id", "count"),
        average_value=("value", "mean")
    )
    .reset_index()
)

df.to_csv(OUTPUT_DIR / "curated_pipeline_output.csv", index=False)
source_summary.to_csv(OUTPUT_DIR / "source_system_summary.csv", index=False)

print("Healthcare pipeline design demo complete.")
print(source_summary)
print("Outputs saved to:", OUTPUT_DIR)
