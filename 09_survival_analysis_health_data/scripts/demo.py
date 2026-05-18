
import os
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

os.makedirs("09_survival_analysis_health_data/outputs", exist_ok=True)

patients = pd.read_csv("data/generated/patients.csv")

kmf = KaplanMeierFitter()

kmf.fit(
    durations=patients["days_followup"],
    event_observed=patients["event"]
)

kmf.plot_survival_function()

plt.title("Kaplan-Meier Survival Curve")
plt.tight_layout()

plt.savefig("09_survival_analysis_health_data/outputs/km_curve.png")

print("Saved KM curve.")
