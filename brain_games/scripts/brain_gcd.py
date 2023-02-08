# !/usr/bin/python3

from brain_games.games import gcd
from brain_games.game_engine import create_gameplay


def main():
    '''Guess greatest common divisor. 3 correct or 1 fall'''
    create_gameplay(gcd)


if __name__ == '__main__':
    main()
