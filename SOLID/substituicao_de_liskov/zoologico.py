class Animal:

    def comer(self):
        print('O animal está comendo')
    
    def dormir(self):
        print('O animal está dormindo')
    
    def andar(self):
        print('O animal está andando')

class Aves(Animal):

    def __init__(self) -> None:
        super().__init__()

    def cantar(self):
        print('A ave está cantando')

class Pinguim(Aves):

    def __init__(self) -> None:
        super().__init__()

    def escorregar(self):
        print('O pinguem está escorregando no gelo')


class Pessoa:

    def observar(self, animal: Animal) -> None:
        animal.comer()    


gabriel = Pessoa()
pinguim = Aves()
gabriel.observar(pinguim)