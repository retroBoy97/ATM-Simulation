import tkinter as tk
from ADMIN.Casette.casette_gui import CasetteGUI

class CasetteButton:
    def __init__(self, root, menuRoot, id):
        self.root = root
        self.menuRoot = menuRoot
        self.id = id

        self.frame = tk.Frame(root, width=150, height=100)
        self.frame.pack_propagate(False)  # prevent the frame from resizing
        self.frame.pack(pady=20, expand=True)

        self.button = tk.Button(
            self.frame,
            text=str(id),
            command=lambda: self.click()
        )
        self.button.pack(expand=True, fill="both")

    def click(self):
        new_window = tk.Toplevel(self.menuRoot)
        CasetteGUI(new_window, self.id)
