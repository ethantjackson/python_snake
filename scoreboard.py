from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.write_score()

    def increment_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=("Courier", 18), align="center")

    def reset_score(self):
        self.high_score = max(self.high_score, self.score)
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.write_score()
