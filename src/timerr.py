import os
import screens
import time
import threading

def endTimer():
    os.system('cls')
    print("You ran out of time!")
    time.sleep(2)

    loseScreen = screens.loseScreen()
    loseScreen.display()
    print("hel")
    loseScreen.restartOrQuit()



