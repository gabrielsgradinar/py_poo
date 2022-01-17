from typing import Any


class Pessoa:

    def __init__(self, nome) -> None:
        self.__local = None
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

    def se_apresentar(self) -> None:
        print(f'Olá, eu sou {self.__nome}')

    
    def set_local(self, local: Any) -> None:
        self.__local = local

    def get_local(self) -> Any:
        return self.__local
