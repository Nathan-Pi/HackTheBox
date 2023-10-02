import json
import random
def askQuestion():
    accessedNumbers = []
    same = True
    file = open('assets/questionBank.json')
    questionBank = json.load(file)

    count = len(questionBank['question'])
    while same == True:
        randomNumber = random.randint(0,count)
        if randomNumber not in accessedNumbers:
            same = False 

    
    print(questionBank['question'][randomNumber])
    accessedNumbers.append(randomNumber)
    
def answer():
    answer = input("Answer: ")
    return answer

askQuestion()