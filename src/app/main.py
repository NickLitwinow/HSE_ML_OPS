from fastapi import FastAPI, HTTPException
from src.models.dummy_model import load_model as load_dummy_model, predict as dummy_predict, ClientFeatures
import os
import joblib

app = FastAPI(title="Сервис Прогнозирования Дефолта по Кредитам")

# --- Глобальное состояние ---
model = None

# --- Событие запуска ---
@app.on_event("startup")
def load_model():
    global model
    # Попытка загрузить реальную модель, откат к заглушке, если не найдена
    model_path = "models/model_v0.2.0.pkl"
    if os.path.exists(model_path):
        print(f"Загрузка реальной модели из {model_path}...")
        try:
            model = joblib.load(model_path)
            print("Реальная модель успешно загружена.")
        except Exception as e:
            print(f"Не удалось загрузить реальную модель: {e}. Используется заглушка.")
            model = "dummy"
    else:
        print("Файл модели не найден. Используется заглушка.")
        model = "dummy"

# --- Эндпоинты ---
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в Сервис Прогнозирования Дефолта по Кредитам"}

@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Модель не загружена")
    return {"status": "ok", "model_loaded": True}

@app.post("/predict")
def predict_endpoint(client: ClientFeatures):
    try:
        # --- Задание со звездочкой: Обработка граничных случаев ---
        # Симуляция критической ошибки (например, деление на ноль), если доход равен 0
        if client.income == 0:
            raise ZeroDivisionError("Доход не может быть равен нулю для расчета скоринга")
            
        if model == "dummy":
            # Использование логики заглушки
            result = dummy_predict({"version": "1.0-dummy"}, client)
            result["version"] = "1.0-dummy"
            return result
            
        elif model:
            # Логика реальной модели (пока используем заглушку для безопасности в демо)
            # В реальном сценарии здесь было бы model.predict(features)
            result = dummy_predict({"version": "v0.2.0-simulated"}, client)
            result["model_version"] = "v0.2.0-simulated"
            return result
        else:
            raise HTTPException(status_code=503, detail="Модель не инициализирована")
            
    except ZeroDivisionError as e:
        # Перехват специфической ошибки и возврат 500
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")
    except Exception as e:
        # Перехват всех остальных ошибок
        raise HTTPException(status_code=500, detail=f"Непредвиденная ошибка: {str(e)}")
