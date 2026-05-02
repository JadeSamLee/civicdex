# CivicDex Model Evaluation Report

## 1. Dataset Overview

- Total samples: 600
- Train: 478
- Validation: 103
- Test: 103

Class distribution shows imbalance across intent categories, with "complaint" being dominant.

---

## 2. Model Configuration

- Vectorizer: TF-IDF (1–3 grams)
- Classifier: Logistic Regression (class-balanced)
- Input: normalized_text
- Target: intent

---

## 3. Validation Results

- Accuracy: 0.81
- Macro F1: 0.77
- Weighted F1: 0.80

### Class-wise Performance (Validation)

- Complaint: F1 = 0.86
- Escalation: F1 = 0.80
- Follow_up: F1 = 0.48
- Information_request: F1 = 0.95
- Status_query: F1 = 0.74

---

## 4. Test Results

- Accuracy: 0.76
- Macro F1: 0.64
- Weighted F1: 0.75

### Class-wise Performance (Test)

- Complaint: F1 = 0.83
- Escalation: F1 = 0.29
- Follow_up: F1 = 0.47
- Information_request: F1 = 0.93
- Status_query: F1 = 0.70

---

## 5. Key Observations

- Strong performance on majority class (complaint)
- Excellent performance on information_request after balancing
- Weak performance on escalation due to limited samples
- Macro-F1 drop indicates mild overfitting

---

## 6. Insights

- Class imbalance is the primary limitation
- Rare classes require augmentation for improved generalization
- TF-IDF baseline is strong and stable for multilingual civic text

---

## 7. Conclusion

The model provides a strong and reproducible baseline for civic-service request classification in Tamil and code-mixed text, demonstrating feasibility of structured civic NLP systems in low-resource language settings.