from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 200

    data = response.json()
    assert "response" in data
    assert "You said: hello" in data["response"]