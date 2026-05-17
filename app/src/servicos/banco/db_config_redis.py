from typing import Dict

from mypy.types import Any
from redis import Redis

from app.src.servicos.banco.idb_config import IdbConfig
from config.config import Config


class DbConfigRedis(IdbConfig[Redis]):

    def obter_driver(self) -> Redis:
        redis = Redis(**self.obter_parametros_conexao())
        return redis

    def obter_parametros_conexao(self) -> Dict[str, Any]:
        parametros_conexao = {
            'host': Config.URL_REDIS,
            'port': Config.PORTA_REDIS,
            'db': Config.DB_REDS,
            'decode_responses': True
        }
        return parametros_conexao


if __name__ == '__main__':
    db = DbConfigRedis()
    print(db.obter_parametros_conexao())
    print(db.obter_driver())

