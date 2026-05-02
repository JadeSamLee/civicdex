import streamlit as st
import joblib
import os

# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = os.path.join("baselines", "model.pkl")
model = joblib.load(MODEL_PATH)

# -----------------------------
# UI CONFIG
# -----------------------------
st.set_page_config(
    page_title="CivicDex AI Assistant",
    layout="centered"
)

st.title("CivicDex: Civic Service Request AI")
st.write("Multilingual civic complaint understanding for Tamil and Tanglish inputs.")

# -----------------------------
# Input
# -----------------------------
user_input = st.text_area("Enter your civic complaint / request:")

# -----------------------------
# Label mapping (IMPORTANT FOR DEMO)
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
    "escalation": "Senior Municipal Officer",
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
# Prediction
# -----------------------------
if st.button("Analyze Request"):

    if user_input.strip() == "":
        st.warning("Please enter a request.")
    else:
        pred = model.predict([user_input])[0]

        st.subheader("Prediction Results")

        st.write(f"**Intent:** {pred}")
        st.write(f"**Category:** {category_map.get(pred, 'Unknown')}")
        st.write(f"**Department:** {department_map.get(pred, 'General Office')}")
        st.write(f"**Urgency:** {urgency_map.get(pred, 'Medium')}")

        st.success("Request processed successfully.")