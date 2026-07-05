from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AIFlow CI/CD Pipeline Working!"
    }