from turtle import Turtle, Screen

scrn = Screen()
scrn.bgcolor("black")

benny_the_triangle = Turtle()
benny_the_triangle.shape("triangle")


def draw_square() -> None:
    for i in range(0, 4):
        benny_the_triangle.forward(100)
        benny_the_triangle.left(90)


def draw_dashed_line() -> None:
    for i in range(0, 10):
        benny_the_triangle.pd()
        benny_the_triangle.forward(10)
        benny_the_triangle.pu()
        benny_the_triangle.forward(10)


def draw_diff_shapes():
    angle = 360
    step = 70
    shape_faces = 3
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
    color_index = 0
    for y in range(10):
        benny_the_triangle.color(COLOR[color_index])
        for i in range(shape_faces):
            benny_the_triangle.forward(step)
            benny_the_triangle.right(angle / shape_faces)
        shape_faces += 1
        color_index += 1

draw_diff_shapes()


scrn.exitonclick()
