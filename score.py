from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.start = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 260)
        self.write(f"SCORE: {self.start}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"SCORE: {self.start} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.start += 1
        self.update_scoreboard()

    def reset(self):
        if self.start > self.high_score:
            self.high_score = self.start
            with open('data.txt', mode="w") as data:
                data.write(f"{self.high_score}")
        self.start = 0
        self.update_scoreboard()

    def high_score_read(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())
