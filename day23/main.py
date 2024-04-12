from random import randint
from turtle import Screen
from screen import Game_screen
from player import Player
from cars import Cars
import time
import random
from scoreboard import Scoreboard

scrn = Game_screen()
player = Player()
cars = Cars()
scoreboard = Scoreboard()
scrn.keyboard_event(player)
game_speed = 0.1
while True:
    time.sleep(game_speed)
    scrn.update_screen()
    random_chance = random.randint(1, 6)
    if random_chance == 1:
        cars.create_car()
    if cars.generate_traffic_and_detect_collide(player=player):
        scoreboard.display_game_over()
        break
    if player.is_finished():
        cars.level_up()
        player.go_to_starting_pos()
        scoreboard.update_level()
    
    

scrn.exit_on_click()
