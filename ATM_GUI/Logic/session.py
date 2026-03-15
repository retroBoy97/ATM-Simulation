
class Session:
    def __init__(self):
        self.cardNumber = None
        self.PIN = None
        self.cardStatus = None
        self.isBlocked = False

    def set_ATM_GUI(self, ATMGUI):
        self.ATMGUI = ATMGUI

    def resetATM(self):
        self.cardNumber = None
        self.PIN = None
        self.cardStatus = None
        self.isBlocked = False
        self.ATMGUI.reset()

