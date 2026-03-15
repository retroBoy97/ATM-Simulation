import tkinter as tk
from ADMIN.admin import Admin
from ADMIN.Menu.menu_ui import MenuUI

class EnterButton:
    def __init__(self, root, loginRoot, idEntry, passwordEntry, instructionLabel):
        self.root = root
        self.loginRoot = loginRoot
        self.idEntry = idEntry
        self.passwordEntry = passwordEntry
        self.instructionLabel = instructionLabel

        self.frame = tk.Frame(root)
        self.frame.pack(pady=5)

        self.button = tk.Button(
            self.frame,
            text = "Enter",
            width = 25,
            height = 4,
            command = lambda: self.enter()
        )
        self.button.pack()

    def enter(self):
        id = self.idEntry.id_entry.get()
        password = self.passwordEntry.password_entry.get()
        admin, message = Admin.loadFromDb(id)

        if message == "Invalid id":
            self.instructionLabel.displayMessage("Invalid id or password \n Try again")
            self.idEntry.clear()
            self.passwordEntry.clear()

        else:
            if password == admin.password:
                self.loginRoot.destroy()
                menu_window = tk.Tk()
                MenuUI(menu_window)

            else:
                self.instructionLabel.displayMessage("Invalid id or password \n Try again")
                self.idEntry.clear()
                self.passwordEntry.clear()

