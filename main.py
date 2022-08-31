import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def check_move():
    screen.onkeypress(player.go_up, "Up")


frames_counter = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

is_game_on = True
player = Player()
screen.listen()
scoreboard = Scoreboard()
car_manager = CarManager()

while is_game_on:
    time.sleep(0.1)
    check_move()
    if player.is_finish():
        scoreboard.level += 1
        scoreboard.update_level()
        car_manager.increment_speed()

    if frames_counter % 3 == 0:
        car_manager.create_car()

    car_manager.move_cars()
    screen.update()
    frames_counter += 1

screen.exitonclick()
