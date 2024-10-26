from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def questions_generator(self):
        pass

    @abstractmethod
    def check_answer(self, numbers):
        pass