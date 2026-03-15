import tkinter as tk

from ATM_GUI.inputOutput.screen_gui import ScreenGUI
from ATM_GUI.inputOutput.keyboard_gui import KeyboardGUI
from ATM_GUI.inputOutput.card_reader_gui import CardReaderGUI
from ATM_GUI.Logic.session import Session
from ATM_GUI.Logic.pin_validator import PINValidator
from ATM_GUI.Dispensers.printer import Printer
from ATM_GUI.Dispensers.money_dispenser import MoneyDispenser
from ATM_GUI.inputOutput.undo_button import UndoButton
from ATM_GUI.admin_button import AdminButton

from ATM_LOGIC.atm import ATM

from ATM_GUI.inputOutput.choice_keyboard import ChoiceKeyboard

class ATMGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ATM Simulator")
        self.root.geometry("1200x800")

        # === Step 1: Configure the root grid layout ===
        for r in range(8):
            self.root.rowconfigure(r, weight=1)
        for c in range(6):  
            self.root.columnconfigure(c, weight=1)

        self.session = Session()
        self.session.set_ATM_GUI(self)

        # Screen (cols 1–3, rows 0–3)
        self.screen_frame = tk.Frame(self.root)
        self.screen_frame.grid(row=0, column=1, rowspan=2, columnspan=3, sticky="nsew")

        # Main keyboard (cols 1–3, rows 4–7) → you can add this later
        self.keyboard_frame = tk.Frame(self.root)
        self.keyboard_frame.grid(row=4, column=1, rowspan=4, columnspan=3, sticky="nsew")

        # Devices (card reader, money dispenser, printer) → will go in col 5, each 2 rows
        self.device_frames = []
        for i in range(3):
            f = tk.Frame(self.root)
            f.grid(row=i*2, column=5, rowspan=2, sticky="nsew")
            self.device_frames.append(f)

        # === Step 3: Instantiate your components into those frames ===

        self.atm = ATM.loadFromDb()
        print(self.atm.currency[50])


        self.screen = ScreenGUI(self.screen_frame)
        self.moneyDispenser = MoneyDispenser(self.device_frames[1])
        self.printer = Printer(self.device_frames[2])

        # Just call it once with the main root window
        self.choiceKeyboard = ChoiceKeyboard(
            self.root,                    # parent is root grid
            button_map={                 # map button numbers to grid columns
                1: (0, 0),
                2: (1, 0),
                3: (0, 4),
                4: (1, 4),
                5: (2, 0),
                6: (2, 4),
            },
            session=self.session,
            screen=self.screen,
            atm=self.atm,
            moneyDispenser = self.moneyDispenser,
            printer = self.printer
        )


        # Frame for Undo Button
        self.undo_frame = tk.Frame(self.root)
        self.undo_frame.grid(row=2, column=2, rowspan=2, sticky="nsew")

        # Create Undo Button instance
        self.undoButton = UndoButton(self.undo_frame, self.screen)
        self.choiceKeyboard.undoButton = self.undoButton
        self.undoButton.choiceKeyboard = self.choiceKeyboard

        # Frame for Admin Button
        self.admin_frame = tk.Frame(self.root, width = 20, height = 5)
        self.admin_frame.grid(row = 6, column = 5)
        self.adminButton = AdminButton(self.admin_frame, self.root)

        self.pinValidator = PINValidator(self.session, self.screen)

        self.keyboard = KeyboardGUI(
            self.keyboard_frame,
            self.screen,
            self.pinValidator,
            self.choiceKeyboard,
            self.session,
        )
        
        self.cardReader = CardReaderGUI(self.device_frames[0], self.session, self.screen, self.keyboard, self.pinValidator, self.adminButton)

        self.root.mainloop()

    def reset(self):
        self.moneyDispenser.clear()
        self.printer.clear()

        self.keyboard.reset()
        self.screen.reset()
        self.undoButton.reset()
        self.adminButton.state = "Activated"
        self.cardReader.reset()
        
        self.pinValidator.reset()

        