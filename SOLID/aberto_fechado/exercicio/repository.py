from sqlite3 import connect


class Repositorio:

    def select(self, db_connection) -> None:
        connection = db_connection.conectar()
        print(f'Conectei ao banco {connection}')
        print('Fazendo um SELECT * FROM ...')
        db_connection.desconectar()

    
    def insert(self, db_connection):
        connection = db_connection.conectar()
        print(f'Conectei ao banco {connection}')
        print('Fazendo um INSERT VALUES ...')
        db_connection.desconectar()