class Elevador:

    def __init__(self, terreo: int, andar_maximo: int) -> None:
        self.__terreo = terreo
        self.__andar_maximo = andar_maximo

    
    def subir(self, andar_atual: int, proximo: int) -> int:
        proximo_andar = andar_atual + proximo

        if proximo_andar > self.__andar_maximo:
            raise Exception('Andar não existe, você chegou no último andar')

        print(f'Indo para o Andar: {proximo_andar}')

        return proximo_andar
    

    def descer(self, andar_atual: int, proximo: int) -> int:
        proximo_andar = andar_atual - proximo

        if proximo_andar < self.__terreo:
            raise Exception('Andar não existe, você já está no térreo')

        print(f'Indo para o Andar: {proximo_andar}')

        return proximo_andar
    
    