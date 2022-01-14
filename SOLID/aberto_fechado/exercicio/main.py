from repository import Repositorio
from databases import PostgresDB, MysqlDB

db_psql = PostgresDB()
db_mysql = MysqlDB()

repo = Repositorio()

repo.insert(db_psql)
print('-------------------------------------')
repo.insert(db_mysql)