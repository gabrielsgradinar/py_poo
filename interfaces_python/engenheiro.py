from interfaces.formas import FormasInterface

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: FormasInterface):
        perimero = terreno.get_perimetro()
        print(f'{self.nome} mediu o perimetro: {perimero} m')

    def medir_area(self, terreno: FormasInterface):
        area = terreno.get_perimetro()
        print(f'{self.nome} mediu a area: {area} m')