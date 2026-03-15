import tkinter as tk

class PasswordEntry:
    def __init__(self, root):
        self .root = root

        self.password_label = tk.Label(
            self.root, 
            text="Password:", 
            width=20, 
            height=3, 
            bg="#f0f4f8",
            relief="raised",
            borderwidth=1
        )
        self.password_label.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        # Frame to hold Entry
        password_entry_frame = tk.Frame(           
            self.root, 
            bg="#3498db",
            height=60,
            width=200 
        )
        password_entry_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        password_entry_frame.grid_propagate(False)

        # Entry inside Frame (fills available space)
        self.password_entry = tk.Entry(
            password_entry_frame,
            font=("Arial", 17),
            fg="black",
            justify="left",
            show="*",                 # Show asterisks instead of text
            selectbackground="lightblue",
            selectforeground="black"
        )
        self.password_entry.pack(fill="both", expand=True, padx=5, pady=5)

    def clear(self):
        self.password_entry.delete(0, tk.END)