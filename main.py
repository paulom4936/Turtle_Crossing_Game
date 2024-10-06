import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("turtle crossing")
screen.tracer(0)
scoreboard = Scoreboard()
car = CarManager()
screen.setup(width=600, height=600)

player = Player()

screen.listen()

screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="s", fun=player.move_down)

game_is_on = True
while game_is_on:
    time.sleep(player.speed)
    car.start()
    screen.update()

    if player.ycor() > 280:
        player.next_level()
        scoreboard.scoring()

    for i in range(len(car.car_list)):
        crash = car.car_list[i].xcor()
        if car.car_list[i].distance(player) < 20 and (crash < 20 or crash > - 20):
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
