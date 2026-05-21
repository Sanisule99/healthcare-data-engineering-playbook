import streamlit as st
import pandas as pd

st.title('Healthcare Dashboard Starter')
st.caption('Synthetic or public-use data only. Do not upload PHI.')

uploaded_file = st.file_uploader('Upload a healthcare CSV', type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write('Data preview')
    st.dataframe(df.head())
    st.write('Shape:', df.shape)
