from fastapi import FastAPI
from app.schema import DiabetesInput
from app.utils import predict_diabetes
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Diabetes Prediction API"}



@app.post("/predict")
def predict(input_data: DiabetesInput):

    try:
        prob, pred = predict_diabetes(input_data.dict())
        return {
            "probability": round(prob, 4),
            "prediction": pred
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))