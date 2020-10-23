def run_game(game):
    for i in range(3):
        lap = game()
        if lap:
            continue
        return False
    return True


def game_result(res, name):
    if res:
        print(f"Congratulations, {name}")
    else:
        print(f"Let's try again, {name}")
