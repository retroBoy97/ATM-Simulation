import tkinter as tk

from ADMIN.exit_button import ExitButton
from ADMIN.Login.id_entry import idEntry
from ADMIN.Login.password_entry import PasswordEntry
from ADMIN.Login.instruction_label import InstructionLabel
from ADMIN.Login.enter_button import EnterButton

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("800x500")

        # Configure grid weights for resizing
        for i in range(4):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.root.grid_columnconfigure(j, weight=1)

        # Exit Button
        self.exit_button_frame = tk.Frame(self.root)
        self.exit_button_frame.grid(row = 3, column = 0)
        self.exit_button = ExitButton(self.exit_button_frame, self.root)
        
        self.idEntry = idEntry(self.root)
        self.passwordEntry = PasswordEntry(self.root)
        self.instructionLabel = InstructionLabel(self.root)

        # Enter Button
        self.enter_button_frame = tk.Frame(self.root)
        self.enter_button_frame.grid(row = 3, column = 1)
        self.enter_button = EnterButton(self.enter_button_frame, self.root, self.idEntry, self.passwordEntry, self.instructionLabel)

