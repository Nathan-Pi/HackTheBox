def StartAgain():
    choice= int(input("1 To start again, Or 2 to end the game."))
    if choice == 1:
        main()
    elif choice == 2:
        print("Quitting..")
        quit()
    else:
        print("Invalid Input")
        StartAgain()