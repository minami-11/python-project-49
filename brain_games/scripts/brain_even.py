# !/usr/bin/python3

from brain_games.games import even_odd
from brain_games.game_engine import create_gameplay


def main():
    '''Guess even or odd. 3 correct or 1 fall'''
    create_gameplay(even_odd)


if __name__ == '__main__':
    main()
