from random import randint, choice


RULES = "What number is missing in the progression?"


def start_round():
    _start = randint(1, 99)
    _step = randint(1, 10)
    _end = _start + (10 * _step)
    sequence = list(range(_start, _end, _step))
    answer = choice(sequence)
    question = [x if x != answer else '..' for x in sequence]
    question = " ".join(map(str, question))
    return question, str(answer)
