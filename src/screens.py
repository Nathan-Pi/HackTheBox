import json
import os


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
            choice = int(input("\n1 to restart, or 2 to quit: "))
            if choice == 1:
                return True
            elif choice == 2:
                print("Quitting...")
                quit()
            else:
                print("Invalid Input")


class startScreen(Screen):

    def __init__(self, entries=10) -> None:
        Screen.__init__(self)
        self.leaderboard = []
        self.entries = entries
        with open('assets/leaderboard.json', "r") as file:
            data = json.load(file)
        # for i in range(self.entries):
        #     try:
        #         self.leaderboard.append(
        #                             (data["leaderboard"][i]["name"] + ":",
        #                              data["leaderboard"][i]["score"]))
        #     except Exception:
        #         pass
        self.names = [entry['name'] for entry in data['leaderboard']]
        self.scores = [entry['score'] for entry in data['leaderboard']]

    def showLeaderboard(self) -> None:
        print("Leaderboard:")
        for i in range(len(self.names)):
            print(f"{i + 1}. {self.names[i]} - {self.scores[i]}")

    def start(self):
        while True:
            choice = int(input("\n1 to start, or 2 to quit: "))
            if choice == 1:
                name = str(input("Enter a name: "))
                return name
            elif choice == 2:
                print("Quitting...")
                quit()
            else:
                print("Invalid Input")

    def display(self):
        super().display()
        self.showLeaderboard()


class loseScreen(Screen):

    def display(self):

        os.system('cls')
        print("""
 __     __           _               _     _ 
 \ \   / /          | |             | |   | |
  \ \_/ /__  _   _  | |     ___  ___| |_  | |
   \   / _ \| | | | | |    / _ \/ __| __| | |
    | | (_) | |_| | | |___| (_) \__ \ |_  |_|
    |_|\___/ \__,_| |______\___/|___/\__| (_)
              """)

        print("""
                            ,--.
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
              """)
# feel free to remove the skull, i thought it was funny


class winScreen(Screen):

    def display(self):

        os.system('cls')
        print("""
 __     __          __          ___         _ 
 \ \   / /          \ \        / (_)       | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __   | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \  | |
    | | (_) | |_| |    \  /\  /  | | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_| (_)
              """)

        print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⣋⣉⡙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠮⡞⠁⠀⠈⢢⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⣇⠀⡇⠀⠀⠀⢸⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⡏⢰⠙⠚⢧⣀⢀⣠⠞⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡸⠀⡎⠀⣀⡤⠏⠉⠧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⠃⢰⡵⠊⠁⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡀⠀⣀⡠⡆⠀⠀⠀⠀⠀⣆⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⡇⠀⠀⠀⠀⠀⡏⢣⡀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢸⠀⠙⢤⡈⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢠⠖⣒⣶⠖⠒⠒⠒⠲⠷⣒⠒⠒⠒⠒⣺⣶⠖⠒⠓⢤⣹⠶⣒⠲⡄⠀⠀
    ⠀⢠⠏⣞⣟⠉⠀⣖⠒⣲⠀⠀⠈⣳⠀⠀⡎⡞⠉⠀⣖⢒⣢⠀⠀⠈⡇⠹⡄⠀
    ⢠⠏⠀⠘⠪⢅⣀⣀⠉⣀⣀⡠⠔⠁⠀⠀⠙⠮⣇⣀⣀⠉⣀⣀⡤⠖⠁⠀⠹⡄
    ⡟⠒⠒⠒⠒⠒⠒⠓⠛⠚⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠚⠛⠛⠒⠒⠒⠒⠒⠒⢻
    ⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸
              """)

    # def appendLeaderboard(self, name, score):
    #     new_entry = {
    #         "name": name,
    #         "score": score
    #     }
    #     file = open('assets/leaderboard.json', "r")
    #     data = json.load(file)
    #     file.close()
    #     file = open('assets/leaderboard.json', "w")
    #     data["leaderboard"].append(new_entry)
    #     json.dump(data, file, indent=4)
    #     file.close()

    def appendLeaderboard(self, name, score):
        new_entry = {
            "name": name,
            "score": score
        }

        try:
            with open('assets/leaderboard.json', "r") as file:
                data = json.load(file)

            data["leaderboard"].append(new_entry)

            with open('assets/leaderboard.json', "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
