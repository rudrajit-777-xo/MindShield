import joblib

model = joblib.load("models/model.pkl")

def predict_risk(features):
    return model.predict([features])[0]