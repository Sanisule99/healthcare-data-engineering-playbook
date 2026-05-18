
import os
import numpy as np
import pandas as pd

os.makedirs("10_synthetic_data_privacy/outputs", exist_ok=True)

rng = np.random.default_rng(42)
n = 300

synthetic = pd.DataFrame({
    "age": rng.integers(18, 90, size=n),
    "systolic_bp": rng.integers(95, 185, size=n),
    "glucose": rng.normal(115, 30, size=n).round(1),
    "risk_group": rng.choice(["low", "medium", "high"], size=n)
})

synthetic.to_csv("10_synthetic_data_privacy/outputs/synthetic_health_data.csv", index=False)
print("Saved synthetic health data.")
