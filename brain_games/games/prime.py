from random import randrange
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False

    if number % 2 == 0 and number != 2:
        return False

    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def prepare_round():
    number = randrange(100)
    question = str(number)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
