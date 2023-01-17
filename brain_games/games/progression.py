from random import randint, choice


def start_message():
    return 'What number is missing in the progression?'


def question():
    '''Random arithmetic progression'''
    progress_length = randint(5, 10)
    progress_point = randint(0, 50)
    progress_step = randint(2, 10)
    arithm_progress = []
    for _ in range(progress_length):
        arithm_progress.append(str(progress_point))
        progress_point += progress_step
    guess_numb = choice(arithm_progress)
    arithm_progress[arithm_progress.index(guess_numb)] = '..'
    return ' '.join(arithm_progress)


def progression_checker(string: str):
    '''Returns missing number in progression'''
    progress = string.split()
    x = progress.index('..')
    count = 0
    while True:
        if progress[count].isdigit() and progress[count + 1].isdigit():
            step = int(progress[count + 1]) - int(progress[count])
            break
        count += 1
    if x == len(progress) - 1:
        return int(progress[x - 1]) + step
    return (int(progress[x + 1]) - step, int(progress[x - 1]) + step)[bool(x)]
