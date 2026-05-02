# =========================================
# CivicDex Routing Engine (Safe + Clean)
# =========================================

def get_department(prediction, user_input: str):

    text = str(user_input).lower().strip() if user_input else ""
    prediction = str(prediction).lower().strip() if prediction else "unknown"

    # -----------------------------
    # COMPLAINT ROUTING (keyword-based)
    # -----------------------------
    if prediction == "complaint":

        if any(w in text for w in ["water", "tanker", "tap", "pipeline"]):
            return "Water Supply Department"

        if any(w in text for w in ["road", "pothole", "street", "asphalt"]):
            return "Roads Department"

        if any(w in text for w in ["light", "electricity", "power", "current", "street light"]):
            return "Electricity Department"

        if any(w in text for w in ["garbage", "waste", "drainage", "sewage", "smell"]):
            return "Sanitation Department"

        if any(w in text for w in ["hospital", "doctor", "medical", "ambulance"]):
            return "Public Health Department"

        return "Municipal Services Department"

    # -----------------------------
    # INTENT-BASED ROUTING (non-complaints)
    # -----------------------------
    routing_map = {
        "status_query": "Service Tracking Unit",
        "follow_up": "Complaint Resolution Unit",
        "information_request": "Citizen Information Center",
        "escalation": "Senior Municipal Officer",
        "application_help": "Citizen Services Department",
        "document_help": "Documentation Support Center"
    }

    return routing_map.get(prediction, "General Municipal Services")