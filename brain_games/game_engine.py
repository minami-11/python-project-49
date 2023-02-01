import prompt
from brain_games.cli import welcome_user


def game_frame(game_module):
    '''Rules > question > answer > check > result'''
    user = welcome_user()
    print(game_module.START_MESSAGE)
    CORRECT = 0
    while CORRECT < 3:
        question_and_answer = game_module.question_checker()
        guess = question_and_answer[0]
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = question_and_answer[1]
        if correct_answer == user_answer:
            CORRECT += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            break
    if CORRECT == 3:
        print(f'Congratulations, {user}!')
