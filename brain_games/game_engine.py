def run_game(game):
    for i in range(3):
        outcome, answer, question = game()
        if outcome:
            print("Correct!")
            continue
        print(f"{answer} is wrong answer ;(. Correct answer was {question}.")
        return False
    return True


def game_result(res, name):
    if res:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
