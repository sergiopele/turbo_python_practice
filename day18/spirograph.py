from turtle import Turtle, Screen
import random


circle = Turtle()
scrn = Screen()
scrn.colormode(255)
circle.speed("fastest")
scrn.bgcolor("black")

def random_color() -> tuple:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

def draw_circle(size_of_gap:int) -> None:
        range_ = int(round(360 / size_of_gap) + 1)
        for i in range(range_):
                circle.circle(100)
                circle.left(size_of_gap)
                circle.color(random_color())

draw_circle(60)
scrn.exitonclick()