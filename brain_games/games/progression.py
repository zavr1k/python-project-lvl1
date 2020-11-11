from random import randint, choice


DESCRIPTION = "What number is missing in the progression?"


def prepare_round():
    _length = randint(5, 15)
    _start = randint(1, 99)
    _step = randint(1, 10)
    _end = _start + (_length * _step)
    sequence = list(range(_start, _end, _step))
    answer = choice(sequence)
    question = " ".join([str(x) if x != answer else '..' for x in sequence])
    return question, str(answer)
