from turtle import Turtle


PADDLES_SIZE = (4, 0.5)
PADDLES_HEADING = 90
PADDLES_COLOR = "white"
PADDLES_UP_LIMIT = 250
PADDLES_DOWN_LIMIT = -250
PADDLES_STEP = 25



class Paddle(Turtle):
        def __init__(self, paddle_Xpos, paddle_Ypos):
                super().__init__()
                self.create_paddle(paddle_Xpos, paddle_Ypos)

        def create_paddle(self, paddle_Xpos, paddle_Ypos):
                self.hideturtle()
                self.penup()
                self.setheading(PADDLES_HEADING)
                self.color(PADDLES_COLOR)
                self.goto(x=paddle_Xpos, y=paddle_Ypos)
                self.shape("square")
                self.shapesize(stretch_len=PADDLES_SIZE[0], stretch_wid=PADDLES_SIZE[1])
                self.showturtle()
        

        def move_paddle_up(self):
                if not self.ycor() >= PADDLES_UP_LIMIT:
                        self.forward(PADDLES_STEP)
        
        def move_paddle_down(self):
                if not self.ycor() <= PADDLES_DOWN_LIMIT:
                        self.back(PADDLES_STEP)
                
