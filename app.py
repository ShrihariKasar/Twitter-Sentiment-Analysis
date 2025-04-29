from flask import Flask, render_template, request, redirect, url_for, session
from transformers import pipeline

app = Flask(__name__)

# Use the generated secret key
app.secret_key = b"\x9d\xf1D\x92\x80\xbd\x9c\x9d1\xf7\x881\xca\xe0g\x8b'\x19],\xc0b\x80\xea"

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tweet = request.form["tweet"]
        result = classifier(tweet)[0]
        session["tweet"] = tweet  # Store the tweet in session
        session["sentiment"] = result['label'].capitalize()
        session["confidence"] = round(result['score'] * 100, 2)
        return redirect(url_for("index"))

    tweet = session.pop("tweet", None)
    sentiment = session.pop("sentiment", None)
    confidence = session.pop("confidence", None)
    return render_template("index.html", tweet=tweet, sentiment=sentiment, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)