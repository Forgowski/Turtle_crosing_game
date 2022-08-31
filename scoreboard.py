from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"level: {self.level}", False, "left", FONT)

    def update_level(self):
        self.clear()
        self.write(f"level: {self.level}", False, "left", FONT)

    def end_of_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
