from typing import Protocol, TypeVar

MOTOR_WEB_SCRAPING = TypeVar("MOTOR_WEB_SCRAPING")
SAIDA = TypeVar("SAIDA", covariant=True)


class IWebScraping(Protocol[MOTOR_WEB_SCRAPING, SAIDA]):

    @property
    def url(self) -> str | None:
        ...

    @url.setter
    def url(self, value: str) -> None:
        ...

    def obter_motor(self) -> MOTOR_WEB_SCRAPING | None: ...

    def obter_dados(self, dados: MOTOR_WEB_SCRAPING) -> SAIDA: ...
