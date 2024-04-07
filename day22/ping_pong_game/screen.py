from turtle import Turtle, Screen

from paddles import Paddles


RESOLUTION = (800, 600)
SCREEN_TITLE = "Ping Pong by Serhii"
BACKGROUND_COLOR = "black"
LINE_SIZE = 4
LINE_COLOR = "grey"
KEY_EVENT_UP = "Up"
KEY_EVENT_DOWN = "Down"


class Game_screen:

    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.title(SCREEN_TITLE)
        self.screen.setup(width=RESOLUTION[0], height=RESOLUTION[1])
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.draw_line()
        self.screen.tracer(1)

    def close_window_on_click(self):
        self.screen.exitonclick()

    def draw_line(self):
        self.line = Turtle()
        self.line.speed("fastest")
        self.line.hideturtle()
        self.line.color(LINE_COLOR)
        self.line.penup()
        self.line.pensize(LINE_SIZE)
        self.line.goto(0, -300)
        for i in range(-300, 300, 5):
            if i % 3 == 0:
                self.line.pendown()
                self.line.goto(0, i)
                self.line.penup()
            else:
                self.line.penup()
                self.line.goto(0, i)

    def update_screen(self):
        self.screen.update()

    def paddle_1_keyboard_events(self, paddle_obj: Paddles):
        self.screen.listen()
        self.screen.onkey(key=KEY_EVENT_UP, fun=paddle_obj.move_paddle_up)
        self.screen.onkey(key=KEY_EVENT_DOWN, fun=paddle_obj.move_paddle_down)
