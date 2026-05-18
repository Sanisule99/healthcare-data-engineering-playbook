
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
