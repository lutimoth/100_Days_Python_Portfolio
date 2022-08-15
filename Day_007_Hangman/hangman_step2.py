#Step 2 - Adding in display and first correct letter

import random
word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

#Testing code - To make sure we know what word is chosen and can pick an appropriate letter
print(f'Pssst, the solution is {word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

for l in range(len(word)):
    display.append("_")

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for l in range(len(word)):
    if word[l] == guess:
        display[l] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)