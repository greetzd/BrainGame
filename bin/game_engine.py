from games.game import Game

def play(name, game: Game):
    correct_answers_counter = 0

    game.start()

    while correct_answers_counter < 3:
        numbers = game.questions_generator()
        answer = int(input("Answer: "))

        if check_answer(game, numbers, answer):
            correct_answers_counter += 1
        else:
            print(f"Let's try again, {name}.")
            return

    print(f"Congratulations, {name}!")
    print(f"Correct answers:  {name}!")


def check_answer(game: Game, numbers, answer):
    correct_answer = game.check_answer(numbers)
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer. Correct answer was '{correct_answer}'.")
        return False