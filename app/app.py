# =========================================
# CivicDex Streamlit Application
# Multilingual Civic AI System
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix

from routing import get_department

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="CivicDex AI", layout="wide")

st.title("CivicDex: Multilingual Civic AI Assistant")

st.markdown("""
This system classifies civic-service requests in Tamil, Tanglish, and English,
and routes them to the correct municipal department.
""")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("baselines/civicdex_model.pkl")

model = load_model()

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/civicdex_test.csv")

df = load_data()

TEXT_COL = "normalized_text"
LABEL_COL = "intent"

X_test = df[TEXT_COL].astype(str)
y_test = df[LABEL_COL]

# -----------------------------
# Navigation
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Live Prediction", "Model Performance", "Dataset Insights"]
)

# =====================================================
# LIVE PREDICTION
# =====================================================
if menu == "Live Prediction":
    st.header("Civic Request Classification")

    user_input = st.text_area("Enter civic complaint (Tamil / Tanglish / English)")

    if st.button("Predict"):
        if user_input.strip():

            pred = model.predict([user_input])[0]
            dept = get_department(pred, user_input)

            st.success(f"Predicted Intent: {pred}")
            st.info(f"Assigned Department: {dept}")

# =====================================================
# MODEL PERFORMANCE
# =====================================================
elif menu == "Model Performance":
    st.header("Model Evaluation Dashboard")

    y_pred = model.predict(X_test)

    acc = np.mean(y_pred == y_test)

    st.metric("Accuracy", f"{acc:.2f}")

    st.subheader("Classification Report")

    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(pd.DataFrame(report).transpose())

    st.subheader("Confusion Matrix")

    labels = sorted(df[LABEL_COL].unique())
    cm = confusion_matrix(y_test, y_pred, labels=labels)

    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d",
                xticklabels=labels,
                yticklabels=labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    st.pyplot(fig)

# =====================================================
# DATASET INSIGHTS
# =====================================================
elif menu == "Dataset Insights":
    st.header("Dataset Analytics")

    st.subheader("Intent Distribution")

    fig1, ax1 = plt.subplots()
    df[LABEL_COL].value_counts().plot(kind="bar", ax=ax1)
    st.pyplot(fig1)

    st.subheader("Sample Data")
    st.dataframe(df.head(10))