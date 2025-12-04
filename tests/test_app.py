from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

# 1. Успешный сценарий (Happy Path)
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

# 2. Некорректный ввод (Ошибка валидации)
def test_predict_bad_input():
    # Отсутствует обязательное поле 'income'
    payload = {
        "age": 30,
        "months_on_book": 12,
        "credit_limit": 20000.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

def test_predict_invalid_type():
    # 'age' должно быть int, передана строка
    payload = {
        "age": "thirty", 
        "income": 60000.0,
        "months_on_book": 12,
        "credit_limit": 20000.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422

# 3. Проверка работоспособности (Health Check)
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "model_loaded": True}

# 4. Корневой эндпоинт
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Добро пожаловать в Сервис Прогнозирования Дефолта по Кредитам"}

# 5. Задание со звездочкой: Граничный случай (Ошибка 500)
def test_predict_internal_error():
    # Симуляция деления на ноль передачей income=0
    payload = {
        "age": 30,
        "income": 0.0,
        "months_on_book": 12,
        "credit_limit": 20000.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 500
    assert "Внутренняя ошибка сервера" in response.json()["detail"]

# 6. Тесты из ветки функциональности (Merged)
def test_score_low_risk():
    data = {
        "age": 25,
        "income": 70000,
        "months_on_book": 6,
        "credit_limit": 12000
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "low_risk"

def test_score_high_risk():
    data = {
        "age": 30,
        "income": 25000,
        "months_on_book": 4,
        "credit_limit": 5000
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json()["prediction"] == "high_risk"

def test_score_internal_error():
    data = {
        "age": 30,
        "income": 0,
        "months_on_book": 12,
        "credit_limit": 20000
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 500
    assert "Internal Server Error" in response.json()["detail"]
