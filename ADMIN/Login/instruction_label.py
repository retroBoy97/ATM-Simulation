import tkinter as tk

class InstructionLabel:
    def __init__(self, root):
        self.root = root

        # Shared styles
        self.font_style = ("Segoe UI", 20, "bold")
        self.bg_color = "#f0f4f8"         # light background
        self.border_color = "#4a90e2"     # border color
        self.fg_color = "#333333"         # dark text

        self.frame = tk.Frame(
            root,
            bg=self.bg_color ,
            highlightbackground=self.border_color,
            highlightthickness=2
        )
        self.frame.grid(row=0, column=0, sticky="nsew",columnspan = 2, padx=10, pady=(10, 5))

        self.label = tk.Label(
            self.frame,
            text="Welcome to the ATM\nPlease enter your id:",
            font=self.font_style,
            bg=self.bg_color,
            fg=self.fg_color,
            justify="center",
            wraplength=800
        )
        self.label.pack(expand=True, fill="both", padx=10, pady=10)

    def displayMessage(self, message):
        self.label.config(text = message)