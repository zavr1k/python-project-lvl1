#!/usr/bin/env python
import brain_games.games.game_progression as game
from brain_games.game_engine import run_game, game_result
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    game.rules()
    result = run_game(game.progression)
    game_result(result, name)


if __name__ == "__main__":
    main()
