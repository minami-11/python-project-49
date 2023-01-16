def prime_checker(number: int) -> str:
    '''Prime or not'''
    match number:
        case 1: return 'no'
        case 2: return 'yes'
    divider = 2
    result = []
    while True:
        if number % divider == 0:
            result.append(divider)
        elif divider > number / 2:
            break
        if len(result) > 0:
            return 'no'
        divider += 1
    return 'yes'
