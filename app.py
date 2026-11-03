from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import joblib

app = FastAPI(title="Mini Ticket Router")
MODEL_PATH = Path(__file__).parent / "router.joblib"
model = joblib.load(MODEL_PATH)
TEAMS = ["comp.graphics", "rec.autos", "sci.med", "talk.politics.guns"]

class Ticket(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(ticket: Ticket):
    probs = model.predict_proba([ticket.text])[0]
    best = int(probs.argmax())
    return {"team": TEAMS[best], "confidence": round(float(probs[best]), 3)}