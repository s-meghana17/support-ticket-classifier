# Customer Support Ticket Classifier

This project classifies customer support tickets into categories such as:

- Technical
- Billing
- Cancellation
- Product
- Refund

It also assigns a priority level (Low / Medium / High).

## Tech Stack
- Python
- Scikit-learn (TF-IDF + Logistic Regression)
- Flask
- Rule-based priority system

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Train model:
   python train.py

3. Run Flask app:
   python app.py

4. Open browser:
   http://127.0.0.1:5000/

## Features
- Multi-class text classification
- Business rule overrides for better accuracy
- Web interface using Flask
