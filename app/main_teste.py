from bs4 import BeautifulSoup

from src.servicos.extracao_sites.web_scraping_g1 import WebScrapingG1
from src.servicos.extracao_sites.web_scraping_rss import WebScrapingRss

web_scraping_rss = WebScrapingRss()
web_scraping_g1 = WebScrapingG1()
# servico_arquivo = ArquivoDOCX()


web_scraping_rss.url = 'https://g1.globo.com/rss/g1/sp/ribeirao-preto-franca/'
motor = web_scraping_rss.obter_motor()
if isinstance(motor, BeautifulSoup):
    resultados = web_scraping_rss.obter_dados(dados=motor)

    for link in resultados:

        web_scraping_g1 = WebScrapingG1()
        web_scraping_g1.url = link['url_rss']
        motor_g1 = web_scraping_g1.obter_motor()
        if isinstance(motor_g1, BeautifulSoup):
            noticia_g1 = web_scraping_g1.obter_dados(dados=motor_g1)
            if noticia_g1.texto:
                print(link)
                print(noticia_g1)



        print()

