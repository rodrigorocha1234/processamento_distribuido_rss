from bs4 import BeautifulSoup

from app.servicos.extracao_sites.web_scraping_bs4 import WebScrapingBs4


class WebScrapingRss(WebScrapingBs4):

    def __init__(self):
        super().__init__()

    def obter_dados(self, dados: BeautifulSoup) -> BeautifulSoup:
        pass
