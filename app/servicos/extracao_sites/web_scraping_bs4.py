from abc import abstractmethod
from typing import Union, List, Optional, Generator, Dict, Any

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout, ReadTimeout, TooManyRedirects, \
    RequestException


class WebScrapingBs4:

    def __init__(self):
        self._url = None
        self._parser_html = 'xml'

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: Union[str, List[str]]):
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
    def obter_dados(self, dados: BeautifulSoup) -> Generator[Dict[str, Any], None, None]:
        """
        Método para obter os dados de um site
        :param dados:
        :return:
        """
        pass
