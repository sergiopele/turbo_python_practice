from turtle import Turtle
import random
from xmlrpc.client import Boolean
from player import Player

CARS_SIZE = (1, 2)
RBG_COLOR_SET = (0, 255)
RANDOM_X_POSITION_RANGE = (-240, 200)
ALLOWED_DISTANCE_TO_CAR = 23


class Cars(Turtle):
    def __init__(self):
        self.cars = []
        self.car_speed = [1, 10]

    def generate_random_color(self) -> tuple:
        r_color = random.randint(RBG_COLOR_SET[0], RBG_COLOR_SET[1])
        b_color = random.randint(RBG_COLOR_SET[0], RBG_COLOR_SET[1])
        g_color = random.randint(RBG_COLOR_SET[0], RBG_COLOR_SET[1])
        return (r_color, b_color, g_color)

    def create_car(self):
        self.new_car = Turtle()
        initial_speed = 10
        self.new_car.speed(initial_speed)
        self.new_car.up()
        self.new_car.setheading(180)
        self.new_car.hideturtle()
        self.new_car.shape("square")
        self.new_car.shapesize(stretch_wid=CARS_SIZE[0], stretch_len=CARS_SIZE[1])
        self.new_car.color(self.generate_random_color())
        self.new_car.goto(
            310, random.randint(RANDOM_X_POSITION_RANGE[0], RANDOM_X_POSITION_RANGE[1])
        )
        self.new_car.showturtle()
        self.cars.append(self.new_car)

    def generate_traffic_and_detect_collide(self, player: Player) -> bool:
        for car in self.cars:
            car.forward(random.randint(self.car_speed[0], self.car_speed[1]))
            if car.distance(player) <= ALLOWED_DISTANCE_TO_CAR:
                return True 
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
        return False

    def level_up(self):
        self.car_speed = [self.car_speed[0] + 5, self.car_speed[1] + 10]
