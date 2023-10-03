import json
import random
import time as t

def askQuestion():
    accessedNumbers = []
    same = True

    file = open('assets/questionBank.json')
    questionBank = json.load(file)

    count = len(questionBank['question'])
    while same == True:
        randomNumber = random.randint(0,count-1)
        if randomNumber not in accessedNumbers:
            same = False 

    
    print(questionBank['question'][randomNumber])
    accessedNumbers.append(randomNumber)
    return randomNumber


def validateAnswer(questionNum, answer, correctTry, incorrectTry):

    file = open('assets/questionBank.json')
    questionBank = json.load(file)
    correctAnswer = questionBank['answer'][questionNum]
 

    answer = str(answer)
    correctAnswer = str(correctAnswer)

    
    if answer == correctAnswer:
        print("Correct!")
        t.sleep(2)
        correctTry += 1
        return correctTry
    else:
        print("Incorrect!")
        incorrectTry += 1
        print("The correct answer was: ", correctAnswer)
        print('-'*40)
        t.sleep(2)
        return incorrectTry
    


def getAnswer():
    try:
        answer = input("Answer: ")
    except:
        print("Error")

    return answer


