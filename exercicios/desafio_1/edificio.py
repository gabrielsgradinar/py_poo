from elevador import Elevador


class Edificio:

    def __init__(self) -> None:
        self.__andares = 15
        self.__terreo = 1
        self.__elevador = Elevador(self.__terreo, self.__andares)
        self.__andar_atual = 1

    
    def subir(self, proximo_andar: int) -> None:
        self.__andar_atual = self.__elevador.subir(self.__andar_atual, proximo_andar)


    def descer(self, proximo_andar: int) -> None:
        self.__andar_atual = self.__elevador.descer(self.__andar_atual, proximo_andar)
