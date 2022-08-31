import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def check_move():
    screen.onkey(player.go_up, "Up")


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

is_game_on = True
player = Player()
screen.listen()
scoreboard=Scoreboard()

while is_game_on:
    time.sleep(0.1)
    check_move()
    if player.is_finish():
        scoreboard.level += 1
        scoreboard.update_level()
    screen.update()

screen.exitonclick()
