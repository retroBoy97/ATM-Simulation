import tkinter as tk
import pygame
from datetime import datetime

from ATM_LOGIC.bank_account import BankAccount
from ATM_LOGIC.card import Card
from ATM_LOGIC.request_checkbook import RequestCheckbook


class ChoiceKeyboard:
    def __init__(self, root, button_map, session, screen, atm, moneyDispenser, printer):
        self.root = root
        self.session = session
        self.screen = screen
        self.moneyDispenser = moneyDispenser
        self.printer = printer
        self.atm = atm
        self.function = None
        self.buttons = []

        # Configure required rows/columns
        for r, _ in button_map.values():
            root.rowconfigure(r, weight=1)
        for _, c in button_map.values():
            root.columnconfigure(c, weight=1)

        btn_style = {
            'font': ('Arial', 10),
            'relief': 'raised',
            'bd': 2,
            'bg': '#e0e0e0'
        }

        for num, (row, col) in button_map.items():
            btn = tk.Button(
                root,
                text=str(num),
                command=lambda n=num: self.click(n),
                **btn_style
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            self.buttons.append(btn)

        pygame.mixer.init()

    def click(self, number):
        if(self.function == "mainMenu"):
            account = BankAccount.loadFromDb(self.session.cardNumber)
            match number:
                case 1: 
                    self.screen.instruction_label.config(
                        text="Your balance is : " + str(account.balance),
                        justify="left",  # Left-align for menu items
                        font=self.screen.font_style
                    )
                    self.undoButton.state = "Activated"

                case 2:
                    self.screen.displayWithdrawalMenu()
                    self.function = "withdrawalMenu"
                    self.undoButton.state = "Activated"

                case 3:
                    history = account.transactionHistory

                    if not history:
                        message = "No transactions yet."
                    else:
                        # Take the last 5 transactions (or fewer)
                        recent_history = history[-5:]

                        lines = []
                        for i, txn in enumerate(recent_history, 1):
                            ts = txn['timestamp'].strftime("%Y-%m-%d %H:%M")
                            amt = f"{txn['type']}: {txn['amount']:.2f}"
                            lines.append(f"{i}. {ts} | {amt} DT")

                        message = "Last Transactions:\n" + "\n".join(lines)

                    self.screen.displayMessage(message)
                    self.undoButton.state = "Activated"

                case 4:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.screen.displayMessage(now)
                    self.undoButton.state = "Activated"

                case 5:
                    request = RequestCheckbook(self.session.cardNumber)
                    request.depositRequest()
                    self.screen.displayMessage("Successful request")
                    self.root.after(3000, self.screen.displayMenu)

                case 6:
                    self.screen.displayMessage("Please take your card")
                    self.root.after(6000, self.reset)
            
            pygame.mixer.music.load("C:/Users/MSI/Downloads/Beep Button Sound Effect.mp3")
            pygame.mixer.music.play(loops = 0)
            
                
        elif (self.function == "withdrawalMenu"):
            amount_map = {
                1: 10,
                2: 20,
                3: 30,
                4: 50,
                5: 100,
                6: 200
            }
            amount = amount_map.get(number)
            if amount is None:
                self.screen.displayMessage("Invalid selection.")
                return

            # Retrieve Card and withdraw
            card = Card.loadFromDb(self.session.cardNumber)
            result, withdrawalStatus = self.atm.processWithdrawal(card, amount)
            self.function = None

            if withdrawalStatus == "Success":
                self.undoButton.state = "Blocked"
                self.screen.displayMessage("Success")
                self.screen.parent.after(3000, lambda: self.screen.displayMessage("Please take your card"))
                self.screen.parent.after(5000, lambda: self.screen.displayMessage("Please take your money"))
                self.screen.parent.after(5000, lambda: self.moneyDispenser.displayDispensedBills(result))  
                self.screen.parent.after(7000, lambda: self.moneyDispenser.clear())
                self.screen.parent.after(9000, lambda: self.screen.displayMessage("Please take your receipt"))        
                self.screen.parent.after(9000, lambda: self.printer.printReceipt(self.session.cardNumber))
                self.root.after(14000, self.reset)

            elif (withdrawalStatus == "ATM cannot dispense the exact amount"):
                self.screen.displayMessage("An error occured \n The amount could not be withdrawn")           
                self.screen.parent.after(3000, lambda: self.screen.displayMessage("Please take your card"))
                self.undoButton.state = "Blocked"
                self.root.after(9000, self.reset)            

            elif (withdrawalStatus == "Insufficient balance"):
                self.screen.displayMessage("Your balance is insufficient")
                self.screen.parent.after(3000, lambda: self.screen.displayMenu())
                self.function = "mainMenu" 

            pygame.mixer.music.load("C:/Users/MSI/Downloads/Beep Button Sound Effect.mp3")
            pygame.mixer.music.play(loops = 0)

            
            
    def reset(self):
        self.function = None
        self.session.resetATM()