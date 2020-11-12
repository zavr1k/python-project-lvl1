import prompt


def run_game(game=None, rounds_total=3):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'(Hello, {name}!)')
    if game:
        print(game.DESCRIPTION)
        for _ in range(rounds_total):
            question, answer = game.prepare_round()
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
