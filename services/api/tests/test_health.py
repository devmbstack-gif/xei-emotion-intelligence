"""Smoke tests for health and root routes."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "XEI Emotion Intelligence"
    assert "empathic AI" in body["message"]


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_v1_status() -> None:
    response = client.get("/v1/status")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["capability"] == "emotion-aware AI"
