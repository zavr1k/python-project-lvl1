from random import randrange


RULES = "Find the greatest common divisor of given numbers."


def get_gcd(*args):
    numbers = list(args)  # puts the inout arguments into a list
    n = max(numbers)

    for i in range(n, 0, -1):  # generates a descending list from the biggest input number down to 1
        if all(num % i == 0 for num in numbers):  # if all the (input numbers mod i) divide equally
            return i


def get_q_a():
    number1 = randrange(199)
    number2 = randrange(199)
    question = f"{number1} {number2}"
    answer = str(get_gcd(number1, number2))
    return question, answer
