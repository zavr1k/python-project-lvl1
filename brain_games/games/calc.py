from random import randrange, choice
from operator import sub, add, mul


RULES = "What is the result of the expression?"
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
}


def get_q_a():
    number1 = randrange(99)
    number2 = randrange(99)
    operator = choice(list(OPERATORS.keys()))
    question = f"{number1} {operator} {number2}"
    answer = OPERATORS[operator](number1, number2)
    return question, str(answer)
