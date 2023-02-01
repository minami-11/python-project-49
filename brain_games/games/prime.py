from random import randint


START_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_LIM = 0
MAX_LIM = 50


def prime(number: int) -> str:
    '''Yes if prime, else no'''
    match number:
        case 1: return 'no'
        case 2: return 'yes'
    if all(number % divider for divider in range(2, int(number / 2))):
        return 'yes'
    return 'no'


def question_checker() -> list:
    '''Generates random numb and returns Yes if prime, else No'''
    question = randint(MIN_LIM, MAX_LIM)
    answer = prime(question)
    return [question, answer]
