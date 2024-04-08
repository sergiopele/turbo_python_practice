from pdb import run
from scoreboard import Scoreboard
from paddles import Paddle
from screen import Game_screen
from ball import Ball
import time

new_screen = Game_screen()
paddle = Paddle(-380, 0)
paddle2 = Paddle(370, 0)
ball = Ball()
scoreboard = Scoreboard()
new_screen.update_screen()
new_screen.paddle_1_keyboard_events(paddle)
new_screen.paddle_2_keyboard_events(paddle2)
run_time = 0.1
while True:
    new_screen.update_screen()
    time.sleep(run_time)
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.xcor() < -360 and ball.distance(paddle) < 50) or (
        ball.xcor() >= 360 and ball.distance(paddle2) < 50
    ):
        ball.bounce_from_paddle()
        run_time *= 0.5
        print(run_time)
    if ball.xcor() < -370:
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()
        run_time=0.1
    if ball.xcor() > 365:
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()
        run_time=0.1


new_screen.close_window_on_click()
