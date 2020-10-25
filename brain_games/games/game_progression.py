from random import randrange, choice
import prompt


def rules():
    print("What number is missing in the progression?")


def progression():
    _start = randrange(99)
    _step = randrange(1, 10)
    _end = _start + (10 * _step)
    sequence = enumerate(range(_start, _end, _step))
    d = dict(sequence)
    q = choice(list(d.keys()))
    question = d[q]
    d[q] = ".."
    print("Question:", *d.values())
    answer = prompt.integer("Your answer: ")
    if answer == question:
        return True, answer, question
    return False, answer, question
