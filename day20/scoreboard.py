from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 25, "bold")
SCORE_FILE_PATH = "day20/score.txt"


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
            arg=f"🔴Score: {self.score}, Record: {self.read_score()}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.__display_score()

    def reset(self):
        if self.score > self.read_score():
            self.write_score(self.score)
        self.score = 0
        self.clear()
        self.__display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="💀GAME OVER", align=ALIGNMENT, font=FONT)

    def write_score(self, input_:int):
        with open(SCORE_FILE_PATH, mode="w") as high_score_:
                 high_score_.write(f"{input_}")

    def read_score(self) -> int:
         with open(SCORE_FILE_PATH, mode="r") as high_score_:
                 return int(high_score_.read())