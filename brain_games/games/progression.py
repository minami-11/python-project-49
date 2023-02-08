from random import randint, choice


START_MESSAGE = 'What number is missing in the progression?'
MIN_LIMIT = 0
MAX_LIMIT = 50
LENGTH_MIN = 5
LENGTH_MAX = 10
STEP_MIN = 2
STEP_MAX = 10


def cut_number_from_progression(progression: list) -> list:
    '''Cut number from progression and return them back'''
    guess_number = choice(progression)
    progression[progression.index(guess_number)] = '..'
    return [' '.join(progression), str(guess_number)]


def make_question_and_answer() -> list:
    '''Generates random arithmetic progression with missing number'''
    progress_length = randint(LENGTH_MIN, LENGTH_MAX)
    progress_point = randint(MIN_LIMIT, MAX_LIMIT)
    progress_step = randint(STEP_MIN, STEP_MAX)
    arithm_progress = []
    for _ in range(progress_length):
        arithm_progress.append(str(progress_point))
        progress_point += progress_step
    question, answer = cut_number_from_progression(arithm_progress)
    return [question, answer]
