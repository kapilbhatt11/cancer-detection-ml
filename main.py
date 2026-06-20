from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Cancer Detection API")

# Model aur scaler load karo
with open('cancer_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Input format define karo
class PatientData(BaseModel):
    features: list[float]  # 30 features

@app.get("/")
def home():
    return {"message": "Cancer Detection API is running!"}


@app.post("/predict")
def predict(data: PatientData):
    # Scale karo
    features = np.array(data.features).reshape(1, -1)
    scaled = scaler.transform(features)
    
    # Predict karo
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0]

    print(f"Raw probability: {probability}")  # ← ye add karo

    return {
        "prediction": int(prediction),
        "result": "Benign" if prediction == 1 else "Malignant",
        "confidence": f"{round(float(max(probability)) * 100, 2)}%"
    }
    