def gcd_checker(numb_string: str):
    '''Euclidean algorithm for gcd'''
    a, b = map(int, numb_string.split())
    if a == 0 and b == 0:
        return 0
    elif a == 0 or b == 0:
        return max(a, b)
    while a != b:
        if a >= b:
            a = a - b
        else:
            b = b - a
    return a
