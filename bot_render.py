from fastapi import FastAPI
from ai_brain import ask_ai

app = FastAPI()

@app.get("/")
def home():
    return {"status": "NextLevel AI Assistant Running"}

@app.get("/chat")
def chat(message: str):
    return {"reply": ask_ai(message)}
