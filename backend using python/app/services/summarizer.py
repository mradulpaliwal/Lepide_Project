# app/services/summarizer.py
from transformers import pipeline

summarizer = pipeline("summarization", model="gpt2")

def summarize_document(content: str) -> str:
    summary = summarizer(content, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
