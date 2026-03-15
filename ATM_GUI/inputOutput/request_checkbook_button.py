import tkinter as tk
import pygame

from ATM_LOGIC.request_checkbook import RequestCheckbook

class RequestChekbookButton:
    def __init__(self, root, screen, session):
        self.root = root
        self.screen = screen    
        self.session = session
        self.state = "Blocked"

        self.button = tk.Button(
            root,
            text="Request \n checkbook",
            command=self.handleRequest
        )
        self.button.pack(expand=True, fill = 'both')  

        pygame.mixer.init()

    def handleRequest(self):
        if self.state == "Activated":
            pygame.mixer.music.load("C:/Users/MSI/Downloads/Beep Button Sound Effect.mp3")
            pygame.mixer.music.play(loops = 0)
            request = RequestCheckbook(self.session.cardNumber)
            request.depositRequest()
            self.screen.displayMessage("Successful request")
            self.root.after(3000, self.screen.displayMenu)