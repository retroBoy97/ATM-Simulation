import tkinter as tk
import pygame

class UndoButton:
    def __init__(self, parent, screen):
        self.screen = screen
        self.state = "Blocked"
        self.button = tk.Button(
            parent,
            text="Undo",
            command=self.handle_undo
        )
        self.button.pack(expand=True, fill = 'both')  

        pygame.mixer.init()

    def handle_undo(self):
        if self.state == "Activated":
            pygame.mixer.music.load("C:/Users/MSI/Downloads/Beep Button Sound Effect.mp3")
            pygame.mixer.music.play(loops = 0)
            self.choiceKeyboard.function = "mainMenu"
            self.screen.displayMenu()

    def reset(self):
        self.state = "Blocked"
