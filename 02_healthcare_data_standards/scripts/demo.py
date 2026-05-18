
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
