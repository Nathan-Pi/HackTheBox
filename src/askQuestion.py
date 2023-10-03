import json
import random
import time as t

def askQuestion(accessedNumbers):
    same = True

    file = open('assets/questionBank.json')
    questionBank = json.load(file)

    count = len(questionBank['question'])
    while same == True:
        randomNumber = random.randint(0,count-1)
        if randomNumber not in accessedNumbers:
            same = False 

    
    print(questionBank['question'][randomNumber])
    print(randomNumber)
    accessedNumbers.append(randomNumber)
    print(accessedNumbers)
    return randomNumber


def validateAnswer(questionNum, answer, correctTry, incorrectTry, code):

    file = open('assets/questionBank.json')
    questionBank = json.load(file)
    correctAnswer = questionBank['answer'][questionNum]
 

    if str(answer).upper() == str(correctAnswer).upper():
        print("Correct!")
        t.sleep(2)
        correctTry += 1
        print("You have unlocked a new part of the code! : \n\n \t ", str(code[:correctTry]).replace('[', '').replace(']', ''))

        return True
    else:
        print("Incorrect!")
        incorrectTry += 1
        print("The correct answer was: ", correctAnswer)
        print('-'*40)
        t.sleep(2)
        return False
    
    


def getAnswer():
    try:
        answer = input("Answer: ")
    except:
        print("Error")

    return answer


def generateCode(numOfDigits):
    code = []
    for i in range(numOfDigits):
        code.append(random.randint(1,9))
    return code

def difficultyChoice():
    difficulty = int(input("Would you to like to play on \n1) Easy\n2) Medium\n3) Hard\n: "))
    return difficulty



def codeEntry(code):
    print(f"Well done, you unlocked the safe!\n\n\n The code was: {str(code).replace('[', '').replace(']', '')}\n\n")

