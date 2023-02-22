import prompt


def create_gameplay(game_module):
    '''Rules > question > answer > check > result'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.START_MESSAGE)
    for round_number in ('1_round', '2_round', '3_round'):
        guess, correct_answer = game_module.make_question_and_answer()
        print(f'Question: {guess}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
            if round_number == '3_round':
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
