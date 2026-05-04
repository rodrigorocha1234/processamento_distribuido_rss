from celery import Celery

celery_app = Celery(
    "demo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

@celery_app.task
def soma(a, b):
    print(f"Processando soma: {a} + {b}")
    return a + b


