import streamlit as st
import pandas as pd
import joblib
import os
from preprocessing import prepareData

st.set_page_config(
    page_title="Machine Learning Model",
    layout="wide",
    page_icon="🧠"
)

st.title("Model Prediction")

model_path = os.path.join(os.path.dirname(__file__), '../model.pkl')

# Load the trained model
model = joblib.load(model_path)

# Toggle between prediction modes
prediction_mode = st.radio(
    "Select Prediction Mode",
    ("Single Prediction", "Batch Prediction (File Upload)", "Batch Prediction (Manual Input)")
)

if prediction_mode == "Single Prediction":
    st.sidebar.subheader("Input Customer Details to Predict Churn")

    # Collect user inputs for the relevant features
    senior_citizen = st.sidebar.selectbox("Senior Citizen", ("Yes", "No"))
    partner = st.sidebar.selectbox("Partner", ("Yes", "No"))
    dependents = st.sidebar.selectbox("Dependents", ("Yes", "No"))
    tenure = st.sidebar.slider("Tenure (months)", 0, 72, 1)
    internet_service = st.sidebar.selectbox("Internet Service", ("DSL", "Fiber optic", "No"))
    online_security = st.sidebar.selectbox("Online Security", ("Yes", "No"))
    contract = st.sidebar.selectbox("Contract", ("Month-to-month", "One year", "Two year"))
    payment_method = st.sidebar.selectbox("Payment Method", ("Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"))
    monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=18.25, step=0.5, max_value=118.75)

    # Prepare input data for prediction
    input_data = {
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "Contract": contract,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": monthly_charges * tenure,
    }

    input_df = pd.DataFrame([input_data])

    # Display input data
    st.subheader("Customer Details")
    st.write(input_df)

    # Predict churn for the single input
    if st.button("Predict"):
        df = input_df.copy()
        df['Churn'] = 0  # Placeholder for churn, not used in prediction
        df["SeniorCitizen"] = df["SeniorCitizen"].apply(lambda x: 1 if x == "Yes" else 0)
        X, _ = prepareData(df)  # Preprocess the input data
        y_pred = model.predict(X)  # Using the model pipeline to predict
        print(y_pred)
        churn_result = "Yes" if y_pred == 1 else "No"

        # Highlighted Prediction Display
        if churn_result == "Yes":
            st.markdown(f"<h2 style='color: red; text-align: center;'>🚨 Prediction: The customer will churn! 🚨</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color: green; text-align: center;'>✅ Prediction: The customer will NOT churn ✅</h2>", unsafe_allow_html=True)

elif prediction_mode == "Batch Prediction (File Upload)":
    st.subheader("Upload Batch Data for Prediction")

    # Upload a CSV file for batch prediction
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        batch_data = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.subheader("Uploaded Data")
        st.write(batch_data)

        # Check if required columns are present
        required_columns = [
            "SeniorCitizen", "Partner", "Dependents", "tenure", "InternetService",
            "OnlineSecurity",  "Contract", "PaymentMethod", "MonthlyCharges", "TotalCharges"
        ]

        if all(column in batch_data.columns for column in required_columns):
            # Predict churn for the batch input using the model pipeline
            if st.button("Predict Batch"):
                batch_data["Churn"] = 0  # Placeholder for churn, not used in prediction
                batch_data["SeniorCitizen"] = batch_data["SeniorCitizen"].apply(lambda x: 1 if x == "Yes" else 0)
                X, _ = prepareData(batch_data)  # Preprocess the input data
                predictions = model.predict(X)
                batch_data = batch_data.drop(columns=["Churn"])  # Remove placeholder churn column
                batch_data["Churn_Prediction"] = ["Yes" if pred == 1 else "No" for pred in predictions]

                st.subheader("Prediction Results")
                st.write(batch_data)

                # Option to download results
                csv = batch_data.to_csv(index=False).encode('utf-8')
                st.download_button("Download Predictions", data=csv, file_name="predictions.csv", mime="text/csv")
        else:
            st.write("Error: Uploaded CSV does not contain all required columns.")

elif prediction_mode == "Batch Prediction (Manual Input)":
    st.subheader("Manual Input for Batch Prediction")

    # Set the number of rows for manual batch input
    num_rows = st.number_input("Number of Customers to Input", min_value=1, max_value=100, step=1, value=1)

    # Create an empty list to collect manual input data
    manual_data_list = []

    # Loop to collect inputs for each customer
    for i in range(num_rows):
        st.markdown(f"**Customer {i + 1} Details**")
        senior_citizen = st.selectbox(f"Senior Citizen (Customer {i + 1})", ("Yes", "No"), key=f"senior_citizen_{i}")
        partner = st.selectbox(f"Partner (Customer {i + 1})", ("Yes", "No"), key=f"partner_{i}")
        dependents = st.selectbox(f"Dependents (Customer {i + 1})", ("Yes", "No"), key=f"dependents_{i}")
        tenure = st.slider(f"Tenure (Customer {i + 1})", 0, 72, 1, key=f"tenure_{i}")
        internet_service = st.selectbox(f"Internet Service (Customer {i + 1})", ("DSL", "Fiber optic", "No"), key=f"internet_service_{i}")
        online_security = st.selectbox(f"Online Security (Customer {i + 1})", ("Yes", "No"), key=f"online_security_{i}")
        contract = st.selectbox(f"Contract (Customer {i + 1})", ("Month-to-month", "One year", "Two year"), key=f"contract_{i}")
        payment_method = st.selectbox(f"Payment Method (Customer {i + 1})", ("Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"), key=f"payment_method_{i}")
        monthly_charges = st.number_input(f"Monthly Charges (Customer {i + 1})", min_value=18.25, step=0.5, max_value=118.75, key=f"monthly_charges_{i}")
        total_charges = monthly_charges * tenure
        churn = 0  # Placeholder for churn, not used in prediction

        # Append customer data to the list
        manual_data_list.append({
            "SeniorCitizen": senior_citizen,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "InternetService": internet_service,
            "OnlineSecurity": online_security,
            "Contract": contract,
            "PaymentMethod": payment_method,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": monthly_charges * tenure,
            "Churn": churn
        })

    # Convert the list of dictionaries to a DataFrame
    manual_data = pd.DataFrame(manual_data_list)

    st.subheader("Manual Batch Data")
    st.write(manual_data)

    # Predict churn for the manual batch input
    if st.button("Predict Batch (Manual)"):
        df = manual_data.copy()
        df["SeniorCitizen"] = df["SeniorCitizen"].apply(lambda x: 1 if x == "Yes" else 0)
        X, _ = prepareData(df)  # Preprocess the input data
        predictions = model.predict(X)  # Using the model pipeline to predict
        manual_data = manual_data.drop(columns=["Churn"])  # Remove placeholder churn column
        manual_data["Churn_Prediction"] = ["Yes" if pred == 1 else "No" for pred in predictions]

        st.subheader("Prediction Results")
        st.write(manual_data)
