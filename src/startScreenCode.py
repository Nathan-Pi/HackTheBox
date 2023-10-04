import baseScreen
import json

class startScreen(baseScreen.Screen):

    def __init__(self, entries=10) -> None:
        baseScreen.Screen.__init__(self)
        self.leaderboard = []
        self.entries = entries
        nameAndScore = []
        with open('assets/leaderboard.json', "r") as file:
            data = json.load(file)
        
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

