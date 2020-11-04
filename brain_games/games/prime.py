from random import randrange
from math import sqrt


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def start_round():
    number = randrange(100)
    question = str(number)
    if is_prime_number(number):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
