from coffee_menu import menu, price, coins_type_inserted
import os
resource = {
        "Water" : 300,
        "Milk": 200,
        "Coffee": 100,
        "Money": 0
}
user_order = ""

def clear_screen():
        os.system("clear")

def take_order() -> str:
        while True:
                user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
                if user_input == "report":
                        print_report()
                elif user_input in ["espresso","latte","cappuccino","off"]:
                        return user_input
                else:
                        print("Please provide correct input")

def print_report():
        print(f"Water: {resource["Water"]}\nMilk: {resource["Milk"]}\nCoffee: {resource["Coffee"]}\nMoney: {resource["Money"]}")

def check_resource_sufficient(order:str) -> bool:
        global resource, user_order
        if order == "off": return False
        ingredients = menu[order.title()]
        evaluate_capacity = resource
        for i in evaluate_capacity:
                evaluate_capacity[i] -= ingredients.get(i,0)
                if evaluate_capacity[i] < 0:
                        print(f"Sorry there is not enough {i}.")
                        return False 
        user_order = order.title()
        resource = evaluate_capacity
        return True

def process_coins() -> bool:
        order_price = price[user_order]
        while True:
                print(f"Your order is {user_order}, price: ${order_price}")
                print("Please insert coins: ")
                for coin in coins_type_inserted:
                        while True:
                                payment = input(f"How many {coin}: ")
                                if payment.isdecimal() and int(payment) >= 0:
                                        coins_type_inserted[coin] = int(payment)
                                        break
                                elif payment == "off": return False
                                print("Please provide valid coin")

                sum = round((coins_type_inserted["pennies"] * 0.01) + (coins_type_inserted["nickles"] * 0.05) + (coins_type_inserted["dimes"] * 0.10) + (coins_type_inserted["quarters"] * 0.25), 2)
                print(f"You inserted {sum}")
                if sum > order_price:
                        print(f"Here is ${round(sum - order_price, 2)} dollars in change.")
                else:
                        print("Sorry that's not enough money. Money refunded.")
                        return False
                resource["Money"] += order_price
                return True
        
def make_coffee():
        global user_order
        if not (check_resource_sufficient(take_order()) and process_coins()):
                return False
        print_report()
        print(f"“Here is your {user_order}. Enjoy!")
        return True

def another_order():
        return True if input("Do you want make another order? Type 'y' or 'n'").lower() == "y" else False
        

while True:
        if not (make_coffee() and another_order()):
                break

    
