import json
import random
import time
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


def validateAnswer(questionNum, answer):

    file = open('assets/questionBank.json')
    questionBank = json.load(file)
    correctAnswer = questionBank['answer'][questionNum]
 

    answer = str(answer)
    correctAnswer = str(correctAnswer)

    
    if answer == correctAnswer:
        print("Correct!")
    else:
        print("Incorrect!")
    


def getAnswer():
    try:
        answer = input("Answer: ")
    except:
        print("Error")

    return answer


