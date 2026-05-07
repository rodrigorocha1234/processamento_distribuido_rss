from celery import Celery
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

celery_app = Celery(
    "data_pipeline",
    broker=f"redis://{REDIS_HOST}:6379/0",
    backend=f"redis://{REDIS_HOST}:6379/0",
    include=["tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
)