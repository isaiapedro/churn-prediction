import streamlit as st
import joblib
import numpy as np
import pandas as pd
import preprocessing as prep

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please enter the values and hit predict")

st.divider()

age = st.number_input("Enter age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter tenure", min_value=0, max_value=130, value=10)

monthlycharge = st.number_input("Enter monthly charge", min_value=30, max_value=150)

gender = st.selectbox("Enter the gender", ["Male", "Female"])

contracttype = st.selectbox("Enter contract type", ["Month-to-Month", "One-Year", "Two-Year"])

internetservice = st.selectbox("Enter internet service", ["None", "DSL", "Fiber Optic"])

techsupport = st.selectbox("Tech Support?", ["Yes", "No"])

st.divider()

predictButton = st.button("Predict")

st.divider()

if predictButton:
    input_data = {
        'Age': age,
        'Gender': gender,
        'Tenure': tenure,
        'MonthlyCharges': monthlycharge,
        'ContractType': contracttype,
        'InternetService': internetservice,
        'TechSupport': techsupport
    }
    
    input_df = pd.DataFrame([input_data])
    
    input_df['Churn'] = 'No'

    X_processed, _ = prep.prepareData(input_df)

    X_scaled = scaler.transform(X_processed)

    prediction = model.predict(X_scaled)[0]
    prediction_proba = model.predict_proba(X_scaled)[0]

    st.balloons()

    if prediction == 1:
        st.error(f"**Predição: Churn** (Cancelamento Provável)")
        st.write(f"Probabilidade de Churn: **{prediction_proba[1]:.2%}**")
    else:
        st.success(f"**Predição: Não Churn** (Cliente Fiel)")
        st.write(f"Probabilidade de Permanência: **{prediction_proba[0]:.2%}**")

else:
    st.write("Please enter the values and use predict button")