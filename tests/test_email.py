from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


def test_send_email_success():
    mock_response = {"id": "test-email-id-123"}

    with patch("app.routers.email.send_email", return_value=mock_response):
        response = client.post("/email/send", json={
            "to": "test@example.com",
            "subject": "Hello",
            "body": "<p>Test email</p>",
        })

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["email_id"] == "test-email-id-123"


def test_send_email_invalid_address():
    response = client.post("/email/send", json={
        "to": "not-an-email",
        "subject": "Hello",
        "body": "<p>Test</p>",
    })

    assert response.status_code == 422  # Pydantic validation error


def test_send_email_service_failure():
    with patch("app.routers.email.send_email", side_effect=Exception("Resend API error")):
        response = client.post("/email/send", json={
            "to": "test@example.com",
            "subject": "Hello",
            "body": "<p>Test</p>",
        })

    assert response.status_code == 500


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}