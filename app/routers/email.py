from fastapi import APIRouter, HTTPException
from app.models import EmailRequest, EmailResponse
from app.services.email_service import send_email
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/email", tags=["email"])


@router.post("/send", response_model=EmailResponse)
def send_email_now(request: EmailRequest):
    try:
        result = send_email(
            to=request.to,
            subject=request.subject,
            body=request.body,
        )
        return EmailResponse(
            success=True,
            message="Email sent successfully.",
            email_id=result.get("id"),
        )
    except Exception as e:
        logger.error(f"Failed to send email: {type(e).__name__}")
        raise HTTPException(status_code=500, detail="Failed to send email.")