print('''
*******************************************************************************
|                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
         |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == 'left':
    choice2 = input("You fall into a lake, would you like to swim or wait?").lower()
    if choice2 == 'wait':
        print('You wait and the waves of the lake push you gently to shore, you land on a beach with three doors.\n')
        choice3 = input('The doors are red, blue, and yellow. Which door do you choose?\n').lower()
        if choice3 == 'red':
            print('You approach the red door and feel an intense heat. You push on and open the door. As you turn the handle, a huge burst of flame engulfs you.\n Game Over')
        elif choice3 == 'blue':
            print('You approach the blue door and hear some noises. You open the door to find an entryway into a den of wild beasts. They eat you.\n Game Over')
        elif choice3 == 'yellow':
            print('You approach the yellow door. You open it and find a treasure chest right behind it. You win!')
        else:
            print("Don't try to cheat the system! A meteor lands on you. Game Over")
    else:
        print('A giant trout discovers your attempt to be clever. It eats you. Game Over')
else:
    print('You fall in a hole and die, sorry. Game Over')