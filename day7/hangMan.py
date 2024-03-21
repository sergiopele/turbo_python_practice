import random
import stages
import words
import os

word_to_guess = random.choice(words.word_list)

def generate_word_length() -> list:
        print(f"{stages.logo}\n\n\n")
        word_length = []
        for i in word_to_guess:
                word_length += "_"
        return word_length
        

def is_game_end(life:int) -> bool:
        if not life == 0:
                if "_" in word_length:
                        return False
                else:
                        print('You Win!')
                        return True
        else:
                print("Game Over")
                return True
        

def print_word_length():
        print(word_length)


def user_input() -> str:
        user_input = input("Guess a letter\n").lower()
        while not user_input.isalpha() or len(user_input) >= 2:
                print("Wrong input\nPlease enter one letter a-Z")
                user_input = input("Guess a letter:\n").lower()
        return user_input


def enter_letter(var:str, life:int) -> int:
        os.system("clear")
        user_input = var
        fail = True
        for letter in range(0,len(word_to_guess)):
                if word_to_guess[letter] == user_input:
                        word_length[letter] = user_input
                        fail = False
        if fail:
                life -= 1
                print(stages.stages[life])
        
        return life  


def game_runner():
        life = 7 
        while is_game_end(life) == False:
                life = enter_letter(user_input(), life)
                print_word_length()
                



word_length = generate_word_length()
print_word_length()
game_runner()
                