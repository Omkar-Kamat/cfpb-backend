---
title: CFPB T5 Summarizer
emoji: 📝
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: 3.50.2
python_version: "3.10"
app_file: app.py
pinned: false
---

# CFPB T5 Summarizer

Abstractive summarization of CFPB complaint narratives using `t5-base`.

**Endpoint:** `POST /run/predict`
**Input:** `{"data": ["text to summarize"]}`
**Output:** `{"data": ["summary text"]}`

Inputs shorter than 40 words are returned unchanged.
