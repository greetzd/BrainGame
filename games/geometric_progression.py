import random
import math
from games.game import Game

class GeometricProgression(Game):

    def __init__(self):
        self.hidden_element_index = None

    def start(self):
        print("What number is missing in the progression?")

    def numbers_generator(self, progression_length, foundation_of_progression):
        return [foundation_of_progression ** i for i in range(progression_length)]

    def questions_generator(self):
        progression_length = random.randint(5, 10)
        self.hidden_element_index = random.randint(0, progression_length - 1)
        foundation_of_progression = random.randint(2, 10)

        numbers = self.numbers_generator(progression_length, foundation_of_progression)

        print(" ".join(".." if i == self.hidden_element_index else str(num) for i, num in enumerate(numbers)))

        return numbers

    def check_answer(self, numbers):
        return numbers[self.hidden_element_index]