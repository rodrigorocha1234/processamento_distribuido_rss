import os.path

from bs4 import BeautifulSoup

from servicos.guardar_dados.arquivo_docx import ArquivoDOCX
from src.servicos.extracao_sites.web_scraping_g1 import WebScrapingG1
from src.servicos.extracao_sites.web_scraping_rss import WebScrapingRss

web_scraping_rss = WebScrapingRss()
web_scraping_g1 = WebScrapingG1()



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
                url_g1 = link['url_rss']
                if isinstance(url_g1, str):
                    nome_arquivo = ''.join(
                        url_g1.split('.')[-2].split('/')[-1].replace('-', '_') + '.docx'
                    )
                    print(nome_arquivo)
                    print()
                    servico_arquivo = ArquivoDOCX(noticia=noticia_g1)
                    servico_arquivo.nome_arquivo =  os.path.join('noticias', nome_arquivo)
                    servico_arquivo.noticia = noticia_g1
                    servico_arquivo.gerar_documento()
                    servico_arquivo()





        print()

