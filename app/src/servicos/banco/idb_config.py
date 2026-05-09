from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict, Protocol

DRIVER = TypeVar('DRIVER')


class IdbConfig(Protocol[DRIVER]):

    @abstractmethod
    def obter_driver(self) -> DRIVER:
        pass

    @abstractmethod
    def obter_parametros_conexao(self) -> Dict[str, str]:
        pass
