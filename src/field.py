class Field:

    zero = 0
    field_length = 50
    field_height = 20
    bar_length = 5

    my_bar_position = (zero, field_height / 2)
    opponent_bar_position = (field_length - 1, field_height / 2)
    ball_position = field_length / 2, field_height / 2

    def move_my_bar(self, direction):
        if direction == "up":
            self.my_bar_position = (self.my_bar_position[0], self.my_bar_position[1] - 1)
        elif direction == "down":
            self.my_bar_position = (self.my_bar_position[0], self.my_bar_position[1] + 1)

    def __str__(self):
        result = ""

        for y in reversed(range(self.field_height)):
            for x in range(self.field_length):
                if self.my_bar_position[0] == x and abs(self.my_bar_position[1] - y) < self.bar_length / 2:
                    result += "█"
                elif self.opponent_bar_position[0] == x and abs(self.opponent_bar_position[1] - y) < self.bar_length / 2:
                    result += "█"
                elif self.ball_position[0] == x and self.ball_position[1] == y:
                    result += "⚫"
                else:
                    result += " "
            result += "\n"

        return result
