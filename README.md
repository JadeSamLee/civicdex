# CivicDex: A Multilingual Public-Service Request Dataset for Civic AI


CivicDex is a structured, open-source dataset project designed to support the development of AI systems for public-service request understanding, routing, and assistance in Tamil, Tanglish, and mixed-language user inputs. The project is built around a practical gap in current AI data availability: civic-service and government-facing request data in under-resourced Indian languages is limited, inconsistently structured, and difficult to reuse for benchmarking or product development. This directly aligns with the challenge goal of building open datasets for underserved domains, scarce public data settings, and under-resourced languages. [1][2][3]

## Project Summary

CivicDex is intended to function as a seed dataset and reusable benchmark for civic-service AI use cases. The dataset captures realistic public-service interactions such as complaints, information requests, document-related help, service delays, grievance follow-ups, and routing needs. It is designed for machine learning, prompt engineering, retrieval, workflow automation, and multilingual public-service system design. The dataset is not positioned as a giant web-scale corpus; instead, it is a high-clarity, well-annotated, extensible foundation that other developers and researchers can expand. This type of transparent, purposeful documentation is consistent with best practices recommended for data cards and dataset publishing. [4][5][6]

## Core Problem

Many public-service workflows depend on unstructured citizen requests, but most open NLP datasets focus on broad classification tasks, social media, or high-resource languages. Tamil and Tamil-English code-mixed civic requests are especially underrepresented in reusable benchmark datasets, even though such inputs are common in real public-service contexts. CivicDex addresses this by defining a structured data format for civic intent understanding, service-category mapping, urgency estimation, and department routing. [1][3][7]

## Primary Objectives

CivicDex is designed to achieve the following objectives:

- Build an original, openly shareable dataset for Tamil and code-mixed civic-service language. [1][2]
- Support underserved public-service and governance-related NLP tasks. [1]
- Provide a reusable benchmark for intent classification, request categorization, and service routing. [6][4]
- Demonstrate that a small but carefully designed seed dataset can still be useful when documented well and validated with a baseline. [4][7]
- Offer an extensible structure that future contributors can scale into a larger public benchmark. [5][7]

## What CivicDex Should Demonstrate

The project should communicate its purpose clearly without requiring additional verbal explanation. A person reading the repository should immediately understand that CivicDex is:

- A civic-domain dataset, not a general chatbot dataset. [1]
- Focused on Tamil, Tanglish, and multilingual citizen-service text. [1][7]
- Built for practical AI tasks such as complaint classification, routing, and citizen assistance. [6][4]
- Intentionally designed as a seed dataset with a documented growth path. [4][5]
- Strong enough to support at least one basic validation benchmark. [4]

## Scope of the Dataset

CivicDex should include realistic examples of public-service interactions that a citizen might submit in a text-based system, complaint portal, mobile app, civic chatbot, or grievance redressal platform. The dataset may include synthetic but realistic samples, provided the documentation clearly distinguishes synthetic generation from real-world collection and avoids copying public complaint text verbatim. Transparent source and generation documentation is important for trustworthy dataset publication. [4][5]

Recommended request types include:

- Complaint reporting
- Service outage reporting
- Status inquiry
- Document assistance request
- Application help request
- Escalation or grievance follow-up
- Public information query
- Routing to the correct department

## Language Coverage

CivicDex should explicitly support multiple input styles commonly seen in real user requests:

- Tamil script
- Tanglish or romanized Tamil
- Tamil-English code-mixed text
- Simple English paraphrases where useful for glossing or benchmarking

The repository should explain that multilingual and code-mixed support matters because under-resourced language infrastructure often fails when real user inputs do not remain in a single standardized format. [1][7]

## Benchmark Tasks

CivicDex should support at least one primary benchmark and optionally several secondary ones.

### Primary Task

**Intent Classification**

The first and most important benchmark should be intent classification. Given a citizen request, the model predicts the high-level user intent.

Example intent labels:

- complaint
- information_request
- status_query
- document_help
- application_help
- follow_up
- escalation

### Secondary Tasks

- **Category Classification**: Predict the service category, such as roads, water, sanitation, electricity, certificates, welfare, or public health.
- **Department Routing**: Predict which department or service unit should handle the request.
- **Urgency Classification**: Predict whether the request is low, medium, or high urgency.
- **Language-Type Detection**: Detect Tamil, Tanglish, or code-mixed usage.
- **Normalization**: Map noisy user input into a cleaner canonical version.

These tasks make the dataset more reusable across NLP, workflow automation, and product design use cases. [4][6]

## Recommended Dataset Size

CivicDex can begin as a seed dataset. A practical initial size is 200 to 500 rows, with a goal of high annotation quality rather than large scale. This is acceptable when the documentation makes the design choices clear and when at least one small validation step is included. The repository should state that the initial version is a seed release intended for structured extension. [1][4][7]

## Data Design Principles

The dataset should be designed with the following principles:

- **Originality**: Text should be original, synthetic, contributed, or carefully transformed, not copied verbatim from public records. [4][5]
- **Transparency**: The README and data card should clearly state whether each sample is synthetic, human-authored, paraphrased, or collected. [4][5]
- **Task usefulness**: Every field should support at least one benchmark or practical workflow. [6][4]
- **Extensibility**: Labels and schema should be easy to scale to more districts, more languages, and more services. [7][5]
- **Practical realism**: Samples should resemble real citizen messages, including short, noisy, and incomplete requests. [7]

## Dataset Schema

The main dataset should be stored in a structured CSV or JSON file. A recommended schema is below.

| Field | Type | Description |
|---|---|---|
| request_id | string | Unique identifier for each sample |
| raw_text | string | Original user input in Tamil, Tanglish, code-mixed, or English |
| normalized_text | string | Cleaned or normalized version of the request |
| english_gloss | string | Short English translation or gloss |
| language_type | string | One of: tamil, tanglish, code_mixed, english |
| intent | string | High-level request intent |
| category | string | Service category |
| department | string | Responsible department or service office |
| urgency | string | Low, medium, or high |
| severity | string | Operational severity if relevant |
| locality | string | Generalized locality or placeholder area |
| district | string | District or region tag if used |
| source_type | string | synthetic, human_written, paraphrased, collected |
| split | string | train, validation, or test |
| notes | string | Optional comments for annotation or ambiguity |

The schema should remain simple enough for Kaggle and Hugging Face users to understand quickly. Clear structure and accessibility are core dataset publishing expectations. [6][4]

## Label Taxonomy

A separate taxonomy file should define each allowed label and its meaning.

### Intent Labels

| Label | Meaning |
|---|---|
| complaint | User reports a problem requiring action |
| information_request | User asks for instructions or public information |
| status_query | User asks about progress or current request state |
| document_help | User needs help obtaining or understanding a document |
| application_help | User needs help with a service application or form |
| follow_up | User follows up on an earlier request |
| escalation | User expresses dissatisfaction and requests higher attention |

### Category Labels

Suggested categories may include:

- roads
- sanitation
- water_supply
- drainage
- electricity
- certificates
- welfare
- public_health
- street_lighting
- waste_management
- housing
- transport

### Urgency Labels

| Label | Meaning |
|---|---|
| low | Inconvenience with no immediate safety risk |
| medium | Important issue needing timely response |
| high | Safety-critical or severe service failure |

## Example Rows

The dataset documentation should include a few representative rows.

| request_id | raw_text | english_gloss | language_type | intent | category | department | urgency |
|---|---|---|---|---|---|---|---|
| CDX_0001 | எங்கள் தெருவில் மூன்று நாட்களாக குப்பை எடுக்கவில்லை | Garbage has not been collected in our street for three days | tamil | complaint | waste_management | sanitation_department | medium |
| CDX_0002 | street light work pannala, full dark ah iruku | The street light is not working and it is completely dark | tanglish | complaint | street_lighting | electrical_maintenance | high |
| CDX_0003 | birth certificate apply panna eppadi | How do I apply for a birth certificate | tanglish | information_request | certificates | citizen_services | low |

Examples help users understand task framing immediately, which is a core strength of well-documented datasets. [4][6]

## Train, Validation, and Test Split

The dataset should include a documented split strategy. For an initial 300-row release, an example split is:

- Train: 70%
- Validation: 15%
- Test: 15%

The split procedure should attempt to minimize near-duplicate leakage across splits. The documentation should explain that the test set is held out for benchmark reporting. [4][6]

## Validation Strategy

Because the dataset is a seed dataset, it should include one lightweight validation benchmark to demonstrate usefulness.

### Recommended Validation

Implement a tiny baseline model for **intent classification**.

Recommended baseline:

- Input: `raw_text` or `normalized_text`
- Features: TF-IDF or simple sentence embeddings
- Model: Logistic Regression
- Metric: Macro-F1

This is preferred over rule-only validation because a small model provides a stronger signal that the dataset is learnable and useful for downstream ML. Baseline-oriented validation is a standard and effective way to demonstrate dataset usability, especially in low-resource settings. [4][6]

### Secondary Validation

Optionally include 5 to 10 manual example-based routing demonstrations showing:

- input text
- expected intent
- expected category
- expected department

This gives qualitative evidence of realism and label consistency. [4]

## Statistics to Report

CivicDex does not require advanced mathematical analysis, but it should report basic dataset statistics clearly.

Recommended statistics:

- Total number of rows
- Number of rows per split
- Label distribution for `intent`
- Label distribution for `category`
- Label distribution for `language_type`
- Count of high-urgency requests
- Count of synthetic versus collected examples
- Duplicate count or duplicate-check summary if applicable

These simple statistics help communicate quality, coverage, and reproducibility without turning the project into a research-heavy paper. [4][6]

## Repository Structure

A clean repository structure for CivicDex should look like this:

```text
CivicDex/
├── README.md
├── DATASET_CARD.md
├── LICENSE
├── data/
│   ├── civicdex_main.csv
│   ├── civicdex_train.csv
│   ├── civicdex_validation.csv
│   └── civicdex_test.csv
├── taxonomy/
│   ├── intent_labels.json
│   ├── category_labels.json
│   ├── urgency_labels.json
│   └── language_type_labels.json
├── docs/
│   ├── annotation_guidelines.md
│   ├── schema.md
│   ├── methodology.md
│   └── examples.md
├── baselines/
│   ├── intent_classification_baseline.ipynb
│   └── intent_classification_baseline.py
└── results/
    └── baseline_metrics.md
```

This structure makes the project easy to navigate for judges, contributors, and downstream users. Clear documentation and organization are part of good dataset publication practice. [6][8]

## README Requirements

The README should stand on its own and answer the following questions immediately:

- What is CivicDex?
- Why does it matter?
- Which language problem does it address?
- What tasks does it support?
- What is included in the repository?
- How can someone use it?
- How was the data created?
- What are the limitations?

A strong README is especially important for Kaggle and public dataset presentation because users often decide within seconds whether a dataset is useful. [6][8]

## Data Card Requirements

The Data Card or Dataset Card should include:

- Dataset motivation
- Intended users
- Intended tasks
- Collection or generation process
- Annotation methodology
- Known limitations
- Risks and ethical considerations
- Licensing and reuse conditions

Data Cards are a recognized best practice for transparent dataset documentation and help communicate dataset purpose, assumptions, and appropriate use. [4][5]

## Ethical and Privacy Considerations

CivicDex should avoid storing personally identifiable information such as full names, exact addresses, government ID numbers, or phone numbers. Any locally specific examples should be generalized or anonymized. The documentation should clearly state that the dataset is intended for research, prototyping, and civic AI benchmarking, not for automated denial, surveillance, or harmful profiling. Transparency and responsible use language strengthen the credibility of the dataset. [4][5]

## Growth Plan

CivicDex should present itself not just as a static dataset but as an expandable infrastructure project.

The roadmap can include:

- More Tamil regional variation
- More district and municipal mappings
- Additional code-mixed variants
- More service categories
- More benchmark tasks
- Human validation rounds
- Cross-lingual extension to other Indian languages

This growth plan is important because a strong seed dataset becomes more valuable when it clearly shows how the ecosystem can build on it. [7][5]

## Submission Framing for the Challenge

If this project is submitted to The Uncharted Data Challenge, CivicDex should explicitly frame itself as:

- A dataset for an underserved civic-service NLP domain. [1]
- A contribution to scarce open-source Tamil public-service language data. [1][3]
- A resource for an under-resourced language context. [1]
- An openly documented benchmark with practical downstream use. [2][6]

The submission should also credit Adaptive Data by Adaption if required by the challenge instructions. [1]

## Final Positioning Statement

CivicDex should be presented as a practical, well-documented, benchmark-oriented civic AI dataset for Tamil and code-mixed public-service requests. Its strength is not raw scale but clarity of design, usability, extensibility, and relevance to under-resourced civic language technology. A reader should be able to understand the problem, inspect the schema, view sample records, run a baseline, and immediately see how the dataset can be reused or extended. This is the standard the repository should aim to meet. [1][4][6]
