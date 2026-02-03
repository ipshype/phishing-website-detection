from flask import Flask, request, render_template_string
import numpy as np
from feature_extraction import extract_features

app = Flask(__name__)

# Load HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_template = f.read()

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]

    # Extract 5 URL-based features
    features = extract_features(url)
    features = np.array(features).reshape(1, -1)

    # ---- SIMPLE PHISHING DETECTION LOGIC ----
    score = 0

    if features[0][0] > 75:   # long URL
        score += 1
    if features[0][1] == 1:   # @ symbol
        score += 1
    if features[0][2] == 1:   # dash (-)
        score += 1
    if features[0][3] == 0:   # not HTTPS
        score += 1
    if features[0][4] > 3:    # many subdomains
        score += 1

    if score >= 3:
        result = "🚨 Phishing Website"
    else:
        result = "✅ Legitimate Website"

    return render_template_string(html_template, prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)

