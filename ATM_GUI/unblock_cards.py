import sqlite3

conn = sqlite3.connect("atm.db")
cursor = conn.cursor()

cursor.execute("""
                UPDATE cards
               SET status = "Valid"
               """)

conn.commit()
conn.close() 