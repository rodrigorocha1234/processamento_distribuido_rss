from abc import abstractmethod, ABC
from typing import Optional, TypeVar, Generic

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout, ReadTimeout, TooManyRedirects, \
    RequestException

from app.src.servicos.extracao_sites.i_web_scraping import IWebScraping

SAIDA = TypeVar("SAIDA")


class WebScrapingBs4(ABC, Generic[SAIDA], IWebScraping[BeautifulSoup, SAIDA]):

    def __init__(self, parser: str):
        self._url: Optional[str] = None
        self._parser_html = parser

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    def obter_motor(self) -> Optional[BeautifulSoup]:

        try:
            if self._url is None:
                raise ValueError("URL não pode ser None")

            response = requests.get(url=self._url)
            response.raise_for_status()
            conteudo_response = response.content

            try:
                soup = BeautifulSoup(conteudo_response, self._parser_html)
                return soup

            except Exception as e:

                return None

        except HTTPError as http_err:
            return None
        except ConnectionError:

            return None
        except ConnectTimeout:

            return None
        except ReadTimeout:

            return None
        except TooManyRedirects:

            return None
        except RequestException as req_err:

            return None
        except Exception as e:

            return None

    @abstractmethod
    def obter_dados(self, dados: BeautifulSoup) -> SAIDA:
        """
        Método para obter os dados do site
        """
        pass
