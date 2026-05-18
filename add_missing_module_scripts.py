from pathlib import Path

BASE = Path(r"C:\Users\sanis\Git\healthcare-data-engineering-playbook")

def write(path, content):
    file_path = BASE / path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")

write("02_healthcare_data_standards/scripts/demo.py", """
import os
import pandas as pd

os.makedirs("02_healthcare_data_standards/outputs", exist_ok=True)

df = pd.DataFrame({
    "standard": ["HL7", "FHIR", "OMOP"],
    "main_use": [
        "Clinical messaging",
        "API-based clinical data exchange",
        "Common data model for analytics"
    ],
    "why_it_matters": [
        "Moves healthcare data between systems",
        "Supports modern interoperability",
        "Enables multi-site research and analytics"
    ]
})

df.to_csv("02_healthcare_data_standards/outputs/standards_summary.csv", index=False)
print("Saved healthcare standards summary.")
""")

write("03_data_pipeline_design/scripts/demo.py", """
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
""")

write("05_feature_engineering_health_data/scripts/demo.py", """
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
""")

write("06_imbalanced_medical_datasets/scripts/demo.py", """
import os
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

os.makedirs("06_imbalanced_medical_datasets/outputs", exist_ok=True)

rng = np.random.default_rng(42)
n = 500

df = pd.DataFrame({
    "feature_1": rng.normal(size=n),
    "feature_2": rng.normal(size=n),
    "rare_event": rng.binomial(1, 0.08, size=n)
})

X = df[["feature_1", "feature_2"]]
y = df["rare_event"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model = DummyClassifier(strategy="most_frequent")
model.fit(X_train, y_train)
pred = model.predict(X_test)

with open("06_imbalanced_medical_datasets/outputs/classification_report.txt", "w") as f:
    f.write(classification_report(y_test, pred, zero_division=0))

print("Saved imbalanced dataset report.")
""")

write("07_data_validation_clinical_data/scripts/demo.py", """
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
    f.write("\\n".join(issues))

print("Saved validation report.")
""")

write("08_reproducible_pipelines/config.yaml", """
input_file: data/generated/patients.csv
output_dir: 08_reproducible_pipelines/outputs
""")

write("08_reproducible_pipelines/scripts/demo.py", """
import os
import yaml
import pandas as pd

with open("08_reproducible_pipelines/config.yaml") as f:
    config = yaml.safe_load(f)

os.makedirs(config["output_dir"], exist_ok=True)

df = pd.read_csv(config["input_file"])
summary = df.groupby("sex")["patient_id"].count().reset_index(name="n_patients")

summary.to_csv(os.path.join(config["output_dir"], "sex_counts.csv"), index=False)
print("Saved reproducible pipeline output.")
""")

write("10_synthetic_data_privacy/scripts/demo.py", """
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
""")

write("12_future_health_data_systems/scripts/demo.py", """
import os
import pandas as pd

os.makedirs("12_future_health_data_systems/outputs", exist_ok=True)

df = pd.DataFrame({
    "theme": [
        "Interoperability",
        "Multimodal data",
        "Federated learning",
        "Foundation models",
        "Reproducible pipelines"
    ],
    "why_it_matters": [
        "Moves data across systems",
        "Combines EHR, imaging, labs, genomics, and claims",
        "Supports privacy-preserving multi-site learning",
        "Enables reusable AI across tasks",
        "Improves trust and repeatability"
    ]
})

df.to_csv("12_future_health_data_systems/outputs/future_health_data_systems.csv", index=False)
print("Saved future systems summary.")
""")

print("Added demo scripts for modules 02, 03, 05, 06, 07, 08, 10, and 12.")
