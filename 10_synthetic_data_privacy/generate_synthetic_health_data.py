import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

n = 100

patients = pd.DataFrame({
    "patient_id": [f"P{i:04d}" for i in range(1, n + 1)],
    "age": np.random.randint(18, 90, size=n),
    "sex": np.random.choice(["F", "M"], size=n),
    "race_ethnicity": np.random.choice(
        ["Black", "White", "Hispanic", "Asian", "Other"],
        size=n
    ),
    "chronic_condition_count": np.random.poisson(lam=2, size=n),
    "encounter_count": np.random.poisson(lam=3, size=n)
})

patients["high_risk_flag"] = (
    (patients["age"] >= 65)
    | (patients["chronic_condition_count"] >= 4)
    | (patients["encounter_count"] >= 6)
).astype(int)

encounters = []

for _, row in patients.iterrows():
    for i in range(max(row["encounter_count"], 1)):
        encounters.append({
            "encounter_id": f"E{row['patient_id'][1:]}_{i+1}",
            "patient_id": row["patient_id"],
            "encounter_type": np.random.choice(
                ["outpatient", "emergency", "inpatient"],
                p=[0.55, 0.25, 0.20]
            ),
            "length_of_stay_days": np.random.choice(
                [0, 1, 2, 3, 4, 5, 7, 10],
                p=[0.45, 0.18, 0.12, 0.08, 0.06, 0.05, 0.04, 0.02]
            )
        })

encounters = pd.DataFrame(encounters)

patients.to_csv(DATA_DIR / "synthetic_patients.csv", index=False)
encounters.to_csv(DATA_DIR / "synthetic_encounters.csv", index=False)

summary = pd.DataFrame({
    "metric": [
        "total_patients",
        "total_encounters",
        "high_risk_patients",
        "average_age",
        "average_chronic_condition_count"
    ],
    "value": [
        len(patients),
        len(encounters),
        patients["high_risk_flag"].sum(),
        round(patients["age"].mean(), 2),
        round(patients["chronic_condition_count"].mean(), 2)
    ]
})

summary.to_csv(OUTPUT_DIR / "synthetic_data_summary.csv", index=False)

print("Synthetic healthcare data generated.")
print("Files saved to:", DATA_DIR)
print(summary)
