from random import randint


def question_checker() -> list:
    '''Generates random numb and returns Yes if even, else No'''
    question = randint(MIN_LIM, MAX_LIM)
    answer = 'no' if question % 2 else 'yes'
    return [question, answer]


START_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_LIM = 0
MAX_LIM = 50
