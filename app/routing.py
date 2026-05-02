# =========================================
# CivicDex Routing Engine (Production Safe)
# Hybrid Routing
# =========================================

def get_department(prediction, user_input: str):

    text = str(user_input).lower() if user_input else ""
    prediction = str(prediction).lower() if prediction else "unknown"

    # -----------------------------
    # WATER
    # -----------------------------
    if prediction == "complaint":
        if any(w in text for w in ["water", "tanker", "tap", "pipeline"]):
            return "Water Supply Board"

    # -----------------------------
    # ROADS
    # -----------------------------
    if prediction == "complaint":
        if any(w in text for w in ["road", "pothole", "street", "asphalt"]):
            return "Municipal Roads Department"

    # -----------------------------
    # ELECTRICITY
    # -----------------------------
    if prediction == "complaint":
        if any(w in text for w in ["light", "electricity", "power", "current"]):
            return "Electricity Board"

    # -----------------------------
    # SANITATION
    # -----------------------------
    if prediction == "complaint":
        if any(w in text for w in ["garbage", "waste", "drainage", "sewage", "smell"]):
            return "Sanitation Department"

    # -----------------------------
    # HEALTH
    # -----------------------------
    if prediction == "complaint":
        if any(w in text for w in ["hospital", "doctor", "medical", "ambulance"]):
            return "Public Health Department"

    # -----------------------------
    # NON-ML INTENTS
    # -----------------------------
    routing_map = {
        "status_query": "Service Tracking Department",
        "follow_up": "Complaint Resolution Unit",
        "information_request": "Citizen Information Center",
        "escalation": "Senior Municipal Officer",
        "application_help": "Citizen Services Department",
        "document_help": "Documentation Support Center"
    }

    return routing_map.get(prediction, "General Municipal Services")