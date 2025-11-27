from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Credit Default Prediction Service"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_score_low_risk():
    data = {
        "age": 25,
        "income": 70000,
        "months_on_book": 6,
        "credit_limit": 12000
    }
    response = client.post("/score/", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "low_risk"

def test_score_high_risk():
    data = {
        "age": 30,
        "income": 25000,
        "months_on_book": 4,
        "credit_limit": 5000
    }
    response = client.post("/score/", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "high_risk"
