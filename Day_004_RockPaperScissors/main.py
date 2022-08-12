rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
from sys import exit

choice = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if player >= 3 or player < 0:
    print('Invalid number, you lose!')
    exit()
else:
    print(choice[player])
    
computer = random.randint(0,2)

print("Computer chose:")
print(choice[computer])


if player == computer:
    print('You tied!')
elif player == 0 and computer == 2:
    print('You win!')
elif computer == 0 and player == 2:
    print('You lose!')
elif player > computer:
    print('You win!')
else: 
    print('You lose!')