from random import randrange, choice
import prompt


RULES = "What number is missing in the progression?"


def progression():
    _start = randrange(99)
    _step = randrange(1, 10)
    _end = _start + (10 * _step)
    sequence = enumerate(range(_start, _end, _step))
    progression_dict = dict(sequence)
    missing_char = choice(list(progression_dict.keys()))
    hidden_char = progression_dict[missing_char]
    progression_dict[missing_char] = ".."
    print("Question:", *progression_dict.values())
    answer = prompt.integer("Your answer: ")
    if answer == hidden_char:
        return True, answer, hidden_char
    return False, answer, hidden_char
