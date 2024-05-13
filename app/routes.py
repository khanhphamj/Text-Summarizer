from flask import request, render_template
from load_model.load import summarizer
from app import app


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        summary = summarizer(text, max_length=1000, min_length=30, do_sample=False)
        return render_template('summary.html', original_text=text, summary_text=summary[0]["summary_text"])
    return render_template('index.html')
