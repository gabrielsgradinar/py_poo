from .interface import Repositorio

class MongoRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print(f'Inserindo {dado} no banco MongoDB')

    def deletar(self, dado) -> None:
        print(f'Removendo {dado} no banco MongoDB')