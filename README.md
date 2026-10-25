
# 🔍 Fake Review Detection and Sentiment Analysis System

A machine learning-based web application that predicts whether a review is likely Fake or Genuine and performs sentiment analysis.

## 📌 Project Overview

This project combines Machine Learning, Natural Language Processing (NLP), and Flask to analyze online reviews.

The system provides:
- Fake / Genuine Review Prediction
- Prediction Confidence Score
- Positive / Negative / Neutral Sentiment
- Low-Confidence Warning
- User-Friendly Web Interface

## 🎯 Objectives

- Identify potentially deceptive reviews.
- Classify reviews as Fake or Genuine.
- Analyze review sentiment.
- Display prediction confidence.
- Provide an easy-to-use web application.

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- TextBlob
- Pandas and NumPy
- Joblib
- HTML and CSS

## 📊 Dataset

Source: Deceptive Opinion Spam Corpus

Dataset type: Hotel reviews

Total reviews: 1000

- Fake Reviews: 500
- Genuine Reviews: 500

Dataset file: `data/reviews_1000.csv`

## 🤖 Machine Learning Model

Algorithm: Logistic Regression

Feature Extraction: TF-IDF

Training Data: 800 reviews

Testing Data: 200 reviews

### Model Evaluation

- Test Accuracy: 89.5%
- Correct Predictions: 179
- Incorrect Predictions: 21

Confusion Matrix:

| Actual / Predicted | Fake | Genuine |
|---|---:|---:|
| Fake | 91 | 9 |
| Genuine | 12 | 88 |

The reported accuracy is based on a held-out hotel review test set. Performance on product reviews has not yet been established.

## ⚙️ System Workflow

1. User enters a review.
2. Flask validates the input.
3. The ML model predicts Fake or Genuine.
4. The system calculates a confidence score.
5. TextBlob analyzes sentiment.
6. Low-confidence predictions are flagged.
7. The final result is displayed.

## ✨ Features

### Fake Review Detection
Predicts whether a review is likely fake or genuine.

### Sentiment Analysis
Classifies sentiment as Positive, Negative, or Neutral.

### Confidence Score
Displays the model's prediction confidence.

### Uncertainty Warning
Predictions below 60% confidence are marked as uncertain.

The 60% threshold is a demonstration rule and has not been scientifically calibrated.

### Web Interface
Provides a responsive interface for entering and analyzing reviews.

## 📂 Project Structure

```text
Sentiment_FakeReview_Project/
├── app.py
├── train_model.py
├── prepare_dataset.py
├── requirements.txt
├── README.md
├── data/
│   └── reviews_1000.csv
├── models/
│   └── fake_review_model.pkl
├── templates/
│   └── index.html
└── documentation/
    ├── system_architecture.md
    ├── methodology.md
    ├── dataset_description.md
    ├── model_evaluation.md
    └── testing_report.md
```

## 🚀 How to Run the Project

### 1. Download the repository

Clone the repository using Git or download its ZIP file from GitHub.

### 2. Open the project folder

Open a terminal in the downloaded project folder.

### 3. Create a virtual environment

```cmd
python -m venv venv
```

### 4. Activate the environment (Windows CMD)

```cmd
venv\Scripts\activate.bat
```

### 5. Install dependencies

```cmd
pip install -r requirements.txt
```

### 6. Start the Flask application

```cmd
python app.py
```

### 7. Open the browser

```text
http://127.0.0.1:5000
```

## 🧪 Testing

Functional testing covered:
- Empty review validation
- Short review validation
- Positive sentiment
- Negative sentiment
- Neutral sentiment
- Confidence scores
- Low-confidence warnings

Detailed testing information is available in `documentation/testing_report.md`.

## ⚠️ Limitations

- The model was trained on hotel reviews.
- Product review performance requires separate evaluation.
- Predictions are probabilistic and may be incorrect.
- Confidence scores do not prove review authenticity.
- More diverse datasets are needed for generalization.

## 🔮 Future Scope

- Larger product-review datasets
- Advanced NLP and Transformer models
- Multilingual sentiment analysis
- Reviewer behavior analysis
- Database integration
- Cloud deployment

## 🎓 Project Information

**Project Title:** Fake Review Detection and Sentiment Analysis System

**Team Name:** ReviewGuard

**Project Type:** Minor Project-I

**Domain:** Artificial Intelligence and Machine Learning

**Application Type:** Web-Based Application

## 👩‍💻 Conclusion

This project demonstrates the integration of Machine Learning, NLP, and Flask for review classification and sentiment analysis.

The system achieved 89.5% test accuracy on the selected hotel review dataset and provides a functional web interface for review analysis.
