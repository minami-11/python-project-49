# !/usr/bin/python3

import brain_games.games.calculate
from brain_games.game_engine import game_frame


def main():
    '''Guess calc math expression. 3 correct or 1 fall'''
    game_frame(brain_games.games.calculate)


if __name__ == '__main__':
    main()
