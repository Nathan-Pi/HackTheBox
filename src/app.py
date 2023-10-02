import askQuestion
import startAgain


def main():
    
    questionNum = askQuestion.askQuestion()
    answer = askQuestion.getAnswer()
    askQuestion.validateAnswer(questionNum, answer)
    if startAgain.startAgain() == 1:
        main()
    else:
        quit()

