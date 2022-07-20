from ball import Ball
from bar import Bar
from field import Field
from score import Score


class Game:

    def __init__(self, field, score):
        self.field = field
        self.score = score

    def play(self):
        pass


def start():
    game = Game(Field(), Score())
    game.play()


if __name__ == "__main__":
    start()
