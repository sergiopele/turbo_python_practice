from turtle import Turtle, Screen

cursor = Turtle()
scrn = Screen()
cursor.speed("fastest")


def move_forwards():
    cursor.forward(10)


def move_backwards():
    cursor.backward(10)


def turn_left():
    cursor.left(10)


def turn_right():
    cursor.right(10)


def clear_drawings():
    cursor.home()
    cursor.clear()


scrn.listen()
scrn.onkey(key="w", fun=move_forwards)
scrn.onkey(key="s", fun=move_backwards)
scrn.onkey(key="a", fun=turn_left)
scrn.onkey(key="d", fun=turn_right)
scrn.onkey(key="c", fun=clear_drawings)

scrn.exitonclick()
