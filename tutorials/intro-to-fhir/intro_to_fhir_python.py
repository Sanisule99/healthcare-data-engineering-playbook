"""
Intro to FHIR APIs with Python

This script demonstrates how to query a public FHIR API and convert selected
FHIR resources into simple pandas DataFrames.

Educational use only. Do not use real patient data in this demo.
"""

import requests
import pandas as pd

BASE_URL = "https://hapi.fhir.org/baseR4"


def get_fhir_bundle(resource_type: str, params: dict | None = None) -> dict:
    """Query a FHIR server and return a FHIR Bundle as JSON."""
    url = f"{BASE_URL}/{resource_type}"
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def extract_patients(bundle: dict) -> pd.DataFrame:
    """Extract basic patient fields from a FHIR Patient search Bundle."""
    rows = []
    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})
        if resource.get("resourceType") != "Patient":
            continue
        name = resource.get("name", [{}])[0]
        rows.append({
            "patient_id": resource.get("id"),
            "gender": resource.get("gender"),
            "birth_date": resource.get("birthDate"),
            "family_name": name.get("family"),
            "given_name": " ".join(name.get("given", [])) if name.get("given") else None,
        })
    return pd.DataFrame(rows)


def extract_observations(bundle: dict) -> pd.DataFrame:
    """Extract basic observation fields from a FHIR Observation search Bundle."""
    rows = []
    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})
        if resource.get("resourceType") != "Observation":
            continue
        code = resource.get("code", {}).get("coding", [{}])[0]
        value_quantity = resource.get("valueQuantity", {})
        subject = resource.get("subject", {}).get("reference", "")
        rows.append({
            "observation_id": resource.get("id"),
            "patient_reference": subject,
            "code": code.get("code"),
            "display": code.get("display"),
            "value": value_quantity.get("value"),
            "unit": value_quantity.get("unit"),
            "effective_datetime": resource.get("effectiveDateTime"),
        })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    print("Querying public FHIR server...")

    patient_bundle = get_fhir_bundle("Patient", params={"_count": 10})
    patients_df = extract_patients(patient_bundle)
    print("\nPatients")
    print(patients_df.head())

    observation_bundle = get_fhir_bundle("Observation", params={"_count": 10})
    observations_df = extract_observations(observation_bundle)
    print("\nObservations")
    print(observations_df.head())
