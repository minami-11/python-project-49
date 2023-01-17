from random import randint


def start_message():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    return randint(0, 50)


def even_odd_checker(number: int) -> str:
    return ['yes', 'no'][number % 2]
