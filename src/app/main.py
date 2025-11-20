from fastapi import FastAPI

app = FastAPI(title="Credit Default Prediction Service")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Credit Default Prediction Service"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
