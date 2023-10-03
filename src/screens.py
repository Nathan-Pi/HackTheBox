import json
import os


class Screen:
    def __init__(self, displayText="", inputRequired=False) -> None:
        self.logo = '''
  _    _            _      _______ _             _____        __     
 | |  | |          | |    |__   __| |           / ____|      / _|    
 | |__| | __ _  ___| | __    | |  | |__   ___  | (___   __ _| |_ ___ 
 |  __  |/ _` |/ __| |/ /    | |  | '_ \ / _ \  \___ \ / _` |  _/ _ \
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


class startScreen(Screen):
    def __init__(self, entries=10) -> None:
        Screen.__init__(self)
        self.leaderboard = []
        self.entries = entries
        file = open('assets/leaderboard.json')
        data = json.load(file)
        for i in range(self.entries):
            try:
                self.leaderboard.append(
                                    (data["leaderboard"][i]["name"] + ":",
                                     data["leaderboard"][i]["score"]))
            except Exception:
                pass

    def showLeaderboard(self) -> None:
        print(self.leaderboard)

    def x(self):
        while True:
            choice = int(input("\n1 to start, or 2 to quit."))
            if choice == 1:
                name = str(input("Enter a name: "))
                return name
            elif choice == 2:
                print("Quitting...")
                quit()
            else:
                print("Invalid Input")

