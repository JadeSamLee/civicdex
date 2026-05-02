"""
CivicDex - Baseline Intent Classification Model

This script trains a baseline NLP model for civic-service request
classification using TF-IDF and Logistic Regression.

Author: CivicDex Project
Purpose: Benchmark model for Tamil/Tanglish civic request understanding
"""

import os
import numpy as np
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# ============================================================
# CONFIGURATION
# ============================================================

# Dataset paths
TRAIN_PATH = os.path.join("data", "civicdex_train.csv")
VAL_PATH = os.path.join("data", "civicdex_val.csv")
TEST_PATH = os.path.join("data", "civicdex_test.csv")

# Model output path
MODEL_PATH = os.path.join("baselines", "civicdex_model.pkl")

# Text and label columns
TEXT_COLUMN = "normalized_text"
LABEL_COLUMN = "intent"

# Reproducibility
np.random.seed(42)


# ============================================================
# DATA LOADING FUNCTION
# ============================================================

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads dataset and removes missing values.

    Args:
        file_path (str): Path to CSV file

    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    df = pd.read_csv(file_path)
    df = df.dropna(subset=[TEXT_COLUMN, LABEL_COLUMN])
    return df


# Load datasets
train_df = load_data(TRAIN_PATH)
val_df = load_data(VAL_PATH)
test_df = load_data(TEST_PATH)

# Split features and labels
X_train, y_train = train_df[TEXT_COLUMN], train_df[LABEL_COLUMN]
X_val, y_val = val_df[TEXT_COLUMN], val_df[LABEL_COLUMN]
X_test, y_test = test_df[TEXT_COLUMN], test_df[LABEL_COLUMN]


# ============================================================
# MODEL DEFINITION
# ============================================================

model = Pipeline([
    # Text vectorization using TF-IDF
    ("tfidf", TfidfVectorizer(
        max_features=25000,
        ngram_range=(1, 3),
        sublinear_tf=True
    )),

    # Linear classifier for intent classification
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])


# ============================================================
# TRAINING
# ============================================================

print("\n==============================")
print("Training CivicDex baseline model")
print("==============================\n")

model.fit(X_train, y_train)


# ============================================================
# VALIDATION EVALUATION
# ============================================================

print("\n==============================")
print("Validation Results")
print("==============================\n")

val_predictions = model.predict(X_val)

print(classification_report(
    y_val,
    val_predictions,
    zero_division=0
))


# ============================================================
# TEST EVALUATION
# ============================================================

print("\n==============================")
print("Test Results")
print("==============================\n")

test_predictions = model.predict(X_test)

print(classification_report(
    y_test,
    test_predictions,
    zero_division=0
))


# ============================================================
# SAVE MODEL
# ============================================================

os.makedirs("baselines", exist_ok=True)

joblib.dump(model, MODEL_PATH)

print("\nModel successfully saved at:")
print(MODEL_PATH)


# ============================================================
# SAMPLE PREDICTION (SANITY CHECK)
# ============================================================

sample_inputs = [
    "garbage not collected in street for 3 days",
    "how to apply for ration card",
    "status of my complaint not updated"
]

print("\nSample Predictions:")
print(model.predict(sample_inputs))