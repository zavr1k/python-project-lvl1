#!/usr/bin/env python
from brain_games.game_engine import run_game
import brain_games.games.even as even


def main():
    run_game(even)


if __name__ == '__main__':
    main()
