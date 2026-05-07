from abc import abstractmethod
from typing import Union, List

from bs4 import BeautifulSoup


class WebScrapingBs4:

    def __init__(self):
        self.__url = None

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: Union[str, List[str]]):
        self.__url = url

    def obter_motor(self) -> BeautifulSoup:
        pass

    @abstractmethod
    def obter_dados(self, dados: BeautifulSoup) -> BeautifulSoup:
        pass
