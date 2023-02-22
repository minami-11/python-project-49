from random import randint, choice


START_MESSAGE = 'What number is missing in the progression?'
MIN_LIMIT = 0
MAX_LIMIT = 50
LENGTH_MIN = 5
LENGTH_MAX = 10
STEP_MIN = 2
STEP_MAX = 10


def generate_progression(length: int, start_point: int, step: int) -> list:
    '''Generates random arithmetic progression'''
    arithm_progress = []
    for _ in range(length):
        arithm_progress.append(str(start_point))
        start_point += step
    return arithm_progress


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
    arithmetic_progression = generate_progression(progress_length,
                                                  progress_point, progress_step)
    question, answer = cut_number_from_progression(arithmetic_progression)
    return [question, answer]
