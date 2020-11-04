from brain_games.cli import welcome_user
import prompt


def run_game(game):
    name = welcome_user()
    print(game.RULES)
    for _ in range(3):
        question, answer = game.start_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            continue
        print(f"{user_answer} is wrong answer ;(. "
              f"Correct answer was {answer}. \n"
              f"Let's try again, {name}!")
        return
    print(f"Congratulations, {name}!")
