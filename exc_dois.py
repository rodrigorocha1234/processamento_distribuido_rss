from celery import Celery, chain, group, chord
from dataclasses import dataclass
from typing import List


# =========================================================
# CONFIGURAÇÃO CELERY
# =========================================================

app = Celery(
    "data_pipeline",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
)


# =========================================================
# MODELOS
# =========================================================

@dataclass
class News:
    url: str
    content: str


# =========================================================
# TASKS - EXTRAÇÃO
# =========================================================

@app.task
def extract_urls() -> List[str]:
    """
    Simula leitura de RSS.
    """
    print("\n[EXTRACT] Coletando URLs do RSS...\n")

    return [
        "https://g1.globo.com/noticia-1",
        "https://g1.globo.com/noticia-2",
        "https://g1.globo.com/noticia-3",
        "https://g1.globo.com/noticia-4",
        "https://g1.globo.com/noticia-5",
    ]


# =========================================================
# TASKS - FETCH
# =========================================================

@app.task
def fetch_content(url: str) -> dict:
    """
    Simula download da notícia.
    """

    print(f"[FETCH] Baixando conteúdo: {url}")

    fake_html = f"""
    <html>
        <body>
            Conteúdo da notícia {url}
        </body>
    </html>
    """

    return {
        "url": url,
        "content": fake_html
    }


# =========================================================
# TASKS - TRANSFORMAÇÃO
# =========================================================

@app.task
def transform(news: dict) -> dict:
    """
    Simula transformação/limpeza.
    """

    print(f"[TRANSFORM] Limpando conteúdo: {news['url']}")

    cleaned_text = (
        news["content"]
        .replace("<html>", "")
        .replace("</html>", "")
        .replace("<body>", "")
        .replace("</body>", "")
        .strip()
        .upper()
    )

    return {
        "url": news["url"],
        "content": cleaned_text
    }


# =========================================================
# TASKS - LOAD
# =========================================================

@app.task
def save(news: dict) -> str:
    """
    Simula persistência.
    """

    print(f"[LOAD] Salvando notícia: {news['url']}")

    filename = news["url"].split("/")[-1] + ".txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(news["content"])

    return f"Arquivo salvo: {filename}"


# =========================================================
# TASK - SUMÁRIO FINAL
# =========================================================

@app.task
def summarize(results: List[str]) -> dict:
    """
    Consolida resultados finais.
    """

    print("\n[SUMMARY] Pipeline finalizado\n")

    return {
        "total_processado": len(results),
        "arquivos": results
    }


# =========================================================
# ORQUESTRADOR
# =========================================================

@app.task
def build_parallel_pipeline(urls):

    workflow = chord(
        group(
            chain(
                fetch_content.s(url),
                transform.s(),
                save.s()
            )
            for url in urls
        ),
        summarize.s()
    )

    result = workflow.apply_async()

    return result.id


# =========================================================
# PIPELINE PRINCIPAL
# =========================================================

def run_pipeline():

    workflow = chain(
        extract_urls.s(),
        build_parallel_pipeline.s()
    )

    result = workflow.apply_async()

    print("\n[PIPELINE] Executando pipeline...\n")

    final_result = result.get()

    print("\n[RESULTADO FINAL]\n")
    print(final_result)


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    run_pipeline()