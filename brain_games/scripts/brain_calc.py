#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games.game_calc import calc
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    start_game(calc, name)


if __name__ == '__main__':
    main()
