import os


def is_docker():
    return os.path.exists("/.dockerenv") or os.getenv("DOCKER_ENV") == "true"


def get_redis_host():
    return "redis" if is_docker() else "localhost"


REDIS_HOST = get_redis_host()

CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL",
    f"redis://{REDIS_HOST}:6379/0"
)

CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND",
    f"redis://{REDIS_HOST}:6379/0"
)