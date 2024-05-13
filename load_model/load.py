import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load the downloaded model and tokenizer
model_path = os.path.abspath("download_model/model/text_summarization_model")
tokenizer_path = os.path.abspath("download_model/tokenizer/text_summarization_tokenizer")

model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

# Create a new summarization pipeline using the downloaded model and tokenizer
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
