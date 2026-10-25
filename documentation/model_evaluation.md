
# Model Evaluation Report

## Project Title
Fake Review Detection and Sentiment Analysis System

## 1. Model Overview
The system uses TF-IDF for feature extraction
and Logistic Regression for review classification.

The model predicts whether a review is
Fake (Deceptive) or Genuine (Truthful).

## 2. Dataset Details
Dataset: Deceptive Opinion Spam Corpus
Total Reviews: 1000

Fake Reviews: 500
Genuine Reviews: 500

Training Data: 800 reviews (80%)
Testing Data: 200 reviews (20%)

## 3. Model Evaluation Metrics

Accuracy: 89.5%

Classification Report:

Class       Precision   Recall   F1-Score
Fake          0.88       0.91      0.90
Genuine       0.91       0.88      0.89

## 4. Confusion Matrix

                  Predicted
                  Fake   Genuine
Actual Fake        91       9
Actual Genuine     12      88

## 5. Result Interpretation

Out of 200 test reviews:

- 179 reviews were correctly classified.
- 21 reviews were incorrectly classified.
- 91 fake reviews were correctly detected.
- 88 genuine reviews were correctly detected.
- 9 fake reviews were predicted as genuine.
- 12 genuine reviews were predicted as fake.

## 6. Website Testing

Test Case 1:
Review: This product is amazing and I really loved it.
The quality is excellent and I highly recommend it.

Prediction: Uncertain (Likely Fake)
Confidence: 54.6%
Sentiment: Positive

Test Case 2:
Review: I stayed at this hotel for three nights.
The room was clean, the staff was helpful,
and the breakfast was good.
Overall, I had a comfortable stay.

Prediction: Genuine
Confidence: 65.4%
Sentiment: Positive

## 7. Limitations

The model was trained and tested on hotel reviews.

The 89.5% accuracy does not establish the same
performance on general product reviews.

The 60% uncertainty threshold is a demonstration
setting and has not been independently validated.

## 8. Conclusion

The model achieved 89.5% accuracy on the
held-out hotel-review test dataset.

The Flask application successfully integrates
review classification, confidence scoring,
sentiment analysis, and uncertainty warnings.
