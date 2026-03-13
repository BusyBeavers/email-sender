# Email Sender Microservice
Uses the Resend API to send and schedule emails and FastAPI for docs page.

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

## Running Tests
```bash
python -m pytest
```
