from random import randint, choice


def start_message():
    return 'What is the result of the expression?'


def question():
    a = randint(0, 50)
    b = randint(0, 50)
    math_actions = ['+', '-', '*']
    return ' '.join(map(str, [a, choice(math_actions), b]))


def calc_checker(math_string: str) -> int:
    '''Converts math_string to a mathematical operation'''
    a, math_operator, b = math_string.split()
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    return action_list.get(math_operator)
