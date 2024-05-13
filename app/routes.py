from flask import request, render_template
from load_model.load import summarizer
from app import app
from models.summaries import Summary
from crud.summary_crud import create_summary
from datetime import datetime
from app import app
from app.db.db import get_db


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        summary_text = summarizer(text, max_length=1000, min_length=30, do_sample=False)[0]["summary_text"]

        # Create a new summary
        new_summary = Summary(datetime=datetime.now(), main_content=text, summarizer=summary_text)

        # Get a database session
        db = next(get_db())

        # Add the new summary to the database
        create_summary(db, new_summary)

        return render_template('summary.html', original_text=text, summary_text=summary_text)
    return render_template('index.html')
