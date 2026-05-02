import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# -----------------------------
# Configuration
# -----------------------------
DATA_PATH = os.path.join("data", "civicdex_train.csv")
VAL_PATH = os.path.join("data", "civicdex_val.csv")

MODEL_PATH = os.path.join("baselines", "model.pkl")
VECTORIZER_PATH = os.path.join("baselines", "vectorizer.pkl")

TEXT_COLUMN = "normalized_text"
LABEL_COLUMN = "intent"   # You can switch to "category" later

# -----------------------------
# Load Data
# -----------------------------
def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=[TEXT_COLUMN, LABEL_COLUMN])
    return df

train_df = load_data(DATA_PATH)
val_df = load_data(VAL_PATH)

X_train = train_df[TEXT_COLUMN].astype(str)
y_train = train_df[LABEL_COLUMN]

X_val = val_df[TEXT_COLUMN].astype(str)
y_val = val_df[LABEL_COLUMN]

# -----------------------------
# Model Pipeline
# -----------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        lowercase=True
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

# -----------------------------
# Training
# -----------------------------
print("Training baseline model...")
model.fit(X_train, y_train)

# -----------------------------
# Evaluation
# -----------------------------
print("\nValidation Results:\n")

y_pred = model.predict(X_val)

report = classification_report(y_val, y_pred)
print(report)

# -----------------------------
# Save Model
# -----------------------------
os.makedirs("baselines", exist_ok=True)

joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")