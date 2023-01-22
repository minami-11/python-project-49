from random import randint, choice


def start_message():
    return 'What is the result of the expression?'


def question() -> str:
    '''Generates random game question'''
    a = randint(0, 50)
    b = randint(0, 50)
    math_actions = ['+', '-', '*']
    return ' '.join(map(str, [a, choice(math_actions), b]))


def checker(math_string: str) -> str:
    '''Converts math_string to a mathematical operation'''
    a, math_operator, b = math_string.split()
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    return str(action_list.get(math_operator))
