from random import randint
from math import gcd


def question_checker() -> list:
    '''Generates random math numb and finds it's gcd'''
    a = randint(MIN_LIM, MAX_LIM)
    b = randint(MIN_LIM, MAX_LIM)
    question = f'{a} {b}'
    answer = str(gcd(a, b))
    return [question, answer]


START_MESSAGE = 'Find the greatest common divisor of given numbers.'
MIN_LIM = 0
MAX_LIM = 50
