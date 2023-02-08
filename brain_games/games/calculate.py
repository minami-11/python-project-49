from random import randint, choice


START_MESSAGE = 'What is the result of the expression?'
MIN_LIMIT = 0
MAX_LIMIT = 50


def convert_string_to_math(number_1: int, number_2: int, math_operator: str):
    '''Converts string to math expression with end result'''
    action_list = {'+': int(number_1) + int(number_2),
                   '-': int(number_1) - int(number_2),
                   '*': int(number_1) * int(number_2)}
    return action_list.get(math_operator)


def make_question_and_answer() -> list:
    '''Generates random math expression and it's result'''
    number_1 = randint(MIN_LIMIT, MAX_LIMIT)
    number_2 = randint(MIN_LIMIT, MAX_LIMIT)
    math_actions = ['+', '-', '*']
    math_operator = choice(math_actions)
    question = f'{number_1} {math_operator} {number_2}'
    answer = str(convert_string_to_math(number_1, number_2, math_operator))
    return [question, answer]
