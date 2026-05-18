
import os
import pandas as pd

os.makedirs("07_data_validation_clinical_data/outputs", exist_ok=True)

labs = pd.read_csv("data/generated/labs.csv")

issues = []

if labs["patient_id"].duplicated().any():
    issues.append("Duplicate patient IDs found.")

if (labs["systolic_bp"] < 60).any() or (labs["systolic_bp"] > 300).any():
    issues.append("Implausible systolic blood pressure values found.")

if labs["glucose"].dropna().lt(0).any():
    issues.append("Negative glucose values found.")

if not issues:
    issues.append("No major validation issues found.")

with open("07_data_validation_clinical_data/outputs/validation_report.txt", "w") as f:
    f.write("\n".join(issues))

print("Saved validation report.")
