class MinhaClasse:

    estatico = 'Teste'  # Variável de classe

    def __init__(self,estado) -> None:
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = "Topper"


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)
obj1.print_estatico()
obj1.mudar_estatico()
obj1.print_estatico()
obj2.print_estatico()

print(MinhaClasse.estatico)