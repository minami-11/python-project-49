from random import randint, choice
import prompt
from brain_games.games.even_odd import even_odd_checker
from brain_games.games.calculate import calc_checker
from brain_games.games.gcd import gcd_checker
from brain_games.games.progression import progression_checker
from brain_games.games.prime import prime_checker


def game_generator(game_name: str) -> (str | int):
    '''Generates questions for games'''
    math_actions = ['+', '-', '*']
    a = randint(0, 50)
    b = randint(0, 50)
    game_pack = {'even_odd': a,
                 'calc': ' '.join(map(str, [a, choice(math_actions), b])),
                 'gcd': f'{a} {b}',
                 'progress': progression_checker(),
                 'prime': a}
    return game_pack.get(game_name)


def game_answer(game_name: str, guess: (str | int)) -> str:
    '''Returns correct answer for each game'''
    match game_name:
        case 'even_odd': return even_odd_checker(guess)
        case 'calc': return str(calc_checker(guess))
        case 'gcd': return str(gcd_checker(guess))
        case 'progress': return None
        case 'prime': return prime_checker(guess)


def gamelogic_frame(game_name: str) -> str:
    '''Game engine'''
    answer_pack = {'correct': 0, 'wrong': 0}
    while all([answer_pack['correct'] < 3, answer_pack['wrong'] < 1]):
        if game_name == 'progress':
            guess, game_correct_answer = game_generator(game_name)
        else:
            guess = game_generator(game_name)
            game_correct_answer = game_answer(game_name, guess)
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
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
