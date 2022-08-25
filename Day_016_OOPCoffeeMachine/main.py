from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()


ordering = True

print(logo)
print("☕ Welcome to the coffee shop! ☕")

while ordering:
    order = input(f"What would you like? {menu.get_items()}: ").lower()

    if order == 'off':
        print("Good bye!")
        ordering = False
        break

    if order == 'report':
        machine.report()
        money.report()

    if order in menu.get_items():
        drink = menu.find_drink(order)
        print(f"Your {order} is ${drink.cost}.")
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(drink)

    if order == 'refill':
        machine.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    another_cup = input("Would you like order something else? (y/n): ")
    if another_cup == 'y':
        continue
    else:
        print("Good bye! Thanks for coming!")
        ordering = False
        break
