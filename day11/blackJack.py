import random
import os

cpu = {
        "player_name": "CPU", 
        "cards": [],
        "scores": 0,
        "bidding": True
        }
user = {
        "player_name": "Player", 
        "cards":[],
        "scores": 0,
        "bidding": True,
        }

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def reset_scores(): 
        cpu["cards"] = []
        cpu["scores"] = 0
        cpu["bidding"] = True
        user["cards"] = []
        user["scores"] = 0
        user["bidding"] = True

def card_picker(is_first_round:bool, player:dict):
        do_bidding = player["bidding"]
        name = player["player_name"]
        score = player["scores"]
        if is_first_round:
                for i in range(0,2):
                        player["cards"].append(cards[random.randint(0, len(cards) - 1)])
        else:        
                player["cards"].append(cards[random.randint(0, len(cards) - 1)]) if do_bidding else print(f"{name} does not bidding, score: {score} ")

def calculate_score(player:dict):
        total_sum = sum(player["cards"])
        def calculate_scores_when_over_21():
                replace_11 = [1 if x == 11 else x for x in player["cards"]]
                player["cards"] = replace_11
                player["scores"] = sum(player["cards"])
        def calculate_scores_when_below_21():
                player["scores"] = total_sum
        calculate_scores_when_over_21() if total_sum > 21 else calculate_scores_when_below_21()

                
def continue_game(player:dict):
        score = player["scores"]
        player_name = player["player_name"]
        if score > 17 and player["bidding"] == True:
                if player_name == "CPU":
                        player["bidding"] = False
                        print(f"{player_name} stops bidding. Score: {score}")
                        return False
                else:
                        do_you_continue = input(f"Your current score is: {score}.\nDo you want to get another card? 'y' or 'n'")
                        player["bidding"] = True if do_you_continue.lower() in "y" else False
                        return player["bidding"]
                        
                
def define_winner():
        user_score = user["scores"]
        cpu_scores = cpu["scores"]
        user_bidding = user["bidding"]
        cpu_bidding = cpu["bidding"]
        if (not user_bidding and not cpu_bidding) or user_score > 21 or cpu_scores > 21:
                if (user_score > 21 and cpu_scores < 21) or ((user_score < 21) < (cpu_scores < 22)):
                        print("You LOSE")
                        return True
                elif (user_score < 22 and cpu_scores < 22) and user_score == cpu_scores:
                        print("Draw")
                        return True
                elif(user_score < 21 and cpu_scores > 21) or (user_score < 21 and cpu_scores > 21) or (user_score == 21 and cpu_scores != 21):
                        print("You WIN!")
                        return True
                else:
                        return False
        else:
                if user_score == 21:
                        print("You WIN!")
                        return True
                elif cpu_scores == 21:
                        print("You Lose")
                        return True
                else:
                        return False

def play_game():
        continue_playing = True
        while continue_playing:
                reset_scores()
                card_picker(True, cpu)
                card_picker(True, user)
                calculate_score(user)
                calculate_score(cpu)
                print(f"{cpu["player_name"]} scores: {cpu["scores"]}")
                print(f"{user["player_name"]} scores: {user['scores']}")
                continue_playing
                while not define_winner():
                        continue_game(cpu)
                        continue_game(user)
                        card_picker(False, cpu)
                        card_picker(False, user)
                        calculate_score(user)
                        calculate_score(cpu)
                        print(f"{cpu["player_name"]} scores: {cpu["scores"]}")
                        print(f"{user["player_name"]} scores: {user['scores']}")
                continue_playing = True if input("Do you want to play gane again? Type 'y' or 'n'") == "y" else False
                os.system("clean") 
                
play_game()        


