import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Health Data Explorer", layout="wide")

st.title("Health Data Explorer App")
st.caption("Upload and explore synthetic, public, or de-identified health datasets.")

DATA_DIR = Path(__file__).parent / "data"
sample_path = DATA_DIR / "sample_health_metrics.csv"

st.sidebar.header("Data Source")
use_sample = st.sidebar.checkbox("Use sample dataset", value=True)

uploaded_file = st.sidebar.file_uploader("Or upload a CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif use_sample:
    df = pd.read_csv(sample_path)
else:
    st.info("Upload a CSV or select the sample dataset.")
    st.stop()

st.subheader("Data Preview")
st.dataframe(df.head(20), use_container_width=True)

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isna().sum().sum()))

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Column Types")
    dtype_df = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns]
    })
    st.dataframe(dtype_df, use_container_width=True)

with right:
    st.subheader("Missingness by Column")
    missing_df = df.isna().sum().reset_index()
    missing_df.columns = ["column", "missing_count"]
    st.dataframe(missing_df, use_container_width=True)

st.divider()

numeric_cols = df.select_dtypes(include="number").columns.tolist()

if numeric_cols:
    st.subheader("Numeric Column Explorer")
    selected_metric = st.selectbox("Select numeric metric", numeric_cols)
    st.bar_chart(df[selected_metric])

    st.subheader("Summary Statistics")
    st.dataframe(df[numeric_cols].describe(), use_container_width=True)

st.divider()

st.subheader("Simple Filter")

filter_col = st.selectbox("Choose column to filter", df.columns)
unique_values = df[filter_col].dropna().unique().tolist()

if len(unique_values) <= 50:
    selected_values = st.multiselect(
        f"Select values for {filter_col}",
        unique_values,
        default=unique_values
    )
    filtered = df[df[filter_col].isin(selected_values)]
else:
    filtered = df

st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered CSV",
    data=csv,
    file_name="filtered_health_data.csv",
    mime="text/csv"
)

st.caption("Educational app. Do not upload protected health information.")
