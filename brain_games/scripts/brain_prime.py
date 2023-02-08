# !/usr/bin/python3

from brain_games.games import prime
from brain_games.game_engine import create_gameplay


def main():
    '''Guess is number prime or not. 3 correct or 1 fall'''
    create_gameplay(prime)


if __name__ == '__main__':
    main()
