from random import randint


def start_message():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    return randint(0, 50)


def checker(number: int) -> str:
    '''Yes if even, else returns no'''
    return ['yes', 'no'][number % 2]
