import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

n = 300

age = np.random.randint(18, 90, size=n)
prior_encounters = np.random.poisson(lam=2, size=n)
chronic_condition_count = np.random.poisson(lam=1.5, size=n)
abnormal_lab_flag = np.random.binomial(1, 0.20, size=n)

# Rare outcome probability
risk_score = (
    0.03
    + 0.02 * (age >= 65)
    + 0.03 * (prior_encounters >= 4)
    + 0.04 * (chronic_condition_count >= 3)
    + 0.05 * abnormal_lab_flag
)

risk_score = np.clip(risk_score, 0, 0.35)
rare_event = np.random.binomial(1, risk_score)

df = pd.DataFrame({
    "patient_id": [f"P{i:04d}" for i in range(1, n + 1)],
    "age": age,
    "prior_encounters": prior_encounters,
    "chronic_condition_count": chronic_condition_count,
    "abnormal_lab_flag": abnormal_lab_flag,
    "rare_event": rare_event
})

df.to_csv(DATA_DIR / "imbalanced_health_data.csv", index=False)

print("Synthetic imbalanced dataset created.")
print(df["rare_event"].value_counts(normalize=True))
