import os
import screens
import time as t


def endTimer():
    os.system('cls')
    print("You ran out of time!")
    t.sleep(2)

    loseScreen = screens.loseScreen()
    loseScreen.display()
    loseScreen.restartOrQuit()


