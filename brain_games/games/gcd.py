from random import randint


def start_message():
    return 'Find the greatest common divisor of given numbers.'


def question() -> str:
    a = randint(0, 50)
    b = randint(0, 50)
    return f'{a} {b}'


def checker(numb_string: str) -> str:
    '''Euclidean algorithm for gcd'''
    a, b = map(int, numb_string.split())
    if a == 0 and b == 0:
        return '0'
    elif a == 0 or b == 0:
        return str(max(a, b))
    while a != b:
        if a >= b:
            a = a - b
        else:
            b = b - a
    return str(a)
