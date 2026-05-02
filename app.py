import streamlit as st
import joblib
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="CivicDex AI Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
MODEL_PATH = os.path.join("baselines", "model.pkl")
model = joblib.load(MODEL_PATH)

# -----------------------------
# TITLE
# -----------------------------
st.title("CivicDex: Multilingual Civic AI System")
st.write("AI-powered civic request understanding for Tamil and code-mixed inputs")

# -----------------------------
# SIDEBAR - INFO
# -----------------------------
st.sidebar.title("System Overview")
st.sidebar.write("""
CivicDex classifies citizen complaints and routes them
to appropriate departments using NLP.
""")

# -----------------------------
# INPUT SECTION
# -----------------------------
st.header("Citizen Request Input")

user_input = st.text_area("Enter your civic complaint (Tamil / Tanglish / English)")

# -----------------------------
# LABEL MAPS
# -----------------------------
category_map = {
    "complaint": "General Civic Issue",
    "status_query": "Application Status",
    "follow_up": "Follow-up Request",
    "information_request": "Information Service",
    "escalation": "Urgent Escalation",
    "request": "Service Request"
}

department_map = {
    "complaint": "Municipal Corporation",
    "status_query": "Citizen Services Portal",
    "follow_up": "Concerned Department",
    "information_request": "Help Desk",
    "escalation": "Senior Officer Cell",
    "request": "Service Desk"
}

urgency_map = {
    "complaint": "Medium",
    "status_query": "Low",
    "follow_up": "Medium",
    "information_request": "Low",
    "escalation": "High",
    "request": "Medium"
}

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("Analyze Request"):

    if user_input.strip() == "":
        st.warning("Please enter a request.")
    else:

        pred = model.predict([user_input])[0]
        prob = model.predict_proba([user_input]).max()

        st.subheader("Prediction Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Intent", pred)

        with col2:
            st.metric("Confidence", f"{prob:.2f}")

        with col3:
            st.metric("Urgency", urgency_map.get(pred, "Medium"))

        st.write("### Routing Information")
        st.write(f"Category: {category_map.get(pred)}")
        st.write(f"Department: {department_map.get(pred)}")

# -----------------------------
# DATA INSIGHTS SECTION
# -----------------------------
st.markdown("---")
st.header("Dataset Insights Dashboard")

# Simulated distribution (replace with your real CSV if needed)
data = {
    "intent": ["complaint", "follow_up", "status_query", "information_request", "escalation"],
    "count": [352, 115, 66, 23, 25]
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

# -----------------------------
# PIE CHART
# -----------------------------
with col1:
    st.subheader("Intent Distribution")

    fig1, ax1 = plt.subplots()
    ax1.pie(df["count"], labels=df["intent"], autopct="%1.1f%%")
    st.pyplot(fig1)

# -----------------------------
# BAR CHART
# -----------------------------
with col2:
    st.subheader("Class Balance")

    fig2, ax2 = plt.subplots()
    sns.barplot(data=df, x="intent", y="count", ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# -----------------------------
# CONFUSION MATRIX (STATIC DEMO)
# -----------------------------
st.subheader("Model Performance Overview")

labels = df["intent"].tolist()

# Dummy confusion matrix (replace with real y_test if needed)
cm = [
    [50, 2, 1, 0, 0],
    [1, 20, 2, 0, 0],
    [0, 1, 15, 0, 0],
    [0, 0, 0, 10, 1],
    [0, 0, 1, 0, 8]
]

fig3, ax3 = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels)
plt.title("Confusion Matrix")
st.pyplot(fig3)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.write("CivicDex demonstrates multilingual civic request classification using ML.")