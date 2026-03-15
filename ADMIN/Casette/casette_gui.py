import tkinter as tk
from tkinter import messagebox, font
from ATM_LOGIC.casette import Casette
from ADMIN.Casette.Fill.fill_button import FillButton

class CasetteGUI:
    def __init__(self, root, id):
        self.root = root
        self.root.title(f"Casette #{id} Info")
        self.root.geometry("360x260")
        self.root.resizable(False, False)

        # Define fonts
        header_font = font.Font(family="Helvetica", size=16, weight="bold")
        label_font  = font.Font(family="Helvetica", size=12)

        # Outer padding
        container = tk.Frame(root, padx=15, pady=15, bg="#ffffff")
        container.pack(fill="both", expand=True)

        # Card frame
        card = tk.Frame(container, bd=2, relief="groove", padx=10, pady=10, bg="#f9f9f9")
        card.pack(fill="both", expand=True)

        # Header
        header = tk.Label(
            card,
            text="Casette Status",
            font=header_font,
            bg="#f9f9f9"
        )
        header.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Load data
        casette = Casette.loadFromDb(int(id))
        if not casette:
            messagebox.showerror("Not Found", f"No casette with ID {id} found.")
            dispensed, remaining = "—", "—"
        else:
            dispensed  = casette.dispensed
            remaining  = casette.remaining

        total = dispensed + remaining if isinstance(dispensed, int) else "—"

        # Labels and values
        fields = [
            ("Dispensed:", dispensed),
            ("Remaining:", remaining),
            ("Total:", total),
        ]

        for i, (label_text, value) in enumerate(fields, start=1):
            lbl = tk.Label(card, text=label_text, font=label_font, anchor="w", bg="#f9f9f9")
            val = tk.Label(card, text=value,      font=label_font, anchor="e", bg="#f9f9f9")
            lbl.grid(row=i, column=0, sticky="w", padx=(0,10), pady=5)
            val.grid(row=i, column=1, sticky="e", pady=5)

        # Button row frame
        button_row = tk.Frame(container, bg="#ffffff")
        button_row.pack(pady=(10, 0))

        # Close button (left)
        close_button = tk.Button(
            button_row,
            text="Close",
            width=10,
            command=root.destroy
        )
        close_button.pack(side="left", padx=5)

        FillButton(button_row, id, self.root)

        
