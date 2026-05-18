
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("01_healthcare_data_sources/outputs", exist_ok=True)

patients = pd.read_csv("data/generated/patients.csv")

patients["sex"].value_counts().plot(kind="bar", title="Patients by Sex")

plt.tight_layout()
plt.savefig("01_healthcare_data_sources/outputs/patients_by_sex.png")

print("Saved figure.")
