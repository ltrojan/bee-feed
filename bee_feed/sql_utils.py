import sqlite3
import datetime

from . import queries


def url_to_addr(url):
    if url[:10] == "sqlite:///":
        url = url[10:]
    return url


def connect_db(url):
    return sqlite3.connect(url_to_addr(url))


def init_db(db):
    db.cursor().executescript(queries.clean_db)
    db.cursor().executescript(queries.create_db)
    db.commit()


def get_entries(db):
    cur = db.execute(queries.get_entries)
    return cur.fetchall()


def add_entry(db, *data):
    db.execute(
        queries.add_entry,
        list(data) + [datetime.date.today()])
    db.commit()
