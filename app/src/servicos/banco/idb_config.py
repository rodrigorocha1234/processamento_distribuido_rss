from abc import abstractmethod
from typing import TypeVar, Dict, Protocol

DRIVER = TypeVar('DRIVER', covariant=True)


class IdbConfig(Protocol[DRIVER]):

    @abstractmethod
    def obter_driver(self) -> DRIVER:
        pass

    @abstractmethod
    def obter_parametros_conexao(self) -> Dict[str, str]:
        pass
