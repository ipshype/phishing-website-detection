import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    features.append(len(url))                             # URL length
    features.append(1 if "@" in url else 0)               # @ symbol
    features.append(1 if "-" in url else 0)               # dash symbol
    features.append(1 if url.startswith("https") else 0) # HTTPS
    features.append(urlparse(url).netloc.count("."))      # subdomains

    return features
