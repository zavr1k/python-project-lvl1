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
    result = operators[operator](number1, number2)
    if answer == int(result):
        print("Correct!")
        return True
    print(f"{answer} is wrong answer ;(. Correct answer was {result}")
    return False


def rules():
    print("What is the result of the expression?")
