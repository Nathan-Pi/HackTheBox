import baseScreen
import random 
import json
import time

class questionScreen(baseScreen.Screen):

    def __init__(self) -> None:
        baseScreen.Screen.__init__(self)
        self.accessedNumbers = []
        self.questionNum = 0
        self.answer = ""
        self.correctAnswer = ""
        self.correctTries = 0
        self.incorrectTries = 0
        self.difficulty = 0
        self.code = []

    def difficultyChoice(self):
        difficulty = int(input("Would you to like to play on \n1) Easy\n2) Medium\n3) Hard\n: "))
        if difficulty not in [1, 2, 3]:
            print("Invalid Difficulty! Try again")
            self.difficultyChoice()
        self.difficulty = difficulty
        for i in range(self.difficulty + 2):
            self.code.append(random.randint(1, 9))

    def askQuestion(self):

        same = True

        file = open('assets/questionBank.json')
        questionBank = json.load(file)

        count = len(questionBank['question'])
        while same is True:
            self.questionNum = random.randint(0, count-1)
            if self.questionNum not in self.accessedNumbers:
                same = False

        print(questionBank['question'][self.questionNum])
        self.accessedNumbers.append(self.questionNum)

    def getAnswer(self):

        try:
            userInput = input("Answer: ")
        except Exception:
            print("Error")

        self.answer = userInput

    def validateAnswer(self):

        file = open('assets/questionBank.json')
        questionBank = json.load(file)
        self.correctAnswer = questionBank['answer'][self.questionNum]

        if str(self.answer).upper() == str(self.correctAnswer).upper():
            print("Correct!")
            self.correctTries += 1
            print("You have unlocked a new part of the code! : \n\n \t ",
                  str(self.code[0:self.correctTries])
                  .replace('[', '')
                  .replace(']', ''))
            time.sleep(1)
        else:
            print("Incorrect!")
            self.incorrectTries += 1
            print("The correct answer was: ", self.correctAnswer)
            time.sleep(1)

    def codeEntry(self):
        var = ''

        for i in self.code:
            var += str(i)

        code = int(var)
        for x in range(3):
            enteredCode = int(input("Enter the code! (eg 000)\n\n\t:  "))
            if enteredCode == code:
                print("Correct!")
                return True
            else:
                print("That's not quite right!")
        print("The safe turned on its anti-bruteforce defense! You have to try hack the safe again!")
        return False

    def killQuestion(self):
        del questionScreen
        