# !/usr/bin/python3

from brain_games.games import even_odd
from brain_games.game_engine import game_frame


def main():
    '''Guess even or odd. 3 correct or 1 fall'''
    game_frame(even_odd)


if __name__ == '__main__':
    main()
