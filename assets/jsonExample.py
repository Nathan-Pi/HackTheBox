import json
file = open('assets/questionBank.json')
questionBank = json.load(file)
print(questionBank['question'][0])
print(questionBank['answer'][0])
