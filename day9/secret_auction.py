import os
from day9.art import logo

print(f"{logo}\nWelcome to the secret auction program.")
bids = {}

def inputBid() -> int:
    bid = input("What's your bid?: $")
    while (not bid.isdecimal()) or int(bid) < 1:
        bid = input("Please enter valid numeric value\nWhat's your bid?: $")
    return bid

def calculate_max_bid(input:dict):
      key = max(input)
      value = input[key]
      print(f"The winner is {key} with a bid of ${value}")

while True:
        name = input("What is your name?: ")
        bid = inputBid()
        bids[name] = bid
        if not input("Are there any other bidders? Type 'yes' or 'no'.").lower() in "yes":
                break
        os.system("clear")

os.system("clear")
calculate_max_bid(bids)
