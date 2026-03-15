import sqlite3
import tkinter as tk

class State:
    def __init__(self, num50Bills, num20Bills, num10Bills):
        self.num50Bills = num50Bills
        self.num20Bills = num20Bills
        self.num10Bills = num10Bills

    def saveState(self):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO state (num50Bills, num20Bills, num10Bills)
                       VALUES (?, ?, ?)
                       """, (self.num50Bills, self.num20Bills, self.num10Bills))

        conn.commit()
        conn.close()

    @staticmethod
    def loadFromDb():
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT remaining from casettes
                       """)
        
        result = cursor.fetchall()
        num50Bills = result[0][0]
        num20Bills = result[1][0]
        num10Bills = result[2][0]

        return State(num50Bills, num20Bills, num10Bills)
    
state = State.loadFromDb()
print(state.num50Bills)
print(state.num20Bills)
print(state.num10Bills)
