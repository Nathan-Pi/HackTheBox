def startScreen():
    import json
    entries = 10
    file = open('assets/leaderboard.json')
    data = json.load(file)
    print("Welcome to Hack The Safe! - a Terrifying Net Force production \n")
    for i in range(entries):
        try:
            print(
                data["leaderboard"][i]["name"] + ":",
                data["leaderboard"][i]["score"])
        except Exception:
            print("empty for now")

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
startScreen()