# Comportamento se torna uma classe
from .interfaces import Ihabilidade


class LutaEspada(Ihabilidade):

    def __init__(self, nivel) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Luta com espada')

    def nivel_atributo(self):
        print(f'Nível de uso Espada: {self.nivel}')