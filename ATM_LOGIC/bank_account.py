from datetime import datetime
import sqlite3

class BankAccount:
    def __init__(self, fullName, cardNumber, password):
        print("Bank account created")
        self.fullName = fullName
        self.cardNumber = cardNumber
        self.password = password
        self.balance = 0
        self.transactionHistory = []
        
    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if (amount <= 0):
            print("the amount should be positive")
        self.balance += amount
        self.addDeposit(amount)
        # Add deposit and transaction in database
        self.depositDb(self.cardNumber, amount)


    def addDeposit(self, amount):
        if (amount <= 0):
            print("Amount should be positive")
        entry = {
            'timestamp': datetime.now(),
            'amount': amount,
            'type' : "Deposit"
        }
        self.transactionHistory.append(entry)

    def withdraw(self, amount):
        self.balance -= amount
        self.addWithdrawal(amount)
        # Add deposit and transaction in database
        self.withdrawDb(self.cardNumber, amount)
        
    def addWithdrawal(self, amount):
        if (amount <= 0):
            print("Amount should be positive")
        entry = {
            'timestamp': datetime.now(),
            'amount': amount,
            'type' : "Withdrawal",
            'balance_after': self.balance
        }
        self.transactionHistory.append(entry)
  
    def viewTransactionHistory(self):
        if not self.transactionHistory:
            print("No transactions yet.")
            return

        print("Date & Time          | Type       | Amount")
        print("---------------------|------------|---------")
        for t in self.transactionHistory:
            timestamp = t['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp}  | {t['type']:10} | ${t['amount']:7.2f}")

    def depositDb(self, cardNumber, amount):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE accounts
                       SET balance = balance + ?
                       WHERE id = (
                            SELECT account_id
                            FROM cards
                            WHERE cards.card_number = ?
                       )
        """, (amount, cardNumber))

        if cursor.rowcount == 0:
            conn.close()
            raise Exception("No account found for card : ", cardNumber)
        
        cursor.execute("""
                       INSERT INTO transactions (account_id, type, amount, timestamp)
                       VALUES(
                       (SELECT account_id from cards WHERE card_number = ?),
                       "Deposit",
                       ?,
                       ?
                       )
        """, (cardNumber, amount, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    def withdrawDb(self, cardNumber, amount):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE accounts
                       SET balance = balance - ?
                       WHERE id = (
                            SELECT account_id
                            FROM cards
                            WHERE cards.card_number = ?
                       )
        """, (amount, cardNumber))

        if cursor.rowcount == 0:
            conn.close()
            raise Exception("No account found for card : ", cardNumber)
        
        cursor.execute("""
                       INSERT INTO transactions (account_id, type, amount, timestamp)
                       VALUES(
                       (SELECT account_id from cards WHERE card_number = ?),
                       "Withdrawal",
                       ?,
                       ?
                       )
        """, (cardNumber, amount, datetime.now().isoformat()))
        conn.commit()
        conn.close

    @staticmethod
    def loadFromDb(cardNumber):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT a.full_name, a.password, a.balance, a.id
                       FROM accounts a
                       JOIN cards c 
                       ON c.account_id = a.id
                       WHERE c.card_number = ?
        """, (cardNumber, ))
        accountRow = cursor.fetchone()
        
        if accountRow:
            fullName, password, balance, accountId = accountRow
            account = BankAccount(fullName, cardNumber, password)
            account.balance = balance
            cursor.execute("""
                           SELECT t.type, t.amount, t.timestamp
                           FROM transactions t
                           WHERE t.account_id = ?
                           ORDER BY t.timestamp ASC
                            """, (accountId, ))
            transactionRows = cursor.fetchall()
            if transactionRows:
                for row in transactionRows:
                    type, amount, timestamp = row
                    entry = {
                        "timestamp": datetime.fromisoformat(timestamp),
                        "amount": amount,
                        "type": type
                    }
                    account.transactionHistory.append(entry)
            
            return account
        else:
            raise Exception("Invalid card number")
        