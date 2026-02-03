import pandas as pd
import pickle
import os
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ---------- FEATURE EXTRACTION ----------
def extract_features(url):
    features = []

    features.append(len(url))                             # URL length
    features.append(1 if "@" in url else 0)               # @ symbol
    features.append(1 if "-" in url else 0)               # dash symbol
    features.append(1 if url.startswith("https") else 0) # HTTPS
    features.append(urlparse(url).netloc.count("."))      # subdomains

    return features

# ---------- LOAD DATASET ----------
data = pd.read_csv("dataset/phishing.csv")

# Assume dataset has columns: 'URL' and 'Result'
urls = data["URL"]
labels = data["Result"]

# ---------- EXTRACT FEATURES ----------
X = [extract_features(url) for url in urls]
y = labels

# ---------- TRAIN TEST SPLIT ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------- TRAIN MODEL ----------
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# ---------- EVALUATE ----------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# ---------- SAVE MODEL ----------
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/model.pkl", "wb"))

print("Model retrained and saved successfully")
