import tkinter as tk
from ATM_LOGIC.card import Card
import sqlite3
from ATM_GUI.inputOutput.screen_gui import ScreenGUI
from ATM_GUI.Logic.pin_validator import PINValidator
from ATM_GUI.Logic.session import Session

class CardReaderGUI:
    def __init__(self, root, session, screen, keyboard, pinValidator, adminButton):
        self.session = session
        self.screen = screen
        self.keyboard = keyboard
        self.pinValidator = pinValidator
        self.adminButton = adminButton

        # Load all existing card numbers
        self.cardNumbers = self.loadCardNumbers()
        self.root = root

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.button = tk.Button(
            self.frame,
            text = "Select card",
            width = 25,
            height = 4,   
        )
        self.button.pack()

        # Bind hover events to show/hide the menu
        self.button.bind("<Enter>", self.displayMenu)
        self.button.bind("<Leave>", self.hideMenu)

        self.selectedCard = None
        self.menu = None

    def loadCardNumbers(self):
        conn = sqlite3.connect("atm.db")
        cursor = conn.cursor()

        cursor.execute(""" SELECT card_number FROM cards """)
        rows = cursor.fetchall()
        
        conn.close()
        return[row[0] for row in rows]
    
    # Show a pop-up menu with cardNumbers numbers when hovering
    def displayMenu(self, event):
        if (self.cardNumbers):
            # Create a new menu each time to ensure fresh data
            self.menu = tk.Menu(self.root, tearoff=0)
            for cardNumber in self.cardNumbers:
                self.menu.add_command(
                    label = cardNumber,
                    command=lambda cn=cardNumber: self.selectCardNumber(cn)
                )
            try:
                self.menu.tk_popup(event.x_root, event.y_root)
            finally:
                if self.menu:
                    self.menu.grab_release()

    def hideMenu(self, event):
        if(self.menu):
            self.menu.unpost()
            self.menu = None

    def selectCardNumber(self, cardNumber):
        self.selectedCard = Card.loadFromDb(cardNumber)
        self.session.cardNumber = cardNumber
        self.session.PIN = self.selectedCard.PIN
        self.session.cardStatus = self.selectedCard.status
        self.pinValidator.setSession(self.session)
        self.button.config(text = f"Card : {cardNumber}")
        self.adminButton.State = "Blocked"

        if(self.session.cardStatus == "Blocked"):
            self.screen.displayMessage("Your card is Blocked")
            self.keyboard.state = "Blocked"
            self.root.after(4000, self.session.resetATM)
        else:
            self.button.config(text = f"Card : {cardNumber}")
            self.screen.displayMessage("Please enter your PIN")
            self.keyboard.state = "Activated"



    def getCurrentCard(self):
        if self.currentCard:
            return self.currentCard
        return None
    
    def reset(self):
        self.selectedCard = None
        self.session.cardNumber = None
        self.session.PIN = None
        self.session.cardStatus = None
        self.button.config(text="Select card")

        
    







