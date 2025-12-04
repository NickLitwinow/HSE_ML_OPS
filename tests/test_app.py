from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_predict_happy_path():
    payload = {
        "age": 30,
        "income": 60000.0,
        "months_on_book": 12,
        "credit_limit": 20000.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "score" in data
    assert data["prediction"] in ["low_risk", "high_risk"]
    assert isinstance(data["score"], float)

def test_predict_bad_input():
    payload = {
        "age": 30,
        "months_on_book": 12,
        "credit_limit": 20000.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_predict_invalid_type():
    payload = {
        "age": "thirty", 
        "income": 60000.0,
        "months_on_book": 12,
        "credit_limit": 20000.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "model_loaded": True}

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Credit Default Prediction Service"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
