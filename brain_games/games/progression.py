from random import randint, choice


def question_checker() -> list:
    '''Generates random arithmetic progression with missing number'''
    progress_length = randint(LENGTH_MIN, LENGTH_MAX)
    progress_point = randint(MIN_LIM, MAX_LIM)
    progress_step = randint(STEP_MIN, STEP_MAX)
    arithm_progress = []
    for _ in range(progress_length):
        arithm_progress.append(str(progress_point))
        progress_point += progress_step
    guess_numb = choice(arithm_progress)
    arithm_progress[arithm_progress.index(guess_numb)] = '..'
    question = ' '.join(arithm_progress)
    answer = str(guess_numb)
    return [question, answer]


START_MESSAGE = 'What number is missing in the progression?'
MIN_LIM = 0
MAX_LIM = 50
LENGTH_MIN = 5
LENGTH_MAX = 10
STEP_MIN = 2
STEP_MAX = 10
