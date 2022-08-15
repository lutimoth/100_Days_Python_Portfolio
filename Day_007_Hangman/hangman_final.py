#Step 4 - Adding in lose condition

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


end = False
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code - To make sure we know what word is chosen and can pick an appropriate letter
print(f'Pssst, the solution is {word}.')

display = []
for l in range(len(word)):
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.


while not end:
    guess = input("Guess a letter: ").lower()
    #Check Guessed letter
    for l in range(len(word)):
        #print(f"Current position: {l}\n Current letter: {word[l]}\n Guessed letter: {guess}")
        if word[l] == guess:
            display[l] = guess
    
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
    if guess not in word:
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if lives == 0:
        end = True
        print("You lose")

    if '_' not in display:
        end = True
        print("You win!")

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])