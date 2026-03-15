import sqlite3

class Casette:
    def __init__(self, id, dispensed, remaining):
        self.id = id
        self.dispensed = dispensed
        self.remaining = remaining

    @staticmethod
    def loadFromDb(id):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT c.dispensed, c.remaining
                       FROM casettes c
                       WHERE c.id = ?
                       """, (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            dispensed, remaining = row
            return Casette(id, dispensed, remaining)
        
        return None
    
    @staticmethod
    def reset():
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE casettes
                       SET dispensed = 0, remaining = 0, total = 0
                       """)
        
        conn.commit()
        conn.close()
    
    @staticmethod
    def fill(id, numBills):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE casettes
                       SET remaining = remaining + ?, total = total + ?
                       WHERE id = ?
                       """, (numBills, numBills, id))
        
        conn.commit()
        conn.close()

    @staticmethod
    def dispense(id, numBills):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE casettes
                       SET remaining = remaining - ?, dispensed = dispensed + ?
                       WHERE id = ?
                       """, (numBills, numBills, id))
        
        conn.commit()
        conn.close()



        
