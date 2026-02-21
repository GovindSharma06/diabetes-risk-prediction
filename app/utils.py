import joblib
import pandas as pd

model = joblib.load("models/final_diabetes_model.pkl")
features = joblib.load("models/model_features.pkl")
threshold = joblib.load("models/model_threshold.pkl")

def predict_diabetes(data_dict):

    df = pd.DataFrame([data_dict])
    df = df[features]

    prob = model.predict_proba(df)[:,1][0]
    prediction = int(prob >= threshold)

    return prob, prediction