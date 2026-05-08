from abc import ABC
import os

from app.src.modelo.noticia import Noticia


class Arquivo(ABC):

    def __init__(self, noticia: Noticia) -> None:
        self._caminho_raiz: str = os.getcwd()
        self._nome_arquivo: str = ""
        self._noticia: Noticia = noticia

    @property
    def nome_arquivo(self) -> str:
        return self._nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, nome_arquivo: str) -> None:
        self._nome_arquivo = nome_arquivo

    @property
    def noticia(self) -> Noticia:
        return self._noticia

    @noticia.setter
    def noticia(self, nova_noticia: Noticia) -> None:

        if not isinstance(nova_noticia, Noticia):
            raise TypeError(
                "O atributo noticia deve ser uma instância de Noticia"
            )

        self._noticia = nova_noticia