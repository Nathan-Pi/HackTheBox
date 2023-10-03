
def startAgain():
    choice= int(input("Would you like to:\n1) Start Again \n or \n2) End Game\n: "))
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    else:
        print("Invalid Input")
        startAgain()
