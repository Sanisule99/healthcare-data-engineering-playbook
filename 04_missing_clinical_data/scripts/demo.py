
import os
import pandas as pd

os.makedirs("04_missing_clinical_data/outputs", exist_ok=True)

labs = pd.read_csv("data/generated/labs.csv")

missing = labs.isna().mean()

missing.to_csv("04_missing_clinical_data/outputs/missingness.csv")

print(missing)
