import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []
colors = colorgram.extract("day18/hirst_paint/image.jpg", 30)

def extract_rgb_colors(color_donor, accumulator ):
        for i in color_donor:
                r = i.rgb.r
                g = i.rgb.g
                b = i.rgb.b
                accumulator.append((r,g,b))

extract_rgb_colors(colors, rgb_colors)

scrn = Screen()
scrn.colormode(255)
dots = Turtle()
dots.speed("fastest")
dots.shape("classic")
dots.hideturtle()
dots.pensize(20)
dots.pu()
dots.goto(-250,-250)
home_position = dots.pos()

increment = 0
for y in range(10):
        for i in range(10):
                dots.pd()
                dots.color(random.choice(rgb_colors))
                dots.forward(1)
                dots.pu()
                dots.forward(50)
        increment += 50
        dots.goto(home_position[0], home_position[1] + increment)

scrn.exitonclick()

