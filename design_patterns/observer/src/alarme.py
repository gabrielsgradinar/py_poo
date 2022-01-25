from typing import List
from .interfaces import Observador

class Alarme:

    def __init__(self) -> None:
        self.beep = False
        self.dorminhocos: List[Observador] = []

    def add_pessoa(self, pessoa: Observador) -> None:
        self.dorminhocos.append(pessoa)

    def estado_alarme(self) -> bool:
        return self.beep

    def tocar(self) -> None:
        self.beep = True
        for pessoa in self.dorminhocos:
            pessoa.update()

        self.dorminhocos = []