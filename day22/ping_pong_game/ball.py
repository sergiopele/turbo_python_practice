from turtle import Turtle
BALL_COLOR = "white"


class Ball(Turtle):

    def __init__(
        self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
