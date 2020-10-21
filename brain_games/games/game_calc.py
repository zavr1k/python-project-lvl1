from random import randrange, choice
import prompt


def _sum(a, b):
    return a + b


def _sub(a, b):
    return a - b


def _mul(a, b):
    return a * b


def calc():
    operators = ('+', '-', '*')
    operators_library = {
        '+': _sum,
        '-': _sub,
        '*': _mul,
    }
    number1 = randrange(99)
    number2 = randrange(99)
    operator = choice(operators)
    print(f"Question: {number1} {operator} {number2}")
    answer = prompt.integer("Your answer: ")
    result = operators_library[operator](number1, number2)
    if answer == int(result):
        return True, "Correct!"
    return False, f"{answer} is wrong answer ;(. Correct answer was {result}"
