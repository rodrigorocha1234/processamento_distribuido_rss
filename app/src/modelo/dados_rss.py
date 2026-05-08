from datetime import datetime
from typing import TypedDict


class DadosRss(TypedDict):
    titulo_rss: str
    url_imagem_rss: str
    url_rss: str
    data_publicacao_rss: datetime
