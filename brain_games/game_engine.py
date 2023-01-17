import prompt
from brain_games.cli import welcome_user
import brain_games.games as games


def game_start_message(game_name: str):
    '''Each game enter message'''
    match game_name:
        case 'even_odd': return games.even_st()
        case 'calc': return games.calc_st()
        case 'gcd': return games.gcd_st()
        case 'progress': return games.progress_st()
        case 'prime': return games.prime_st()


def question_generator(game_name: str) -> str:
    match game_name:
        case 'even_odd': return games.even_q()
        case 'calc': return games.calc_q()
        case 'gcd': return games.gcd_q()
        case 'progress': return games.progress_q()
        case 'prime': return games.prime_q()


def answer_generator(game_name: str, guess: str):
    match game_name:
        case 'even_odd': return games.even_answ(guess)
        case 'calc': return str(games.calc_answ(guess))
        case 'gcd': return str(games.gcd_answ(guess))
        case 'progress': return str(games.progress_answ(guess))
        case 'prime': return games.prime_answ(guess)


def game_frame(game_name: str):
    USER = welcome_user()
    print(game_start_message(game_name))
    answer_pack = {'correct': 0, 'wrong': 0}
    while all([answer_pack['correct'] < 3, answer_pack['wrong'] < 1]):
        guess = question_generator(game_name)
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = answer_generator(game_name, guess)
        if correct_answer == user_answer:
            answer_pack['correct'] += 1
            print('Correct!')
        else:
            answer_pack['wrong'] += 1
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
    if answer_pack['correct'] == 3:
        print(f'Congratulations, {USER}!')
    else:
        print(f"Let's try again, {USER}!")
