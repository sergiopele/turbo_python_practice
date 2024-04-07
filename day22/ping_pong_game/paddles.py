from turtle import Turtle


PADDLE_1_POSITION = (-380,0)
PADDLE_2_POSITION = (370,0)
PADDLES_SIZE = (4, 0.5)
PADDLES_HEADING = 90
PADDLES_COLOR = "white"
PADDLES_UP_LIMIT = 250
PADDLES_DOWN_LIMIT = -250
PADDLES_STEP = 15



class Paddles():
        def __init__(self):
                self.create_paddle_1()
                self.create_paddle_2()

        def create_paddle_1(self):
                self.paddle_1 = Turtle()
                self.paddle_1.hideturtle()
                self.paddle_1.penup()
                self.paddle_1.setheading(PADDLES_HEADING)
                self.paddle_1.color(PADDLES_COLOR)
                self.paddle_1.goto(PADDLE_1_POSITION)
                self.paddle_1.shape("square")
                self.paddle_1.shapesize(stretch_len=PADDLES_SIZE[0], stretch_wid=PADDLES_SIZE[1])
                self.paddle_1.showturtle()
        
        def create_paddle_2(self):
                self.paddle_2 = Turtle()
                self.paddle_2.hideturtle()
                self.paddle_2.penup()
                self.paddle_2.color(PADDLES_COLOR)
                self.paddle_2.setheading(PADDLES_HEADING)
                self.paddle_2.goto(PADDLE_2_POSITION)
                self.paddle_2.shape("square")
                self.paddle_2.shapesize(stretch_len=PADDLES_SIZE[0], stretch_wid=PADDLES_SIZE[1])
                self.paddle_2.showturtle()

        def move_paddle_up(self):
                if not self.paddle_1.ycor() >= PADDLES_UP_LIMIT:
                        self.paddle_1.forward(PADDLES_STEP)
        
        def move_paddle_down(self):
                if not self.paddle_1.ycor() <= PADDLES_DOWN_LIMIT:
                        self.paddle_1.back(PADDLES_STEP)
                
