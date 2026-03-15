

from ATM_LOGIC.bank_account import BankAccount
from ATM_LOGIC.atm import ATM
from ATM_LOGIC.bank import Bank
from ATM_LOGIC.card import Card
import sys

### Initialization
bank = Bank("Al Tijari")



atm = ATM(10, 5, 3)
bank.addATM(atm)

### Main program
print("Welcome to the ATM")
print("please enter your card")
cardNumber = input()
card = atm.cardReader.readCard(cardNumber)
if (card.status == "Expired"):
    print("Your card is Expired")
    atm.cardReader.returnCard()
realPIN = card.getPIN()
print(realPIN)
print("Please enter your PIN")
PIN = (input())
attempts = 2
while(PIN != realPIN and attempts > 0):
    print("PIN is wrong, reenter it")
    PIN = (input())       
    attempts -= 1
if attempts == 0:
    atm.cardReader.blockCard()
        
        
while True:
    atm.displayMenu()
    choice = int(input())
    match choice:
        case 1:
            print("Your current balance is", atm.checkBalance(cardNumber))

        case 2:
            print("Please select an amount to withdraw")
            print("1 : 10 DT")
            print("2 : 40 DT")
            print("3 : 100 DT")
            print("4 : 200 dt")
            amountChosen = int(input())
            match amountChosen:
                case 1:
                    print (atm.processWithdrawal(card, 10))
                case 2:
                    print (atm.processWithdrawal(card, 40))
                case 3:
                    print (atm.processWithdrawal(card, 100))
                case 4:
                    print (atm.processWithdrawal(card, 200))
                    print()

            print("Do you like a receipt ?")
            print("1 : Yes")
            print("2 : NO")
            choiceReceipt = int(input())
            match choiceReceipt:
                case 1:
                    atm.printer.printReceipt()
                    atm.cardReader.returnCard()
                    
                case 2:
                    atm.cardReader.returnCard()
            break

        case 3:
            print (atm.viewTransactionHistory(card))

        case 4:
            print("See you next time")
            sys.exit()
