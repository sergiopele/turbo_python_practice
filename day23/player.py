from turtle import Turtle
OTHER_SIDE_OF_ROAD = 270
STARTING_POS = 0, -270


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
        self.goto(STARTING_POS)
        self.showturtle()

    def is_finished(self) -> bool:
        return True if self.ycor() > OTHER_SIDE_OF_ROAD else False
    
    def go_to_starting_pos(self):
        self.goto(STARTING_POS)
