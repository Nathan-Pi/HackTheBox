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
    return randomNumber


def validateQuestion(questionNum, answer):

    file = open('assets/questionBank.json')
    questionBank = json.load(file)
    correctAnswer = questionBank['question'][questionNum]

    if isinstance(answer, int):
        pass
    else:
        answer = answer.upper()
        answer = answer.strip()
        correctAnswer = correctAnswer.upper()
        correctAnswer = correctAnswer.strip()


    if answer == correctAnswer:
        print("Correct!")
    else:
        print("Incorrect!")



def answer():
    answer = input("Answer: ")
    return answer


