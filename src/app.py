import askQuestion
import screens
import timerr

import os
import threading as th



def main():
   
    os.system('cls')
    correctTry = 0
    incorrectTry = 0
    accessedNumbers = []
    score = 0

    startScreen = screens.startScreen()
    startScreen.display()
    username = startScreen.start()

    numOfDigits = askQuestion.difficultyChoice()
    numOfDigits += 2

    timer = th.Timer(5, timerr.endTimer)
    timer.start()

    code = askQuestion.generateCode(numOfDigits)

    while correctTry < numOfDigits and incorrectTry < 4:
        questionNum = askQuestion.askQuestion(accessedNumbers)
        answer = askQuestion.getAnswer()
        isCorrect = askQuestion.validateAnswer(questionNum, answer, correctTry, incorrectTry, code)
        if isCorrect is True:
            correctTry += 1
        elif isCorrect is False:
            incorrectTry += 1
        os.system('cls')

    if correctTry == numOfDigits:
        success = askQuestion.codeEntry(code)
        if success is True:
            winScreen = screens.winScreen()
            winScreen.display()
            winScreen.appendLeaderboard(username, score)
            winScreen.restartOrQuit()
            main()

    elif incorrectTry == 4:
        print("The safe turned on its anti-bruteforce defense! You have to try hack the safe again!")
        loseScreen = screens.loseScreen()
        loseScreen.display()
        loseScreen.restartOrQuit()
        main()

main()
