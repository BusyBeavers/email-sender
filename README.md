# Email Sender Microservice
Uses the Resend API to send and schedule emails and FastAPI for docs page.
Runs locally.

Requires a Resend account to test emails. [Sign up here](https://resend.com/signup)

## Setup

1. Navigate to this folder:
```bash
cd email-sender
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and fill in your own Resend API key:
```bash
cp .env.example .env
```

5. Start the server:
```bash
uvicorn app.main:app --reload
```

The server runs at `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` to test the endpoints in your browser.

---
 
## Calling the Service
 
Make sure the server is running first, then call it from your own project.
 
### Send an Email
 
**Python:**
```python
import requests
 
response = requests.post("http://127.0.0.1:8000/email/send", json={
    "to": "recipient@example.com",
    "subject": "Hello",
    "body": "<p>Hello from my app!</p>"
})
 
data = response.json()
print(data)
# {"success": true, "message": "Email sent successfully.", "email_id": "..."}
```
 
**JavaScript (fetch):**
```javascript
const response = await fetch("http://127.0.0.1:8000/email/send", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        to: "recipient@example.com",
        subject: "Hello",
        body: "<p>Hello from my app!</p>"
    })
});
 
const data = await response.json();
console.log(data);
// { success: true, message: "Email sent successfully.", email_id: "..." }
```
 
---
 
### Schedule an Email
 
**Python:**
```python
import requests
 
response = requests.post("http://127.0.0.1:8000/email/schedule", json={
    "to": "recipient@example.com",
    "subject": "Reminder",
    "body": "<p>Don't forget!</p>",
    "send_at": "2025-12-01T10:00:00Z"  # must be a future datetime in ISO 8601 format
})
 
data = response.json()
print(data)
# {"success": true, "message": "Email scheduled successfully.", "job_id": "...", "scheduled_for": "..."}
```
 
**JavaScript (fetch):**
```javascript
const response = await fetch("http://127.0.0.1:8000/email/schedule", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        to: "recipient@example.com",
        subject: "Reminder",
        body: "<p>Don't forget!</p>",
        send_at: "2025-12-01T10:00:00Z"  // must be a future datetime in ISO 8601 format
    })
});
 
const data = await response.json();
console.log(data);
// { success: true, message: "Email scheduled successfully.", job_id: "...", scheduled_for: "..." }
```
 
---

## Running Tests
```bash
python -m pytest
```
