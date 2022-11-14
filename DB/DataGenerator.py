from DB.DBConnector import DBConnector
from random import randint
from datetime import datetime, timedelta


def random_date(date_start: datetime, date_end: datetime):
    diff = int((date_end - date_start).days)
    return date_start + timedelta(days=randint(0, diff))


class DataGenerator:
    def __init__(self, db_con: DBConnector):
        self.db_con = db_con

    def generate_users(self, cnt: int):
        for i in range(cnt):
            self.db_con.insert_row(self.db_con.users, age=randint(18, 50))

    def generate_items(self, cnt: int):
        for i in range(cnt):
            self.db_con.insert_row(self.db_con.items, price=randint(10, 10000))

    def generate_purchases(self, cnt: int):
        users = self.db_con.execute_query('SELECT * FROM "Users"').fetchall()
        user_ids = list(map(lambda x: x[0], users))
        items = self.db_con.execute_query('SELECT * FROM "Items"').fetchall()
        item_ids = list(map(lambda x: x[0], items))
        for i in range(cnt):
            date = random_date(datetime(2020, 1, 1), datetime(2022, 11, 1))
            item_id = item_ids[randint(0, len(item_ids) - 1)]
            user_id = user_ids[randint(0, len(user_ids) - 1)]
            self.db_con.insert_row(self.db_con.purchases, itemId=item_id, userId=user_id, date=date)

    def fillDB(self):
        self.generate_users(10000)
        self.generate_items(10000)
        self.generate_purchases(200000)


if __name__ == "__main__":
    generator = DataGenerator(DBConnector())
    generator.fillDB()
