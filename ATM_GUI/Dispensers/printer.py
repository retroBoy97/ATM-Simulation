import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pygame

class Printer:
    def __init__(self, root):
        # Outer frame
        self.frame = ttk.Frame(root, padding=10, borderwidth=2, relief="groove")
        self.frame.pack(fill='both', expand=True)

        # Title label
        self.title_label = tk.Label(
            self.frame,
            text="Printer",
            font=("Segoe UI", 14, "bold"),
            fg="#333",
            anchor="center"
        )
        self.title_label.pack(pady=(0, 5))

        # Main display area
        self.label = tk.Label(
            self.frame,
            text="",
            font=("Segoe UI", 12),
            justify="left",
            anchor="w",
            bg="#f0f0f0"
        )
        self.label.pack(fill="both", expand=True, padx=5, pady=5)

        pygame.mixer.init()

    from datetime import datetime

    def printReceipt(self, cardNumber):
        pygame.mixer.music.load("C:/Users/MSI/Downloads/Printer Receipt - Sound Effect.mp3")
        pygame.mixer.music.play(loops = 0)
        text = f"Bank: Al Tijari\nCard number: {cardNumber}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.label.config(text=text)


    def clear(self):
        self.label.config(text="")
