from typing import Any


class Casa:
    
    def __init__(self) -> None:
        self.__endereco = "Rua Clevelância"
        self.__proprietario = None

    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes!')

    def get_endereco(self) -> str:
        return self.__endereco

    def set_proprietario(self, proprietario: Any) -> None:
        self.__proprietario = proprietario

    def get_proprietario(self) -> Any:
        return self.__proprietario 