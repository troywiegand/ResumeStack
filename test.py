import sqlite3
import sys

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

db = sqlite3.connect('./resume.db')
db.row_factory = dict_factory
classes = db.execute("SELECT * FROM Classes").fetchall()

for c in classes:
    print(c)


print("\n\nALL UPPER LEVEL CLASSES \n")

classes = db.execute("SELECT * FROM Classes WHERE Code LIKE '__3%' OR Code LIKE '__4%'").fetchall()

for c in classes:
    print(c)

