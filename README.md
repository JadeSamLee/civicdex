# CivicDex: Multilingual Civic AI Assistant

A multilingual dataset and working AI system that understands and routes civic-service requests in Tamil, Tanglish, and code-mixed language.

## The Problem

Public-service systems receive large volumes of unstructured citizen requests. In regions like Tamil Nadu, these requests are often written in Tamil, Tanglish, or mixed-language formats that existing NLP systems do not handle well.

As a result:
- Requests are not automatically understood
- Routing to the correct department is manual
- Response times increase
- Citizens experience delays and frustration

## The Solution

CivicDex provides:

- A structured multilingual dataset of civic-service requests
- A baseline AI model for intent and category prediction
- A working demo application that simulates real-world request routing

This project demonstrates how AI can be applied to improve civic service workflows in under-resourced language settings.

## Quick Demo

Example input (Tamil):
"எங்கள் தெருவில் மூன்று நாட்களாக குப்பை எடுக்கவில்லை"

Output:
- Intent: complaint
- Category: sanitation
- Department: sanitation department
- Urgency: medium
- English: Garbage not collected for 3 days

## Quick Start

```bash
pip install -r requirements.txt
python baselines/train_model.py
streamlit run app.py