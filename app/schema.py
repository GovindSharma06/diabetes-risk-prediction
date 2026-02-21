from pydantic import BaseModel

class DiabetesInput(BaseModel):
    age: float
    hypertension: int
    heart_disease: int
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int
    gender_Male: int
    smoking_history_current: int
    smoking_history_ever: int
    smoking_history_former: int
    smoking_history_never: int
    smoking_history_not_current: int