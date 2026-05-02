import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="CivicDex AI",
    layout="wide"
)

st.title("CivicDex: Multilingual Civic AI Assistant")

st.markdown(
    """
This system classifies civic-service requests written in Tamil, Tanglish, and code-mixed language.
It performs intent classification shows real-world civic routing workflows.
"""
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load("baselines/model.pkl")

model = load_model()

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/civicdex_test.csv")
    return df

df = load_data()

TEXT_COL = "normalized_text"
LABEL_COL = "intent"

X_test = df[TEXT_COL].astype(str)
y_test = df[LABEL_COL]

# -----------------------------
# Sidebar Navigation
# -----------------------------
option = st.sidebar.radio(
    "Navigation",
    ["Live Prediction", "Model Performance", "Dataset Insights"]
)

# =====================================================
# TAB 1: LIVE PREDICTION
# =====================================================
if option == "Live Prediction":
    st.header("Live Civic Request Classification")

    user_input = st.text_area(
        "Enter civic complaint (Tamil / Tanglish / English):"
    )

    if st.button("Predict"):
        if user_input.strip() != "":
            pred = model.predict([user_input])[0]

            st.success(f"Predicted Intent: {pred}")

            # Simple routing logic (demo layer)
            routing_map = {
                "complaint": "Municipal Grievance Cell",
                "status_query": "Service Tracking Department",
                "follow_up": "Complaint Resolution Unit",
                "information_request": "Citizen Information Center",
                "escalation": "Senior Municipal Officer"
            }

            dept = routing_map.get(pred, "General Services")

            st.info(f"Suggested Department: {dept}")

# =====================================================
# TAB 2: MODEL PERFORMANCE
# =====================================================
elif option == "Model Performance":
    st.header("Model Evaluation Dashboard")

    y_pred = model.predict(X_test)

    acc = np.mean(y_pred == y_test)

    st.metric("Accuracy", f"{acc:.2f}")

    st.subheader("Classification Report")

    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()

    st.dataframe(report_df)

    st.subheader("Confusion Matrix")

    labels = sorted(df[LABEL_COL].unique())

    cm = confusion_matrix(y_test, y_pred, labels=labels)

    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    st.pyplot(fig)

# =====================================================
# TAB 3: DATASET INSIGHTS
# =====================================================
elif option == "Dataset Insights":
    st.header("Dataset Analytics")

    st.subheader("Intent Distribution")

    fig1, ax1 = plt.subplots()
    df[LABEL_COL].value_counts().plot(kind="bar", ax=ax1)
    st.pyplot(fig1)

    st.subheader("Language Type Distribution (if available)")

    if "language_type" in df.columns:
        fig2, ax2 = plt.subplots()
        df["language_type"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2)
        st.pyplot(fig2)

    st.subheader("Sample Data")

    st.dataframe(df.head(10))