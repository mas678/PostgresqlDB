from DB.DBConnector import DBConnector
from DB.DataGenerator import DataGenerator
from SQL_Queries import A1, A2, B, C, D


def better_out(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        ans = []
        for row in res:
            ans.append(row)
        return ans
    return wrapper


@better_out
def task_A1(db_con: DBConnector):
    return db_con.execute_query(A1)


@better_out
def task_A2(db_con: DBConnector):
    return db_con.execute_query(A2)


@better_out
def task_B(db_con: DBConnector):
    return db_con.execute_query(B)


@better_out
def task_C(db_con: DBConnector):
    return db_con.execute_query(C)


@better_out
def task_D(db_con: DBConnector):
    return db_con.execute_query(D)


def fillDB(db_con: DBConnector):
    generator = DataGenerator(db_con)
    generator.generate_users(1000)
    generator.generate_items(1000)
    generator.generate_purchases(10000)


def main():
    db_con = DBConnector()
    db_con.create_db()
    print(task_A1(db_con))
    print(task_A2(db_con))
    print(task_B(db_con))
    print(task_C(db_con))
    print(task_D(db_con))


if __name__ == "In f__main__":
    main()
