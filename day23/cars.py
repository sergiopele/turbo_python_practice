from turtle import Turtle
import random

CARS_SIZE = (1, 2)
RBG_COLOR_SET = (0, 255)
RANDOM_X_POSITION_RANGE = (-240, 200)


class Cars(Turtle):
    def __init__(self):
        self.cars = []

    def generate_random_color(self) -> tuple:
        r_color = random.randint(RBG_COLOR_SET[0], RBG_COLOR_SET[1])
        b_color = random.randint(RBG_COLOR_SET[0], RBG_COLOR_SET[1])
        g_color = random.randint(RBG_COLOR_SET[0], RBG_COLOR_SET[1])
        return (r_color, b_color, g_color)

    def create_car(self):
        self.new_car = Turtle()
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

    def generate_traffic(self):
        for car in self.cars:
            car.forward(random.randint(1,10))
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
