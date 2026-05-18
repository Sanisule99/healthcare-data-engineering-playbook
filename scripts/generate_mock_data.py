
import os
import numpy as np
import pandas as pd

os.makedirs("data/generated", exist_ok=True)

rng = np.random.default_rng(42)
n = 200

patients = pd.DataFrame({
    "patient_id": [f"P{i:04d}" for i in range(1, n+1)],
    "age": rng.integers(18, 90, size=n),
    "sex": rng.choice(["F", "M"], size=n),
    "days_followup": rng.integers(30, 1500, size=n),
    "event": rng.binomial(1, 0.3, size=n)
})

labs = pd.DataFrame({
    "patient_id": patients["patient_id"],
    "systolic_bp": rng.integers(90, 190, size=n),
    "glucose": rng.normal(110, 25, size=n)
})

patients.to_csv("data/generated/patients.csv", index=False)
labs.to_csv("data/generated/labs.csv", index=False)

print("Mock healthcare data generated.")
