from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.write(f"Score: {self.score}", font=("Courier", 18), align="center")

    def increment_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=("Courier", 18), align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=("Courier", 24), align="center")
