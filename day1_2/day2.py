print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
bill_split_people = int(input("How many people to split the bill? "))
calculate_result = "{:.2f}".format(round(((total_bill * (tip / 100)) + total_bill) / bill_split_people, 2))
print(f"Each person should pay: ${calculate_result}")