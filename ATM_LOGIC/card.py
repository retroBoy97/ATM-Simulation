import sqlite3
from ATM_LOGIC.bank_account import BankAccount

class Card:
    def __init__(self, cardNumber, PIN, account):
        self.cardNumber = cardNumber
        self.PIN = PIN
        self.status = "Valid"
        self.account = account

    def getPIN(self):
        return self.PIN
    
    def getCardNumber(self):
        return self.cardNumber
    
    def getStatus(self):
        return self.status
    
    def getAccount(self):
        return self.account
    
    @staticmethod
    def loadFromDb(cardNumber):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT c.card_number, c.pin, c.status,
                    a.id, a.password, a.full_name, a.balance
            FROM cards c
            JOIN accounts a on c.account_id = a.id
            WHERE c.card_number = ? 
            """, (cardNumber,))
        
        row = cursor.fetchone()
        conn.close()

        if row:
            # Unpack values
            cardNumber, PIN, status, accountId, password, fullName, balance = row

            # Create bankAccount instance
            bankAccount = BankAccount(fullName, cardNumber, password)
            bankAccount.balance = balance

            # Create card instance
            card = Card(cardNumber, PIN, bankAccount)
            card.status = status
            return card
        
        else:
            raise Exception("Invalid card number")
        
    
