# !/usr/bin/python3

from brain_games.games import progression
from brain_games.game_engine import game_frame


def main():
    '''Guess missing number in progression. 3 correct or 1 fall'''
    game_frame(progression)


if __name__ == '__main__':
    main()
