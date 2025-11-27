from fastapi import FastAPI
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

@app.post("/score/")
def score(client: ClientFeatures):
    prediction_res = predict(
        ml_model,
        client
    )
    return prediction_res
