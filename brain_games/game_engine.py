import prompt


def create_gameplay(game_module):
    '''Rules > question > answer > check > result'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.START_MESSAGE)
    correct = 0
    while correct < 3:
        guess, correct_answer = game_module.make_question_and_answer()
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            correct += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if correct == 3:
        print(f'Congratulations, {name}!')
