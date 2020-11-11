from random import randrange, choice
from operator import sub, add, mul


DESCRIPTION = "What is the result of the expression?"
OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
}


def prepare_round():
    number1 = randrange(99)
    number2 = randrange(99)
    operator = choice(list(OPERATIONS.keys()))
    question = f"{number1} {operator} {number2}"
    answer = OPERATIONS[operator](number1, number2)
    return question, str(answer)
