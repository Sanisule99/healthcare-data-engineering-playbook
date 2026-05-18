
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
