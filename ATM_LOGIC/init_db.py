import sqlite3

conn = sqlite3.connect("atm.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
               id integer PRIMARY KEY AUTOINCREMENT,
               password STRING NOT NULL,
               full_name TEXT NOT NULL,
               balance REAL
               );""" )

cursor.execute("""
CREATE TABLE IF NOT EXISTS cards(
               card_number TEXT PRIMARY KEY,
               pin TEXT NOT NULL,
               status TEXT NOT NULL,
               account_id INTEGER NOT NULL,
               FOREIGN KEY (account_id) REFERENCES accounts(id)         
               );""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (account_id) REFERENCES accounts(id)
                );""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS atm(
               num50Bills INTEGER,
               num20Bills INTEGER,
               num10Bills INTEGER
               );""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS casettes(
               id INTEGER NOT NULL,
               dispensed INTEGER,
               remaining INTEGER
               );""")

cursor.execute("""
               ALTER TABLE casettes
                ADD COLUMN total INTEGER DEFAULT 0;
               """)

cursor.execute("""
               UPDATE casettes
                SET total = dispensed + remaining;
               """)




'''
cursor.execute("""
               INSERT INTO atm (num50Bills, num20Bills, num10Bills)
               VALUES (?, ?, ?)
                """, (200, 300, 500))

cursor.execute("""
               INSERT INTO casettes (id, dispensed, remaining)
               VALUES (?, ?, ?)
               """, (50, 0, 200))

cursor.execute("""
               INSERT INTO casettes (id, dispensed, remaining)
               VALUES (?, ?, ?)
               """, (20, 0, 300))

cursor.execute("""
               INSERT INTO casettes (id, dispensed, remaining)
               VALUES (?, ?, ?)
               """, (10, 0, 500))



print("Database initialized with test data.")
'''


conn.commit()
conn.close()    