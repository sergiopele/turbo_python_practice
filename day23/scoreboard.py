from turtle import Turtle
DEFAULT_COLOR = "white"
CENTER = 0,0

class Scoreboard(Turtle):
        def __init__(self) -> None:
                super().__init__()
                self.level = 1
                self.hideturtle()
                self.up()
                self.color(DEFAULT_COLOR)
                self.goto(180,270)
                self.display_level()

        def display_level(self):
                self.write(f"Level {self.level}", align="left", font=("Courier", 20, "normal"))

        def display_game_over(self):
                self.goto(CENTER)
                self.write(f"GAME OVER", align="center", font=("Courier", 50, "normal"))

        def update_level(self):
                self.clear()
                self.level += 1
                self.display_level()