from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.left(90)
        self.speed = 0.01
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def move_up(self):
        self.setheading(90)
        self.move()

    def move_down(self):
        self.setheading(270)
        self.move()

    def next_level(self):
        self.goto(STARTING_POSITION)
        self.speed *= 0.5
