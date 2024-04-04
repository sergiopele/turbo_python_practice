from turtle import Screen
import time
from snake import Snake

scrn = Screen()
scrn.setup(width=600, height=600)
scrn.tracer(0)
scrn.bgcolor("black")
scrn.title("Snake")
snake = Snake()
scrn.listen()
scrn.onkey(key="Up", fun=snake.up_direction)
scrn.onkey(key="Down", fun=snake.down_direction)
scrn.onkey(key="Left", fun=snake.left_direction)
scrn.onkey(key="Right", fun=snake.right_direction)

game_is_on = True
while game_is_on:
    scrn.update()
    time.sleep(0.1)
    snake.move()


scrn.exitonclick()
