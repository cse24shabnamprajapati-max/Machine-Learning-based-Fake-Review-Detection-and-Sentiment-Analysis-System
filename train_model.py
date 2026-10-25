
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "reviews_1000.csv"
MODEL_PATH = BASE_DIR / "models" / "fake_review_model.pkl"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Remove missing and duplicate reviews
df = df.dropna(subset=["review", "label"])
df = df.drop_duplicates(subset=["review"])

print("Total Reviews:", len(df))
print(df["label"].value_counts())

# Features and labels
X = df["review"]
y = df["label"]

# Split dataset: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1, 2)
    )),
    ("classifier", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Evaluation
print("\nModel Evaluation")
print("------------------------")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=["fake", "genuine"]))

# Save trained model
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, MODEL_PATH)

print("\nModel trained successfully!")
print("Saved as:", MODEL_PATH)
