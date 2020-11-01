from random import randrange
import prompt


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    number = randrange(0, 999, 1)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    answer = answer.lower()
    if number % 2 == 0:
        question = 'yes'
    else:
        question = 'no'
    if answer == question:
        return True, answer, question
    return False, answer, question
