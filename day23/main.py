from random import randint
from turtle import Screen
from screen import Game_screen
from player import Player
from cars import Cars
import time
import random

scrn = Game_screen()
player = Player()
cars = Cars()
scrn.keyboard_event(player)
while True:
    time.sleep(0.1)
    scrn.update_screen()
    random_chance = random.randint(1, 6)
    if random_chance == 1:
        cars.create_car()
    cars.generate_traffic()
    

scrn.exit_on_click()
