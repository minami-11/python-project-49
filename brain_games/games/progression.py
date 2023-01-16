from random import randint, choice


def progression_checker() -> list:
    '''Random arithmetic progression -> [progression str, correct answer]'''
    progress_length = randint(5, 10)
    progress_point = randint(0, 50)
    progress_step = randint(2, 10)
    question = []
    for _ in range(progress_length):
        question.append(str(progress_point))
        progress_point += progress_step
    guess_numb = choice(question)
    question[question.index(guess_numb)] = '..'
    return [' '.join(question)] + [str(guess_numb)]
