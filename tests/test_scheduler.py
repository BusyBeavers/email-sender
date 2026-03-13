from fastapi.testclient import TestClient
from unittest.mock import patch
from datetime import datetime, timezone, timedelta
from app.main import app

client = TestClient(app)


def future_time(minutes=10):
    return (datetime.now(timezone.utc) + timedelta(minutes=minutes)).isoformat()


def past_time(minutes=10):
    return (datetime.now(timezone.utc) - timedelta(minutes=minutes)).isoformat()


def test_schedule_email_success():
    with patch("app.routers.scheduled.schedule_email", return_value="job-abc-123"):
        response = client.post("/email/schedule", json={
            "to": "test@example.com",
            "subject": "Scheduled",
            "body": "<p>Scheduled email</p>",
            "send_at": future_time(),
        })

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["job_id"] == "job-abc-123"


def test_schedule_email_past_datetime():
    response = client.post("/email/schedule", json={
        "to": "test@example.com",
        "subject": "Scheduled",
        "body": "<p>Scheduled email</p>",
        "send_at": past_time(),
    })

    assert response.status_code == 400
    assert "future" in response.json()["detail"].lower()


def test_schedule_email_invalid_address():
    response = client.post("/email/schedule", json={
        "to": "bad-email",
        "subject": "Scheduled",
        "body": "<p>Test</p>",
        "send_at": future_time(),
    })

    assert response.status_code == 422