import prompt
from brain_games.cli import welcome_user


def game_frame(game_module):
    '''Rules > question > answer > check > result'''
    USER = welcome_user()
    print(game_module.start_message())
    answer_pack = {'correct': 0, 'wrong': 0}
    while all([answer_pack['correct'] < 3, answer_pack['wrong'] < 1]):
        guess = game_module.question()
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = game_module.checker(guess)
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
