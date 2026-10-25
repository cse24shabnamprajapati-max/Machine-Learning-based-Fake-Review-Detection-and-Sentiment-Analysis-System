
# System Architecture

## Project Title
Fake Review Detection and Sentiment Analysis System

## 1. Overview
The proposed system is a web-based application that uses
Machine Learning and Natural Language Processing (NLP)
to analyze reviews and predict whether they are likely
to be fake or genuine.

The system also identifies the sentiment of a review
as Positive, Negative, or Neutral.

## 2. System Architecture

User Enters Review
        |
        v
Flask Web Application
        |
        v
Input Validation
        |
        +-----------------------+
        |                       |
        v                       v
Machine Learning Model     TextBlob
        |                       |
        v                       v
Fake/Genuine Prediction    Sentiment Analysis
        |
        v
Confidence Score
        |
        +-----------------------+
        |
        v
Low Confidence Check
        |
        v
Final Result Displayed on Website

## 3. Main Components

### Frontend
HTML and CSS provide a simple interface where users
can enter reviews and view prediction results.

### Backend
Python and Flask handle user requests, input validation,
model prediction, and result display.

### Machine Learning
TF-IDF converts review text into numerical features.
Logistic Regression classifies reviews as Fake or Genuine.

### Sentiment Analysis
TextBlob analyzes the polarity of reviews and classifies
sentiment as Positive, Negative, or Neutral.

### Dataset
The model uses 1,000 labeled hotel reviews:
- 500 Fake (Deceptive)
- 500 Genuine (Truthful)

### Confidence Score
The model provides a prediction probability.
Predictions below 60% confidence are displayed
with an uncertainty warning.

## 4. Model Performance
Training Samples: 800
Testing Samples: 200
Test Accuracy: 89.5%

Note: The model was evaluated on hotel reviews.
Performance on general product reviews has not
yet been established.

## 5. Conclusion
The system combines Machine Learning, NLP, and
a Flask web interface to provide review classification,
confidence scores, and sentiment analysis.
