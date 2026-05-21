import requests
import pandas as pd

FHIR_BASE_URL = "https://hapi.fhir.org/baseR4"

def fetch_patients(count=10):
    url = f"{FHIR_BASE_URL}/Patient"
    response = requests.get(
        url,
        params={"_count": count},
        timeout=30
    )
    response.raise_for_status()
    return response.json()

def patient_bundle_to_dataframe(bundle):
    rows = []

    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})

        name_list = resource.get("name", [])

        first_name = None
        last_name = None

        if name_list:
            first_name = (
                " ".join(name_list[0].get("given", []))
                if name_list[0].get("given")
                else None
            )

            last_name = name_list[0].get("family")

        rows.append({
            "id": resource.get("id"),
            "gender": resource.get("gender"),
            "birthDate": resource.get("birthDate"),
            "first_name_present": first_name is not None,
            "last_name_present": last_name is not None,
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    bundle = fetch_patients(count=10)

    df = patient_bundle_to_dataframe(bundle)

    print(df.head())

    df.to_csv(
        "fhir_patients_sample_output.csv",
        index=False
    )

    print("Saved: fhir_patients_sample_output.csv")
