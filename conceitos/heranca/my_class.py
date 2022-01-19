class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Santos'

    def comer(self) -> None:
        print('Estou comendo !!')

    def estudar(self) -> None:
        print('Estou estudando')


class Filha(Mae):

    def __init__(self, endereco) -> None:
        super().__init__(endereco)

    
    def brincar(self, brinquedo: str) -> None:
        print(f'Estou brincando com {brinquedo}')


class Neta(Filha):

    def __init__(self, endereco) -> None:
        super().__init__(endereco)



mae = Mae('Rua do Bolo')
julia = Filha('Rua Nova Guiné')
julia.brincar('Boneca')

print(mae.endereco)
print(julia.endereco)