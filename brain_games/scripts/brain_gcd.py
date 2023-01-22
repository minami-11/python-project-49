# !/usr/bin/python3

import brain_games.games.gcd
from brain_games.game_engine import game_frame


def main():
    '''Guess greatest common divisor. 3 correct or 1 fall'''
    game_frame(brain_games.games.gcd)


if __name__ == '__main__':
    main()
