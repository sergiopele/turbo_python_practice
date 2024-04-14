from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scrn = Screen()
scrn.setup(width=600, height=600)
scrn.tracer(0)
scrn.bgcolor("black")
scrn.title("Snake")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scrn.listen()
scrn.onkey(key="Up", fun=snake.up_direction)
scrn.onkey(key="Down", fun=snake.down_direction)
scrn.onkey(key="Left", fun=snake.left_direction)
scrn.onkey(key="Right", fun=snake.right_direction)

while True:
    scrn.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.refresh_score()
        scrn.update()
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


scrn.exitonclick()
