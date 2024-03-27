import logo
import random
import os

def is_number_guessed():
        global attempts
        user = int(user_guess)
        guess = int(guess_number)
        if user > guess:
                attempts -= 1
                print(f"The number {user} is too high\nYou have {attempts} attempts")
                return False
        elif user < guess:
                attempts -= 1
                print(f"The number {user} is too low\nYou have {attempts} attempts")
                return False
        else:
                os.system("clear")
                print(f"{logo.logo_winner}\nYou are correct, the guess number is {guess}")
                return True
        
def verify_input():
        user = input("Make a guess: ")
        while user.isdecimal() == False:
                user = input("Input must be a number. Make a guess: ")
        return user


play_again = True
while play_again == True:
        print(f"{logo.logo}\nWelcome to the number Guessing Game!")
        print(f"I am thinking of a number between 1 and 100.")
        guess_number = random.randint(1,100)
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
        attempts = 5 if difficulty_level.lower() == "hard" else 10
        print(f"You have {attempts} attempts")
        guessed = False  
        while attempts > 0 and not guessed:
                user_guess = verify_input()
                guessed = is_number_guessed()

        os.system("clear")
        print(f"{logo.logo_lose}")
        play_again = True if input("Do you want play again? Type 'y' or 'n'").lower() == "y" else False
        


