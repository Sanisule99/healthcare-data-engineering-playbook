
import os
import pandas as pd

os.makedirs("05_feature_engineering_health_data/outputs", exist_ok=True)

patients = pd.read_csv("data/generated/patients.csv")
labs = pd.read_csv("data/generated/labs.csv")

df = patients.merge(labs, on="patient_id", how="left")
df["age_65_plus"] = (df["age"] >= 65).astype(int)
df["high_bp_flag"] = (df["systolic_bp"] >= 140).astype(int)
df["high_glucose_flag"] = (df["glucose"] >= 126).astype(int)

df.to_csv("05_feature_engineering_health_data/outputs/engineered_features.csv", index=False)
print("Saved engineered features.")
