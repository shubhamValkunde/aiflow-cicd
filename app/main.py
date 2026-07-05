from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "AIFlow running",
        "services": {
            "redis": None,
            "postgres": None,
            "qdrant": None
        }
    }


# 🔥 AI AGENT ENDPOINT (FIRST VERSION)
@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message

    return {
        "response": f"You said: {user_message}",
        "memory": {
            "stored": False,
            "reason": "Memory layer not connected yet"
        }
    }