from sqlalchemy import Table, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy_utils import database_exists, create_database
from DB.Tables import USERS, PURCHASES, ITEMS, metadata
# import psycopg2


class DBConnector:
    DATABASE = {
        'drivername': 'postgresql',
        'host': 'localhost',
        'port': '5432',
        'username': 'postgres',
        'password': '12345',
        'database': 'mydb'
    }
    metadata = metadata
    users = USERS
    purchases = PURCHASES
    items = ITEMS

    def __init__(self):
        self.engine = create_engine(URL(**self.DATABASE))
        self.con = self.engine.connect()

    def create_db(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.metadata.create_all(self.engine)

    def delete_all_tables(self):
        self.metadata.drop_all()

    def drop_all_tables(self):
        self.users.drop()
        self.purchases.drop()
        self.items.drop()

    def insert_row(self, table: Table, **values):
        self.con.execute(table.insert().values(**values))

    def execute_query(self, query):
        return self.con.execute(query)

    def delete_all_rows(self, table: Table):
        self.con.execute(table.delete())