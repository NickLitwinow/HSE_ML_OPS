import argparse
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def load_data():
    # Simulate loading data (replace with actual data loading logic later)
    print("Loading synthetic data...")
    X, y = make_classification(
        n_samples=1000, 
        n_features=20, 
        n_informative=10, 
        random_state=42
    )
    return X, y

def train(output_dir="models"):
    X, y = load_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Improved Model: Pipeline with Scaling
    print("Training Improved Model (Scaling + Logistic Regression)...")
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=1000))
    ])
    
    pipeline.fit(X_train, y_train)
    
    # Evaluation
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, "model_v0.2.0.pkl")
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Credit Default Prediction Model")
    parser.add_argument("--output-dir", type=str, default="models", help="Directory to save the model")
    args = parser.parse_args()
    
    train(args.output_dir)
