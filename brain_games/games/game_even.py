from random import randrange
import prompt


def even():
    number = randrange(0, 999, 1)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    answer = answer.lower()
    if number % 2 == 0:
        if answer == 'yes':
            return True, "Correct!"
        return False, "'yes' is wrong answer ;(. Correct answer was 'no'." \
                      " \nLet's try again, "
    if answer == 'no':
        return True, "Correct!"
    return False, "'yes' is wrong answer ;(. Correct answer was 'no'." \
                  " \nLet's try again, "
