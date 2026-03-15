from ATM_LOGIC.card import Card
import sys

class CardReader:
    def __init__(self):
        print("Card reader created")

    def readCard(self, cardNumber):
        return Card.loadFromDb(cardNumber)

    def returnCard(self):
        print("Here is your card")
        sys.exit()

    #move to atm
    def blockcard(self):
        print("Your card has been blocked")
        sys.exit()