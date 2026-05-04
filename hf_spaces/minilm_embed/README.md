---
license: mit
language: en
library_name: transformers
pipeline_tag: text-classification
tags:
  - bert
  - sentiment
  - cfpb
  - finance
  - complaints
---

# CFPB BERT Sentiment Classifier

Fine-tuned BERT for sentiment analysis of CFPB consumer complaint narratives.

## Labels

| ID | Label    |
|----|----------|
| 0  | negative |
| 1  | neutral  |
| 2  | positive |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("[32m✓ Logged in[0m/cfpb-bert-sentiment")
m   = AutoModelForSequenceClassification.from_pretrained("[32m✓ Logged in[0m/cfpb-bert-sentiment")
m.eval()

x = tok("The bank ignored my dispute.", return_tensors="pt",
        max_length=128, padding="max_length", truncation=True)
with torch.no_grad():
    probs = torch.softmax(m(**x).logits, dim=1)[0]

print(["negative","neutral","positive"][int(probs.argmax())], probs.tolist())
```

Base model: `bert-base-uncased`. Max sequence length: 128.
