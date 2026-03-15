import tkinter as tk
from ATM_LOGIC.casette import Casette

class FillWindow:
    def __init__(self, root, casetteId, casetteRoot):
        self.casetteId = casetteId
        self.root = root
        self.casetteRoot = casetteRoot
        self.root.title("Fill Window")
        self.root.geometry("250x200")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(
            self.root, 
            text="Enter number of cards", 
            width=20, 
            height=3, 
            bg="#f0f4f8",
            relief="raised",
            borderwidth=1
        )
        self.label.grid(row=0, column=0, columnspan = 2, sticky="nsew", padx=5, pady=5)

        # Frame to hold Entry
        entry_frame = tk.Frame(           
            self.root, 
            bg="#3498db",
            height=60,
            width=200 
        )
        entry_frame.grid(row=1, column=0, columnspan = 2, sticky="nsew", padx=5, pady=5)
        entry_frame.grid_propagate(False)

        # Entry inside Frame (fills available space)
        self.entry = tk.Entry(
            entry_frame,
            font=("Arial", 15),
            fg="black",
            justify="left",
            selectbackground="lightblue",
            selectforeground="black"
        )
        self.entry.pack(fill="both", expand=True, padx=5, pady=5)

        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#f5f7fa")
        button_frame.grid(row = 2)

        self.confirm_button = tk.Button(
            button_frame,
            text="Confirm",
            bg="#2ecc71",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=10,
            command= lambda: self.confirm()
        )
        self.confirm_button.grid(row = 2, column = 0)

        # Back Button
        self.back_button = tk.Button(
            button_frame,
            text="Back",
            bg="#e74c3c",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=10,
            command=self.root.destroy
        )
        self.back_button.grid(row = 2, column = 1)

    def display_message(self, message):
        self.instruction_label.config(text=message)

    def confirm(self):
        value = self.entry.get()
        
        if not value.isdigit():
            self.label.config(text="❌ Please enter a positive number")
            self.entry.delete(0, tk.END)
            return

        number = int(value)
        if number <= 0:
            self.label.config(text="❌ Number must be greater than 0")
            self.entry.delete(0, tk.END)
            return

        self.confirm_button.config(state="disabled")
        self.back_button.config(state="disabled")
        Casette.fill(self.casetteId, number)
        self.label.config(text="Success")
        self.root.after(2000, self.casetteRoot.destroy)


        

