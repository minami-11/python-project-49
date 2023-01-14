from random import randint
import prompt


def even_odd_checker(number: int) -> str:
    return ['yes', 'no'][number % 2]


def even_odd_gamelogic() -> str:
    '''Guess game. Even or odd. 3 correct or 1 fall'''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_pack = {'correct': 0, 'wrong': 0}
    while all([answer_pack['correct'] < 3, answer_pack['wrong'] < 1]):
        guess_numb = randint(0, 100)
        print(f'Question: {guess_numb}')
        user_answer = prompt.string('Your answer: ')
        if even_odd_checker(guess_numb) == user_answer:
            answer_pack['correct'] += 1
            print('Correct!')
        else:
            answer_pack['wrong'] += 1
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{even_odd_checker(guess_numb)}'.")
    return "Win" if answer_pack.get('correct') == 3 else "Fall"
