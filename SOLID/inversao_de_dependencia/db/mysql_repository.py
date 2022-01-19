from .interface import Repositorio

class MySqlRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print(f'Inserindo {dado} no banco MySQL')

    def deletar(self, dado) -> None:
        print(f'Removendo {dado} no banco MySQL')