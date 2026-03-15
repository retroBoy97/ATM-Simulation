import tkinter as tk

class AdminButton:
    def __init__(self, root, atmRoot):
        self.root = root
        self.atmRoot = atmRoot
        self.state = "Activated"

        self.button = tk.Button(
            root,
            text = "Admin",
            command = self.click
        )
        self.button.pack(expand=True, fill='both')  

    def click(self):
        if self.state == "Activated":
            from ADMIN.Login.login_ui import LoginUI
            self.atmRoot.destroy()
            login_window = tk.Tk()
            LoginUI(login_window)