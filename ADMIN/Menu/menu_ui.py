import tkinter as tk
from ADMIN.Menu.instruction_label import InstructionLabel
from ADMIN.Menu.casette_button import CasetteButton
from ADMIN.exit_button import ExitButton
from ADMIN.Menu.reset_button import ResetButton

class MenuUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Casettes")
        self.root.geometry("800x400")
        self.root.configure(bg="#f0f0f0")

        # Configure grid layout
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1, uniform="column")
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)

        # Instruction label (top row)
        self.instructionLabel = InstructionLabel(self.root)

        # Button frames (middle row)
        self.buttonFrames = []
        for i in range(3):
            frame = tk.Frame(self.root, bg="#ffffff", bd=1, relief="ridge")
            frame.grid(row=1, column=i, padx=10, pady=10, sticky="nsew")  # Balanced spacing
            self.root.grid_columnconfigure(i, weight=1)
            self.buttonFrames.append(frame)

        # Casette buttons inside frames
        CasetteButton(self.buttonFrames[0], self.root, 50)
        CasetteButton(self.buttonFrames[1], self.root, 20)
        CasetteButton(self.buttonFrames[2], self.root, 10)

        # Bottom buttons row (exit and reset)
        self.exit_button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.exit_button_frame.grid(row=2, column=0, sticky="w", padx=20, pady=10)
        ExitButton(self.exit_button_frame, self.root)

        self.reset_button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.reset_button_frame.grid(row=2, column=2, sticky="e", padx=20, pady=10)
        ResetButton(self.reset_button_frame)
