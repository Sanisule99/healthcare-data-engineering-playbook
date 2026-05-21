import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Healthcare Analytics Dashboard", layout="wide")

DATA_DIR = Path(__file__).parent / "data"

patients = pd.read_csv(DATA_DIR / "dashboard_patients.csv")
encounters = pd.read_csv(DATA_DIR / "dashboard_encounters.csv")
diagnoses = pd.read_csv(DATA_DIR / "dashboard_diagnoses.csv")

st.title("Healthcare Analytics Dashboard")
st.caption("Synthetic data example for healthcare informatics and data engineering workflows.")

patient_encounters = encounters.merge(patients, on="patient_id", how="left")

diagnosis_summary = diagnoses["diagnosis_description"].value_counts().reset_index()
diagnosis_summary.columns = ["diagnosis_description", "count"]

st.sidebar.header("Filters")
encounter_types = sorted(patient_encounters["encounter_type"].unique())
selected_encounter_types = st.sidebar.multiselect(
    "Encounter type",
    encounter_types,
    default=encounter_types
)

sex_options = sorted(patient_encounters["sex"].dropna().unique())
selected_sex = st.sidebar.multiselect(
    "Sex",
    sex_options,
    default=sex_options
)

filtered = patient_encounters[
    patient_encounters["encounter_type"].isin(selected_encounter_types)
    & patient_encounters["sex"].isin(selected_sex)
]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients", patients["patient_id"].nunique())
col2.metric("Total Encounters", len(filtered))
col3.metric("Average LOS", round(filtered["length_of_stay_days"].mean(), 2))
col4.metric("Inpatient Encounters", int((filtered["encounter_type"] == "inpatient").sum()))

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Encounters by Type")
    st.bar_chart(filtered["encounter_type"].value_counts())

with right:
    st.subheader("Age Distribution")
    st.bar_chart(filtered["age"].value_counts().sort_index())

st.divider()

left2, right2 = st.columns(2)

with left2:
    st.subheader("Diagnosis Frequency")
    st.dataframe(diagnosis_summary, use_container_width=True)

with right2:
    st.subheader("Patient Utilization")
    utilization = (
        filtered.groupby(["patient_id", "sex", "race", "age"])
        .agg(
            total_encounters=("encounter_id", "count"),
            total_los_days=("length_of_stay_days", "sum")
        )
        .reset_index()
        .sort_values("total_encounters", ascending=False)
    )
    st.dataframe(utilization, use_container_width=True)

st.divider()

st.subheader("Filtered Encounter-Level Data")
st.dataframe(filtered, use_container_width=True)

st.caption("Synthetic healthcare data only. No PHI.")
