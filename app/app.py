# =========================================
# CivicDex AI Dashboard (Production UI Upgrade)
# =========================================

import os
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

from sklearn.metrics import classification_report, confusion_matrix
from routing import get_department

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="CivicDex AI Dashboard",
    layout="wide"
)

st.title("CivicDex: Civic AI Routing System")
st.markdown("Multilingual civic request classification and intelligent routing system")

# -----------------------------
# SAFE PATHS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "baselines", "civicdex_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "data", "civicdex_test.csv")

# -----------------------------
# LOAD MODEL
# -----------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except:
        return None

model = load_model()

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except:
        return pd.DataFrame()

df = load_data()

TEXT_COL = "normalized_text"
LABEL_COL = "intent"

# -----------------------------
# SIDEBAR
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Live Prediction", "Analytics Dashboard", "Model Evaluation"]
)

# =====================================================
# LIVE PREDICTION
# =====================================================
if menu == "Live Prediction":

    st.header("Citizen Request Analyzer")

    user_input = st.text_area("Enter civic request (Tamil / Tanglish / English)")

    if st.button("Analyze"):

        if not user_input.strip():
            st.warning("Please enter a valid request.")
        else:

            if model:
                try:
                    pred = model.predict([user_input])[0]
                except:
                    pred = "unknown"
            else:
                pred = "model_not_found"

            dept = get_department(pred, user_input)

            col1, col2 = st.columns(2)

            with col1:
                st.success(f"Intent: {pred}")

            with col2:
                st.info(f"Department: {dept}")

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================
elif menu == "Analytics Dashboard":

    st.header("Civic System Analytics")

    if df.empty:
        st.warning("No dataset found")
    else:

        # -----------------------------
        # SAFE PREDICTIONS
        # -----------------------------
        if model:
            try:
                df["prediction"] = model.predict(df[TEXT_COL].astype(str))
            except:
                df["prediction"] = "unknown"
        else:
            df["prediction"] = "unknown"

        df["department"] = df.apply(
            lambda r: get_department(r["prediction"], str(r[TEXT_COL])),
            axis=1
        )

        # -----------------------------
        # KPI ROW
        # -----------------------------
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Requests", len(df))
        col2.metric("Unique Intents", df["prediction"].nunique())
        col3.metric("Departments", df["department"].nunique())

        st.markdown("---")

        # -----------------------------
        # INTENT DISTRIBUTION
        # -----------------------------
        st.subheader("Intent Distribution")

        fig, ax = plt.subplots()
        df["prediction"].value_counts().plot(kind="bar", ax=ax)
        ax.set_ylabel("Count")
        st.pyplot(fig)

        # -----------------------------
        # DEPARTMENT DISTRIBUTION
        # -----------------------------
        st.subheader("Department Routing Distribution")

        fig, ax = plt.subplots()
        df["department"].value_counts().plot(kind="barh", ax=ax)
        st.pyplot(fig)

        # -----------------------------
        # HEATMAP (IMPORTANT)
        # -----------------------------
        st.subheader("Intent → Department Heatmap")

        try:
            pivot = pd.crosstab(df["prediction"], df["department"])
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.heatmap(pivot, cmap="YlGnBu", ax=ax)
            st.pyplot(fig)
        except:
            st.info("Heatmap not available")

        # -----------------------------
        # ROUTING GRAPH (SYSTEM VIEW)
        # -----------------------------
        st.subheader("Civic Routing Flow Graph")

        try:
            G = nx.DiGraph()

            for i in range(min(len(df), 200)):
                G.add_edge(df["prediction"].iloc[i], df["department"].iloc[i])

            fig, ax = plt.subplots(figsize=(10, 6))
            pos = nx.spring_layout(G, seed=42)

            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="#A9CCE3",
                node_size=2000,
                font_size=8,
                arrows=True,
                ax=ax
            )

            st.pyplot(fig)

        except:
            st.info("Graph not available")

        # -----------------------------
        # SAMPLE TABLE
        # -----------------------------
        st.subheader("Sample Predictions")

        st.dataframe(df[[TEXT_COL, "prediction", "department"]].head(15))

# =====================================================
# MODEL EVALUATION
# =====================================================
elif menu == "Model Evaluation":

    st.header("Model Performance")

    if df.empty or model is None:
        st.warning("No evaluation available")
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
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                        xticklabels=labels,
                        yticklabels=labels,
                        ax=ax)

            st.pyplot(fig)

        except:
            st.error("Evaluation failed")