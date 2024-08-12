from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import mlflow_predict
# from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str


@app.get("/")
def home():
    return {"test": "ok"}


@app.post("/predict")
def predict(payload: TextIn):
    return {"language": mlflow_predict(payload.text)}