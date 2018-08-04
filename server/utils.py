import sqlite3

from flask import g


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db(no_context=False):
    if no_context:
        db = sqlite3.connect('xggity3')
        db.row_factory = dict_factory
        return db

    if not hasattr(g, 'sqlite_db'):
        db = sqlite3.connect('xggity3')
        db.row_factory = dict_factory
        g.db = db
    return g.db
