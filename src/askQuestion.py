import json
def askQuestion():
    file = open('assets/questionBank.json')
    questionBank = json.load(file)

    print(questionBank['question'][0])

def answer():
    answer = input("Answer: ")
    return answer
