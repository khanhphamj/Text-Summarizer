from flask import request, render_template, redirect, url_for, session, flash
from load_model.load import summarizer
from app import app
from models.summaries import Summary
from crud.summary_crud import create_summary
from datetime import datetime
from app import app
from app.db.db import get_db
from services.summarize_and_capitalize import summarize_and_capitalize


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        if text.strip() == "":
            flash("The text field is empty. Please enter some text to summarize.")
            return redirect(url_for('home'))

        summary_text = summarize_and_capitalize(text)
        return render_template('summary.html', original_text=text, summary_text=summary_text)

    return render_template('index.html')


@app.route('/save_summary', methods=['POST'])
def save_summary():
    text = request.form['original_text']
    summary_text = request.form['summary_text']
    rating = int(request.form.get('rating', 0))

    new_summary = Summary(datetime=datetime.now(), main_content=text, summarizer=summary_text, rating=rating)
    with next(get_db()) as db:
        create_summary(db, new_summary)

    flash("Summary saved successfully!")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

