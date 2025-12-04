from fastapi import FastAPI, HTTPException
from models.dummy_model import load_model, predict, ClientFeatures

app = FastAPI(title="Credit Default Prediction Service")
ml_model = None

@app.on_event("startup")
def startup():
    global ml_model
    ml_model = load_model()
    return ml_model

@app.get("/")
def read_root():
    return {"message": "Welcome to the Credit Default Prediction Service"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(client: ClientFeatures):
    try:
        # --- Star Task: Edge Case Handling ---
        if client.income == 0:
            raise ZeroDivisionError("Income cannot be zero for score calculation")
            
        prediction_res = predict(
            ml_model,
            client
        )
        return prediction_res
        
    except ZeroDivisionError as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")
