FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm && \
    python -c "import nltk; \
        nltk.download('stopwords'); \
        nltk.download('wordnet'); \
        nltk.download('punkt'); \
        nltk.download('punkt_tab'); \
        nltk.download('omw-1.4')"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]
