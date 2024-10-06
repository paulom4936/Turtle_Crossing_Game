from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.start()

    def start(self):
        if len(self.car_list) < 20:
            self.add_car()
        else:
            self.move_car()

    def add_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.left(180)
        car.color(random.choice(COLORS))
        if len(self.car_list) < 15:
            car.teleport(random.randint(-270, 280), random.randint(-250, 280))
        else:
            car.teleport(300, random.randint(-250, 280))
        self.car_list.append(car)

    def move_car(self):
        list_choice = random.randint(0, len(self.car_list) - 1)
        self.car_list[list_choice].forward(10)
        if self.car_list[list_choice].xcor() < - 330:
            self.car_list[list_choice].teleport(300, random.randint(-250, 280))
