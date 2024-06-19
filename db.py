import sqlite3 as sq
with sq.connect('sappe3.db') as con:
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS useres''')
    cur.execute("""CREATE TABLE IF NOT EXISTS useres(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER DEFAULT 1 ,
    old INTEGER,
    score INTEGER
    )""")









