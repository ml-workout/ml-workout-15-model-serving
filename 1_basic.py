import pickle
from functools import lru_cache
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

MODEL_PATH = "model/model.pkl"


class InputData(BaseModel):
    sentences: List[str]


class OutputData(BaseModel):
    offensive_probas: List[float]


@lru_cache(maxsize=1)
def get_model(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


@app.get("/healthcheck")
def healthcheck():
    return {"status": "OK"}


@app.post("/predict")
def predict(input_data: InputData) -> OutputData:
    model = get_model(MODEL_PATH)

    preds_probas = model.predict_proba(input_data.sentences)[:, 1]
    output = OutputData(offensive_probas=preds_probas)

    return output
