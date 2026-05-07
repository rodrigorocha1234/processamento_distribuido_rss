from typing import Protocol, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class IWebScraping(Protocol[T, U]):

    def obter_motor(self) -> T: ...

    def obter_dados(self, dados: T) -> U: ...
