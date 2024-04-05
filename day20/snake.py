from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self, amount_segments=3):
        for i in range(amount_segments):
            self.__add_segment()

    def __add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        initial_pos = self.segments[-1].pos() if len(self.segments) > 0 else (0, 0)
        new_segment.goto(initial_pos)
        new_segment.color("white")
        self.segments.append(new_segment)

    def extend_snake(self):
        self.create_snake(1)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            last_segment_x = self.segments[i - 1].xcor()
            last_segment_y = self.segments[i - 1].ycor()
            self.segments[i].goto(last_segment_x, last_segment_y)
        self.head.forward(MOVE_DISTANCE)

    def up_direction(self):
        if not self.head.heading() == DOWN:
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
