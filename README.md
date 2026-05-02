# CivicDex: Multilingual Civic Request Understanding and Routing

CivicDex is a multilingual civic-service dataset for understanding and routing public-service requests written in Tamil, Tanglish, English, and code-mixed text. The dataset is designed for intent classification, category prediction, department routing, urgency estimation, and civic AI prototyping in low-resource settings.

## Overview

CivicDex focuses on citizen-facing service requests such as sanitation complaints, water issues, road damage, certificate-related queries, and escalation messages. Each record is structured to support both dataset research and end-to-end application development, including dashboard and routing workflows.

## Problem Statement

Public-service request systems often struggle with multilingual and code-mixed inputs, especially when users mix Tamil and English or write Tamil in Roman script. CivicDex addresses this by providing a structured dataset with normalized text, language markers, intent labels, departmental routing fields, urgency, severity, and train/test split metadata.

## Dataset Description

The primary dataset file is `civicdex_main.csv`. The schema shown in the dataset includes 14 columns: `request_id`, `raw_text`, `normalized_text`, `english_gloss`, `language_type`, `intent`, `category`, `department`, `urgency`, `severity`, `locality`, `district`, `source_type`, and `split`.

### Supported Language Types

- `tamil` — native Tamil script inputs.
- `tanglish` — Tamil written in Roman script.
- `code_mixed` — mixed Tamil-English expressions.
- `english` — English civic-service requests, included in schema definition even though the preview is dominated by Tamil, Tanglish, and code-mixed examples.

## Dataset Schema

| Field | Description |
|---|---|
| `request_id` | Unique identifier for each civic request. |
| `raw_text` | Original user-provided request text. |
| `normalized_text` | Cleaned or normalized version of the request for modeling. |
| `english_gloss` | English gloss or translation-like interpretation of the request. |
| `language_type` | Language form such as tamil, tanglish, or code_mixed. |
| `intent` | Main intent label, such as complaint or status query. |
| `category` | Civic domain category, such as sanitation, roads, or certificates. |
| `department` | Mapped handling department, such as Water Supply Department or Revenue Department. |
| `urgency` | Priority level, such as low, medium, or high. |
| `severity` | Finer-grained severity type, such as service_delay or public_hazard. |
| `locality` | Locality descriptor, such as urban_area. |
| `district` | District label, such as Chennai in the preview rows. |
| `source_type` | Data origin marker, such as real, synthetic, or synthetic_realistic. |
| `split` | Dataset split marker, such as train. |

## Label Space

### Intent Labels

The dataset preview contains at least the following intent labels:

- `complaint`
- `follow_up`
- `status_query`
- `information_request`
- `escalation`
- `application_help`
- `document_help`

### Category Labels

The preview shows multiple domain categories, including:

- `sanitation`
- `water_supply`
- `roads`
- `street_lighting`
- `drainage`
- `electricity`
- `public_health`
- `certificates`
- `welfare`
- `transport`

### Department Labels

The preview maps requests to operational departments such as:

- `Sanitation Department`
- `Water Supply Department`
- `Roads Department`
- `Electricity Department`
- `Drainage Department`
- `Public Health Department`
- `Revenue Department`
- `Welfare Department`
- `Transport Department`

## Benchmark Tasks

CivicDex can support several supervised and rule-assisted tasks:

1. Intent classification from `raw_text` or `normalized_text`.
2. Category classification for civic-service domains.
3. Department routing based on request content and predicted labels.
4. Urgency prediction using intent, lexical cues, and severity patterns.
5. Multilingual and code-mixed civic NLP experimentation using Tamil, Tanglish, and code-mixed records.

## Example Use Cases

- Complaint intake systems for municipalities.
- Citizen grievance triage dashboards.
- AI assistants for form help, service information, and request tracking.
- Escalation-aware routing prototypes for public-service workflows.

## Baseline System Alignment

A baseline application built on CivicDex should align with the actual dataset columns instead of using a reduced schema. In particular, a correct pipeline can use `normalized_text` as model input, predict `intent`, optionally predict `category`, and route to the `department` field already present in the dataset, while also exposing `urgency` and `severity` for downstream decision logic.

## Suggested Repository Structure

```text
CivicDex/
├── app/
│   ├── app.py
│   ├── routing.py
├── baselines/
│   ├── civicdex_model.pkl
├── data/
│   ├── civicdex_main.csv
├── notebooks/
│   ├── baseline_experiments.ipynb
├── requirements.txt
├── README.md
```

This structure is consistent with a dataset-first repository that also includes a simple ML baseline and a Streamlit interface. The exact files may vary, but `civicdex_main.csv` should remain the canonical dataset source referenced by the README.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

If a baseline model is included, it should be trained on the train split indicated by the `split` column and evaluated on a held-out test split if present in the repository. The README should only claim metrics that are actually reproducible from the shared code and files.

## Limitations

- The preview shows a mix of `real`, `synthetic`, and `synthetic_realistic` examples, so the dataset should be described as a hybrid civic dataset rather than a fully real-world collection.
- The visible rows are concentrated in `urban_area` and `Chennai`, so geographic generalization should not be overstated without broader coverage.
- Any performance claims must match the released model artifacts and evaluation scripts, not assumed benchmark numbers.

## Future Improvements

- Expand district coverage beyond the currently previewed Chennai-focused records.
- Increase real annotated samples relative to synthetic and synthetic_realistic entries.
- Add stronger train/test documentation and dataset cards for reproducibility.
- Extend benchmarking to transformer-based multilingual models after publishing a transparent baseline.

## Purpose

CivicDex is best described as a structured multilingual civic dataset for request understanding and routing in public-service settings. It is suitable for low-resource civic NLP research, municipal AI prototyping, multilingual intent classification, and operational routing experiments.