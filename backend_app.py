from fastapi import FastAPI, UploadFile, File
import pandas as pd
import pickle

app = FastAPI()

with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    predictions = model.predict(df)
    results = ["Fraud" if pred==1 else "Not Fraud" for pred in predictions]

    return {"predictions": results}
