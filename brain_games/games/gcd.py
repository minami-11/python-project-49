from random import randint
from math import gcd


START_MESSAGE = 'Find the greatest common divisor of given numbers.'
MIN_LIMIT = 0
MAX_LIMIT = 50


def make_question_and_answer() -> list:
    '''Generates random math numb and finds it's gcd'''
    number_1 = randint(MIN_LIMIT, MAX_LIMIT)
    number_2 = randint(MIN_LIMIT, MAX_LIMIT)
    question = f'{number_1} {number_2}'
    answer = str(gcd(number_1, number_2))
    return [question, answer]
