import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def rule(user_input:int, computer_input:int): 
        win = "You win!"
        lose = "You lose!"
        draw = "Draw"
        print(f"Your input \n{options[user_input]}\n")
        print(f"Computer input \n{options[computer_input]}\n")
        if user_input == 0 and computer_input == 2 or user_input == 1 and computer_input == 0 or user_input == 2 and computer_input == 1:
                print(win)
        elif user_input == computer_input:
                print(draw)
        else:
                print(lose)

options = [rock, paper, scissors]
user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_move = random.randint(0, len(options) - 1)
rule(user_move, computer_move)



