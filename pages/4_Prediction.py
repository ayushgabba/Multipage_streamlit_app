import streamlit as st
import pandas as pd

# Check if dataset and model exist
if 'uploaded_data' in st.session_state and 'trained_model' in st.session_state:
    model = st.session_state['trained_model']
    data = st.session_state['uploaded_data']
    st.write("Model and dataset loaded for prediction.")
else:
    st.write("Please train a model first.")
    st.stop()

# Select features for prediction
features = data.drop(columns=[target]).columns
input_data = st.text_input("Enter input data for prediction (comma separated):")

if input_data:
    input_values = list(map(float, input_data.split(',')))
    prediction = model.predict([input_values])
    st.write(f"Prediction: {prediction[0]}")
