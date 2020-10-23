from random import randrange
import prompt


def even():
    number = randrange(0, 999, 1)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    answer = answer.lower()
    if number % 2 == 0:
        if answer == 'yes':
            print("Correct!")
            return True
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    if answer == 'no':
        print("Correct!")
        return True
    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    return False


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')
