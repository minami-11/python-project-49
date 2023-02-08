# !/usr/bin/python3

from brain_games.games import calculate
from brain_games.game_engine import create_gameplay


def main():
    '''Guess calc math expression. 3 correct or 1 fall'''
    create_gameplay(calculate)


if __name__ == '__main__':
    main()
