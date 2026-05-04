from celery import Celery
import time

app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@app.task
def soma(a, b):
    time.sleep(3)  # simula trabalho pesado
    return a + b


@app.task
def hello(name):
    return f"Olá {name}, Celery está funcionando!"