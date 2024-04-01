import random
from turtle import Turtle, Screen

COLOR = [
    "blue",
    "red",
    "brown",
    "yellow",
    "white",
    "lightblue",
    "orange",
    "pink",
    "green",
    "grey",
    "coral",
]
walker = Turtle()
scrn = Screen()
scrn.colormode(cmode=255)


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


scrn.bgcolor("black")
walker.pensize(15)
walker.shape("classic")
walker.color("white")
DIRECTION = (0, 90, 180, 270)
walker.speed("fast")


for i in range(200):
    random_direction = random.choice(DIRECTION)
    walker.color(random_color())
    walker.pencolor()
    walker.setheading(random_direction)
    walker.forward(30)

scrn.exitonclick()
