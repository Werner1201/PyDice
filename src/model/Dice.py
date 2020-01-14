class Dice:
    faces = 6
    lastFace = 0
    currentFace = 0

    def __init__(self, faces=6):
        self.faces = faces

    def setLast(self, face):
        self.lastFace = face

    def setCurrent(self, face):
        self.currentFace = face

    def getLast(self):
        return self.lastFace

    def getCurrent(self):
        return self.currentFace
