from collections import Counter

import mysql.connector

from Manage.Manage import to_processed_log


def init_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )


def init_db(name_db):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="{}".format(name_db)
    )


def create_db(cursor, name, drop_if_exits=False):
    if drop_if_exits:
        drop_db(cursor, name)
    if drop_if_exits or name not in show_db(cursor):
        cursor.execute("CREATE DATABASE {}".format(name))


def create_tb_problems(cursor):
    if "problems" not in show_tbs(cursor):
        cursor.execute(
            "CREATE TABLE problems (id int NOT NULL AUTO_INCREMENT,link varchar(300) unique not null ,tags varchar(100) not null,level varchar(100),frequency float, PRIMARY KEY (id))")


def drop_db(cursor, name):
    if name in show_db(cursor):
        cursor.execute("DROP DATABASE {}".format(name))


def drop_tb(cursor, name):
    if name in show_tbs(cursor):
        cursor.execute("DROP TABLE {}".format(name))


def del_row_tb_problems(db, filed="", cmpr="=", val=""):
    if filed != "" and cmpr != "" and val != "":
        cursor = db.cursor()
        cursor.execute("DELETE FROM problems WHERE {} {} {}".format(filed, cmpr, val))
        print(cursor.rowcount, " records was deleted")
        db.commit()


def show_db(cursor):
    cursor.execute("SHOW DATABASES")
    names = []
    for name in cursor:
        names.append(name[0])
    return names


def show_tbs(cursor):
    cursor.execute("SHOW TABLES")
    names = []
    for tb_name in cursor:
        names.append(tb_name[0])
    return names


def insert_tb_problems(db, vals):
    cursor = db.cursor()
    sql = "INSERT INTO problems(link,tags,level,frequency) VALUES (%s,%s,%s,%s)"
    try:
        cursor.executemany(sql, vals)
        db.commit()
        print(cursor.rowcount, "records was inserted")
    except Exception as e:
        print("[INSERT ERROR] {} ".format(e.__str__()))


def select_tb_problems(cursor, name, where=False, field="", cmpr="", val=""):
    if not where:
        cursor.execute("SELECT link,tags FROM {}".format(name))
    else:
        cursor.execute("SELECT link,tags,frequency FROM {} WHERE {} {} {}".format(name, field, cmpr, val))
    for line in cursor.fetchall():
        print(line)


db_name = "leetcode_daily"
tb_name = "problems"
my_db = init_db(db_name)
my_cursor = my_db.cursor()
# drop_tb(my_cursor, "problems")
# create_tb_problems(my_cursor)
# vals = to_processed_log()
# insert_tb_problems(my_db, vals)
# del_row_tb_problems(my_db, "id", ">", "0")
x = "'%dp%'"
select_tb_problems(my_cursor, tb_name, True, "tags", "LIKE", x)
