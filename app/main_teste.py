from app.servicos.extracao_sites.i_web_scraping import IWebScraping
from app.servicos.extracao_sites.web_scraping_rss import WebScrapingRss
from app.servicos.tratamento.tratamento import Tratamento


class MainTeste:

    def __init__(self, url_rss: str, servico_web: IWebScraping

    ):

        self.__servico_web = servico_web
        self.__url_rss = url_rss
        self.__servico_web.url = self.__url_rss
        self.__tratamento = Tratamento()


    def rodar_teste(self) -> None:

        motor = self.__servico_web.obter_motor()

        if motor is None:
            print("Erro ao obter HTML")
            return

        url_noticias = self.__servico_web.obter_dados(motor)

        for url in url_noticias:
            print(url)
            break


web_scraping_rss = WebScrapingRss()

m = MainTeste(url_rss="https://g1.globo.com/rss/g1/sp/ribeirao-preto-franca/", servico_web=web_scraping_rss)

m.rodar_teste()
