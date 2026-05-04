from celery import Celery

import os
from celery import Celery

BROKER = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

app = Celery("tasks", broker=BROKER, backend=BACKEND)



app.conf.task_routes = {
    "tasks.*": {"queue": "default"},
}

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="America/Sao_Paulo",
    enable_utc=False,
)