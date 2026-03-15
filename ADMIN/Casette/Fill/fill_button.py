import tkinter as tk

from ATM_LOGIC.casette import Casette
from ADMIN.Casette.Fill.fill_window import FillWindow

class FillButton:
    def __init__(self, root, casetteId, casetteRoot):
        self.root = root
        self.casetteId = casetteId
        self.casetteRoot = casetteRoot
        # Fill button (right)
        fill_button = tk.Button(
            root,
            text="Fill",
            width=10,
            command = lambda : self.fill()
        )
        fill_button.pack(side="left", padx=5)

    def fill(self):
        FillWindow(tk.Toplevel(self.root), self.casetteId, self.casetteRoot)

