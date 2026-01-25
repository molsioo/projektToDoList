from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_create_and_list_tasks():
    r = client.post("/tasks", json={"title": "Test"})
    assert r.status_code == 200

    r = client.get("/tasks")
    assert r.status_code == 200
    assert len(r.json()) >= 1
