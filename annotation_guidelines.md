# Annotation Guidelines for CivicDex

## Overview

This document provides detailed instructions for annotating civic service requests in the CivicDex dataset. All annotators must follow these guidelines to ensure consistency and quality across the dataset.

## Annotation Workflow

The annotation process follows a structured multi-step workflow to ensure consistency and quality:

1. Initial Labeling
   - Annotator assigns intent, category, urgency, and language labels
   - Raw text is normalized and English gloss is added

2. Self-Review
   - Annotator verifies label consistency against guidelines
   - Checks for ambiguity or multiple interpretations

3. Secondary Review
   - A second pass is performed to validate difficult or ambiguous samples
   - Conflicts are resolved using guideline-based reasoning

4. Final Validation
   - Dataset-level consistency checks are performed
   - Duplicate and near-duplicate samples are removed
   
## Intent Classification Guidelines

### 1. Complaint

**Definition**: User reports a problem, issue, or deficiency requiring action from civic authorities.

**Key Indicators**:
- Reports of malfunction, damage, or failure
- Expresses dissatisfaction with current state
- Requests corrective action
- Often includes location details

**Examples**:
- "Road has potholes near school"
- "Garbage not collected for a week"
- "Street light not working"

**Not Complaint**:
- General information requests
- Status inquiries about existing requests
- Requests for application forms

### 2. Information Request

**Definition**: User seeks instructions, procedures, or public information.

**Key Indicators**:
- Asks "how to" or "what is" questions
- Requests process documentation
- Inquires about eligibility or requirements
- Seeks contact information

**Examples**:
- "How to apply for birth certificate?"
- "What documents needed for ration card?"
- "Procedure for water connection"

**Not Information Request**:
- Requests for immediate service (use appropriate intent)
- Complaints about lack of information

### 3. Status Query

**Definition**: User asks about progress or current state of an existing request or service.

**Key Indicators**:
- References previous application or complaint
- Asks about current status
- Inquires about timeline or delay
- Uses phrases like "status of", "update on", "progress of"

**Examples**:
- "Status of my passport application submitted last month"
- "Any update on complaint registered on 15th?"
- "When will water connection be completed?"

**Not Status Query**:
- New requests (use appropriate intent)
- General information about processes

### 4. Document Help

**Definition**: User needs assistance obtaining, understanding, or correcting official documents.

**Key Indicators**:
- Mentions specific document types
- Requests duplicate copies
- Needs help with document procedures
- Lost or damaged documents

**Examples**:
- "Lost driving license, how to get duplicate?"
- "Need caste certificate for college admission"
- "Error in birth certificate, how to correct?"

**Not Document Help**:
- Requests for services that require documents (use appropriate intent)
- General information about documents (use information_request)

### 5. Application Help

**Definition**: User needs assistance with filling forms or completing application processes.

**Key Indicators**:
- Asks about application procedures
- Needs help with form completion
- Inquires about application requirements
- Seeks guidance for submission process

**Examples**:
- "How to fill water connection application?"
- "What to write in ration card application?"
- "Procedure for old age pension application"

**Not Application Help**:
- Requests to submit application on their behalf
- General information queries (use information_request)

### 6. Follow-up

**Definition**: User follows up on previously submitted request or complaint.

**Key Indicators**:
- References earlier submission
- Expresses concern about lack of response
- Requests update on pending matter
- May express frustration about delay

**Examples**:
- "Submitted complaint 10 days ago, no action taken"
- "Following up on my grievance application"
- "Previous request still pending, need urgent attention"

**Distinguish from Status Query**:
- Follow-up implies concern about inaction or delay
- Status query is neutral information-seeking

### 7. Escalation

**Definition**: User expresses dissatisfaction and requests higher-level intervention.

**Key Indicators**:
- Expresses strong dissatisfaction
- Mentions previous unresolved complaints
- Requests higher authority involvement
- Uses urgent or demanding language
- May threaten formal complaint

**Examples**:
- "Unresolved for months, need collector intervention"
- "Complaint ignored, escalating to commissioner"
- "Very poor service, need immediate higher authority attention"

**Not Escalation**:
- First-time complaints (use complaint)
- Polite follow-ups (use follow_up)

## Category Classification Guidelines

### Roads
- Road maintenance, potholes, resurfacing
- Footpath issues
- Road safety concerns
- Signage and markings

### Sanitation
- Garbage collection
- Public toilet cleanliness
- Street cleaning
- Waste disposal issues

### Water Supply
- Water connection problems
- Billing issues
- Water quality complaints
- Supply interruptions

### Drainage
- Drain cleaning
- Flooding during rains
- Sewage overflow
- Blocked drains

### Electricity
- Street lighting
- Power supply issues
- Pole and wiring problems
- Billing complaints

### Certificates
- Birth/death certificates
- Caste/income certificates
- Residence certificates
- Other official documents

### Welfare
- Pension schemes
- Government benefits
- Subsidy programs
- Social welfare schemes

### Public Health
- Hospital services
- Health center issues
- Vaccination programs
- Disease control

### Street Lighting
- Non-functional street lights
- New installation requests
- Maintenance issues

### Waste Management
- Recycling programs
- Composting facilities
- Hazardous waste disposal

### Housing
- Public housing maintenance
- Slum development
- Building permits
- Tenancy issues

### Transport
- Bus services
- Permit applications
- Infrastructure issues
- Public transport facilities

## Urgency Classification Guidelines

### Low Urgency
- Non-safety related inconveniences
- Cosmetic issues
- Long-term improvement requests
- Information requests

**Examples**:
- "Park bench needs painting"
- "Request for new bus stop"
- "Information about pension scheme"

### Medium Urgency
- Affects daily life but not immediately dangerous
- Service interruptions
- Important but not critical issues

**Examples**:
- "Water supply cut for 2 days"
- "Pothole causing traffic jam"
- "Street light not working"

### High Urgency
- Safety-critical situations
- Health hazards
- Severe service failures
- Immediate danger to public

**Examples**:
- "Open manhole without cover"
- "Contaminated water supply"
- "Building collapse risk"
- "Major road blockage"

## Language Type Classification

### Tamil
- Entirely in Tamil script
- Formal Tamil language
- May include Sanskrit loanwords

### Tanglish
- Romanized Tamil
- Phonetic spelling of Tamil words
- Uses English alphabet for Tamil sounds

### Code-Mixed
- Mix of Tamil and English in same sentence
- Tamil grammar with English nouns/technical terms
- Common in educated urban speech

### English
- Standard English
- May include Indian English expressions
- Used for official communication

## Department Mapping Guidelines

### General Principles
- Map to department with primary responsibility
- Use typical urban municipal structure
- When multiple departments involved, choose primary
- Use "multi_department" tag if genuinely shared

### Common Mappings

**Complaints about**: Map to responsible department
- Roads → Roads Department
- Garbage → Sanitation Department
- Water → Water Supply Department
- Lights → Electricity Department

**Certificates**: Citizen Services Office / Revenue Department

**Welfare schemes**: Welfare Department

**Health issues**: Public Health Department

**Housing**: Housing Department / Urban Development

**Transport**: Transport Department / Traffic Police

## Quality Assurance Checklist

Before finalizing annotations:

- [ ] Intent clearly identified based on primary user goal
- [ ] Category appropriate for service domain
- [ ] Department mapping follows standard structure
- [ ] Urgency assessment consistent with guidelines
- [ ] Language type correctly classified
- [ ] No PII or sensitive information present
- [ ] Text properly normalized
- [ ] English gloss accurate and concise

## Inter-Annotator Consistency

To ensure labeling reliability, CivicDex follows consistency principles:

- Annotation decisions are guided strictly by predefined rules
- Edge cases are resolved using majority reasoning or guideline precedence
- Similar samples are cross-checked for uniform labeling
- Ambiguous samples are flagged and reviewed before final inclusion

While formal agreement metrics (e.g., Cohen’s Kappa) are not computed in this version, consistency is enforced through structured review and validation processes.

## Ambiguity Resolution

When uncertain:

1. Choose most likely interpretation
2. Document reasoning in notes field
3. Flag for review if significant uncertainty
4. Maintain consistency with similar cases
5. When in doubt, choose broader category

## Notes Field Usage

Use the notes field for:

- Ambiguities in classification
- Multiple possible interpretations
- Special circumstances
- Edge cases
- Reasoning for difficult decisions

Do not use for:
- Routine annotations
- Information derivable from other fields
- Personal opinions

## Edge Case Handling

Certain civic requests may span multiple intents or categories. In such cases:

- Assign the label corresponding to the primary user goal
- Avoid multi-label classification unless explicitly defined
- Prioritize action-oriented intent over informational phrasing
- When uncertainty persists, choose the broader applicable category

Examples of edge cases include:
- Complaint + follow-up → classify as follow_up if prior context is clear
- Information + application help → classify as application_help if action is required

## Review Process

All annotations should undergo:

1. Initial annotation by trained annotator
2. Quality check by senior annotator
3. Consistency review across similar cases
4. Final validation before inclusion

## Training Requirements

Annotators must:

- Complete this guideline document
- Practice on 20 sample cases
- Achieve 90% agreement with gold standard
- Understand all intent and category definitions
- Be familiar with Tamil language variations

## Updates and Revisions

These guidelines may be updated based on:

- Annotator feedback
- Edge case identification
- New language patterns
- Clarification needs

All changes must be documented and communicated to annotators.
