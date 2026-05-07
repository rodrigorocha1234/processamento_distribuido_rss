from celery import chain, chord, group

from tasks import (
    extract_urls,
    fetch_content,
    transform,
    save,
    summarize
)


def run_pipeline():

    urls = extract_urls.delay().get()

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

    print(result.get())


if __name__ == "__main__":
    run_pipeline()