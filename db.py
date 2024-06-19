import sqlite3 as sq
with sq.connect('sapper3.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE useres(
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")









