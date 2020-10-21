#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games.game_even import even
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(even, name)


if __name__ == '__main__':
    main()
