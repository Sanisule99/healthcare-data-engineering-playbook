import streamlit as st
import pandas as pd

st.title("Healthcare Data Engineering Playbook")

patients = pd.read_csv("data/generated/patients.csv")

st.subheader("Patient Dataset")
st.dataframe(patients.head())

st.subheader("Patient Sex Distribution")
st.bar_chart(patients["sex"].value_counts())