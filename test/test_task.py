from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Nueva tarea", "description": "demo"})
    assert response.status_code == 200
    assert response.json()["title"] == "Nueva tarea"

def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert type(response.json()) is list
