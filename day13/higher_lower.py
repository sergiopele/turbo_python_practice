import random
import logo
from game_data import data
import os

data_to_compare = []
score = 0
random_number_tracker = []

def clean_screen():
        os.system("clear")

def display_main_logo():
        print(logo.logo)

def generate_rand_num() -> int:
        global random_number_tracker
        while True:
                generate_num = random.randint(0,len(data) - 1)
                if not generate_num in random_number_tracker: 
                        random_number_tracker.append(generate_num)
                        return generate_num

def pickup_comparison():
        global random_number_tracker
        global data_to_compare
        if len(data_to_compare) == 0:
                display_main_logo()
                data_to_compare.append(data[generate_rand_num()])
                data_to_compare.append(data[generate_rand_num()])
        else:
                data_to_compare.pop(0)
                random_number_tracker.pop(0)
                data_to_compare.append(data[generate_rand_num()])

def game_runner():
        pickup_comparison()
        compare_a = data_to_compare[0]
        compare_b = data_to_compare[1]
        print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}.")
        print(logo.vs)
        print(f"Against B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}.")
        usr_input = input("Who has more followers? Type 'A' or 'B': ")
        return validate_result(usr_input)

def correct_answer():
        global score
        score += 1
        clean_screen()
        display_main_logo()
        print(f"You are right! Your current score is {score}")

def wrong_answer():
        global score
        clean_screen()
        display_main_logo()
        print(f"Sorry, that's wrong. Final score: {score}")

def validate_result(user_input:str):
        global score
        while True:
                if len(user_input) == 1 and user_input.lower() in ['a', 'b']:
                        break
                user_input = input("Please provide a valid input. Type 'a','A' or 'b','B'.")

        if user_input.lower() == 'a' and data_to_compare[0]["follower_count"] > data_to_compare[1]["follower_count"]:
                correct_answer()
                return True
        elif user_input.lower() == 'b' and data_to_compare[0]["follower_count"] < data_to_compare[1]["follower_count"]:
                correct_answer()
                return True
        else:
                wrong_answer()
                return False
        
while True:
        if not game_runner(): break





