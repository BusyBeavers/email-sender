import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from datetime import datetime
from app.services.email_service import send_email

logger = logging.getLogger(__name__)
 
jobstores = {
    "default": MemoryJobStore()
}

scheduler = BackgroundScheduler(jobstores=jobstores)
 
def start_scheduler():
    if not scheduler.running:
        scheduler.start()
        logger.info("Scheduler started.")
 
def shutdown_scheduler():
    if scheduler.running:
        scheduler.shutdown()
        logger.info("Scheduler shut down.")
 
def schedule_email(to: str, subject: str, body: str, send_at: datetime) -> str:
    job = scheduler.add_job(
        send_email,
        trigger="date",
        run_date=send_at,
        args=[to, subject, body],
    )
 
    logger.info(f"Email job scheduled. Job ID: {job.id}, Send at: {send_at.isoformat()}")
 
    return job.id