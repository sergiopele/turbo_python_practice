import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def input_funct() -> str:
        user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        while not (user_input == "encode" or user_input == "decode"):
                print("Please enter valid input \"encode\" or \"decode\"")
                user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
        return user_input

def encode(message:str, shift:int) -> str:
        result = ""
        for i in message:
                        if i.isalpha():
                                index = alphabet.index(i)
                                if (index + shift) > len(alphabet):
                                        wrap = (index + shift) - len(alphabet)
                                        result += alphabet[wrap]
                                else:
                                        result += alphabet[index + shift]
                        else:
                                result += i
        return result

def decode(message:str, shift:int) -> str:
        result = ""
        for i in message:
                        if i.isalpha():
                                index = alphabet.index(i)
                                if (index - shift) < 0:
                                        wrap = len(alphabet) + (index - shift)
                                        result += alphabet[wrap]
                                else:
                                        result += alphabet[index - shift]
                        else:
                                result += i
        return result

def direction_definer(user_input:str) -> str:
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        while not shift.is_integer() or shift < 1:
                shift = int(input("Shift number can not be a char or less than 1\nPlease enter a valid shift number:\n"))     
        result = ""
        if user_input == "encode":
                result = encode(message, shift)
        else: 
                result = decode(message, shift)
        return result

        

runner = True
while runner:
        print(direction_definer(input_funct()))
        runner = True if input("Do you want continue? Type \"y\" or \"n\"\n").lower() == "y" else False
        os.system("clear")
        

