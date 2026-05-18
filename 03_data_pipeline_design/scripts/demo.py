
import os
import pandas as pd

os.makedirs("03_data_pipeline_design/outputs", exist_ok=True)

patients = pd.read_csv("data/generated/patients.csv")
labs = pd.read_csv("data/generated/labs.csv")

df = patients.merge(labs, on="patient_id", how="left")
df["age_group"] = pd.cut(df["age"], bins=[0, 39, 59, 120], labels=["18-39", "40-59", "60+"])
df["high_bp_flag"] = (df["systolic_bp"] >= 140).astype(int)

df.to_csv("03_data_pipeline_design/outputs/pipeline_output.csv", index=False)
print("Saved pipeline output.")
