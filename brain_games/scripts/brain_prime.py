# !/usr/bin/python3

import brain_games.games.prime
from brain_games.game_engine import game_frame


def main():
    '''Guess is number prime or not. 3 correct or 1 fall'''
    game_frame(brain_games.games.prime)


if __name__ == '__main__':
    main()
