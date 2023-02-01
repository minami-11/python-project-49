# !/usr/bin/python3

from brain_games.games import calculate
from brain_games.game_engine import game_frame


def main():
    '''Guess calc math expression. 3 correct or 1 fall'''
    game_frame(calculate)


if __name__ == '__main__':
    main()
