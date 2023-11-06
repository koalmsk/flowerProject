import sqlite3
import os


db = sqlite3.connect("database/flower_db.sqlite3")
cur = db.cursor()


def format_collections_from_sql(collection) -> list:
    return list(map(lambda x: x[0], collection))


def on_start_up():
    CREATE_FLOWER_TABLE = """
CREATE TABLE IF NOT EXISTS flower (
    id                 INTEGER REFERENCES user (id),
    name               TEXT,
    photo              TEXT,
    planted            TEXT,
    recomendation      TEXT,
    how_often_to_water INTEGER,
    last_water_date    TEXT,
    next_date          TEXT
);
    """

    
    CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS user (
    id       INTEGER UNIQUE
                     PRIMARY KEY AUTOINCREMENT,
    login    TEXT    UNIQUE,
    password TEXT,
    email    TEXT
);
    """

    cur.execute(CREATE_FLOWER_TABLE)
    cur.execute(CREATE_USERS_TABLE)
    db.commit()


def take_user(login: str) -> tuple:
    ans = cur.execute(
    """
    SELECT * FROM user
    WHERE user.login = (?)
    """, (login,)).fetchone()
    return ans


def take_flower(flower_name: str) -> tuple:
    sql_request = """
    SELECT * FROM flower
    WHERE flower.name = (?)
    """

    ans = cur.execute(sql_request, (flower_name, )).fetchone()
    return ans


def is_login_uniq(name: str) -> bool:
    sql_request = """
    SELECT user.login FROM user
    """
    login_list = format_collections_from_sql(cur.execute(sql_request).fetchall())
    return name not in login_list


def insert_user(user_data: tuple[:2]) -> None:
    cur.execute(
    """
    INSERT INTO user (login, password, email)
    VALUES (?, ?, ?)
    """, tuple(user_data))
    db.commit()


def is_flower_name_uniq(flower_name: str, id: int) -> bool:
    sql_request = """
    SELECT flower.name FROM flower
    WHERE id = ?
    """
    flower_name_list = format_collections_from_sql(cur.execute(sql_request, (id, )).fetchall())
    return flower_name not in flower_name_list


def insert_flower(flower_data: tuple) -> None:
    cur.execute(
    """
INSERT INTO flower (id, name, photo, planted, recomendation, how_often_to_water, last_water_date, next_date)
VALUES (?,?,?,?,?,?,?,?)
    """, flower_data)
    db.commit()

def load_flowers_for_table(id: int):

    ans = cur.execute("SELECT * FROM flower WHERE flower.id = ?", (id, )).fetchall()

    return ans

def load_flower_by_name(name: str, id: int):
    return cur.execute("SELECT * FROM flower WHERE flower.name = ? and flower.id = ?", (name, id)).fetchone()

def load_login(id: int):
    ans = (cur.execute("SELECT user.login FROM user WHERE user.id = ?", (id, )).fetchone())[0]
    return ans

def update_flower_card(id: int, name_flower: str, entry: str, value: str):
    cur.execute(
    f"""
UPDATE flower 
SET {entry} = '{value}'
WHERE id = {id} and name = '{name_flower}'
    """)
    db.commit()


# print(is_flower_name_uniq("Роза", 1))