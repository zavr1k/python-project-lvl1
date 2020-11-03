from random import randrange


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prim_number(number):
    prim_numbers = set(get_prim_numbers(number))
    if number in prim_numbers:
        return True
    return False


def get_prim_numbers(number):
    lst = [2]
    for i in range(3, number + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def get_q_a():
    number = randrange(999)
    question = str(number)
    if is_prim_number(number):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
