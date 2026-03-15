import tkinter as tk


class ExitButton:
    def __init__(self, root, loginRoot):
        self.root = root
        self.loginRoot = loginRoot
        self.frame = tk.Frame(root)
        self.frame.pack(pady = 5)

        self.button = tk.Button(
            self.frame,
            text = "Exit",
            width = 25,
            height = 4,   
            command= lambda: self.exit()
        )
        self.button.pack()

    def exit(self):
        from ATM_GUI.atm_gui import ATMGUI
        self.loginRoot.destroy()
        ATMGUI()