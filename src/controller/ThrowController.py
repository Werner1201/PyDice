from random import randint


class Throw:
    faces = 0
    startAt = 1
    endAt = 0
    currentFace = 0

    def __init__(self, faces):
        self.faces = faces
        self.endAt = self.faces

    def Throw(self):
        self.currentFace = randint(self.startAt, self.endAt)
        return self.currentFace
