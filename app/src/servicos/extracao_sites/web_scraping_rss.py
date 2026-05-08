from datetime import datetime
from typing import Generator

from bs4 import BeautifulSoup, Tag

from app.src.servicos.extracao_sites.web_scraping_bs4 import WebScrapingBs4


class WebScrapingRss(WebScrapingBs4):

    def __init__(self):
        super().__init__(parser='xml')
        self.__formatado_data_entrada = "%a, %d %b %Y %H:%M:%S %z"

    def obter_dados(self, dados: BeautifulSoup) -> Generator[dict[str, str | datetime], None, None]:
        for noticia in dados.find_all('item'):
            if not isinstance(noticia, Tag):
                continue
            titulo_noticia_tag = noticia.find('title')
            titulo_noticia = titulo_noticia_tag.text.strip() if titulo_noticia_tag and isinstance(titulo_noticia_tag,
                                                                                                  Tag) else ""

            media_content_tag = noticia.find('media:content')
            url_imagem = str(media_content_tag['url']) if (
                    isinstance(media_content_tag, Tag) and 'url' in media_content_tag.attrs) else ''

            url_tag = noticia.find('guid')
            url = url_tag.text.strip() if url_tag and isinstance(url_tag, Tag) else ''

            data_pub_tag = noticia.find('pubDate')
            data_publicacao = data_pub_tag.text if isinstance(data_pub_tag, Tag) else ''
            data_publicacao = datetime.strptime(data_publicacao, self.__formatado_data_entrada)
            data_publicacao = data_publicacao.strftime("%d-%m-%Y %H:%M:%S")
            data_publicacao = datetime.strptime(data_publicacao, "%d-%m-%Y %H:%M:%S")

            yield {'titulo_rss': titulo_noticia, 'url_imagem_rss': url_imagem, 'url_rss': url,
                   'data_publicacao_rss': data_publicacao

                   }
