import streamlit as st
import pandas as pd

def load_data():
    uploaded_file = st.file_uploader("Upload a dataset", type=["csv", "xlsx", "json"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            return pd.read_json(uploaded_file)
    return None

st.title("Upload Dataset")
data = load_data()

if data is not None:
    st.write("Dataset uploaded successfully!")
    st.dataframe(data.head())
