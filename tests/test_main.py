from fastapi.testclient import TestClient
from app.main import app
#good

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "AIFlow running"
    assert "services" in data
    assert "redis" in data["services"]
    assert "postgres" in data["services"]
    assert "qdrant" in data["services"]