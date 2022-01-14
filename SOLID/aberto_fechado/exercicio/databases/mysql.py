class MysqlDB:

    def __init__(self) -> None:
        self.__conexao = 'Mysql'

    def conectar(self) -> str:
        print('Conectado ao banco Mysql')
        return self.__conexao

    def desconectar(self) -> None:
        print('Desconectando do banco Mysql')