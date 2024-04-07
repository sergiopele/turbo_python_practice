from paddles import Paddles
from screen import Game_screen

new_screen = Game_screen()
paddle = Paddles()
new_screen.update_screen()
new_screen.paddle_1_keyboard_events(paddle)
new_screen.update_screen()




new_screen.close_window_on_click()