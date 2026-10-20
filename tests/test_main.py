from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Api health check successful"}


def test_nope():
    response = client.get("/nope")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
