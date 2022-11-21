from art import logo
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

ordering = True

print(logo)
print("☕ Welcome to the coffee shop! ☕")

while ordering:
    # Prompt user "What would you like"
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # If user asks for a report, print out current report
    if order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${resources['money']:.2f}")

# Turn off if user asks to turn off
    if order == 'off':
        print("Good bye!")
        ordering = False

# Refill if user asks to refill, empty out the "Money"
    if order == 'refill':
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }

    # Coffee maker (deduct resources)
    def make_coffee(coffee):
        for ingredient in MENU[coffee]['ingredients']:
            resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]

    # Check payment amount is valid
    def check_payment(coffee, quarters=0, dimes=0, nickels=0, pennies=0):
        cost = MENU[coffee]['cost']
        payment = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        if payment < cost:
            print("Sorry not enough money. Your coins have been refunded.")
        elif payment == cost:
            make_coffee(coffee)
            print(f"Here is your {coffee}, enjoy!")
        else:
            change = payment - cost
            make_coffee(coffee)
            print(f"Here is your ${change:.2f} change and your {coffee}, enjoy!")

    # Payment Method
    def payment(coffee):
        print(f"Your {coffee} is ${MENU[coffee]['cost']:.2f}.")
        while True:
            try:
                quarters = int(input("How many quarters?: "))
                break
            except ValueError:
                print("please input integer only")
                continue

        while True:
            try:
                dimes = int(input("How many dimes?: "))
                break
            except ValueError:
                print("please input integer only")
                continue

        while True:
            try:
                nickels = int(input("How many nickels?: "))
                break
            except ValueError:
                print("please input integer only")
                continue

        while True:
            try:
                pennies = int(input("How many pennies?: "))
                break
            except ValueError:
                print("please input integer only")
                continue

        check_payment(coffee, quarters, dimes, nickels, pennies)

# Resource Check upon order
    def check_order(coffee):
        for ingredient in MENU[coffee]['ingredients']:
            if MENU[coffee]['ingredients'][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return
        payment(coffee)

    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        check_order(order)

    another_cup = input("Would you like order something else? (y/n): ")
    if another_cup == 'y':
        continue
    else:
        print("Good bye! Thanks for coming!")
        ordering = False
