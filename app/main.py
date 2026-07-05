from fastapi import FastAPI
import os

app = FastAPI()

REDIS_URL = os.getenv("REDIS_URL")
DATABASE_URL = os.getenv("DATABASE_URL")
QDRANT_URL = os.getenv("QDRANT_URL")


@app.get("/")
def home():
    return {
        "status": "AIFlow running",
        "services": {
            "redis": REDIS_URL,
            "postgres": DATABASE_URL,
            "qdrant": QDRANT_URL
        }
    }