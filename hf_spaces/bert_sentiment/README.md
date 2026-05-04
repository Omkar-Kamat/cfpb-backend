---
title: CFPB BERT Sentiment
emoji: 🏦
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 3.50.2
python_version: "3.10"
app_file: app.py
pinned: false
---

# CFPB BERT Sentiment Classifier

Fine-tuned BERT for sentiment analysis of CFPB consumer complaint narratives.

**Endpoint:** `POST /run/predict`
**Input:** `{"data": ["complaint text"]}`
**Output:** `{"data": [{"label": "negative", "probs": [0.92, 0.05, 0.03]}]}`

Labels: 0=negative, 1=neutral, 2=positive
