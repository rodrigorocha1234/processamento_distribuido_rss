from typing import Dict

from redis import Redis

from servicos.banco.idb_config import IdbConfig, DRIVER


class DbConfigRedis(IdbConfig[Redis]):

    def __init__(self, driver: DRIVER):
        pass

    def obter_parametros_conexao(self) -> Dict[str, str]:
        pass

    def obter_driver(self) -> DRIVER:
        pass
