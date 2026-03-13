from fastapi import APIRouter, HTTPException
from app.models import ScheduledEmailRequest, ScheduledEmailResponse
from app.services.scheduler import schedule_email
from app.utils.validation import is_future_datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/email", tags=["scheduled email"])

@router.post("/schedule", response_model=ScheduledEmailResponse)
def schedule_email_endpoint(request: ScheduledEmailRequest):
    if not is_future_datetime(request.send_at):
        raise HTTPException(
            status_code=400,
            detail="send_at must be a datetime in the future."
        )

    try:
        job_id = schedule_email(
            to=request.to,
            subject=request.subject,
            body=request.body,
            send_at=request.send_at,
        )
        return ScheduledEmailResponse(
            success=True,
            message="Email scheduled successfully.",
            job_id=job_id,
            scheduled_for=request.send_at,
        )
    except Exception as e:
        logger.error(f"Failed to schedule email: {type(e).__name__}")
        raise HTTPException(status_code=500, detail="Failed to schedule email.")