# !/usr/bin/python3

import brain_games.games.even_odd
from brain_games.game_engine import game_frame


def main():
    '''Guess even or odd. 3 correct or 1 fall'''
    game_frame(brain_games.games.even_odd)


if __name__ == '__main__':
    main()
