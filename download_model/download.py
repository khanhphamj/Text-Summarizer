from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# Save the model and tokenizer
summarizer.model.save_pretrained("model/text_summarization_model")
summarizer.tokenizer.save_pretrained("tokenizer/text_summarization_tokenizer")