from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-200, 250)
        self.score = 1
        self.score_board()

    def score_board(self):
        self.write(f"Level = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", move=False, font=("Courier", 70, "bold"), align="center")

    def scoring(self):
        self.score += 1
        self.clear()
        self.score_board()
