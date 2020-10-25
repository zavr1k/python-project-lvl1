import prompt
from random import randrange, choice
from operator import sub, add, mul


def calc():
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    number1 = randrange(99)
    number2 = randrange(99)
    operator = choice(list(operators.keys()))
    print(f"Question: {number1} {operator} {number2}")
    answer = prompt.integer("Your answer: ")
    question = operators[operator](number1, number2)
    if answer == int(question):
        return True, answer, question
    return False, answer, question


def rules():
    print("What is the result of the expression?")
