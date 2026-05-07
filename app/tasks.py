from celery_app import celery_app


@celery_app.task
def extract_urls():
    return [f"url_{i}" for i in range(5)]


@celery_app.task
def fetch_content(url):
    return f"conteudo {url}"


@celery_app.task
def transform(content):
    return content.upper()


@celery_app.task
def save(content):
    return f"salvo {content}"


@celery_app.task
def summarize(results):
    return {
        "total": len(results),
        "results": results
    }