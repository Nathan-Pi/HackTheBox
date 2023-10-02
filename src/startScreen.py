def startScreen():

    print("Welcome to Hack The Safe! - a Terrifying Net Force production")

    while True:
        choice = int(input("1 to start, or 2 to quit."))
        if choice == 1:
            name = str(input("Enter a name: "))
            return name
        elif choice == 2:
            print("Quitting...")
            quit()
        else:
            print("Invalid Input")
