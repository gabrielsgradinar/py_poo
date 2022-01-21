from .interfaces import Ihabilidade

class LutaArco(Ihabilidade):

    def __init__(self, nivel) -> None:
        self.nivel = nivel

    def comportamento(self):
        print('Atirar flexas')

    def nivel_atributo(self):
        print(f'Nível de uso Arco: {self.nivel}')