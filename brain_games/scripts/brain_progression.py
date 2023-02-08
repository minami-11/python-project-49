# !/usr/bin/python3

from brain_games.games import progression
from brain_games.game_engine import create_gameplay


def main():
    '''Guess missing number in progression. 3 correct or 1 fall'''
    create_gameplay(progression)


if __name__ == '__main__':
    main()
