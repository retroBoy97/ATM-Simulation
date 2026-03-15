import sqlite3

from ATM_LOGIC.bank_account import BankAccount
from ATM_LOGIC.casette import Casette

class ATM:
    def __init__(self, num50Bills, num20Bills, num10Bills):
        print("ATM created")
        self.currency = {
            50: num50Bills,
            20: num20Bills,
            10: num10Bills
        }


    def processWithdrawal(self, card, amount):

        account = card.getAccount()
        if amount > account.balance:
            return {}, "Insufficient balance"

        result = {}
        amountUnchanged = amount

        for bill in [50, 20, 10]:
            numberNeeded = amount // bill
            numberAvailable = self.currency[bill]
            numberToUse = min(numberNeeded, numberAvailable)
            if numberToUse > 0:
                result[bill] = numberToUse
                self.currency[bill] -= numberToUse
                amount -= bill * numberToUse

        if amount != 0:
            # Rollback
            for bill, qty in result.items():
                self.currency[bill] += qty
            return {}, "ATM cannot dispense the exact amount"

        ATM.updateAtmDb(result.get(50, 0), result.get(20, 0), result.get(10, 0))

        account.withdraw(amountUnchanged)
        return result, "Success"
    
    def viewTransactionHistory(self, card):
        bankAccount = BankAccount.loadFromDb(card.cardNumber)
        bankAccount.viewTransactionHistory()
    
    def checkBalance(self, card):
        bankAccount = BankAccount.loadFromDb(card.cardNumber)
        return bankAccount.balance

    @staticmethod
    def loadFromDb():
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT remaining FROM casettes
                       """)
        results = cursor.fetchall()
        conn.close()

        num50Bills, num20Bills, num10Bills = [row[0] for row in results]

        return ATM(num50Bills, num20Bills, num10Bills)

    @staticmethod
    def updateAtmDb(used50Bills, used20Bills, used10Bills):
        Casette.dispense(50, used50Bills)
        Casette.dispense(20, used20Bills)
        Casette.dispense(10, used10Bills)

    