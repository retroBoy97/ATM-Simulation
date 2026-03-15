import sqlite3

class Admin:
    def __init__(self, id, password, fullName):
        self.id = id
        self.password = password
        self.fullName = fullName

    @staticmethod
    def loadFromDb(id):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT password, full_name
                       FROM admins
                       WHERE id = ?
                       """, (id,))
        
        row = cursor.fetchone()
        conn.close()

        if row:
            password, fullName = row
            admin = Admin(id, password, fullName)
            return admin, "Valid id"
        else:
            return None, "Invalid id"
