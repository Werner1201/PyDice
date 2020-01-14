from src.model.Dice import Dice
from src.controller.ThrowController import Throw
from pick import pick


class DiceController:
    D = None

    def faceNumber(self, faces):
        self.D = Dice(faces)
        pass

    def currentFace(self):
        return self.D.getCurrent()

    def lastFace(self):
        return self.D.getLast()

    def setDice(self, face):
        self.D.setCurrent(face)

    def setLastFace(self, face):
        self.D.setLast(face)

    def Catch(self):
        T = Throw(self.D.faces)
        self.setLastFace(self.currentFace())
        self.setDice(T.Throw())
        return self.currentFace()

    def qCatch(self, message):
        (choice, _) = pick(["Yes", "No"], title=message)
        if(choice == "Yes"):
            return True
        elif(choice == "No"):
            return False
