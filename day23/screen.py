from turtle import Screen
from player import Player

RESOLUTION = (600, 600)
BACKGROUND_COLOR = "black"


class Game_screen:
    def __init__(self):
        self.scrn = Screen()
        self.scrn.setup(width=RESOLUTION[0], height=RESOLUTION[1])
        self.scrn.bgcolor(BACKGROUND_COLOR)
        self.scrn.colormode(cmode=255)
        self.scrn.tracer(0)
        self.scrn.listen()

    def keyboard_event(self, player_obj: Player):
        self.scrn.onkey(key="Up", fun=player_obj.move_forward)

    def update_screen(self):
        self.scrn.update()

    def exit_on_click(self):
        self.scrn.exitonclick()
