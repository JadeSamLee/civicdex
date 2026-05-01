# Dataset Card for CivicDex

## Dataset Description

CivicDex is a multilingual civic-service request dataset designed to support AI system development for public-service request understanding, routing, and assistance in Tamil, Tanglish, and mixed-language contexts.

### Motivation

Civic-service and government-facing request data in under-resourced Indian languages is limited, inconsistently structured, and difficult to reuse for benchmarking or product development. CivicDex addresses this gap by providing a structured, well-documented seed dataset for civic AI applications.

### Intended Users

- NLP researchers working on low-resource languages
- Civic technology developers
- Government technology teams
- Public service workflow automation projects
- Multilingual AI system designers

### Intended Tasks

- Intent classification for civic requests
- Service category prediction
- Department routing recommendations
- Urgency assessment
- Language identification
- Text normalization and canonicalization

## Benchmark Tasks

CivicDex supports the following benchmark tasks:

1. Intent Classification (Primary Task)
   - Input: raw_text or normalized_text
   - Output: intent label (7 classes)
   - Metric: Macro-F1 score

2. Service Category Classification
   - Input: normalized_text
   - Output: category label (12+ classes)

3. Department Routing
   - Input: normalized_text
   - Output: department label

4. Urgency Prediction
   - Input: normalized_text
   - Output: urgency level (low, medium, high)
   
## Dataset Composition

### Data Types

The dataset contains 250 civic service requests with the following characteristics:

- **Language distribution**: Tamil (28%), Tanglish (40%), Code-mixed (32%), English (10%)
- **Intent distribution**: 7 intent categories
- **Category distribution**: 12+ service categories
- **Split distribution**: 70% train, 15% validation, 15% test

### Data Fields

Each sample contains 14 fields:

1. **request_id**: Unique identifier (CDX_001 to CDX_250)
2. **raw_text**: Original user input
3. **normalized_text**: Cleaned and standardized version
4. **english_gloss**: English translation or gloss
5. **language_type**: tamil, tanglish, code_mixed, english
6. **intent**: High-level request intent (7 classes)
7. **category**: Service category (12+ classes)
8. **department**: Responsible department or office
9. **urgency**: low, medium, high
10. **severity**: Operational severity level
11. **locality**: Generalized location (anonymized)
12. **district**: District or region tag
13. **source_type**: synthetic, human_written, paraphrased, collected
14. **split**: train, validation, test

### Label Taxonomies

#### Intent Labels

- **complaint**: User reports a problem requiring action
- **information_request**: User asks for instructions or public information
- **status_query**: User asks about progress or current state
- **document_help**: User needs help obtaining or understanding documents
- **application_help**: User needs help with service applications
- **follow_up**: User follows up on an earlier request
- **escalation**: User expresses dissatisfaction and requests higher attention

#### Category Labels

- roads, sanitation, water_supply, drainage, electricity
- certificates, welfare, public_health, street_lighting
- waste_management, housing, transport

#### Urgency Labels

- **low**: Inconvenience with no immediate safety risk
- **medium**: Important issue needing timely response
- **high**: Safety-critical or severe service failure

#### Language Type Labels

- **tamil**: Formal Tamil in native script
- **tanglish**: Romanized Tamil with phonetic spelling
- **code_mixed**: Tamil structure with English technical terms
- **english**: Standard English

## Why CivicDex Matters

- Tamil and code-mixed civic-service data is underrepresented in NLP benchmarks
- Real-world civic systems rely on noisy, multilingual user inputs
- Existing datasets do not model administrative routing or urgency

CivicDex bridges the gap between academic NLP benchmarks and deployable civic AI systems.

## Collection Process

### Data Generation

The dataset was created through a combination of:

1. **Synthetic generation**: Realistic civic requests written based on common public-service scenarios
2. **Human authorship**: Native Tamil speakers contributed authentic request patterns
3. **Paraphrasing**: Existing patterns adapted to create variations
4. **Collection**: Representative examples from public sources (heavily modified for privacy)

All samples are original and do not contain verbatim copies of real citizen complaints.

### Annotation Methodology

Each sample was annotated with:

1. **Language type identification**: Determined by script and linguistic patterns
2. **Intent classification**: Based on primary user goal
3. **Category assignment**: Based on service domain
4. **Department mapping**: Based on typical civic organizational structure
5. **Urgency assessment**: Based on safety and time-sensitivity criteria
6. **Normalization**: Standardization of spelling and formatting
7. **English gloss**: Translation for benchmarking purposes

### Quality Control

- Manual review of all samples
- Consistency checks across similar requests
- Duplicate detection and removal
- Anonymization verification
- Label distribution balancing

## Data Splits

| Split | Samples | Percentage |
|-------|---------|------------|
| Train | 175 | 70% |
| Validation | 38 | 15% |
| Test | 37 | 15% |

Splits are stratified by intent to ensure balanced class distribution. Near-duplicate detection minimizes leakage across splits.

## Baseline Results

| Task | Model | Metric | Score |
|------|------|--------|-------|
| Intent Classification | TF-IDF + Logistic Regression | Macro-F1 | 0.78 |

The baseline demonstrates that CivicDex is a learnable and structured dataset suitable for downstream machine learning tasks.

## Ethical Considerations

### Privacy Protection

- No personally identifiable information (PII) included
- Full names, exact addresses, government IDs, and phone numbers removed
- Locations generalized to district level
- All examples anonymized or synthetic

### Responsible Use

- Intended for research, prototyping, and civic AI benchmarking
- Not for automated denial, surveillance, or harmful profiling
- Transparent documentation of limitations and assumptions
- Clear communication of appropriate use cases

### Bias and Fairness

- Dataset represents urban Tamil Nadu civic contexts
- May not generalize to rural or other regional contexts
- Language variations reflect educated, literate citizen communication
- Department mappings based on typical urban municipal structures

### Limitations

- Seed dataset size (250 samples) limits model performance
- Geographic scope limited to Tamil Nadu urban contexts
- Language variations may not capture all regional dialects
- Department structures may vary across municipalities
- Synthetic nature may not capture all real-world complexity
- Dataset size may limit generalization for deep learning models

## Reproducibility

The dataset is fully reproducible using the provided data files and baseline scripts. All splits are predefined and stratified to ensure consistent evaluation across experiments.

## Maintenance

### Versioning

This is version 1.0 of the CivicDex dataset. Future versions may include:

- Expanded sample size
- Additional regional variations
- More service categories
- Enhanced annotation detail
- Cross-lingual extensions

### Contributions

Contributions are welcome through:

- Additional labeled samples
- New language variations
- Expanded category definitions
- Improved annotation guidelines
- Bug fixes and documentation improvements

### Contact

For questions, concerns, or contributions, please open an issue on the project repository.

## License

This dataset is licensed under the MIT License. See LICENSE file for details.

## Citation

```bibtex
@misc{civicdex2024,
  title = {CivicDex: A Multilingual Public-Service Request Dataset},
  author = {CivicDex Contributors},
  year = {2024},
  url = {https://github.com/your-repo/civicdex},
  note = {Dataset for civic AI and NLP benchmarking}
}
```
