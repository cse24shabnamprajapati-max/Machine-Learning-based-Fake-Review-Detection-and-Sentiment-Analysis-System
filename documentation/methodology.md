
# Project Methodology

## Project Title
Fake Review Detection and Sentiment Analysis System

## 1. Dataset Collection
The Deceptive Opinion Spam Corpus was used for
training and evaluating the Machine Learning model.

A balanced dataset of 1,000 hotel reviews was prepared:
- 500 Deceptive (Fake) reviews
- 500 Truthful (Genuine) reviews

## 2. Data Preprocessing
The dataset was processed using Python and Pandas.

The following operations were performed:
- Selected review text and labels
- Converted deceptive labels into Fake/Genuine
- Removed missing values
- Removed duplicate reviews
- Randomly shuffled the dataset

## 3. Feature Extraction
TF-IDF (Term Frequency-Inverse Document Frequency)
was used to convert review text into numerical features.

The vectorizer uses:
- English stop-word removal
- Maximum 5,000 features
- Unigrams and bigrams

## 4. Dataset Splitting
The dataset was divided into:
- 80% Training Data (800 reviews)
- 20% Testing Data (200 reviews)

Stratified sampling was used to maintain
balanced class distribution.

## 5. Model Training
Logistic Regression was selected as the
Machine Learning classification algorithm.

The model was trained using the training dataset
and evaluated on unseen test samples.

## 6. Fake Review Detection
The trained model analyzes the entered review
and predicts one of two classes:
- Fake
- Genuine

## 7. Confidence Score
The system uses model prediction probabilities
to display a confidence score.

If the highest probability is below 60%,
the system displays an uncertainty warning.

This threshold is a demonstration setting,
not a scientifically validated cutoff.

## 8. Sentiment Analysis
TextBlob is used to calculate sentiment polarity.

Sentiment is classified as:
- Positive: polarity > 0.1
- Negative: polarity < -0.1
- Neutral: polarity between -0.1 and 0.1

## 9. Model Evaluation
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Test Accuracy: 89.5%

Confusion Matrix:
                 Predicted
                 Fake  Genuine
Actual Fake       91      9
Actual Genuine    12     88

## 10. Web Application
Flask connects the trained ML model
with the HTML/CSS frontend.

The user enters a review, clicks Analyze Review,
and receives:
- Fake/Genuine prediction
- Confidence score
- Sentiment classification
- Uncertainty warning when applicable

## 11. Limitations
The model was trained on hotel reviews.
Its performance on general product reviews
has not yet been established.

Prediction probabilities should not be treated
as proof that a review is fake or genuine.

## 12. Conclusion
The proposed system integrates Machine Learning,
Natural Language Processing, and web development
to classify reviews and analyze sentiment.
