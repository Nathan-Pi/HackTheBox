# testSafe.py

import pytest
from main import askQuestion, validateAnswer, generateCode, difficultyChoice

def test_askQuestion():
    # Create test case for the askQuestion function
    # Ensure it returns valid question number
    accessedNumbers = []
    questionNum = askQuestion(accessedNumbers)
    assert isinstance(questionNum, int)

def test_askQuestion_uniqueness():
    accessedNumbers = []
    unique_questions = set()
    for _ in range(100):  # a large number to check repetition over large num of iterations
        questionNum = askQuestion(accessedNumbers)
        assert questionNum not in unique_questions
        unique_questions.add(questionNum)

def test_validateAnswer():
    # Create test case for the validateAnswer function
    questionNum = 0
    answer = "4"
    correctTry = 0
    incorrectTry = 0
    code = [1, 2, 3, 4, 5]
    assert validateAnswer(questionNum, answer, correctTry, incorrectTry, code) == True

def test_validateAnswer_incorrect():
    questionNum = 0  # assumes answer to the first question is not "Wrong Answer"
    answer = "Wrong Answer"
    correctTry = 0
    incorrectTry = 0
    code = [1, 2, 3, 4, 5]
    assert validateAnswer(questionNum, answer, correctTry, incorrectTry, code) == False

def test_generateCode():
    # Create a test case for the generateCode function
    # Ensure it generates a list of the correct length
    numOfDigits = 5
    code = generateCode(numOfDigits)
    assert len(code) == numOfDigits

def test_generateCode_values():
    numOfDigits = 5
    code = generateCode(numOfDigits)
    for value in code:
        assert 1 <= value <= 9

def test_difficultyChoice():
    # Create a test case for the difficultyChoice function
    # Ensure it returns a valid difficulty level (1, 2, or 3)
    difficulty = difficultyChoice()
    assert difficulty in [1, 2, 3]

if __name__ == "__main__":
    pytest.main()
