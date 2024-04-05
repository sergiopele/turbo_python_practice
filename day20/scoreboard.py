from tkinter.font import Font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.__display_score()

    def __display_score(self):
        self.write(
            arg=f"🔴Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.__display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="💀GAME OVER", align=ALIGNMENT, font=FONT)
