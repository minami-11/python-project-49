from random import randint, choice
import prompt


def even_odd_checker(number: int) -> str:
    return ['yes', 'no'][number % 2]


def calc_checker(math_string: str) -> int:
    '''Сonverts math_string to a mathematical operation'''
    a, math_operator, b = math_string.split()
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    return action_list.get(math_operator)


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


def game_generator(game_name: str) -> (str | int):
    '''Generates questions for games'''
    math_actions = ['+', '-', '*']
    a = randint(0, 50)
    b = randint(0, 50)
    game_pack = {'even_odd': a,
                 'calc': ' '.join(map(str, [a, choice(math_actions), b])),
                 'gcd': f'{a} {b}',
                 'progress': progression_checker()}
    return game_pack.get(game_name)


def gamelogic_frame(game_name: str) -> str:
    '''Game engine'''
    answer_pack = {'correct': 0, 'wrong': 0}
    while all([answer_pack['correct'] < 3, answer_pack['wrong'] < 1]):
        if game_name == 'progress':
            guess, progress_answer = game_generator(game_name)
        else:
            guess = game_generator(game_name)
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        match game_name:
            case 'even_odd': game_correct_answer = even_odd_checker(guess)
            case 'calc': game_correct_answer = str(calc_checker(guess))
            case 'gcd': game_correct_answer = str(gcd_checker(guess))
            case 'progress': game_correct_answer = progress_answer
        if game_correct_answer == user_answer:
            answer_pack['correct'] += 1
            print('Correct!')
        else:
            answer_pack['wrong'] += 1
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{game_correct_answer}'.")
    return "Win" if answer_pack.get('correct') == 3 else "Fall"


def win_or_fall_message(func_result: str, USER: str) -> None:
    '''User gets win or lose message'''
    if func_result == "Win":
        print(f'Congratulations, {USER}!')
    else:
        print(f"Let's try again, {USER}!")
