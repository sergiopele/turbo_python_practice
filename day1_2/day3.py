# height = int(input("Enter your height"))
# print("Good") if height >= 120 else print("Bad")
# if height <=120:
#         print("Good")
# elif height > 200:
#         print("Ok")
# else:
#         print("Bad")



# If we use if: if: if:
# in this case python will check all 3 if blocks

# When we use if: elif: elif: else:
# in this case only on condition block will be executed
        
# Treasure Island Game
print("Welcome to Treasure Island. \n Your mission is to find the treasure\n")

direction = input("Your are  at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if direction.lower() == "left":
        action_at_lake = input("You come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")

        if action_at_lake.lower() == "wait":
                door = input("You arrived at island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which color do you choose?\n")
                
                if door.lower() == "blue":
                        print("Eaten by beasts.\nGame over.")
                elif door.lower() == "red":
                        print("Burned by fire. \nGame Over")
                elif door.lower() == "yellow":
                        print("You Win!")
                else:
                        print("Game Over.")

        else:
                print("Attacked by trout.\nGame Over.")

else:
        print("Fall into a hole.\nGame Over.")

