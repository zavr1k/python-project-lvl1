#!/usr/bin/env python
from random import randrange
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randrange(0, 999, 1)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        answer = answer.lower()
        if number % 2 == 0:
            if answer == 'yes':
                print("Correct!")
                continue
            print("'yes' is wrong answer ;(. Correct answer was 'no'. \n"
                  f"Let's try again, {name}!")
            break
        if answer == 'no':
            print("Correct!")
            continue
        print("'yes' is wrong answer ;(. Correct answer was 'no'. \n"
              f"Let's try again, {name}!")
        break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
