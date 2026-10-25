
# Dataset Description

## Project Title
Fake Review Detection and Sentiment Analysis System

## 1. Dataset Overview
The project uses the Deceptive Opinion Spam Corpus,
a dataset containing truthful and deceptive hotel reviews.

The dataset was downloaded from Kaggle and prepared
for Machine Learning classification.

## 2. Dataset Information
Original Dataset: Deceptive Opinion Spam Corpus
Original Reviews: 1,600
Selected Reviews: 1,000

Review Categories:
- Fake (Deceptive): 500
- Genuine (Truthful): 500

Dataset Format: CSV

## 3. Dataset Files
Original Dataset:
data/deceptive-opinion.csv

Prepared Dataset:
data/reviews_1000.csv

## 4. Dataset Columns

The prepared dataset contains two columns:

review:
Contains the text of a hotel review.

label:
Contains the classification label:
- fake
- genuine

## 5. Data Preparation
The following steps were performed:

1. Loaded the original dataset using Pandas.
2. Selected review text and deceptive labels.
3. Renamed the columns to review and label.
4. Converted deceptive to fake.
5. Converted truthful to genuine.
6. Removed missing and duplicate reviews.
7. Selected 500 reviews from each category.
8. Shuffled the selected reviews.
9. Saved the prepared dataset as reviews_1000.csv.

## 6. Training and Testing

Total Reviews: 1,000

Training Set: 800 reviews (80%)
Testing Set: 200 reviews (20%)

Stratified splitting maintained equal class proportions.

## 7. Model Performance

Algorithm: Logistic Regression
Feature Extraction: TF-IDF

Test Accuracy: 89.5%

Fake Class:
Precision: 0.88
Recall: 0.91
F1-Score: 0.90

Genuine Class:
Precision: 0.91
Recall: 0.88
F1-Score: 0.89

## 8. Dataset Limitations

The dataset contains hotel reviews rather than
general e-commerce product reviews.

Therefore, the reported test accuracy applies
to the selected hotel-review dataset.

Additional product-review data and evaluation
are needed before claiming reliable performance
on online shopping reviews.

## 9. Conclusion

The prepared balanced dataset supports training
and evaluating the Fake Review Detection model.
