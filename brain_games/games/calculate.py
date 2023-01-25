from random import randint, choice


def question_checker() -> list:
    '''Generates random math expression and it's result'''
    a = randint(MIN_LIM, MAX_LIM)
    b = randint(MIN_LIM, MAX_LIM)
    math_actions = ['+', '-', '*']
    math_operator = choice(math_actions)
    question = f'{a} {math_operator} {b}'
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    answer = str(action_list.get(math_operator))
    return [question, answer]


START_MESSAGE = 'What is the result of the expression?'
MIN_LIM = 0
MAX_LIM = 50
