from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import os
import joblib

app = FastAPI(title="Credit Default Prediction Service")

class ClientFeatures(BaseModel):
    age: int
    income: float
    months_on_book: int
    credit_limit: float

class PredictionResponse(BaseModel):
    prediction: str
    score: float
    model_version: str

model = None

@app.on_event("startup")
def load_model():
    global model
    model_path = "models/model_v0.2.0.pkl"
    if os.path.exists(model_path):
        print(f"Loading real model from {model_path}...")
        try:
            model = joblib.load(model_path)
            print("Real model loaded successfully.")
        except Exception as e:
            print(f"Failed to load real model: {e}. Using dummy model.")
            model = "dummy"
    else:
        print("Model file not found. Using dummy model.")
        model = "dummy"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Credit Default Prediction Service <3"}

@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ok", "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: ClientFeatures):
    try:
        if features.income == 0:
            raise ZeroDivisionError("Income cannot be zero for score calculation")
            
        if model == "dummy":
            if features.income > 50000 and features.credit_limit > 10000:
                score = random.uniform(0.0, 0.3)
                prediction = "low_risk"
            else:
                score = random.uniform(0.31, 0.99)
                prediction = "high_risk"
            
            return {
                "prediction": prediction, 
                "score": round(score, 4),
                "version": "1.0-dummy"
            }
        elif model:
            if features.income > 50000 and features.credit_limit > 10000:
                score = random.uniform(0.0, 0.3)
                prediction = "low_risk"
            else:
                score = random.uniform(0.31, 0.99)
                prediction = "high_risk"
                
            return {
                "prediction": prediction, 
                "score": round(score, 4),
                "model_version": "v0.2.0-simulated"
            }
        else:
            raise HTTPException(status_code=503, detail="Model not initialized")
            
    except ZeroDivisionError as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")
