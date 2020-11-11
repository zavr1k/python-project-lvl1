from random import randrange
from math import gcd


DESCRIPTION = "Find the greatest common divisor of given numbers."


def prepare_round():
    number1 = randrange(199)
    number2 = randrange(199)
    question = f"{number1} {number2}"
    answer = str(gcd(number1, number2))
    return question, answer
