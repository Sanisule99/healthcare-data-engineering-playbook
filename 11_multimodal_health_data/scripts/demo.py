
import os
import pandas as pd

os.makedirs("11_multimodal_health_data/outputs", exist_ok=True)

patients = pd.read_csv("data/generated/patients.csv")
labs = pd.read_csv("data/generated/labs.csv")

merged = patients.merge(labs, on="patient_id")

merged.to_csv(
    "11_multimodal_health_data/outputs/multimodal_table.csv",
    index=False
)

print("Saved multimodal table.")
