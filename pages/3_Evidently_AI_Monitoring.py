import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import pandas as pd

# Check if dataset exists
if 'uploaded_data' in st.session_state:
    data = st.session_state['uploaded_data']
    st.write("Dataset loaded for model training.")
else:
    st.write("Please upload a dataset first.")
    st.stop()

# Selecting target variable
target = st.selectbox("Select target variable", data.columns)

# Splitting data into features and target
X = data.drop(columns=[target])
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Model evaluation
st.write(f"Model trained with an accuracy of: {model.score(X_test, y_test):.2f}")

# Evidently AI Dashboard
dashboard = Dashboard(tabs=[DataDriftTab()])
dashboard.calculate(X_train, X_test, y_train, y_test)
dashboard.save("/tmp/dashboard")
st.write("Evidently AI dashboard generated.")
st.markdown(f'<iframe src="file:///tmp/dashboard" width="800" height="600"></iframe>', unsafe_allow_html=True)
