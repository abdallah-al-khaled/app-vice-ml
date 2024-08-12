from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import mlflow_predict
# from app.model.model import __version__ as model_version
from typing import Dict
from typing import Any
app = FastAPI()

class TextIn(BaseModel):
    text: str
class PayloadIn(BaseModel):
    data: Dict[str, str]

@app.get("/")
def home():
    return {"test": "ok"}


@app.post("/predict")
def predict(payload: PayloadIn):
    return {"language": payload.data}