# app.py
from flask import Flask, render_template, request
import joblib
from priority import assign_priority, correct_category

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("models/category_model.pkl")
vectorizer = joblib.load("models/tfidf.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["ticket"]

        # ML prediction
        predicted_category = model.predict(vectorizer.transform([text]))[0]

        # Rule-based override for Billing
        category = correct_category(text, predicted_category)

        # Priority prediction
        priority = assign_priority(text)

        return render_template("index.html",
                               category=category,
                               priority=priority)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
