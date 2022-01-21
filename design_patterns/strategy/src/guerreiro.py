from .habilidades import Ihabilidade

class Guerreiro:

    def __init__(self, habilidade: Ihabilidade):
        self.habilidade = habilidade

    def acao(self):
        # Processamento
        self.habilidade.comportamento()

    def atributos(self):
        self.habilidade.nivel_atributo()