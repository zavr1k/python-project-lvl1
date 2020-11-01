#!/usr/bin/env python
from brain_games.game_engine import run_game, game_result
import brain_games.games.game_calc as game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print(game.RULES)
    result = run_game(game.calc)
    game_result(result, name)


if __name__ == '__main__':
    main()
