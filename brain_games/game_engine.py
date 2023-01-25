import prompt
from brain_games.cli import welcome_user


def game_frame(game_module):
    '''Rules > question > answer > check > result'''
    USER = welcome_user()
    print(game_module.START_MESSAGE)
    CORRECT = 0
    WRONG = 0
    while all([CORRECT < 3, WRONG < 1]):
        question_and_answer = game_module.question_checker()
        guess = question_and_answer[0]
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = question_and_answer[1]
        if correct_answer == user_answer:
            CORRECT += 1
            print('Correct!')
        else:
            WRONG += 1
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
    if CORRECT == 3:
        print(f'Congratulations, {USER}!')
    else:
        print(f"Let's try again, {USER}!")
