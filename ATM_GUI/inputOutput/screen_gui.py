import tkinter as tk

class ScreenGUI:
    def __init__(self, parent):
        # parent: a Frame or window into which the screen is placed
        self.parent = parent

        # Shared styles
        self.font_style = ("Segoe UI", 20, "bold")
        self.bg_color = "#f0f4f8"         # light background
        self.border_color = "#4a90e2"     # border color
        self.fg_color = "#333333"         # dark text

        # Layout inside parent: two rows, one column
        parent.rowconfigure(0, weight=1)
        parent.rowconfigure(1, weight=1)
        parent.columnconfigure(0, weight=1)

        # Top half: Instruction frame
        self.instruction_frame = tk.Frame(
            parent,
            bg=self.bg_color,
            highlightbackground=self.border_color,
            highlightthickness=2
        )
        self.instruction_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        self.instruction_label = tk.Label(
            self.instruction_frame,
            text="Welcome to the ATM\nPlease enter your card:",
            font=self.font_style,
            bg=self.bg_color,
            fg=self.fg_color,
            justify="center",
            wraplength=800
        )
        self.instruction_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Bottom half: PIN display frame
        self.pin_frame = tk.Frame(
            parent,
            bg=self.bg_color,
            highlightbackground=self.border_color,
            highlightthickness=2
        )
        self.pin_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

        self.pin_label = tk.Label(
            self.pin_frame,
            text="",
            font=("Consolas", 24),
            bg=self.bg_color,
            fg="#2e86c1",
            justify="center"
        )
        self.pin_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Internal state
        self.displayedPIN = ""

    def displayMessage(self, newText):
        self.instruction_label.config(text=newText)

    def displayPIN(self, PIN):
        self.displayedPIN = PIN
        self.pin_label.config(text=PIN)

    def clearPIN(self):
        self.displayedPIN = ""
        self.displayPIN("")

    def getDisplayedPIN(self):
        return self.displayedPIN

    def displayMenu(self):
        # Remove PIN frame and expand instruction_frame to full height
        self.pin_frame.grid_forget()
        self.instruction_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.instruction_label.config(
            text="1 : Check your balance\n"
                 "2 : Withdraw money\n"
                 "3 : View Transaction History\n"
                 "4 : View date\n"
                 "5 : Request Checkbook\n"
                 "6 : Exit",
            justify="left",
            font=self.font_style
        )
        self.clearPIN()

    def displayWithdrawalMenu(self):
        self.instruction_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.instruction_label.config(
            text="1 : 10 DT\n"
                 "2 : 20 DT\n"
                 "3 : 30 DT\n"
                 "4 : 50 DT\n"
                 "5 : 100 DT\n"
                 "6 : 200 DT",
            justify="left",
            font=self.font_style
        )

    def reset(self):
        self.displayMessage("Please enter your card")
        self.pin_frame = tk.Frame(
            self.parent,
            bg=self.bg_color,
            highlightbackground=self.border_color,
            highlightthickness=2
        )
        self.pin_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

        self.pin_label = tk.Label(
            self.pin_frame,
            text="",
            font=("Consolas", 24),
            bg=self.bg_color,
            fg="#2e86c1",
            justify="center"
        )
        self.pin_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Internal state
        self.displayedPIN = ""
        