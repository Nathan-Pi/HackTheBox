
def startAgain():
    choice= int(input("Would you like to:\n"))
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    else:
        print("Invalid Input")
        startAgain()