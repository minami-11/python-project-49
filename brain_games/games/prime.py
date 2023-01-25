from random import randint


def question_checker() -> list:
    '''Generates random numb and returns Yes if prime, else No'''
    question = randint(MIN_LIM, MAX_LIM)
    prime_list = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103)
    answer = 'yes' if question in prime_list else 'no'
    return [question, answer]


START_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_LIM = 0
MAX_LIM = 50
