# Dataset Card for CivicDex

## Dataset Description

CivicDex is a multilingual civic-service request dataset designed for AI systems that classify and route public-service requests in Tamil, Tanglish, and code-mixed English.

It supports real-world civic NLP tasks such as complaint classification and service routing in low-resource language settings.

---

## Motivation

Civic-service systems often struggle with:

- Tamil and Tanglish inputs
- Noisy, informal citizen messages
- Lack of structured labeled datasets
- Limited resources for civic NLP benchmarks

CivicDex addresses this by providing a structured dataset for **intent classification and civic routing systems**.

---

## Intended Users

- NLP researchers in low-resource languages
- Civic technology developers
- Government digital service teams
- AI system designers for public services

---

## Intended Tasks

Primary task supported:

### Intent Classification
Predict the intent of a civic request.

Labels:
- complaint
- follow_up
- status_query
- information_request
- escalation

---

## Dataset Composition

- Total Samples: ~600
- Languages:
  - Tamil
  - Tanglish
  - Code-mixed English

---

## Data Fields

Each record contains:

- request_id
- raw_text
- normalized_text
- language_type
- intent

---

## Label Definitions

### Intent Labels

- complaint → Civic issue report
- follow_up → Follow-up on existing request
- status_query → Asking request status
- information_request → General civic information request
- escalation → Complaint escalation

---

## Data Splits

| Split | Samples |
|------|--------|
| Train | ~70% |
| Validation | ~15% |
| Test | ~15% |

---

## Why CivicDex Matters

- Improves civic NLP for under-resourced languages
- Supports real-world government service automation
- Enables multilingual AI routing systems

---

## Baseline Results

TF-IDF + Logistic Regression baseline:

- Accuracy: ~75–81%
- Macro F1: ~0.70–0.78

---

## Limitations

- Dataset is a seed dataset (~600 samples)
- Limited real-world annotation diversity
- Focused on Tamil Nadu civic context
- Does not include deep contextual dialogue

---

## Ethical Considerations

- No personal identifying information included
- All data is anonymized or synthetic
- Designed for research and civic AI prototyping only
- Not intended for surveillance or decision enforcement

---

## Future Work

- Expand real-world civic data collection
- Add regional Tamil dialect variation
- Extend to other Indian languages
- Improve multilingual embeddings
- Add urgency classification

---

## Citation

```bibtex
@misc{civicdex,
  title={CivicDex: Multilingual Civic AI Dataset},
  year={2026},
  note={Dataset for civic NLP and routing systems}
}