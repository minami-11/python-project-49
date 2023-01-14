from random import randint, choice
import prompt


def even_odd_checker(number: int) -> str:
    return ['yes', 'no'][number % 2]


def calc_checker(math_string: str):
    a, math_operator, b = math_string.split()
    action_list = {'+': int(a) + int(b),
                   '-': int(a) - int(b),
                   '*': int(a) * int(b)}
    return action_list.get(math_operator)


def game_generator(game_name: str) -> (str | int):
    math_actions = ['+', '-', '*']
    a = randint(0, 100)
    b = randint(0, 100)
    game_pack = {'even_odd': a,
                 'calc': ' '.join(map(str, [a, choice(math_actions), b]))}
    return game_pack.get(game_name)


def gamelogic_frame(game_name: str) -> str:
    '''Game engine'''
    answer_pack = {'correct': 0, 'wrong': 0}
    while all([answer_pack['correct'] < 3, answer_pack['wrong'] < 1]):
        guess = game_generator(game_name)
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        match game_name:
            case 'even_odd': game_correct_answer = even_odd_checker(guess)
            case 'calc': game_correct_answer = str(calc_checker(guess))
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
