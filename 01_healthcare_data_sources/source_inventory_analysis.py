import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "source_inventory.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

summary_by_type = df["data_type"].value_counts().reset_index()
summary_by_type.columns = ["data_type", "count"]

summary_by_sensitivity = df["sensitivity_level"].value_counts().reset_index()
summary_by_sensitivity.columns = ["sensitivity_level", "count"]

summary_by_type.to_csv(OUTPUT_DIR / "summary_by_data_type.csv", index=False)
summary_by_sensitivity.to_csv(OUTPUT_DIR / "summary_by_sensitivity.csv", index=False)

print("Healthcare data source inventory analysis complete.")
print(summary_by_type)
print(summary_by_sensitivity)
