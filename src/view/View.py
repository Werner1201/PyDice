from src.model.Message import Message
from src.controller.DiceController import DiceController


class View:
    m = Message()
    dc = DiceController()
    faces = 0

    def startup(self):
        print(self.m.totalStart)

    def numFaces(self):
        self.faces = int(input(self.m.qNumDeFaces))
        self.dc.faceNumber(self.faces)

    def qThrowDice(self):
        if(self.dc.qCatch(self.m.qThrowDice) == 1):
            self.faceRolled()

    def qThrowControl(self):
        return self.dc.qCatch(self.m.qThrowDice2)

    def rollDice(self):
        return self.dc.Catch()

    def faceRolled(self):
        print(self.m.awnDiceThrown+str(self.rollDice()))

    def closeMessage(self):
        print("Closing Program.")