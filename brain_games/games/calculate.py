def calc_checker(math_string: str) -> int:
    '''Converts math_string to a mathematical operation'''
    a, math_operator, b = math_string.split()
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    return action_list.get(math_operator)
