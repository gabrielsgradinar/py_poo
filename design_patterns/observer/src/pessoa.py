from .interfaces import Observador


class Pessoa(Observador):
    
    def __init__(self) -> None:
        self.acordada = False

    def esta_acordada(self) -> bool:
        return self.acordada
    
    def update(self):
        print('Opa, acordei')
        self.acordada = True
