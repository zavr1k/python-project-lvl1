import prompt

from random import randrange
from brain_games.formulas import is_prim_number


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    number = randrange(999)
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    question = is_prim_number(number)
    if answer == question:
        return True, answer, question
    return False, answer, question
