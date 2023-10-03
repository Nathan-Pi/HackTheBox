import askQuestion
import startAgain
import screens


def main():

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

    if correctTry == numOfDigits:
        askQuestion.codeEntry(code)
    elif incorrectTry == numOfDigits:
        print("lose")

    if startAgain.startAgain() == 1:
        main()
    else:
        quit()


main()
