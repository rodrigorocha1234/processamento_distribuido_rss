from celery import Celery
import requests
from bs4 import BeautifulSoup

app = Celery('etl_pipeline', broker='redis://redis:6379/0')

@app.task
def extract():
    return requests.get("https://g1.globo.com/rss/g1/").text

@app.task
def transform(xml):
    soup = BeautifulSoup(xml, "xml")
    return [item.link.text for item in soup.find_all("item")]

@app.task
def load(links):
    for link in links:
        print("Saving:", link)

@app.task
def etl():
    xml = extract.delay().get()
    links = transform.delay(xml).get()
    load.delay(links)