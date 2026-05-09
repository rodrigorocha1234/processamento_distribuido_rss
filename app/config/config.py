from typing import Final

from dotenv import load_dotenv

load_dotenv()
import os


class Config:
    URL_REDIS: Final[str] = os.environ['URL_REDIS']
    PORTA_REDIS: Final[str] = os.environ['PORTA_REDIS']
    DB_REDS: Final[str] = os.environ['DB_REDS']
    TEMPO_EXPIRACAO_REDIS: Final[str] = os.environ['TEMPO_EXPIRACAO_REDIS']
