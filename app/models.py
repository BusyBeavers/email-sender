from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
 
class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
 
class ScheduledEmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    send_at: datetime  # must be a future datetime
 
class EmailResponse(BaseModel):
    success: bool
    message: str
    email_id: Optional[str] = None
 
class ScheduledEmailResponse(BaseModel):
    success: bool
    message: str
    job_id: Optional[str] = None
    scheduled_for: Optional[datetime] = None