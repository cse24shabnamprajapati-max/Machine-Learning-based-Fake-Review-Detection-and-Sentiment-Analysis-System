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

        # Check empty review
        if not review:
            result = "⚠️ Please enter a product review."

        # Check very short review
        elif len(review.split()) < 3:
            result = "⚠️ Please enter a longer review for better analysis."

        else:
            # -----------------------------
            # Fake / Genuine Prediction
            # -----------------------------
            prediction = model.predict([review])[0]

            # Confidence score
            probabilities = model.predict_proba([review])[0]
            confidence = max(probabilities) * 100

            # -----------------------------
            # Sentiment Analysis
            # -----------------------------
            sentiment_score = TextBlob(review).sentiment.polarity

            # Neutral range:
            # -0.1 to +0.1
            if sentiment_score > 0.1:
                sentiment = "Positive"
            elif sentiment_score < -0.1:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            # -----------------------------
            # Final Result
            # -----------------------------
            if confidence < 60:
                result = (
                    f"⚠️ Uncertain Prediction | "
                    f"Likely: {prediction.capitalize()} | "
                    f"Confidence: {confidence:.1f}% | "
                    f"Sentiment: {sentiment} | "
                    f"Low confidence - interpret with caution."
                )

            elif prediction == "fake":
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
