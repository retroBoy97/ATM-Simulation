import tkinter as tk

from ATM_LOGIC.casette import Casette
from ADMIN.state import State

class ResetButton:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(root)
        self.frame.pack(pady=5)

        self.button = tk.Button(
            self.frame,
            text = "Reset",
            width = 25,
            height = 4,
            command = lambda: self.reset()
        )
        self.button.pack()

    def reset(self):
        confirm_window = tk.Toplevel(self.root)
        confirm_window.title("Confirm Reset")
        confirm_window.geometry("300x150")

        # Message
        label = tk.Label(confirm_window, text="Are you sure you want to reset?", font=("Arial", 12))
        label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(confirm_window)
        button_frame.pack()

        yes_button = tk.Button(
            button_frame,
            text="Yes",
            width=10,
            command=lambda: self.perform_reset(confirm_window)
        )
        yes_button.grid(row=0, column=0, padx=10)

        no_button = tk.Button(
            button_frame,
            text="No",
            width=10,
            command=confirm_window.destroy
        )
        no_button.grid(row=0, column=1, padx=10)

    def perform_reset(self, window):
        window.destroy()
        state = State.loadFromDb()
        state.saveState()
        Casette.reset()
        

