from pipeline.pipeline import run_pipeline

from router.routes import router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import threading
from sqlalchemy import func


# Configure server
app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["GET"],
)


# Schedule data pipeline
scheduler = BackgroundScheduler()

@app.on_event("startup")
def startup():

    scheduler.start()
    
    # Run pipeline in background without blocking -> the application starts without waiting for pipeline to finish running
    threading.Thread(target=run_pipeline).start()
    
    # Schedule pipelne runs daily at 2:00 AM
    scheduler.add_job(
        run_pipeline,
        trigger=CronTrigger(hour=2, minute=0),
    )

@app.on_event("shutdown")
def shutdown():
    scheduler.shutdown()
    