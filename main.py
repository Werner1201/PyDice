from src.view.View import View


def main():
    V = View()
    V.startup()
    V.numFaces()
    V.qThrowDice()
    stop = input("Press any key to continue...")
    while(V.qThrowControl()):
        V.faceRolled()
        stop = input("Press any key to continue...")
    V.closeMessage()


main()
