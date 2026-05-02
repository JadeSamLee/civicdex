# =========================================
# CivicDex AI Dashboard (Production Ready)
# Multilingual Civic Routing System
# =========================================

import os
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix
from routing import get_department

# -----------------------------
# SAFE PATH CONFIG (DEPLOYMENT SAFE)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "baselines", "civicdex_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "data", "civicdex_test.csv")

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="CivicDex AI", layout="wide")

st.title("CivicDex: Civic AI Routing System")
st.markdown("Multilingual civic request classification and intelligent department routing system.")

# -----------------------------
# SAFE MODEL LOADING
# -----------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except:
        return None

model = load_model()

# -----------------------------
# SAFE DATA LOADING
# -----------------------------
@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except:
        return pd.DataFrame(columns=["normalized_text", "intent", "language_type"])

df = load_data()

TEXT_COL = "normalized_text"
LABEL_COL = "intent"

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Live Prediction", "Analytics Dashboard", "Model Evaluation"]
)

# =====================================================
# LIVE PREDICTION
# =====================================================
if menu == "Live Prediction":

    st.header("Citizen Request Analysis")

    user_input = st.text_area("Enter civic complaint (Tamil / Tanglish / English)")

    if st.button("Analyze Request"):

        if not user_input.strip():
            st.warning("Please enter a valid request.")
        else:

            if model is None:
                st.error("Model not found. Please ensure civicdex_model.pkl is trained and placed correctly.")
            else:
                try:
                    pred = model.predict([user_input])[0]
                except:
                    pred = "unknown"

                dept = get_department(pred, user_input)

                col1, col2 = st.columns(2)

                with col1:
                    st.success(f"Predicted Intent: {pred}")

                with col2:
                    st.info(f"Assigned Department: {dept}")

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================
elif menu == "Analytics Dashboard":

    st.header("Dataset & Routing Analytics")

    if df.empty:
        st.warning("Dataset not found or empty.")
    else:

        # Predictions
        if model:
            try:
                df["prediction"] = model.predict(df[TEXT_COL].astype(str))
            except:
                df["prediction"] = "error"
        else:
            df["prediction"] = "no_model"

        df["department"] = df.apply(
            lambda r: get_department(r["prediction"], str(r[TEXT_COL])),
            axis=1
        )

        # -----------------------------
        # INTENT DISTRIBUTION
        # -----------------------------
        st.subheader("Intent Distribution")

        fig1, ax1 = plt.subplots()
        df[LABEL_COL].value_counts().plot(kind="bar", ax=ax1)
        st.pyplot(fig1)

        # -----------------------------
        # PREDICTION DISTRIBUTION
        # -----------------------------
        st.subheader("Prediction Distribution")

        fig2, ax2 = plt.subplots()
        df["prediction"].value_counts().plot(kind="bar", ax=ax2)
        st.pyplot(fig2)

        # -----------------------------
        # ROUTING DISTRIBUTION
        # -----------------------------
        st.subheader("Department Routing Distribution")

        fig3, ax3 = plt.subplots()
        df["department"].value_counts().plot(kind="bar", ax=ax3)
        st.pyplot(fig3)

        # -----------------------------
        # SAMPLE DATA
        # -----------------------------
        st.subheader("Sample Data")

        st.dataframe(df[[TEXT_COL, LABEL_COL, "prediction", "department"]].head(10))

# =====================================================
# MODEL EVALUATION
# =====================================================
elif menu == "Model Evaluation":

    st.header("Model Performance Insights")

    if df.empty or model is None:
        st.warning("Model or dataset not available.")
    else:

        try:
            y_true = df[LABEL_COL]
            y_pred = df["prediction"]

            st.subheader("Classification Report")

            report = classification_report(y_true, y_pred, output_dict=True)
            st.dataframe(pd.DataFrame(report).transpose())

            st.subheader("Confusion Matrix")

            labels = sorted(y_true.unique())
            cm = confusion_matrix(y_true, y_pred, labels=labels)

            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt="d",
                        xticklabels=labels,
                        yticklabels=labels,
                        cmap="Blues")

            st.pyplot(fig)

        except:
            st.error("Evaluation failed due to insufficient or inconsistent data.")