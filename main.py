from src.cli import greetings
from games.geometric_progression import GeometricProgression
from games.lcm import LCM
from bin.game_engine import play

def main():
    name = greetings()

    lcm = LCM()
    geometric_progression = GeometricProgression()

    play(name, lcm)
    play(name, geometric_progression)

if __name__ == "__main__":
    main()
