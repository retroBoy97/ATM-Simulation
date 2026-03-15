import tkinter as tk

class idEntry:
    def __init__(self, root):
        self .root = root

        self.id_label = tk.Label(
            self.root, 
            text="id:", 
            width=20, 
            height=3, 
            bg="#f0f4f8",
            relief="raised",
            borderwidth=1
        )
        self.id_label.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Frame to hold Entry
        id_entry_frame = tk.Frame(           
            self.root, 
            bg="#3498db",
            height=60,
            width=200 
        )
        id_entry_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        id_entry_frame.grid_propagate(False)

        # Entry inside Frame (fills available space)
        self.id_entry = tk.Entry(
            id_entry_frame,
            font=("Arial", 15),
            fg="black",
            justify="left",
            selectbackground="lightblue",
            selectforeground="black"
        )
        self.id_entry.pack(fill="both", expand=True, padx=5, pady=5)

    def clear(self):
        self.id_entry.delete(0, tk.END)