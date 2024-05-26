import psycopg2
from flask import g


def get_db():
    try:
        if 'db' not in g:
            g.db = psycopg2.connect(
                dbname='hack',
                user='postgres',
                password='JustOleg1!',
                host='localhost',
                port='5432'
            )
        return g.db
    except:
        print('Can`t establish connection to database')
