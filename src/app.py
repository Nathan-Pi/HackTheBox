import questionScreenCode
import startScreenCode
import winScreenCode
import loseScreenCode
import os
import turtleCode
import pygame


def main():
    path = os.getcwd()
    file_path = os.path.join(path, 'assets', 'raveMusic.mp3')
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    os.system('cls')
    startScreen = startScreenCode.startScreen(file_path)
    pygame.mixer.music.play()
    startScreen.display()
    username = startScreen.start()
    score = 0

    questionScreen = questionScreenCode.questionScreen()
    questionScreen.difficultyChoice()

    while questionScreen.correctTries < len(questionScreen.code) and questionScreen.incorrectTries < 4:
        questionScreen.askQuestion()
        questionScreen.getAnswer()
        questionScreen.validateAnswer()
        os.system('cls')

    if questionScreen.correctTries == len(questionScreen.code):
        success = questionScreen.codeEntry()
        if success is True:
            winScreen = winScreenCode.winScreen()
            score = winScreen.generateScore(questionScreen)
            winScreen.display()
            winScreen.appendLeaderboard(username, score)
            winScreen.restartOrQuit()
            main()
        else:
            loseScreen = loseScreenCode.loseScreen()
            loseScreen.display()
            loseScreen.restartOrQuit()
            main()

    # incorrect tries seems to be hardcoded here -ethan
    elif questionScreen.incorrectTries == 3:
        print("The safe turned on its anti-bruteforce defense! You have to try hack the safe again!")
        loseScreen = loseScreenCode.loseScreen()
        loseScreen.display()
        loseScreen.restartOrQuit()
        main()


turtleCode.safeDrawing()
main()
