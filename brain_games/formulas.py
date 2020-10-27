from collections import Counter


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


def is_prim_number(number):
    prim_numbers = set(get_prim_numbers(number))
    if number in prim_numbers:
        return 'yes'
    return 'no'


def get_prim_divisors(number):
    simple_divisors = get_prim_numbers(number)
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
