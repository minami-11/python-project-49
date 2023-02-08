from random import randint


START_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_LIMIT = 0
MAX_LIMIT = 50


def is_prime(number: int) -> bool:
    '''True if prime, else False'''
    match number:
        case (0 | 1): return False
        case 2: return True
        case _: return all(number % divider for divider
                           in range(2, int(number / 2 + 1)))


def make_question_and_answer() -> list:
    '''Generates random numb and returns Yes if prime, else No'''
    question = randint(MIN_LIMIT, MAX_LIMIT)
    answer_bool = is_prime(question)
    if answer_bool:
        answer = 'yes'
    else:
        answer = 'no'
    return [question, answer]
