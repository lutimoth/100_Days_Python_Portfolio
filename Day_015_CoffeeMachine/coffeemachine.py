MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

ordering = True


while ordering:
    # TODO Prompt user "What would you like"
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # If user asks for a report, print out current report
    if order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${resources['money']:.2f}")

# TODO Turn off command
    if order == 'off':
        print("Good bye!")
        ordering = False

    # TODO Coffee maker (deduct resources)
    def deduct(coffee):
        for ingredient in MENU[coffee]['ingredients']:
            resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]

    # Check payment amount is valid
    def check_payment(coffee, quarters=0, dimes=0, nickels=0, pennies=0):
        cost = MENU[coffee]['cost']
        payment = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        if payment < cost:
            print("Sorry not enough money. Your coins have been refunded.")
        elif payment == cost:
            deduct(coffee)
            print(f"Here is your {coffee}, enjoy!")
            #reorder()
        else:
            change = payment - cost
            deduct(coffee)
            print(f"Here is your ${change} change and your {coffee}, enjoy!")
            #reorder()

    # Payment Method
    def payment(coffee):
        while True:
            try:
                quarters = int(input("How many quarters?: "))
                break
            except ValueError:
                print("please input integero only")
                continue

        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        check_payment(coffee, quarters, dimes, nickels, pennies)

# TODO Resource Check upon order
    def check_order(coffee):
        for ingredient in MENU[coffee]['ingredients']:
            if MENU[coffee]['ingredients'][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                reorder()
        payment(coffee)

    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        check_order(order)

# TODO Optional: refill to reset resources
    if order == 'refill':
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }

    another_cup = input("Would you like another cup? (y/n): ")
    if another_cup == 'y':
        continue
    else:
        break
