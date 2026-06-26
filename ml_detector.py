import joblib
from .feature_extractor import extract_features

model = joblib.load("waf_model.pkl")

def ml_check(text: str):
    features = extract_features(text)

    pred = model.predict([features])[0]
    score = model.decision_function([features])[0]

    if pred == -1:
        return "malicious", float(score)

    return "clean", float(score)
