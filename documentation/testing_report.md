
# Testing Report

## Project Title
Fake Review Detection and Sentiment Analysis System

## 1. Testing Objective
To verify the functionality of the Flask web application,
including input validation, review classification,
confidence scores, and sentiment analysis.

## 2. Functional Test Cases

### Test Case 1: Empty Review
Input: Empty review box
Expected: Input validation warning
Actual: "Please fill in this field."
Status: PASS

### Test Case 2: Short Review
Input: Good product
Expected: Short review warning
Actual: Please enter a longer review for better analysis.
Status: PASS

### Test Case 3: Positive Review
Input: This product is amazing and I really loved it.
The quality is excellent and I highly recommend it.

Actual Result:
Prediction: Uncertain (Likely Fake)
Confidence: 54.6%
Sentiment: Positive
Status: PASS (Functional output verified)

### Test Case 4: Negative Review
Input: The product quality is very poor. It stopped
working after two days and I am extremely
disappointed with my purchase.

Actual Result:
Prediction: Uncertain (Likely Genuine)
Confidence: 51.9%
Sentiment: Negative
Status: PASS (Functional output verified)

### Test Case 5: Neutral Review
Input: The package arrived on Monday. It contains
one charger, a cable, and a user manual.

Actual Result:
Prediction: Uncertain (Likely Fake)
Confidence: 50.0%
Sentiment: Neutral
Status: PASS (Functional output verified)

### Test Case 6: Hotel Review
Input: I stayed at this hotel for three nights.
The room was clean, the staff was helpful,
and the breakfast was good.
Overall, I had a comfortable stay.

Actual Result:
Prediction: Genuine
Confidence: 65.4%
Sentiment: Positive
Status: PASS (Functional output verified)

## 3. Model Evaluation
Total Reviews: 1000
Training Reviews: 800
Testing Reviews: 200
Test Accuracy: 89.5%

Correct Predictions: 179
Incorrect Predictions: 21

## 4. Observations
- Input validation works correctly.
- Positive, Negative, and Neutral sentiments are displayed.
- Confidence scores are generated.
- Low-confidence predictions display warnings.
- The Flask application processes reviews successfully.

## 5. Limitations
Functional test success does not prove that every
Fake/Genuine prediction is correct.

The model was trained on hotel reviews, so
product-review performance requires further testing.

## 6. Conclusion
The implemented application passed the selected
functional tests. Further testing with labeled
product reviews is recommended.
