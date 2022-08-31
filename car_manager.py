from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.hideturtle()

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.left(180)
        new_car.turtlesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.goto(310, random.randint(-230, 230))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.cars_speed)

    def increment_speed(self):
        self.cars_speed += MOVE_INCREMENT



