from .interfaces import Ihabilidade

class Curar(Ihabilidade):

    def __init__(self, nivel) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Curar Personagem')

    def nivel_atributo(self):
        print(f'Nível de Cura: {self.nivel}')