import tkinter as tk
import pygame
from tkinter import ttk
from ATM_GUI.inputOutput.screen_gui import ScreenGUI
from ATM_GUI.Logic.pin_validator import PINValidator
import sys

class KeyboardGUI:
    def __init__(self, root, screen, pinValidator, choiceKeyboard, session):
        self.root = root
        self.choiceKeyboard = choiceKeyboard
        self.pinValidator = pinValidator    
        self.screen = screen
        self.session = session
        self.state = "Blocked"

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill="both")


        # Modern button style
        btn_font = ("Segoe UI", 14, "bold")
        btn_bg = "#e6e6e6"
        btn_fg = "#000000"
        btn_active_bg = "#d0d0d0"

        # Define the layout of the keypad buttons
        keys = [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9'],
                ['Delete', '0', 'Enter']]

        for i in range(4):  # Rows
            for j in range(3):  # Columns
                key = keys[i][j]
                button = tk.Button(
                    self.frame,
                    text=key,
                    font=btn_font,
                    width=8,
                    height=2,
                    bg=btn_bg,
                    fg=btn_fg,
                    activebackground=btn_active_bg,
                    relief="raised",        # gives slight 3D effect
                    bd=2,                   # border thickness
                    highlightthickness=0,
                    command=lambda k=key: self.click(k)
                )
                button.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")

        # Make all rows and columns expand equally
        for i in range(4):
            self.frame.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.frame.grid_columnconfigure(j, weight=1)

        pygame.mixer.init()


    def click(self, key):
        if (self.state == "Activated"):
            pygame.mixer.music.load("C:/Users/MSI/Downloads/Beep Button Sound Effect.mp3")
            pygame.mixer.music.play(loops = 0)
            
            enteredPIN = self.pinValidator.getEnteredPIN()
            displayedPIN = self.screen.getDisplayedPIN()
            if (key == "Delete" and len(displayedPIN) != 0):
                displayedPIN = displayedPIN[:-1]
                enteredPIN = enteredPIN[:-1]

                self.pinValidator.setEnteredPIN(enteredPIN)
                self.screen.displayPIN(displayedPIN)

            elif (key == "Enter"):
                print(enteredPIN)
                print(displayedPIN)
                pinStatus = self.pinValidator.validatePIN()

                if(pinStatus == "Granted"):
                    if self.session.cardStatus == "Blocked":
                        self.state = "Blocked"
                        self.screen.displayMessage("Your card is blocked")
                        self.screen.clearPIN()
                        self.root.after(4000, self.session.resetATM)
                        return

                    self.screen.displayMessage("Access Granted")
                    self.screen.clearPIN()
                    self.state = "Blocked"
                    self.choiceKeyboard.function = "mainMenu"
                    self.screen.displayMenu()

                elif (pinStatus == "Blocked"):
                    self.screen.displayMessage("Too many attempts \n Your card is blocked ")
                    self.screen.clearPIN()
                    self.state = "Blocked"
                    self.root.after(4000, self.session.resetATM)

                else:
                    self.screen.displayMessage("PIN is wrong \n try again")
                    self.pinValidator.setEnteredPIN("")
                    self.screen.clearPIN()

            else:
                if(len(displayedPIN) != 4):
                    enteredPIN = enteredPIN + key 
                    displayedPIN = displayedPIN + "*"

                    self.pinValidator.setEnteredPIN(enteredPIN)
                    self.screen.displayPIN(displayedPIN)

    def reset(self):
        self.state = "Blocked"

