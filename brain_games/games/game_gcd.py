from random import randrange
import prompt
from brain_games.formulas import get_gcd


def rules():
    print("Find the greatest common divisor of given numbers.")


def gcd():
    number1 = randrange(199)
    number2 = randrange(199)
    print(f"Question: {number1} {number2}")
    answer = prompt.integer("Your answer: ")
    question = get_gcd(number1, number2)
    if answer == question:
        return True, answer, question
    return False, answer, question
