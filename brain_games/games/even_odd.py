from random import randint


START_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_LIMIT = 0
MAX_LIMIT = 50


def make_question_and_answer() -> list:
    '''Generates random numb and returns Yes if even, else No'''
    question = randint(MIN_LIMIT, MAX_LIMIT)
    answer = 'no' if question % 2 else 'yes'
    return [question, answer]
