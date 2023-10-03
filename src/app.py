import askQuestion
import startAgain


def main():
    correctTry = 0
    incorrectTry = 0

    while correctTry <= 3 and incorrectTry <= 3:
        questionNum = askQuestion.askQuestion()
        answer = askQuestion.getAnswer()
        isCorrect = askQuestion.validateAnswer(questionNum, answer, correctTry, incorrectTry)
        if isCorrect == True:
            correctTry += 1
        elif isCorrect == False:
            incorrectTry += 1
        print(correctTry, incorrectTry)

    if correctTry == 3:
        print("win")
    elif incorrectTry == 3:
        print("lose")

    if startAgain.startAgain() == 1:
        main()
    else:
        quit()


main()