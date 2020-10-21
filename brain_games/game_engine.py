def start_game(game, name):
    for i in range(3):
        status, message = game()
        if status:
            print(f"{message}, {name}!")
            continue
        print(f"{message}, {name}!")
        break
    else:
        print(f'Congratulations, {name}!')
