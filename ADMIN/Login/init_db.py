import sqlite3

conn = sqlite3.connect("atm.db")
cursor = conn.cursor()

'''
cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
);
""")

cursor.execute("""
INSERT INTO admins (password, full_name)
VALUES (?, ?)
""", ("ous123", "Oussama Kraiem"))


cursor.execute("""
               CREATE TABLE IF NOT EXISTS state(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               num50Bills INTEGER NOT NULL,
               num20Bills INTEGER NOT NULL,
               num10Bills INTEGER NOT NULL
               )
               """)
'''

cursor.execute("""
               CREATE TABLE IF NOT EXISTS requests(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    card NUMBER TEXT NOT NULL,
                    date TEXT NOT NULL 
               )""")

conn.commit()
conn.close()
