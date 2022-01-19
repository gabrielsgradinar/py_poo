from typing import Any
from db.mysql_repository import MySqlRepositorio
from db.interface import Repositorio
from db.mongo_repositorio import MongoRepositorio


class Usuario:

    def __init__(self, repositorio: Repositorio) -> None:
        self.__repositorio = repositorio

    def armazenar_dados(self, dado: Any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado: Any) -> None:
        self.__repositorio.deletar(dado)


usuario = Usuario(MongoRepositorio())
usuario.armazenar_dados(23)
usuario.remover_dado(21)


usuario = Usuario(MySqlRepositorio())
usuario.armazenar_dados(20)
usuario.remover_dado(15)