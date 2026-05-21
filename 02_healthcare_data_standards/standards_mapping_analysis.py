import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "standard_mapping_example.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

system_summary = df["standard_system"].value_counts().reset_index()
system_summary.columns = ["standard_system", "mapped_count"]

system_summary.to_csv(OUTPUT_DIR / "standard_system_summary.csv", index=False)

print("Healthcare standards mapping analysis complete.")
print(system_summary)
