from flask import Flask, render_template, request
import joblib
from textblob import TextBlob

app = Flask(__name__)

# Load trained ML model

model = joblib.load("models/fake_review_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    review = ""
    result = ""

    if request.method == "POST":
        review = request.form.get("review", "").strip()
    if not review:
        result = "⚠️ Please enter a product review."

    elif len(review.split()) < 3:
        result = "⚠️ Please enter a longer review for better analysis."

    else:
        # Fake/Genuine prediction
        prediction = model.predict([review])[0]

        # Confidence score
        probabilities = model.predict_proba([review])[0]
        confidence = max(probabilities) * 100

        # Sentiment analysis
        sentiment_score = TextBlob(review).sentiment.polarity

        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Final result
        if prediction == "fake":
            result = (
                f"⚠️ Fake Review Detected | "
                f"Confidence: {confidence:.1f}% | "
                f"Sentiment: {sentiment}"
            )
        else:
            result = (
                f"✅ Genuine Review | "
                f"Confidence: {confidence:.1f}% | "
                f"Sentiment: {sentiment}"
            )

    return render_template(
        "index.html",
        review=review,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)