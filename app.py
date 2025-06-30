from flask import Flask, request, jsonify
from textblob import TextBlob
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Sentiment Analysis API!"})

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Please provide JSON with a 'text' field"}), 400

    text = data["text"]
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
    elif polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "negative"

    return jsonify({
        "text": text,
        "polarity": polarity,
        "sentiment": sentiment
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
