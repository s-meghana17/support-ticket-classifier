# train.py
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the cleaned dataset
df = pd.read_csv("data/clean_tickets.csv")

# Features and labels
X = df["text"]
y = df["category"]

# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text to numbers using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluate model
y_pred = model.predict(X_test_vec)
print("Model Evaluation:\n")
print(classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "models/category_model.pkl")
joblib.dump(vectorizer, "models/tfidf.pkl")

print("Training completed and model saved!")
