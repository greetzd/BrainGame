import random
import math
from games.game import Game

class LCM(Game):

    def start(self):
        print("Find the smallest common multiple of given numbers.")

    def numbers_generator(self):
        return [random.randint(1, 100) for i in range(3)]

    def questions_generator(self):
        numbers = self.numbers_generator()
        print(f"Question: {' '.join(map(str, numbers))}")
        return numbers

    def check_answer(self, numbers):
        return math.lcm(*numbers)