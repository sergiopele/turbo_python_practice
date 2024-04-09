from turtle import Turtle


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.turtle_appearance()
        self.set_staring_position()

    def turtle_appearance(self):
        self.shape("turtle")
        self.color("white")
        self.setheading(90)

    def move_forward(self):
        self.forward(10)

    def set_staring_position(self):
        self.hideturtle()
        self.up()
        self.goto(0,-270)
        self.showturtle()

