# tests/test_main.py

from fastapi.testclient import TestClient
from src import server

client = TestClient(server)

def test_get_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "server online"}

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data
    assert data["completed"] is False
