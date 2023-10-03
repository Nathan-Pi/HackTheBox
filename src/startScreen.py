def startScreen():
    import json
    entries = 10
    file = open('assets/leaderboard.json')
    data = json.load(file)
    print('''                                                                                                                                     
    __ __  ____    __ __  _      ______ __ __   ___       _____ ____ _____  ___ 
    |  |  |/    |  /  ]  |/ ]    |      |  |  | /  _]     / ___//    |     |/  _]
    |  |  |  o  | /  /|  ' /     |      |  |  |/  [_     (   \_|  o  |   __/  [_ 
    |  _  |     |/  / |    \     |_|  |_|  _  |    _]     \__  |     |  |_|    _]
    |  |  |  _  /   \_|     \      |  | |  |  |   [_      /  \ |  _  |   _]   [_ 
    |  |  |  |  \     |  .  |      |  | |  |  |     |     \    |  |  |  | |     |
    |__|__|__|__|\____|__|\_|      |__| |__|__|_____|      \___|__|__|__| |_____|  
        ''')
   #print("Welcome to Hack The Safe! - a Terrifying Net Force production \n")
    print("""
                                _____________
                                ||           ||
                                ||           ||
                                ||           ||
                                ||___________||
                                |   _______   |
                                |  |    __ |  |
                                |   |__||  |
                                '--|_______|--'
                                
        """)
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