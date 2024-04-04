from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = [Turtle(shape="square") for i in range(3)]
        self.__add_segment()
        self.head = self.turtles[0]

    def __add_segment(self):
        increment = 0
        for i in range(3):
            turtle_body = self.turtles[i]
            turtle_body.goto(increment, 0)
            turtle_body.color("white")
            turtle_body.penup()
            increment -= 20

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            last_segment_x = self.turtles[i - 1].xcor()
            last_segment_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(last_segment_x, last_segment_y)
        self.head.forward(MOVE_DISTANCE)

    def up_direction(self):
        if not self.head.heading == DOWN:
            self.head.setheading(UP)

    def down_direction(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left_direction(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right_direction(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
