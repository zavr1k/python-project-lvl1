from random import randrange
import prompt
from collections import Counter


def rules():
    print("Find the greatest common divisor of given numbers.")


def gcd():
    number1 = randrange(199)
    number2 = randrange(199)
    print(f"Question: {number1} {number2}")
    answer = prompt.integer("Your answer: ")
    question = get_gcd(number1, number2)
    if answer == question:
        return True, answer, question
    return False, answer, question


def get_prim_divisors(number):
    simple_divisors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                       47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                       107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                       167, 173, 179, 181, 191, 193, 197, 199]
    temp = number
    result = []
    while temp != 1:
        i = 0
        divisor = simple_divisors[i]
        if temp % divisor == 0:
            result.append(divisor)
            temp = temp // divisor
        else:
            while temp % divisor != 0:
                i += 1
                divisor = simple_divisors[i]
            result.append(divisor)
            temp = temp // divisor
    return Counter(result)


def get_gcd(n1, n2):
    one = get_prim_divisors(n1)
    two = get_prim_divisors(n2)
    common = {}
    for el in one:
        if el in two:
            common[el] = min(one[el], two[el])
    res = 1
    for el in common:
        res *= int(el) ** common[el]
    return res
