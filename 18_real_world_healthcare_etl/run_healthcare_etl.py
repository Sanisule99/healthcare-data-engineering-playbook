import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
LOG_DIR = BASE_DIR / "logs"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOG_DIR / "etl_log.txt"

def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

def clean_columns(df):
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
    return df

def validate_required_columns(df, required_cols, table_name):
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"{table_name} missing required columns: {missing}")
    write_log(f"{table_name}: required columns validated")

def run_etl():
    write_log("ETL started")

    patients = pd.read_csv(RAW_DIR / "patients_raw.csv")
    encounters = pd.read_csv(RAW_DIR / "encounters_raw.csv")

    patients = clean_columns(patients)
    encounters = clean_columns(encounters)

    validate_required_columns(
        patients,
        ["patient_id", "sex", "age", "race"],
        "patients"
    )

    validate_required_columns(
        encounters,
        ["encounter_id", "patient_id", "encounter_type", "length_of_stay_days"],
        "encounters"
    )

    before = len(patients)
    patients = patients.drop_duplicates()
    after = len(patients)
    write_log(f"Patients deduplicated: {before - after} duplicate rows removed")

    invalid_age = patients[(patients["age"] < 0) | (patients["age"] > 120)]
    if len(invalid_age) > 0:
        write_log(f"Warning: invalid ages found: {len(invalid_age)}")

    negative_los = encounters[encounters["length_of_stay_days"] < 0]
    if len(negative_los) > 0:
        write_log(f"Warning: negative LOS found: {len(negative_los)}")

    analytic = encounters.merge(
        patients,
        on="patient_id",
        how="left"
    )

    patients.to_csv(PROCESSED_DIR / "patients_clean.csv", index=False)
    encounters.to_csv(PROCESSED_DIR / "encounters_clean.csv", index=False)
    analytic.to_csv(PROCESSED_DIR / "patient_encounter_analytic.csv", index=False)

    write_log("Processed files saved")
    write_log("ETL completed")

if __name__ == "__main__":
    run_etl()
