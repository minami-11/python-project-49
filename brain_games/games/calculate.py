from random import randint, choice


START_MESSAGE = 'What is the result of the expression?'
MIN_LIM = 0
MAX_LIM = 50


def string_to_math_converter(a: int, b: int, math_operator: str):
    '''Converts string to math expression with end result'''
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    return action_list.get(math_operator)


def question_checker() -> list:
    '''Generates random math expression and it's result'''
    a = randint(MIN_LIM, MAX_LIM)
    b = randint(MIN_LIM, MAX_LIM)
    math_actions = ['+', '-', '*']
    math_operator = choice(math_actions)
    question = f'{a} {math_operator} {b}'
    answer = str(string_to_math_converter(a, b, math_operator))
    return [question, answer]
