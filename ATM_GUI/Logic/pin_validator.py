from ATM_GUI.Logic.session import Session
import sqlite3

class PINValidator:
    MAX_ATTEMPTS = 3

    def __init__(self, session, screen):
        self.session = session
        self.screen = screen
        self.enteredPIN = ""
        self.attempts = 0

    def validatePIN(self):
        if (self.session.PIN == self.enteredPIN):
            return "Granted"
        else:
            self.attempts += 1
            if (self.attempts > 2):
                self.blockCard()
                return "Blocked"
            else:
                return "Try Again"
            

    def getEnteredPIN(self):
        return self.enteredPIN
    
    def setEnteredPIN(self, PIN):
        self.enteredPIN = PIN

    def blockCard(self):
        self.session.isBlocked = True
        self.session.cardStatus = "Blocked"
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE cards
                       SET status = "Blocked"
                       WHERE card_number = ?
                       """, (self.session.cardNumber, ))
        conn.commit()
        conn.close()

    def reset(self):
        self.session = None

    def setSession(self, session):
        self.session = session

