import json
import os
import random
import time
from playsound import playsound


class Screen:

    def __init__(self, displayText="", inputRequired=False) -> None:
        self.logo = '''
  _    _            _      _______ _             _____        __     
 | |  | |          | |    |__   __| |           / ____|      / _|    
 | |__| | __ _  ___| | __    | |  | |__   ___  | (___   __ _| |_ ___ 
 |  __  |/ _` |/ __| |/ /    | |  | '_ \ / _ \  \___ \ / _` |  _/ _ |
 | |  | | (_| | (__|   <     | |  | | | |  __/  ____) | (_| | ||  __/
 |_|  |_|\__,_|\___|_|\_\    |_|  |_| |_|\___| |_____/ \__,_|_| \___|
        '''
        self.safe = '''
                         _____________
                        ||           ||
                        ||   ****    ||
                        ||           ||
                        ||___________||
                        |   _______   |
                        |  |    __ |  |
                        |  |   |__||  |
                        '--|_______|--'

        '''
        self.displayText = displayText
        self.inputRequired = inputRequired

    def display(self):
        os.system('cls')
        print(self.logo)
        print(self.safe)
        if self.inputRequired is False:
            print(self.displayText)
            return
        else:
            return input(self.displayText)

    def restartOrQuit(self):
        while True:
<<<<<<< HEAD
            choice = int(input("\n1 to restart, or 2 to quit: "))
            if choice == 1:
                return True
            elif choice == 2:
                print("Quitting...")
                self.playMusic()
                quit()
            else:
                print("Invalid Input")
=======
            try:
                choice = int(input("\n1 to restart, or 2 to quit: "))
                if choice == 1:
                    return True
                elif choice == 2:
                    print("Quitting...")
                    quit()
                else:
                    print("Invalid Input")
            except Exception:
                print("Invalid Entry")
                self.restartOrQuit()
>>>>>>> 4c0c44a5ed9a3c85e460d554b982f0213676fb5c

    def playMusic(self):
        music = 'C:\\Users\\HannahManual\\Desktop\\HackTheBox\\src\\raveMusic.mp3'
        playsound(music)
              
      