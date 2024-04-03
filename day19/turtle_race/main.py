from turtle import Turtle, Screen
import random
import tkinter as tk
from tkinter import messagebox

scrn = Screen()
root = tk.Tk()
root.withdraw()
starting_pos = [-230, -100]
turtles = {}
turtles_color = ["blue", "black", "brown", "orange", "grey", "red", "green", "purple"]
turtles = [
    {turtles_color[i]: Turtle(shape="turtle")} for i in range(len(turtles_color))
]
scrn.setup(width=500, height=400)
bet = scrn.textinput(
    title="Make your bet ",
    prompt=f"Which turtle will win the race? Enter a color: {', '.join(turtles_color)}: ",
)


def draw_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(180, -200)
    finish_line.pendown()
    finish_line.left(90)
    finish_line.forward(400)


increment = 0
for i in range(len(turtles)):
    turtle_obj = turtles[i][turtles_color[i]]
    turtle_obj.penup()
    turtle_obj.color(turtles_color[i])
    turtle_obj.goto(x=starting_pos[0], y=starting_pos[1] + increment)
    increment += 30

draw_finish_line()
race_over = False
winner = ""
while not race_over:
    for i in range(len(turtles)):
        turtle_obj = turtles[i][turtles_color[i]]
        turtle_obj.forward(random.randint(0, 10))
        if turtle_obj.pos()[0] >= 180:
            winner = turtles_color[i]
            race_over = True
            message1 = "You win!" if winner.lower() == bet.lower() else "You lose!"
            messagebox.showinfo("Race Over", f"The winner is {winner}, {message1}")
            break

root.destroy()
scrn.exitonclick()
