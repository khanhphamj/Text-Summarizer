from load_model.load import summarizer


def summarize_and_capitalize(text):
    summary_text = summarizer(text, max_length=1000, min_length=30, do_sample=False)[0]["summary_text"]
    sentences = summary_text.split('. ')
    sentences = [sentence[0].upper() + sentence[1:] for sentence in sentences]
    return '. '.join(sentences)