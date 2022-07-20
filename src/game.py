from field import Field
from score import Score
from printer import Printer


class Game:

    def __init__(self, field, score):
        self.field = field
        self.score = score
        self.printer = Printer()

    def play(self):
        self.printer.print_field(self.field)


def start():
    game = Game(Field(), Score())
    game.play()


if __name__ == "__main__":
    start()
