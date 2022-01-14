class PostgresDB:

    def __init__(self) -> None:
        self.__conexao = 'Postgres'

    def conectar(self) -> str:
        print('Conectado ao banco Postgres')
        return self.__conexao

    def desconectar(self) -> None:
        print('Desconectando do banco Postgres')