import askQuestion
import startAgain
import screens
import os

def main():
    os.system('cls')
    startScreen = screens.startScreen()
    startScreen.display()
    username = startScreen.start()
    correctTry = 0
    incorrectTry = 0
    accessedNumbers = []


    numOfDigits = askQuestion.difficultyChoice()
    numOfDigits += 2

    code = askQuestion.generateCode(numOfDigits)


    while correctTry < numOfDigits and incorrectTry < 4:
        questionNum = askQuestion.askQuestion(accessedNumbers)
        answer = askQuestion.getAnswer()
        isCorrect = askQuestion.validateAnswer(questionNum, answer, correctTry, incorrectTry)
        if isCorrect is True:
            correctTry += 1
        elif isCorrect is False:
            incorrectTry += 1
        os.system('cls')

    if correctTry == numOfDigits:
        askQuestion.codeEntry(code)
    elif incorrectTry == 4:
        print("The safe turned on its anti-bruteforce defense! You have to try hack the safe again!")

    if startAgain.startAgain() == 1:
        main()
    else:
        quit()


main()
