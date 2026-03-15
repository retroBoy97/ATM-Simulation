import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk
import pygame

class MoneyDispenser:
    def __init__(self, root):
        # Outer frame
        self.frame = ttk.Frame(root, padding=10, borderwidth=2, relief="groove")
        self.frame.pack(fill='both', expand=True)

        # Title label
        self.title_label = tk.Label(
            self.frame,
            text="Money Dispenser",
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

    def displayDispensedBills(self, bills_dict):
        pygame.mixer.music.load("C:/Users/MSI/Downloads/Cash Sound Effect.mp3")
        pygame.mixer.music.play(loops = 0)
        if not bills_dict:
            self.label.config(text="No money dispensed.")
            return

        text_lines = ["Money Dispensed:"]
        for bill, count in bills_dict.items():
            text_lines.append(f"{bill} DT x {count}")

        self.label.config(text="\n".join(text_lines))

    def displayMessage(self, message):
        self.label.config(text=message)

    def clear(self):
        self.label.config(text="")
