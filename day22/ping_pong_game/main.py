from paddles import Paddle
from screen import Game_screen

new_screen = Game_screen()
paddle = Paddle(-380,0)
paddle2 = Paddle(370,0)
new_screen.update_screen()
new_screen.paddle_1_keyboard_events(paddle)
new_screen.update_screen()
new_screen.paddle_2_keyboard_events(paddle2)





new_screen.close_window_on_click()