import json
import os
import random
import time
import playsound

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
            try:
                choice = int(input("\nWould you like to: \n1) Restart \n2) Quit \n:  "))
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