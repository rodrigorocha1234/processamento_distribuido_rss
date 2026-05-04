from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
import time
app = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="America/Sao_Paulo",
    enable_utc=False,
)


@app.task(queue="default")
def hello(name):
    return f"Olá {name}"

# 🔹 fila pesada
@app.task(queue="math")
def soma(a, b):
    time.sleep(5)
    return a + b

# 🔹 fila IO
@app.task(queue="io")
def download_simulado(url):
    time.sleep(4)
    return f"baixado {url}"