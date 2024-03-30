from menu import menu, MenuItem
from coffee_maker import coffeeMaker
from money_machine import moneyMachine

menu = menu()
coffeeMaker = coffeeMaker()
moneyMachine = moneyMachine()

while True:
        order = input(f"What would you like? {menu.get_items()} ")
        if order == "report": 
                coffeeMaker.report()
                moneyMachine.report()
        elif order == "off": break
        else:
                drink = menu.find_drink(order)
                if not (coffeeMaker.is_resource_sufficient(drink) 
                        and moneyMachine.make_payment(moneyMachine.process_coins())): break
                coffeeMaker.make_coffee(drink)




