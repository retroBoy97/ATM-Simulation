import sqlite3
from datetime import datetime  # ✅ Correct way to import
from ATM_LOGIC.card import Card


class RequestCheckbook:
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    def depositRequest(self):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO requests (card, date)
            VALUES (?, ?)
        """, (self.cardNumber, self.date))

        conn.commit()
        conn.close()
