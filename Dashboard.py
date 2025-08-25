# tcc.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Telco Customer Churn Dashboard", layout="wide")
# --- Custom CSS Styling ---
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .main-title {
            background-color: #636EFA;
            padding: 20px;
            border-radius: 8px;
            color: white;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        footer {visibility: hidden;}

    background-color: #f4f4f4;

    </style>
""", unsafe_allow_html=True)


# Load dataset
df = pd.read_csv("cleaned_data.csv")
df.columns = df.columns.str.strip().str.lower()

# Convert churn to numeric
df['churn_numeric'] = df['churn'].map({'Yes': 1, 'No': 0})

# Sidebar Filters
st.sidebar.title("🔍 Filter Customers")
with st.sidebar.expander("Filter Options", expanded=True):
    senior = st.selectbox("Senior Citizen", ("All", "Yes", "No"))
    partner = st.selectbox("Partner", ("All", "Yes", "No"))
    internet = st.selectbox("Internet Service", ("All", "DSL", "Fiber optic", "No"))
    payment_method = st.selectbox("Payment Method", ("All", "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"))

# Apply filters
filtered_df = df.copy()
if senior != "All":
    senior_mapped = 1 if senior == "Yes" else 0
    filtered_df = filtered_df.query('seniorcitizen==@senior_mapped')
if partner != "All":
    filtered_df = filtered_df.query('partner==@partner')
if internet != "All":
    filtered_df = filtered_df.query('internetservice==@internet')
if payment_method != "All":
    filtered_df = filtered_df.query('paymentmethod==@payment_method')

# KPIs
churn_rate = filtered_df['churn_numeric'].mean()
total_customers = filtered_df.shape[0]

st.markdown('<div class="main-title">📉 Telco Customer Churn Dashboard</div>', unsafe_allow_html=True)
kpi1, kpi2 = st.columns(2)
kpi1.metric("🔁 Churn Rate", f"{churn_rate:.2%}")
kpi2.metric("👥 Total Customers", f"{total_customers:,}")

st.markdown("---")

# 📊 Visual 1: Contract Type vs Churn
st.subheader("📊 Churn by Contract Type")
fig1 = px.histogram(filtered_df, x="contract", color="churn", barmode="group", title="Churn by Contract Type")
st.plotly_chart(fig1, use_container_width=True)

# 💳 Payment Method vs Churn
st.subheader("💳 Churn by Payment Method")
fig5 = px.histogram(filtered_df, x="paymentmethod", color="churn", barmode="group", title="Churn by Payment Method")
st.plotly_chart(fig5, use_container_width=True)

# 🕒 Tenure Distribution
st.subheader("🕒 Tenure Distribution by Churn")
fig2 = px.histogram(filtered_df, x="tenure", nbins=30, color="churn", title="Tenure Distribution")
st.plotly_chart(fig2, use_container_width=True)

# 💰 Monthly vs Total Charges
st.subheader("💰 Monthly Charges vs Total Charges")
fig3 = px.scatter(filtered_df, x="monthlycharges", y="totalcharges", color="churn", title="Charges Comparison")
st.plotly_chart(fig3, use_container_width=True)

# 🌐 Internet Service vs Churn
st.subheader("🌐 Internet Service Type vs Churn")
fig4 = px.histogram(filtered_df, x="internetservice", color="churn", barmode="group", title="Internet Service Breakdown")
st.plotly_chart(fig4, use_container_width=True)

# 🔁 Correlation Heatmap
st.subheader("📌 Correlation Heatmap (Numeric)")
corr_df = filtered_df.select_dtypes(include='number').corr()
fig6 = px.imshow(corr_df, text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig6, use_container_width=True)

# 📎 Show Data
with st.expander("📋 Show Filtered Data"):
    st.dataframe(filtered_df)
