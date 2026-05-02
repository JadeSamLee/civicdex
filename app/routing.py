# =========================================
# CivicDex Routing Engine
# Hybrid Intent + Keyword-Based Department Mapping
# =========================================

def get_department(prediction, user_input: str):
    text = user_input.lower()

    # WATER
    if prediction == "complaint" and any(w in text for w in ["water", "tanker", "pipeline", "tap"]):
        return "Water Supply Board"

    # ROADS
    if prediction == "complaint" and any(w in text for w in ["road", "pothole", "street", "asphalt"]):
        return "Municipal Roads Department"

    # ELECTRICITY
    if prediction == "complaint" and any(w in text for w in ["light", "electricity", "power", "current"]):
        return "Electricity Board"

    # SANITATION
    if prediction == "complaint" and any(w in text for w in ["garbage", "waste", "drainage", "smell", "sewage"]):
        return "Sanitation Department"

    # HEALTH
    if prediction == "complaint" and any(w in text for w in ["hospital", "doctor", "medical", "ambulance"]):
        return "Public Health Department"

    # STATUS
    if prediction == "status_query":
        return "Service Tracking Department"

    # FOLLOW UP
    if prediction == "follow_up":
        return "Complaint Resolution Unit"

    # INFO REQUEST
    if prediction == "information_request":
        return "Citizen Information Center"

    # ESCALATION
    if prediction == "escalation":
        return "Senior Municipal Officer"

    return "General Municipal Services"