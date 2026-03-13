import resend
import logging
from app.config import settings
 
# Only log that an email was sent, never the recipient or body (security requirement)
logger = logging.getLogger(__name__)
 
resend.api_key = settings.resend_api_key
 
 
def send_email(to: str, subject: str, body: str) -> dict:
    """
    Sends an email immediately via the Resend API.
    Does not log recipient address or email body.
    """
    params: resend.Emails.SendParams = {
        "from": f"{settings.sender_name} <{settings.sender_email}>",
        "to": [to],
        "subject": subject,
        "html": body,
    }
 
    email = resend.Emails.send(params)
 
    logger.info(f"Email sent successfully. ID: {email['id']}")
 
    return email