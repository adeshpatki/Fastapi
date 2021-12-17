import uvicorn
from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Sentiment(BaseModel):
    sentiment: str
    sentiment_probability: float



nlp = pipeline("sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english",
                tokenizer="distilbert-base-uncased-finetuned-sst-2-english")
def generate(data):
    return nlp(data)


@app.get('/')
def get_root():
        return{'message': 'welcome to api'}

@app.get('/api/v1/st')
def sentiment_analysis(data: str):
    sentiment = generate(data)
    return sentiment[0]


