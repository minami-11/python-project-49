# !/usr/bin/python3

import brain_games.games.progression
from brain_games.game_engine import game_frame


def main():
    '''Guess missing number in progression. 3 correct or 1 fall'''
    game_frame(brain_games.games.progression)


if __name__ == '__main__':
    main()
