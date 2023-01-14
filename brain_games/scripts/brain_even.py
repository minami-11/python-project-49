# !/usr/bin/python3

from brain_games.cli import welcome_user
from brain_games.even_odd_logic import even_odd_gamelogic


def main():
    USER = welcome_user()
    if even_odd_gamelogic() == "Win":
        print(f'Congratulations, {USER}!')
    else:
        print(f"Let's try again, {USER}!")


if __name__ == '__main__':
    main()
