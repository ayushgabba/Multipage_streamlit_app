import streamlit as st

st.title("View Dataset")

# This assumes that the dataset was saved globally or via session state
if 'uploaded_data' in st.session_state:
    st.dataframe(st.session_state['uploaded_data'].head())
else:
    st.write("No dataset uploaded yet.")
