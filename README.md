# 🔍 Fake Review Detection System

A machine learning based web application that analyzes product reviews and predicts whether they are likely to be **Fake or Genuine**. The system also performs **Sentiment Analysis** to identify whether the review is **Positive, Negative, or Neutral**.

## 📌 Project Overview

Online shopping platforms contain a large number of customer reviews. Some reviews may be misleading, promotional, or artificially generated.

This project uses **Machine Learning and Natural Language Processing (NLP)** to analyze product reviews and provide an automated prediction.

The system displays:

* 🔎 Fake/Genuine Review Prediction
* 📊 Prediction Confidence
* 😊 Sentiment Analysis
* 💻 User-friendly Web Interface

## 🎯 Objectives

* Detect potentially fake product reviews.
* Classify reviews as Fake or Genuine.
* Analyze the sentiment of a review.
* Display the model's confidence score.
* Provide a simple web-based interface for users.

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Scikit-learn**
* **Joblib**
* **TextBlob**
* **Pandas**
* **NumPy**
* **HTML**
* **CSS**

## ⚙️ How It Works

```text
User enters a product review
          ↓
     Flask Web App
          ↓
 Machine Learning Model
          ↓
   Fake / Genuine
          ↓
   Confidence Score
          ↓
 Sentiment Analysis
          ↓
Positive / Negative / Neutral
          ↓
      Final Result
```

## 📂 Project Structure

```text
Sentiment_FakeReview_Project/
│
├── app.py
├── README.md
│
├── models/
│   └── fake_review_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── data/
│
└── notebooks/
```

## 🚀 How to Run the Project

### 1. Open the project folder

```cmd
cd C:\shab\Sentiment_FakeReview_Project
```

### 2. Activate the virtual environment

```cmd
venv\Scripts\activate.bat
```

### 3. Run the Flask application

```cmd
python app.py
```

### 4. Open in browser

```text
http://127.0.0.1:5000
```

## 🧪 Example

### Input

```text
This product is amazing and I really loved it. The quality is excellent and I highly recommend it.
```

### Output

```text
Genuine Review
Confidence: 60.9%
Sentiment: Positive
```

## ✨ Features

### 1. Fake Review Detection

The trained machine learning model predicts whether a review is likely to be fake or genuine.

### 2. Sentiment Analysis

The system identifies the sentiment of the review as:

* Positive
* Negative
* Neutral

### 3. Confidence Score

The system displays the confidence associated with the model's prediction.

### 4. Web Interface

Users can enter a review directly through the browser and receive the analysis.

## ⚠️ Limitations

The prediction depends on the quality of the training data and the patterns learned by the machine learning model. A model confidence score should not be considered absolute proof that a review is fake or genuine.

## 🔮 Future Scope

* Larger and more diverse datasets
* Advanced NLP techniques
* Deep Learning models
* Transformer-based models
* Reviewer behavior analysis
* Detection of repeated or copied reviews
* Database integration
* Multilingual review analysis
* Cloud deployment

## 🎓 Project Information

**Project:** Fake Review Detection System
**Type:** 3rd Year Minor Project
**Domain:** Machine Learning + NLP + Web Development

## 👩‍💻 Conclusion

The Fake Review Detection System demonstrates how Machine Learning and Natural Language Processing can be used to analyze online product reviews. The system combines fake review detection with sentiment analysis and provides the result through a simple web interface.
