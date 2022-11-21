#Step 3 - Adding in win condition

import random

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

#Testing code - To make sure we know what word is chosen and can pick an appropriate letter
print(f'Pssst, the solution is {word}.')

display = []
for l in range(len(word)):
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

end = False

while not end:
    guess = input("Guess a letter: ").lower()
    #Check Guessed letter
    for l in range(len(word)):
        print(f"Current position: {l}\n Current letter: {word[l]}\n Guessed letter: {guess}")
        if word[l] == guess:
            display[l] = guess
    print(display)

    if '_' not in display:
        end = True
        print("You win!")
