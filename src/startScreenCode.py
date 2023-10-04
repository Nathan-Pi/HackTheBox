import baseScreen
import json


class startScreen(baseScreen.Screen):

    def __init__(self, entries=10) -> None:
        baseScreen.Screen.__init__(self)
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
        
        with open('assets/leaderboard.json', "r") as file:
            data = json.load(file)
        sorted_leaderboard = sorted(data["leaderboard"], key=lambda x: x["score"], reverse=True)

        sorted_data = {"leaderboard": sorted_leaderboard}

        with open('assets/leaderboard.json', "w") as file:
            json.dump(sorted_data, file, indent=4)

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

