import sqlite3
import os


db = sqlite3.connect("database/flower_db.sqlite3")
cur = db.cursor()


def format_dates(date_ints: tuple = None, date_stroke: str = None) -> str or tuple:
    return ("^".join(map(str, date_ints)) if date_stroke is None else tuple(map(int, date_stroke.split("^"))))


def format_collections_from_sql(collection) -> list:
    return list(map(lambda x: x[0], collection))


def on_start_up():
    CREATE_FLOWER_TABLE = """
CREATE TABLE IF NOT EXISTS flower (
    id                 INTEGER REFERENCES user (id),
    name               TEXT    UNIQUE
                               PRIMARY KEY,
    photo              TEXT,
    planted            TEXT,
    recomendation      TEXT,
    how_often_to_water INTEGER,
    last_water_date    TEXT,
    is_waterd          INTEGER
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

