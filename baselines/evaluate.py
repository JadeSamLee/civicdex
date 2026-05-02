"""
Evaluation script for CivicDex baseline model
Computes Accuracy, Macro-F1, and Confusion Matrix
"""

import pandas as pd
import joblib
from sklearn.metrics import classification_report

# Load model
model = joblib.load("baselines/civicdex_model.pkl")

# Load test data
df = pd.read_csv("data/civicdex_test.csv")

X_test = df["normalized_text"]
y_test = df["intent"]

# Predictions
preds = model.predict(X_test)

# Metrics
print("\nCLASSIFICATION REPORT:\n")
print(classification_report(y_test, preds, zero_division=0))