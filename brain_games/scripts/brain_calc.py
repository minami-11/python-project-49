# !/usr/bin/python3

from brain_games.cli import welcome_user
from brain_games.game_engine import gamelogic_frame, win_or_fall_message


def main():
    '''Guess calc math expression. 3 correct or 1 fall'''
    USER = welcome_user()
    print('What is the result of the expression?')
    func_result = gamelogic_frame('calc')
    win_or_fall_message(func_result, USER)


if __name__ == '__main__':
    main()
