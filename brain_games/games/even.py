from random import randrange


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def prepare_round():
    question = randrange(0, 999)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer
