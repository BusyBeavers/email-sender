from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import email, scheduled
from app.services.scheduler import start_scheduler, shutdown_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the scheduler when the app starts
    start_scheduler()
    yield
    # Shut it down cleanly when the app stops
    shutdown_scheduler()

app = FastAPI(
    title="Email Sender Microservice",
    description="Send and schedule emails via the Resend API.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(email.router)
app.include_router(scheduled.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}