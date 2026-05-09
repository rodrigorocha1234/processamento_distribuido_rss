from typing import Dict

from redis import Redis

from servicos.banco.idb_config import IdbConfig


class DbConfigRedis(IdbConfig[Redis]):

    def obter_parametros_conexao(self) -> Dict[str, str]:
        pass

    def obter_driver(self) -> Redis:
        driver = Redis(host='localhost', port=6379, db=0)
        return driver
