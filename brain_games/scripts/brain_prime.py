# !/usr/bin/python3

from brain_games.cli import welcome_user
from brain_games.game_engine import gamelogic_frame, win_or_fall_message


def main():
    '''Guess is number prime or not. 3 correct or 1 fall'''
    USER = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    func_result = gamelogic_frame('prime')
    win_or_fall_message(func_result, USER)


if __name__ == '__main__':
    main()
