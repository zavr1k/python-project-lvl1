from random import randrange


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_round():
    question = randrange(0, 999)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
