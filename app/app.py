# =========================================
# CivicDex AI Dashboard (Stable Production Version)
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
# OPTIONAL NETWORKX (SAFE IMPORT)
# -----------------------------
try:
    import networkx as nx
    HAS_NX = True
except:
    HAS_NX = False

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="CivicDex AI Dashboard", layout="wide")

st.title("CivicDex: Civic AI Routing System")
st.markdown("Multilingual civic request classification + routing intelligence")

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "baselines", "civicdex_model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "data", "civicdex_test.csv")

# -----------------------------
# MODEL
# -----------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except:
        return None

model = load_model()

# -----------------------------
# DATA
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

    user_input = st.text_area("Enter civic request")

    if st.button("Analyze"):

        if not user_input.strip():
            st.warning("Enter valid request")
        else:

            if model:
                try:
                    pred = model.predict([user_input])[0]
                except:
                    pred = "unknown"
            else:
                pred = "model_not_loaded"

            dept = get_department(pred, user_input)

            col1, col2 = st.columns(2)

            col1.metric("Predicted Intent", pred)
            col2.metric("Department", dept)

# =====================================================
# ANALYTICS DASHBOARD (CLEAN + SAFE)
# =====================================================
elif menu == "Analytics Dashboard":

    st.header("System Analytics")

    if df.empty:
        st.warning("Dataset not found")
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
        # KPI ROW (FIXED)
        # -----------------------------
        c1, c2, c3 = st.columns(3)

        c1.metric("Total Requests", len(df))
        c2.metric("Unique Intents", df["prediction"].nunique())
        c3.metric("Departments", df["department"].nunique())

        st.markdown("---")

        # -----------------------------
        # INTENT DISTRIBUTION
        # -----------------------------
        st.subheader("Intent Distribution")

        fig, ax = plt.subplots()
        df["prediction"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

        # -----------------------------
        # DEPARTMENT DISTRIBUTION
        # -----------------------------
        st.subheader("Department Routing")

        fig, ax = plt.subplots()
        df["department"].value_counts().plot(kind="barh", ax=ax)
        st.pyplot(fig)

        # -----------------------------
        # HEATMAP (SAFE)
        # -----------------------------
        st.subheader("Intent → Department Heatmap")

        try:
            pivot = pd.crosstab(df["prediction"], df["department"])

            if pivot.shape[0] > 1 and pivot.shape[1] > 1:
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.heatmap(pivot, cmap="Blues", ax=ax)
                st.pyplot(fig)
            else:
                st.info("Not enough variation for heatmap")

        except:
            st.info("Heatmap unavailable")

        # -----------------------------
        # ROUTING GRAPH (FIXED)
        # -----------------------------
        st.subheader("Routing Flow Graph")

        if HAS_NX:

            try:
                G = nx.DiGraph()

                sample = df.dropna().head(150)

                for _, row in sample.iterrows():
                    if row["prediction"] and row["department"]:
                        G.add_edge(row["prediction"], row["department"])

                if len(G.nodes) > 0:

                    fig, ax = plt.subplots(figsize=(10, 6))
                    pos = nx.spring_layout(G, seed=42)

                    nx.draw(
                        G,
                        pos,
                        with_labels=True,
                        node_size=1800,
                        node_color="#AED6F1",
                        arrows=True,
                        font_size=8,
                        ax=ax
                    )

                    st.pyplot(fig)
                else:
                    st.info("No graph data available")

            except:
                st.info("Graph rendering failed")

        else:
            st.warning("Network graph disabled (networkx not installed)")

        # -----------------------------
        # SAMPLE DATA
        # -----------------------------
        st.subheader("Sample Output")

        st.dataframe(df[[TEXT_COL, "prediction", "department"]].head(15))

# =====================================================
# MODEL EVALUATION (FIXED SAFE MODE)
# =====================================================
elif menu == "Model Evaluation":

    st.header("Model Evaluation")

    if df.empty or model is None:
        st.warning("No evaluation available")
    else:

        try:
            y_true = df[LABEL_COL]
            y_pred = df["prediction"]

            # -----------------------------
            # SAFE CHECK
            # -----------------------------
            if len(set(y_true)) < 2 or len(set(y_pred)) < 2:
                st.warning("Not enough class variation for evaluation.")
            else:

                st.subheader("Classification Report")

                report = classification_report(
                    y_true,
                    y_pred,
                    output_dict=True,
                    zero_division=0
                )

                st.dataframe(pd.DataFrame(report).transpose())

                st.subheader("Confusion Matrix")

                labels = sorted(list(set(y_true) | set(y_pred)))

                cm = confusion_matrix(y_true, y_pred, labels=labels)

                fig, ax = plt.subplots()
                sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                            xticklabels=labels,
                            yticklabels=labels,
                            ax=ax)

                st.pyplot(fig)

        except:
            st.warning("Evaluation not available for current dataset")