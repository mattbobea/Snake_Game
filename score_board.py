from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score = {self.score}", align="center", font=("Arial", 18, "normal"))

    def display(self):
        self.clear()
        self.penup()
        self.goto(0, 230)
        self.pendown()
        self.pencolor("white")
        self.write(f"Score = {self.score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"  GAME OVER!\n Your score is: {self.score}!", align="center", font=("Arial", 18, "normal"))
