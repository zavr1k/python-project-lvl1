from random import choice, randint


RULES = "What number is missing in the progression?"


def get_q_a():
    _start = randint(1, 99)
    _step = randint(1, 10)
    _end = _start + (10 * _step)
    sequence = list(range(_start, _end, _step))
    rand_index = choice(range(len(sequence)))
    answer = str(sequence[rand_index])
    sequence[rand_index] = '..'
    question = ' '.join(map(str, sequence))
    return question, answer
