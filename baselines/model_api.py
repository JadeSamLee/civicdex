"""
Inference API for CivicDex model
Used for Streamlit / demo applications
"""

import joblib

# Load trained model
model = joblib.load("baselines/civicdex_model.pkl")


def predict_intent(text: str):
    """
    Predict civic request intent from raw input text
    """
    prediction = model.predict([text])[0]
    return prediction


# Example usage
if __name__ == "__main__":
    sample = "garbage not collected in my street"
    print("Prediction:", predict_intent(sample))