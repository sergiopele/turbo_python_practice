from turtle import Turtle, Screen

jackson_the_turtle = Turtle()
scrn = Screen()
scrn.listen()
def move_forward():
        jackson_the_turtle.forward(10)

scrn.onkey(key="space", fun=move_forward)
scrn.exitonclick()